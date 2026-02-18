# Isotropic voxel head CT

**Topic ID**: 18741
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/isotropic-voxel-head-ct/18741

---

## Post #1 by @LittleTchat (2021-07-14 20:10 UTC)

<p>Operating system: MacOS Catalina<br>
Slicer version: 4.11</p>
<p>Hi ! I’m new to Slicer and Python, so I apologize in advance if my question has already been asking or if it’s not clear. I’m working with 124 head CTs. The segmentations of the hematoma already had been made when we realize the spacing is not the same in the different orientation. We want to work with isotropic voxel. How can’t we change the dimension of the voxel of the volume and the segmentation with a jupyterNotebook? Manually, I think the module Resampling Scalar volume with a spacing of 1.0, 1.0, 10 and a linear interpolation could work, but how can I do this in a jupyterNotebook?</p>
<p>Thanks !</p>

---

## Post #2 by @lassoan (2021-07-18 02:36 UTC)

<p>You can use the “Specify geometry” button to change a segmentation’s geometry (origin, spacing, axis directions, or extents) as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---

## Post #3 by @LittleTchat (2021-07-19 15:08 UTC)

<p>Thank you, it’s very useful !</p>

---
