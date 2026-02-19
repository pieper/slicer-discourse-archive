---
topic_id: 40844
title: "Strategies For Batch Sequential Segmentation Of 3D Volumes W"
date: 2024-12-25
url: https://discourse.slicer.org/t/40844
---

# Strategies for Batch/Sequential segmentation of 3D volumes with MONAI Auto3DSeg?

**Topic ID**: 40844
**Date**: 2024-12-25
**URL**: https://discourse.slicer.org/t/strategies-for-batch-sequential-segmentation-of-3d-volumes-with-monai-auto3dseg/40844

---

## Post #1 by @Yue-Hin_Loke1 (2024-12-25 03:59 UTC)

<p>Hi there,</p>
<p>I’ve been able to create a Python extension that loops  automatically uses Auto3DSeg to automatically segments multiple .nrrd files sequentially.</p>
<p>I do notice that the turnround time can be long (~ 1.5 minute per 3D dataset on CPU, 10-20 seconds with GPU) and most of the time is spend initializing the interference script as opposed to epochs themselves.</p>
<p>Is there a way for the Auto3DSeg inference script to allow for batch process of multiple 3D .nrrd files? I’ve tried to modify the script (see failed example below) to introduce multiple volume into the script, however it keeps recognizing them as a series of 2D files so it doesn’t work. Appreciate any advice!</p>
<pre><code class="lang-auto">import os
import numpy as np
import fire
import time
import torch
from collections import OrderedDict

import nrrd
from monai.bundle import ConfigParser
from monai.data import decollate_batch, list_data_collate
from monai.utils import convert_to_dst_type, MetaKeys
from monai.inferers import SlidingWindowInfererAdapt
from torch.cuda.amp import autocast
from monai.transforms import (
    Compose,
    CropForegroundd,
    EnsureTyped,
    Invertd,
    LoadImaged,
    NormalizeIntensityd,
    Spacingd,
    Orientationd,
    ScaleIntensityRanged,
    Lambdad,
)


def logits2pred(logits, sigmoid=False, dim=1):
    if isinstance(logits, (list, tuple)):
        logits = logits[0]

    if sigmoid:
        pred = torch.sigmoid(logits)
        pred = (pred &gt;= 0.5).to(dtype=torch.uint8)
    else:
        pred = torch.softmax(logits, dim=dim)
        pred = torch.argmax(pred, dim=dim, keepdim=True).to(dtype=torch.uint8)

    return pred


@torch.no_grad()
def main(model_file, image_files, result_dir, **kwargs):
    """
    Perform sequential inference for multiple `.nrrd` files.

    Args:
        model_file: Path to the trained model.
        image_files: Comma-separated list of `.nrrd` input files.
        result_dir: Directory to save segmentation results.
    """
    start_time = time.time()

    # Parse and validate inputs
    if not os.path.exists(model_file):
        raise ValueError(f"Model file does not exist: {model_file}")

    if isinstance(image_files, str):
        image_files = image_files.split(",")  # Parse the comma-separated input list

    for file in image_files:
        if not os.path.exists(file):
            raise ValueError(f"Input file does not exist: {file}")

    os.makedirs(result_dir, exist_ok=True)

    # Load model
    checkpoint = torch.load(model_file, map_location="cpu")
    if "config" not in checkpoint:
        raise ValueError(f"Config not found in checkpoint: {model_file}")

    config = checkpoint["config"]
    state_dict = checkpoint["state_dict"]
    model = ConfigParser(config["network"]).get_parsed_content()
    model.load_state_dict(state_dict, strict=True)

    print(f'Model epoch: {checkpoint.get("epoch", 0)}')
    print(f'Model metric: {checkpoint.get("best_metric", 0)}')

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device=device, memory_format=torch.channels_last_3d)
    model.eval()

    # Preprocessing transforms
    transforms = Compose([
        LoadImaged(keys="image", ensure_channel_first=True, allow_missing_keys=True),
        EnsureTyped(keys="image", data_type="tensor", dtype=torch.float, allow_missing_keys=True),
        Orientationd(keys="image", axcodes="RAS"),
        CropForegroundd(keys="image", source_key="image", margin=10, allow_smaller=True),
        Spacingd(
            keys=["image"],
            pixdim=config["resample_resolution"],
            mode=["bilinear"],
            dtype=torch.float,
            allow_missing_keys=True,
        ),
    ])
    _add_normalization_transforms(transforms, "image", config["normalize_mode"], config["intensity_bounds"])
    inf_transform = Compose(transforms)

    # Sliding window inferer
    roi_size = config["roi_size"]
    sliding_inferrer = SlidingWindowInfererAdapt(
        roi_size=roi_size, sw_batch_size=1, overlap=0.625, mode="gaussian"
    )

    # Process each file sequentially
    for image_file in image_files:
        print(f"Processing {image_file}...")

        # Preprocess image
        data_dict = inf_transform({"image": image_file})

        # Debugging: Log tensor shape and ROI size
        print(f"Input tensor shape before inference: {data_dict['image'].shape}")
        print(f"Configured ROI size: {roi_size}")

        # Prepare data for inference
        data = data_dict["image"].to(device=device, memory_format=torch.channels_last_3d)

        # Inference
        with autocast(enabled=True):
            logits = sliding_inferrer(inputs=data, network=model)

        pred = logits2pred(logits, sigmoid=config.get("sigmoid", False))

        # Post-process predictions
        post_transforms = Compose([
            Invertd(keys="pred", orig_keys="image", transform=inf_transform, nearest_interp=True),
        ])
        data_dict["pred"] = convert_to_dst_type(pred, data_dict["image"], dtype=torch.uint8)
        seg = data_dict["pred"].cpu().numpy().astype(np.uint8)

        # Save segmentation result
        output_file = os.path.join(result_dir, os.path.basename(image_file).replace(".nrrd", "_seg.nrrd"))
        nrrd_header = nrrd.read_header(image_file)
        nrrd.write(output_file, seg, nrrd_header)
        print(f"Saved segmentation to {output_file}")

    print("Sequential inference completed.")
    print(f"Total computation time: {time.time() - start_time:.2f} seconds")


def _add_normalization_transforms(transforms, key, normalize_mode, intensity_bounds):
    if normalize_mode == "none":
        pass
    elif normalize_mode in ["range", "ct"]:
        transforms.transforms.append(ScaleIntensityRanged(keys=key, a_min=intensity_bounds[0], a_max=intensity_bounds[1],
                                                           b_min=-1, b_max=1, clip=False))
    elif normalize_mode in ["meanstd", "mri"]:
        transforms.transforms.append(NormalizeIntensityd(keys=key, nonzero=True, channel_wise=True))
    elif normalize_mode in ["meanstdtanh"]:
        transforms.transforms.append(NormalizeIntensityd(keys=key, nonzero=True, channel_wise=True))
        transforms.transforms.append(Lambdad(keys=key, func=lambda x: 3 * torch.tanh(x / 3)))
    elif normalize_mode in ["pet"]:
        transforms.transforms.append(Lambdad(keys=key, func=lambda x: torch.sigmoid((x - x.min()) / x.std())))
    else:
        raise ValueError(f"Unsupported normalize_mode: {normalize_mode}")


if __name__ == "__main__":
    fire.Fire(main)

</code></pre>

---
