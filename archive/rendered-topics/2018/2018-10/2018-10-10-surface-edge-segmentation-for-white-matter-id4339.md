# Surface/Edge Segmentation for White Matter

**Topic ID**: 4339
**Date**: 2018-10-10
**URL**: https://discourse.slicer.org/t/surface-edge-segmentation-for-white-matter/4339

---

## Post #1 by @Hassan_Farhat (2018-10-10 02:11 UTC)

<p>Dear Community,</p>
<p>I’m working on segmented Brain MRI images (GM, WM, CSF), I would like to extract a continuous boundary for White matter to be able to test specific algorithms. Since WM maps are probability maps, I have difficulty to extract a linked continuous boundary. I have created as well some phantoms to help test my boundary extraction algorithms. Is there any tools in SLICER that can help in extracting a thin (1 voxel wide) 3D WM boundary?</p>
<p>Best Regards<br>
Hassan Farhat</p>

---

## Post #2 by @lassoan (2018-10-10 13:10 UTC)

<p>You can threshold the probability map to get a thick boundary and then thin it to a single-voxel surface using “Extract skeleton” module (Skeleton type: 2D; Do not prune branches: enabled).</p>

---
