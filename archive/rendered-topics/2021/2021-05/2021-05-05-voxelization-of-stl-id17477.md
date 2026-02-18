# Voxelization of STL

**Topic ID**: 17477
**Date**: 2021-05-05
**URL**: https://discourse.slicer.org/t/voxelization-of-stl/17477

---

## Post #1 by @wangyunning (2021-05-05 15:56 UTC)

<p>Operating system: Windows 10</p>
<p>Slicer version: 4.11.1</p>
<p>Hi all!</p>
<p>I am new to 3Dslicer, and I am doing a project of spinal segmentation. Now I have both the STL model and the segmented CT image of vertebra. I am wondering whether I can fill the gray value corresponding to the pixel points of CT into the three-dimensional STL model in 3Dslicer，so I can get all the grayscale values on this plane.<br>
Any insight into this matter will be greatly appreciated.</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2021-05-21 18:22 UTC)

<p>You can import the model to a segmentation node then use Mask volume effect to fill regions inside/outside the segment with constant value.</p>

---
