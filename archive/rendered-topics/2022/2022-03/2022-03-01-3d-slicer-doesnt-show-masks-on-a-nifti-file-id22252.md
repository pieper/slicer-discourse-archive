# 3D slicer doesn't show masks on a NIfTI file

**Topic ID**: 22252
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/3d-slicer-doesnt-show-masks-on-a-nifti-file/22252

---

## Post #1 by @Kamyar_Ghabili (2022-03-01 22:20 UTC)

<p>Hi. I want to see masked images as NIftI format using 3D slicer. I use “Add Data” option and upload the file. I can see the images on 3D slicer but not the masks (segmentations). Do you have any idea how to fix this? Thank you.</p>

---

## Post #2 by @lassoan (2022-03-01 22:37 UTC)

<p>When you load a nifti file by default it is assumed that it is a scalar volume. Since scalar values are continuous, value of 1 will look almost the same as the background value of 0.</p>
<p>To load a “mask” (it is called a segmentation or labelmap volume in Slicer) you need to indicate this in the “Add data” window as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">here</a>.</p>

---
