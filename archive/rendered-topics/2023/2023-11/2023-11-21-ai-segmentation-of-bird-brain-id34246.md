---
topic_id: 34246
title: "Ai Segmentation Of Bird Brain"
date: 2023-11-21
url: https://discourse.slicer.org/t/34246
---

# AI segmentation of bird brain

**Topic ID**: 34246
**Date**: 2023-11-21
**URL**: https://discourse.slicer.org/t/ai-segmentation-of-bird-brain/34246

---

## Post #1 by @Peter_Nguyen (2023-11-21 17:01 UTC)

<p>Hello! I am a undergraduate student researcher who is new to this area. I’ve recently started working on a project involving automatically segmenting CT scans of Bird Brains. I was wondering if you had tips on how to get started with this process? You mentioned that it is a matter of putting GPUs to use. I have a hand full of unsegmented nrrd files, as well as some manually segmented nrrd files.</p>

---

## Post #2 by @muratmaga (2023-11-21 17:27 UTC)

<p>There are multiple frameworks to train your own custom segmentation network. Here are pointers to two.</p>
<ol>
<li>
<p>Slicer extension for MONAILabel. <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer">MONAILabel/plugins/slicer at main · Project-MONAI/MONAILabel · GitHub</a></p>
</li>
<li>
<p>An example python script to use nn-Unet to train a segmentaiton network that we used in a recent SlicerMorph workshop. <a href="https://github.com/pieper/nnmouse">GitHub - pieper/nnmouse: Sample scripts for training nnU-Net on mouse fetus data</a></p>
</li>
</ol>
<p>In both cases the important thing is to have some label (segmented) data at hand so that you can do supervised training.</p>

---

## Post #3 by @Peter_Nguyen (2023-11-27 15:43 UTC)

<p>Thank you for your help - I am currently trying to follow this <a href="https://colab.research.google.com/drive/1X14nySzCZZ04exz8SZg6bBSdCMHzwZl0#scrollTo=F-o7cshEAlD9" rel="noopener nofollow ugc">guide</a>. But am running into a lot of issues, specifically around data loading. As it is, I have unsegmented nrrd files, manually segmented .seg.nrrd files, as well as folders containing .nii files which are the slices of the 3D nrrd files.</p>
<p>I also started out looking at the <a href="https://github.com/SlicerMorph/SlicerMEMOS" rel="noopener nofollow ugc">memos</a> module, but that is proving difficult to rework into code that works for my purposes. I was wondering if there was access to the code that was used to train/create the best_metric_model_largePatch_noise.pth model?</p>
<p>Edit: Here is the current code that I have tried (scratch), but am coming across an error that I don’t quite understand:</p>
<blockquote>
<p>RuntimeError: Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 1, 0, 108, 108, 455]</p>
</blockquote>
<pre><code class="lang-auto">import os
import torch
from torch.utils.data import DataLoader
from monai.transforms import (
    LoadImaged,
    EnsureChannelFirstd,
    ScaleIntensityd,
    SpatialCropd,
    ToTensord,
    Compose,
)
from monai.data import Dataset, NrrdReader
from monai.networks.nets import UNet
from monai.losses import DiceLoss

# Set your device (cuda if available, otherwise cpu)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class CustomDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.unsegmented_files = [file for file in os.listdir(data_dir) if file.endswith(".nrrd")]
        self.transform = Compose([
            LoadImaged(keys=["image"], reader=NrrdReader()),
            EnsureChannelFirstd(keys=["image"]),
            ScaleIntensityd(keys=["image"]),
            SpatialCropd(keys=["image"], roi_start=(10, 10, 10), roi_end=(118, 118, 118)),
            ToTensord(keys=["image"]),
        ])

    def __len__(self):
        return len(self.unsegmented_files)

    def __getitem__(self, index):
        unsegmented_path = os.path.join(self.data_dir, self.unsegmented_files[index])
        data = {"image": unsegmented_path}
        transformed_data = self.transform(data)
        
        # Check if the transformed image is empty after cropping
        if transformed_data["image"].shape[0] == 0:
            print(f"Skipping empty image after cropping: {unsegmented_path}")
            return self.__getitem__((index + 1) % len(self))  # move to the next item

        return transformed_data

# Create an instance of your dataset

data_dir = "/panfs/jay/groups/25/barkerfk/nguy4214/SimoneData/test"
dataset = CustomDataset(data_dir)

# print(dataset)

# Create a DataLoader for your dataset
batch_size = 1
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=0, pin_memory=True)

