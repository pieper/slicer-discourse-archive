---
topic_id: 3197
title: "Export Segmentation Results 3D Labels To Multiple 2D Images"
date: 2018-06-15
url: https://discourse.slicer.org/t/3197
---

# Export segmentation results (3d labels) to multiple 2d images (for deep learning training)?

**Topic ID**: 3197
**Date**: 2018-06-15
**URL**: https://discourse.slicer.org/t/export-segmentation-results-3d-labels-to-multiple-2d-images-for-deep-learning-training/3197

---

## Post #1 by @xiaowei (2018-06-15 16:12 UTC)

<p>I use Slicer to segment CT/MRI images. Currently I would like to try deep learning on medical image segmentation.</p>
<p>For deep learning, we need to prepare the training data first. Particularly, if we have 200 images for one CT (then the input is 200<em>height</em>width), then we need a labeled image set for this CT and it also has 200 images (200<em>height</em>width).</p>
<p>The problem is I can manually segment the CT now. However, do anyone know how to export the segmented results (e.g., the input is 200<em>height</em>width) to a 2d image set (e.g., 200 images and their dimension is height*width)?<br>
(exporting it to stl and than performing slicing is a choice but  is inconvenient and time-consuming)</p>
<p>I have just used Slicer for 3 months, and thank you for your help.</p>

---

## Post #2 by @lassoan (2018-06-15 16:27 UTC)

<p>I’m not sure that dumping image slices into series of 2D files would be the best approach. Consumer file formats (jpeg, png, etc.) are not well suited for storing metadata that is very common for medical image computing (axis directions, origin, pixel and slice spacing), they may not support 16-bit grayscale images, etc.</p>
<p>I would recommend to have a look at existing approaches for file storage, data normalization, and augmentation for deep learning in medical images.</p>
<p><a class="mention" href="/u/raul">@raul</a>’s group using HDF file format for deep learning, which allows structure storage of 3D medical images (including all metadata, arbitrary pixel type, etc).</p>
<p>You may check out <a href="http://www.deepinfer.org/pages/about/">DeepInfer</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DeepInfer">DeepInfer Slicer extension</a>, see how models are created, etc.</p>
<p>You can get some ideas from <a href="https://arxiv.org/pdf/1709.03485.pdf">NiftyNet</a>, too.</p>

---

## Post #3 by @xiaowei (2018-06-15 19:11 UTC)

<p>Thanks, Lassoan!</p>
<p>Do you know how to export the segmentation results to HDF format?</p>

---

## Post #4 by @lassoan (2018-06-17 01:36 UTC)

<p>I’ll participate in a project to explore this, but we’ll get there in a few months. Maybe <a class="mention" href="/u/raul">@raul</a> can comment on how they create them now.</p>
<p>What you can do easily now is to export segmentation as 4D NRRD file (each segment is a 3D subvolume). If segments don’t overlap then you can also export segmentation to labelmap node and save it as 3D NRRD file.</p>

---

## Post #5 by @Shannon_Chow (2018-12-14 05:45 UTC)

<p>How do you solve this problem？</p>

---
