# Obtaining Volume Information for Brain Segmentation Using Closed-Loop Markups in 3D Slicer

**Topic ID**: 31846
**Date**: 2023-09-22
**URL**: https://discourse.slicer.org/t/obtaining-volume-information-for-brain-segmentation-using-closed-loop-markups-in-3d-slicer/31846

---

## Post #1 by @sund (2023-09-22 14:44 UTC)

<p>Hello everyone,</p>
<p>I have been using the closed-loop markup module in 3D Slicer to segment the brain on individual MRI slices. Now, I am trying to obtain volume information for the entire brain by considering the closed-loop markup delineations from all slices collectively.</p>
<p>Is there a straightforward way to calculate the total volume of the brain based on these closed-loop markups in 3D Slicer? Your guidance and suggestions would be greatly appreciated.</p>
<p>Thank you in advance!</p>

---

## Post #2 by @pieper (2023-09-22 15:36 UTC)

<p>I don’t think there’s an easy way to go from a closed curve markup to a volume calculation.</p>
<p>The Draw tool in the Segment Editor is similar and creates segmentations directly, and volumes can be calculated with the Segment Statistics module.</p>

---
