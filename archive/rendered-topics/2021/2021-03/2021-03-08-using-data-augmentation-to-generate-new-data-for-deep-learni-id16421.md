---
topic_id: 16421
title: "Using Data Augmentation To Generate New Data For Deep Learni"
date: 2021-03-08
url: https://discourse.slicer.org/t/16421
---

# Using data augmentation to generate new data for deep learning

**Topic ID**: 16421
**Date**: 2021-03-08
**URL**: https://discourse.slicer.org/t/using-data-augmentation-to-generate-new-data-for-deep-learning/16421

---

## Post #1 by @Abdulrahman (2021-03-08 06:31 UTC)

<p>Hi everyone,<br>
what is the best module to create new data of MRI heads using affine transformation, the volumes and their segmentation (binary labelmap) saved in NIFTI format ?</p>
<p>detailed steps are really appreciated…</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-03-08 16:15 UTC)

<p>hi - You could try TorchIO.  Let us know if how it works for you.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/fepegar/SlicerTorchIO" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/12688084?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/fepegar/SlicerTorchIO" target="_blank" rel="noopener">fepegar/SlicerTorchIO</a></h3>


  <p><span class="label1">3D Slicer module for TorchIO. Contribute to fepegar/SlicerTorchIO development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2021-03-08 16:39 UTC)

<p>Since affine transformation is so simple, you shouldn’t even need to create new data but augment your input data during learning. If you use monai then you can <a href="https://docs.monai.io/en/latest/highlights.html#medical-image-data-i-o-processing-and-augmentation">enable random transformations during training</a>.</p>

---

## Post #4 by @Abdulrahman (2021-03-08 23:10 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thanks for that, I’ll try it</p>

---

## Post #5 by @Abdulrahman (2021-03-08 23:25 UTC)

<p>Thanks Dr <a class="mention" href="/u/lassoan">@lassoan</a>, the supervisor of our project is a big fan of MATLAB and actually we have achieved good results so far but we need to improve the accuracy.<br>
So is there any module that can accept an image and its segmentation in NIFTI format and apply augmentation on these images?</p>
<p>thanks again for your help</p>

---

## Post #6 by @pieper (2021-03-08 23:31 UTC)

<p>Yes, you can load images and segmentations in nifti format to Slicer.</p>

---

## Post #7 by @Abdulrahman (2021-03-09 00:49 UTC)

<p>Sorry, can you elaborate on this:<br>
(TorchIO returned the error: Traceback (most recent call last):<br>
File “C:/Users/z5049553/AppData/Roaming/NA-MIC/Extensions-29402/TorchIO/lib/Slicer-4.11/qt-scripted-modules/TorchIOTransforms.py”, line 201, in onApplyButton<br>
outputImage = self.currentTransform(inputVolumeNode, outputVolumeNode)<br>
File “C:\Users\z5049553\AppData\Roaming\NA-MIC\Extensions-29402\TorchIO\lib\Slicer-4.11\qt-scripted-modules\TorchIOTransformsLib\Transform.py”, line 119, in <strong>call</strong><br>
tensor = torch.from_numpy(data.astype(np.float32))  # why do I need this? Open a TorchIO issue?<br>
AttributeError: ‘Tensor’ object has no attribute ‘astype’</p>
<p>Transform kwargs:<br>
{‘scales’: (0.5, 1.5), ‘degrees’: (0.0, 45.0), ‘translation’: (0.0, 1.0), ‘isotropic’: True, ‘image_interpolation’: ‘linear’, ‘default_pad_value’: ‘minimum’})</p>
<p>I’m not familiar with Torch environment</p>

---

## Post #8 by @lassoan (2021-03-09 00:57 UTC)

<p>Maybe you are trying to process a color (or multi-channel grayscale) image. Maybe you saved the image to a consumer file format (jpg, png, tiff, …) and the file writer converted automatically. Convert the image to single-component and see if it works well. If not, then report the error to the extension’s bugtracker.</p>

---

## Post #9 by @Abdulrahman (2021-03-09 01:06 UTC)

<p>I exported an image as a volume (.nii) and volume label map as segmentation but doesn’t work.<br>
also I exported the image without segmentation as a single input but still the same error shows up</p>

---

## Post #10 by @lassoan (2021-03-09 01:54 UTC)

<p>If <a class="mention" href="/u/fernando">@Fernando</a> does not respond here within a few days then I would recommend to submit a question/bug report to Torchio.</p>

---

## Post #11 by @Fernando (2021-03-09 08:37 UTC)

<p>Hi, <a class="mention" href="/u/abdulrahman">@Abdulrahman</a>. Thanks <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for pinging me.</p>
<p>The error that you got was fixed yesterday: <a href="https://github.com/fepegar/torchio/issues/475" class="inline-onebox" rel="noopener nofollow ugc">'Tensor' object has no attribute 'astype' · Issue #475 · fepegar/torchio · GitHub</a>. It should work in today’s version (latest Preview).</p>
<p>You can use the Slicer TorchIO extension for experimenting with the transforms parameters but, as Andras, I don’t recommend using it for the actual augmentation. I also think it’s better to augment the data during training, instead of beforehand. This means that training will be more computationally expensive, but you’ll need less storage and, more importantly, your data will be more diverse. An example of augmenting your MRI and corresponding segmentation simultaneously:</p>
<pre><code class="lang-python">import torchio as tio
subject = tio.Subject(
    mri=tio.ScalarImage('path_mri.nii.gz'),
    seg=tio.LabelMap('path_seg.nrrd'),
)
transform = tio.RandomAffine()
transformed = transform(subject)
</code></pre>
<p>There are many examples in the <a href="https://torchio.readthedocs.io/" rel="noopener nofollow ugc">documentation</a>. If you have any questions, you can use the <a href="https://github.com/fepegar/torchio/discussions" rel="noopener nofollow ugc">Discussions</a> tab in the GitHub repository.</p>
<p>I also work very closely with the MONAI team. In my opinion, if you choose to use MONAI, you’ll need to do less coding but have less control over what’s going on.</p>

