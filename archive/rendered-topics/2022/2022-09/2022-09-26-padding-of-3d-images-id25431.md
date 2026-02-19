---
topic_id: 25431
title: "Padding Of 3D Images"
date: 2022-09-26
url: https://discourse.slicer.org/t/25431
---

# Padding of 3d images

**Topic ID**: 25431
**Date**: 2022-09-26
**URL**: https://discourse.slicer.org/t/padding-of-3d-images/25431

---

## Post #1 by @Aditya_Prabhakara_Ka (2022-09-26 02:36 UTC)

<p>Hi,<br>
I have a question regarding the padding of 3d images (.nrrd). Say my image dimension is [256,197,19] and I want my image to have a size of length and width of 256 and channel 30 making it [256,256,30]. What is the syntax for padding of zeros?</p>
<p>If i were to use np.pad(data,((256,----))then how do I adjust my channel width from 19 to 30?</p>
<p>Thank you so much!!!</p>

---

## Post #2 by @lassoan (2022-09-26 02:46 UTC)

<p>Medical images are not just specified by a 3D array of voxels but also by the origin, spacing, and axis directions of the image. Therefore, <em>padding</em> is generally not sufficient to bring images into the same space. Instead, images are <em>resampled</em> to have matching array size, origin, spacing, and axis directions.</p>
<p>This is a built-in feature in many modules (e.g., when you export a segmentation then you can specify a reference volume that specifies the desired geometry) and there are also several modules developed specifically for just resampling (see for example how one is used in this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-random-deformations-to-image">example</a>). If you describe what you would like to achieve, then we can give more specific advice.</p>

---
