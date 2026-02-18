# Voxel-based feature extraction

**Topic ID**: 19060
**Date**: 2021-08-04
**URL**: https://discourse.slicer.org/t/voxel-based-feature-extraction/19060

---

## Post #1 by @Sovan_Mukherjee (2021-08-04 18:29 UTC)

<p>Hi,</p>
<p>I am trying to do a voxel-based feature extraction based on a CT pancreas mask. After setting Voxelbased = True, I extracted 88 features. It created 88 nifti images for individual features. While looking at the images, i realized that it has the extracted feature maps from the mask as well from the background (voxels outside the mask). I would like to feed the feature maps into a classifier to get a probability map. But I don’t feed the features that are calculated outside the mask.</p>
<p>Is there any way I can generate feature map only for the mask voxel?</p>
<p>Will appreciate any help.</p>

---

## Post #2 by @pieper (2021-08-04 22:54 UTC)

<p>You can write a short numpy script mask out only the voxels you want to keep.</p>

---
