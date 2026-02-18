# Marking points on images

**Topic ID**: 18610
**Date**: 2021-07-10
**URL**: https://discourse.slicer.org/t/marking-points-on-images/18610

---

## Post #1 by @anitakh1 (2021-07-10 07:00 UTC)

<p>Sir, how to i mark 0s and 1s as point coordinates in different colors in an image using 3D slicer?</p>

---

## Post #2 by @lassoan (2021-07-12 04:17 UTC)

<p>You can access the volume as a numpy array as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">here</a> and modify the voxels by changing values in this array.</p>

---
