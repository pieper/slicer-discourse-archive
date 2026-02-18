# Trying to understand the different coordinate systems

**Topic ID**: 27332
**Date**: 2023-01-18
**URL**: https://discourse.slicer.org/t/trying-to-understand-the-different-coordinate-systems/27332

---

## Post #1 by @spodamon (2023-01-18 19:04 UTC)

<p>I am trying to make a bounding box based on a segmentation. I initially tried using SimpleITK and their LabelShapeStatisticsImageFilter class and their GetBoundingBox method to get some coordinates. When I tried doing the same thing in Slicer, the coordinates of the bounding box appears to be different. I understand their might be a difference in the coordinate system but I’m not fully understanding it even after reading the documentation. I just want to confirm that both outputs are essentially the same. Is there are a formula I should use to convert the outputs from the SimpleITK method to match the outputs of the Slicer method? Thank you again .</p>

---