# Create a simple 3D U-Net model
model = UNet(
    spatial_dims=3,
    in_channels=1,
    out_channels=1,
    channels=(16, 32, 64, 128, 256),
    strides=(2, 2, 2, 2),
).to(device)

# Set up optimizer and loss function
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_function = DiceLoss(sigmoid=True)
# print(optimizer)

# Train the model
max_epochs = 10
for epoch in range(max_epochs):
    model.train()
    total_loss = 0.0
    for batch in data_loader:
        inputs = batch["image"].to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        
        targets = batch["label"].to(device) 
        loss = loss_function(outputs, targets)
        
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(data_loader)
    print(f"Epoch [{epoch+1}/{max_epochs}], Average Loss: {average_loss}")

# Save the trained model
torch.save(model.state_dict(), "segmentation_model.pth")</code></pre>

---

## Post #4 by @muratmaga (2023-11-27 15:58 UTC)

<aside class="quote no-group" data-username="Peter_Nguyen" data-post="3" data-topic="34246">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peter_nguyen/48/68397_2.png" class="avatar"> Peter_Nguyen:</div>
<blockquote>
<p>I am currently trying to follow this <a href="https://colab.research.google.com/drive/1X14nySzCZZ04exz8SZg6bBSdCMHzwZl0#scrollTo=F-o7cshEAlD9">guide</a>.</p>
</blockquote>
</aside>
<p>I don’t have access to that guide, so I can’t comment how appropriate it is.</p>
<aside class="quote no-group" data-username="Peter_Nguyen" data-post="3" data-topic="34246">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peter_nguyen/48/68397_2.png" class="avatar"> Peter_Nguyen:</div>
<blockquote>
<p>seg.nrrd files</p>
</blockquote>
</aside>
<p>You need to convert the segmentation files to labelmap for training. That might be your data load issue.</p>
<aside class="quote no-group" data-username="Peter_Nguyen" data-post="3" data-topic="34246">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peter_nguyen/48/68397_2.png" class="avatar"> Peter_Nguyen:</div>
<blockquote>
<p>t looking at the <a href="https://github.com/SlicerMorph/SlicerMEMOS">memos</a> module,</p>
</blockquote>
</aside>
<p>The code in memos is inference only, I don’t think that will help you much.</p>
<aside class="quote no-group quote-modified" data-username="Peter_Nguyen" data-post="3" data-topic="34246">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peter_nguyen/48/68397_2.png" class="avatar"> Peter_Nguyen:</div>
<blockquote>
<blockquote>
<p>RuntimeError: Expected 4D (unbatched) or 5D (batched) input to conv3d, but got input of size: [1, 1, 0, 108, 108, 455]</p>
</blockquote>
<pre><code class="lang-auto">
</code></pre>
</blockquote>
</aside>
<p>Try with segmentations converted to labelmap (right click and export as labelmap and save them).</p>

---

## Post #5 by @Peter_Nguyen (2024-01-23 14:32 UTC)

<p>Thank you for all of your help! I have been able to successfully create a model that makes predictions (accuracy TBD), and was looking to integrate it into the MEMOS module. It seems it is not as easy as plugging in my pth file and input images and running the module, as that has not worked for me so far.</p>
<p>My model is a 3D UNet designed for volumetric data and takes a single-channel (grayscale) input and outputs segmentation maps with a specified number of classes (5 in my case). The model was trained on patches extracted from 3D volumes. I was wondering if this approach is affecting whether or not I am able to utilize the model in MEMOS, and if you had any advice on how to go about this implementation?</p>
<p>Thank you again.</p>

---

## Post #6 by @muratmaga (2024-01-23 15:55 UTC)

<p>MEMOS is not a general-purpose tool for unet inference. It shouldn’t work, because I imagine you have different spatial dimensions, labels etc, than what MEMOS is expecting.</p>
<p>having said that you can easily modify those. So edit the source code of MEMOS.py, and change the relevant sections based on your MONAI model settings. Most of those should be in the logic section:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMEMOS/blob/main/MEMOS/MEMOS.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMEMOS/blob/main/MEMOS/MEMOS.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMEMOS/blob/main/MEMOS/MEMOS.py" target="_blank" rel="noopener">SlicerMorph/SlicerMEMOS/blob/main/MEMOS/MEMOS.py</a></h4>


      <pre><code class="lang-py">import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

import logging
import os
import sys
import tempfile
import shutil
import time
from glob import glob
from packaging import version

