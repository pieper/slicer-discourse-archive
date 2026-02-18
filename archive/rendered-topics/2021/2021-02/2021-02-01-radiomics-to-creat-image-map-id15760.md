# Radiomics to creat image map

**Topic ID**: 15760
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/radiomics-to-creat-image-map/15760

---

## Post #1 by @Alsurayhi.H (2021-02-01 01:53 UTC)

<p>Is it possible to create an image map based on specific features extracted using radiomics (for example GLCM feature)?</p>

---

## Post #2 by @JoostJM (2021-03-09 12:32 UTC)

<p>Yes, it is called voxel-based radiomics and is supported in PyRadiomcis. On the commandline, simply add <code>--mode voxel</code> to enable this. However it is much, much more computationally intensive and will take a long time to compute (everything is calculated for each voxel instead of each image).</p>

---

## Post #3 by @Alsurayhi.H (2021-03-11 16:15 UTC)

<p>Thanks for your reply</p>

---