---

## Post #12 by @Abdulrahman (2021-03-09 23:49 UTC)

<p>Hi, <a class="mention" href="/u/fernando">@Fernando</a><br>
Thanks for your reply. I’ve deleted and installed TorchIO again but the same error still existing.<br>
Meanwhile, I’m gonna try to augment during training as you advised.</p>
<p>Thanks again</p>

---

## Post #13 by @Fernando (2021-03-10 11:12 UTC)

<p>What version of Slicer are you using (Help → About 3D Slicer)? Can you please install the <a href="https://download.slicer.org/" rel="noopener nofollow ugc">Preview release</a> and try again?</p>

---

## Post #14 by @Abdulrahman (2021-03-10 23:36 UTC)

<p>It is (4.11.20200930 r29402 / 002be18). I’ve installed the latest release and it works.</p>
<p>Thanks</p>

---

## Post #15 by @Abdulrahman (2021-03-29 07:02 UTC)

<p>Hi, <a class="mention" href="/u/fernando">@Fernando</a><br>
Hoping you’re well,</p>
<p>After almost 3 weeks of hard attempts to deal with MATLAB, I found it is the time to move to PYTHON.</p>
<p>As you suggest using MONAI, Do you recommend any step by step materials for beginners?</p>
<p>My project simply is implement 3D Unet to segment healthy brains. Datasets have been segmented using Slicer and saved in NIFTI format (images + labelmap).</p>
<p>Thanks again <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #16 by @Fernando (2021-03-29 09:18 UTC)

<p>Here’s a tutorial to segment brains from healthy subjects using a 3D U-Net: <a href="https://github.com/fepegar/torchio/tree/master/examples#general" rel="noopener nofollow ugc">TorchIO tutorial on Google Colab</a>.</p>
<p>If you decide to use MONAI instead, there are some tutorials <a href="https://github.com/Project-MONAI/tutorials" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #17 by @dave3d (2021-03-29 13:39 UTC)

<p>The SimpleITK Notebooks have an example on using SimpleITK to do data augmentation that might be of interest.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks/blob/master/Python/70_Data_Augmentation.ipynb" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks/blob/master/Python/70_Data_Augmentation.ipynb" target="_blank" rel="noopener nofollow ugc">InsightSoftwareConsortium/SimpleITK-Notebooks/blob/master/Python/70_Data_Augmentation.ipynb</a></h4>
<pre><code class="lang-ipynb">{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "&lt;h1 align=\"center\"&gt;Data Augmentation for Deep Learning &lt;a href=\"https://mybinder.org/v2/gh/InsightSoftwareConsortium/SimpleITK-Notebooks/master?filepath=Python%2F70_Data_Augmentation.ipynb\"&gt;&lt;img style=\"float: right;\" src=\"https://mybinder.org/badge_logo.svg\"&gt;&lt;/a&gt;&lt;/h1&gt;\n",
    "\n",
    "This notebook illustrates the use of SimpleITK to perform data augmentation for deep learning. Note that the code is written so that the relevant functions work for both 2D and 3D images without modification.\n",
    "\n",
    "Data augmentation is a model based approach for enlarging your training set. The problem being addressed is that the original dataset is not sufficiently representative of the general population of images. As a consequence, if we only train on the original dataset the resulting network will not generalize well to the population (overfitting). \n",
    "\n",
    "Using a model of the variations found in the general population and the existing dataset we generate additional images in the hope of capturing the population variability. Note that if the model you use is incorrect you can cause harm, you are generating observations that do not occur in the general population and are optimizing a function to fit them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
</code></pre>

  This file has been truncated. <a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks/blob/master/Python/70_Data_Augmentation.ipynb" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #18 by @Fernando (2021-03-29 13:55 UTC)

<p>Thanks, <a class="mention" href="/u/dave3d">@dave3d</a>. Although TorchIO’s API is very similar to <code>torchvision</code>'s, it relies heavily on SimpleITK for preprocessing and augmentation.</p>

---

## Post #19 by @Abdulrahman (2021-03-30 06:25 UTC)

<p>Hi, <a class="mention" href="/u/fernando">@Fernando</a><br>
sorry for keep asking.</p>
<p>Do know any tutorial for  3D multi-class semantic segmentation of brain (classes are CSF, white matter and grey matter)?</p>
<p>Thanks</p>

---

## Post #20 by @Fernando (2021-03-30 10:25 UTC)

<p>This discussion is not really related to Slicer. You can post on the TorchIO <a href="https://github.com/fepegar/torchio/discussions" rel="noopener nofollow ugc">Discussions</a> tab, if you have more unrelated questions.</p>
<p>I haven’t written any tutorial for multiclass segmentation, but it’s really very similar to the one I shared, so I recommend you take a look.</p>

---