#
# MEMOS
#
class MEMOS(ScriptedLoadableModule):
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMEMOS/blob/main/MEMOS/MEMOS.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Peter_Nguyen (2024-01-30 15:09 UTC)

<p>Hello! I was making some changes to try and implement what you had mentioned, but was wondering how I can actually test the changes I make in 3D Slicer? Is there a simpler way to test changes that I have made to MEMOS.py?</p>

---

## Post #8 by @muratmaga (2024-01-30 15:31 UTC)

<p>You can edit and save the memos.py and restart the slicer and give it a try.</p>
<p>You can save a few clicks if you enable the developer mode (see slicer documentation)</p>

---

## Post #9 by @Peter_Nguyen (2024-01-30 15:40 UTC)

<p>I am able to download/edit MEMOS.py locally using VSCode, but was confused on how to load and use the edited version on 3D Slicer. I’m unsure what you mean by editing, is there a way to edit the module in 3D Slicer?</p>

---

## Post #10 by @muratmaga (2024-01-30 15:42 UTC)

<p>As long as you save the changed/edited MEMOS.py, the same you can simply restart slicer and the “changed” memos will be loaded into the slicer (not ours).</p>
<p>If you enable the Developer Mode things will be easier. Please look at slicer documentation at <a href="http://slicer.readthedocs.io">slicer.readthedocs.io</a>.</p>

---

## Post #11 by @Peter_Nguyen (2024-01-30 15:47 UTC)

<p>Thank you. I will look into developer mode!</p>

---

## Post #12 by @muratmaga (2024-01-30 16:58 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#developer-mode" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/settings.html#developer-mode</a></p>
<p>In short you do not need to rebuild slicer from the source to make changes to a python module. Just enable the developer mode, click the Edit button that will appear on top of the Memos module to make your changes to memos.py, save and then hit the reload button to reinitialize the memos module with your changes.</p>
<p>These will appear on top of python modules after you enable the Developer Mode and restart Slicer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2531d743ccfbcde28a20309b042c65dce355e5e.png" data-download-href="/uploads/short-url/yzHCvfr8qPsfMcXUqrK6gAMcct8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2531d743ccfbcde28a20309b042c65dce355e5e_2_669x499.png" alt="image" data-base62-sha1="yzHCvfr8qPsfMcXUqrK6gAMcct8" width="669" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2531d743ccfbcde28a20309b042c65dce355e5e_2_669x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2531d743ccfbcde28a20309b042c65dce355e5e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2531d743ccfbcde28a20309b042c65dce355e5e.png 2x" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">932×696 62.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Peter_Nguyen (2024-02-27 15:31 UTC)

<p>Hello again, I have been working on implementing my custom model into the MEMOS.py module, debugging, etc using developer mode. However, I am now encountering the issue seen in the attached  jpeg when trying to run my model with my own input. I was wondering if you have encountered this issue before? Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bf97b78a0dbd39a674deefb225f8d627e548296.jpeg" data-download-href="/uploads/short-url/jYgSFxHMIC4DhDHMEFDYrahrt5Q.jpeg?dl=1" title="Screen Shot 2024-02-27 at 9.26.22 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf97b78a0dbd39a674deefb225f8d627e548296_2_690x431.jpeg" alt="Screen Shot 2024-02-27 at 9.26.22 AM" data-base62-sha1="jYgSFxHMIC4DhDHMEFDYrahrt5Q" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf97b78a0dbd39a674deefb225f8d627e548296_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf97b78a0dbd39a674deefb225f8d627e548296_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf97b78a0dbd39a674deefb225f8d627e548296_2_1380x862.jpeg 2x" data-dominant-color="302F34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2024-02-27 at 9.26.22 AM</span><span class="informations">1920×1200 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @muratmaga (2024-02-27 16:49 UTC)

<aside class="quote no-group" data-username="Peter_Nguyen" data-post="13" data-topic="34246">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peter_nguyen/48/68397_2.png" class="avatar"> Peter_Nguyen:</div>
<blockquote>
<p>However, I am now encountering the issue seen in the attached jpeg when trying to run my model with my own input.</p>
</blockquote>
</aside>
<p>If you altered the MEMOS.py to fit your needs, then we can’t really help you, you really need to debug yourself. Is there anything in the Slicer log file. Screenshot only displays a crash notification.</p>
<p>Also you are using a fairly old Slicer, I would suggest working with the latest preview (or at least the current stable) version, if you are using MEMOs as a template to build your own module.</p>

---
