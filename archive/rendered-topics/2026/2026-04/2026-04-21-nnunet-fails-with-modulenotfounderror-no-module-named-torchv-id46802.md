---
topic_id: 46802
title: "Nnunet Fails With Modulenotfounderror No Module Named Torchv"
date: 2026-04-21
url: https://discourse.slicer.org/t/46802
---

# nnUNet fails with ModuleNotFoundError: No module named 'torchvision.ops'

**Topic ID**: 46802
**Date**: 2026-04-21
**URL**: https://discourse.slicer.org/t/nnunet-fails-with-modulenotfounderror-no-module-named-torchvision-ops/46802

---

## Post #1 by @aabrown100-git (2026-04-21 20:43 UTC)

<p>Using nnUNet extension with custom weights fails with the following error output.</p>
<pre><code class="lang-auto">Start
********************************************************************************
nnUNet is already installed (2.7.0) and compatible with requested version (nnunetv2).
Transferring volume to nnUNet in /private/var/folders/33/__w9plc529j6m3g2gyk2rwnr0000gn/T/Slicer-OEHhHb
Starting nnUNet with the following parameters:

/Applications/Slicer.app/Contents/lib/Python/bin/nnUNetv2_predict -i /private/var/folders/33/__w9plc529j6m3g2gyk2rwnr0000gn/T/Slicer-OEHhHb/input -o /private/var/folders/33/__w9plc529j6m3g2gyk2rwnr0000gn/T/Slicer-OEHhHb/output -d Dataset850_TotalSegMRI_part1_organs_1088subj -tr nnUNetTrainer_2000epochs_NoMirroring -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cpu -chk checkpoint_final.pth --disable_tta

JSON parameters :
{
    "folds": "",
    "device": "cpu",
    "stepSize": 0.5,
    "disableTta": true,
    "nProcessPreprocessing": 1,
    "nProcessSegmentationExport": 1,
    "checkPointName": "",
    "modelPath": {
        "_path": "/Users/aaronbrown/Library/CloudStorage/GoogleDrive-abrown97@stanford.edu/My Drive/Stanford/CHiPS/Workflows/Segmentation/Dataset850_TotalSegMRI_part1_organs_1088subj"
    }
}
nnUNet preprocessing...
A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.0.2 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11&gt;=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy&lt;2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "/Applications/Slicer.app/Contents/lib/Python/bin/nnUNetv2_predict", line 5, in &lt;module&gt;
    from nnunetv2.inference.predict_from_raw_data import predict_entry_point
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/inference/predict_from_raw_data.py", line 13, in &lt;module&gt;
    import torch
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/__init__.py", line 1477, in &lt;module&gt;
    from .functional import *  # noqa: F403
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/functional.py", line 9, in &lt;module&gt;
    import torch.nn.functional as F
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/__init__.py", line 1, in &lt;module&gt;
    from .modules import *  # noqa: F403
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/modules/__init__.py", line 35, in &lt;module&gt;
    from .transformer import TransformerEncoder, TransformerDecoder, \
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/modules/transformer.py", line 20, in &lt;module&gt;
    device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/utilities/plans_handling/plans_handler.py:37: UserWarning: Detected old nnU-Net plans format. Attempting to reconstruct network architecture parameters. If this fails, rerun nnUNetv2_plan_experiment for your dataset. If you use a custom architecture, please downgrade nnU-Net to the version you implemented this or update your implementation + plans.
  warnings.warn("Detected old nnU-Net plans format. Attempting to reconstruct network architecture "
#######################################################################
Please cite the following paper when using nnU-Net:
Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., &amp; Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.
#######################################################################

perform_everything_on_device=True is only supported for cuda devices! Setting this to False
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Python/bin/nnUNetv2_predict", line 8, in &lt;module&gt;
sys.exit(predict_entry_point())
             ^^^^^^^^^^^^^^^^^^^^^
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/inference/predict_from_raw_data.py", line 998, in predict_entry_point
    predictor.initialize_from_trained_model_folder(
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/inference/predict_from_raw_data.py", line 100, in initialize_from_trained_model_folder
    trainer_class = recursive_find_python_class(join(nnunetv2.__path__[0], "training", "nnUNetTrainer"),
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/utilities/find_class_by_name.py", line 21, in recursive_find_python_class
    tr = recursive_find_python_class(join(folder, modname), class_name, current_module=next_current_module)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/utilities/find_class_by_name.py", line 12, in recursive_find_python_class
    m = importlib.import_module(current_module + "." + modname)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "&lt;frozen importlib._bootstrap&gt;", line 1387, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 1360, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 1331, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 935, in _load_unlocked
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/training/nnUNetTrainer/primus/primus_trainers.py", line 5, in &lt;module&gt;
    from dynamic_network_architectures.architectures.primus import Primus
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/dynamic_network_architectures/architectures/primus.py", line 5, in &lt;module&gt;
    from timm.layers import RotaryEmbeddingCat
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/timm/__init__.py", line 2, in &lt;module&gt;
    from .layers import (
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/timm/layers/__init__.py", line 23, in &lt;module&gt;
    from .classifier import create_classifier, ClassifierHead, NormMlpClassifierHead, ClNormMlpClassifierHead
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/timm/layers/classifier.py", line 15, in &lt;module&gt;
from .create_norm import get_norm_layer
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/timm/layers/create_norm.py", line 29, in &lt;module&gt;
    from torchvision.ops.misc import FrozenBatchNorm2d
ModuleNotFoundError: No module named 'torchvision.ops'
Loading inference results...
Inference ended in error:
Failed to load the segmentation.
Something went wrong during the nnUNet processing.
Please check the logs for potential errors and contact the library maintainers.
</code></pre>
<p>Using Slicer 5.10.0 on 2020 MacBook Pro, OSX Tahoe 26.3.1.</p>

---
