---
topic_id: 24772
title: "Fix Image Resolutions And Number Of Slices Of Ct Images To F"
date: 2022-08-15
url: https://discourse.slicer.org/t/24772
---

# Fix Image Resolutions and number of slices of CT images to fit with pet image

**Topic ID**: 24772
**Date**: 2022-08-15
**URL**: https://discourse.slicer.org/t/fix-image-resolutions-and-number-of-slices-of-ct-images-to-fit-with-pet-image/24772

---

## Post #1 by @morgenmuesli (2022-08-15 19:18 UTC)

<p>Hello, I am a total beginner with 3d Slicer so please excuse me and feel free to direct me to the appropriate page if the question is trivial.<br>
I’ve got a Dataset of labeled PET/CT Volumes, where there are Full Body PET and low dose CT Volume and high dose CT Volume of the breast areas which I want to use as training data.</p>
<p>The problem is that the resolution of the PET Data is 200x200x619 and shows the whole body while the resolution of the high-dose CT Data is 512x512x278.</p>
<p>The Volumes are pre-registered by the segmentation author but I need that the resolution of both volumes to be equal.</p>
<p>How can I do this in 3d Slicer and how can I automate it to preprocess the whole dataset.</p>
<p>Thanks for your advice.</p>
<p>Cheers Christoph</p>

---

## Post #2 by @pieper (2022-08-23 18:42 UTC)

<p>If you didn’t already figure this out, you can use the Resample Image (BRAINS) module for this task.</p>

---
