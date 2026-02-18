# How to import two stl, superimpose and get volume differences

**Topic ID**: 14262
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/how-to-import-two-stl-superimpose-and-get-volume-differences/14262

---

## Post #1 by @bharat (2020-10-27 05:45 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2021-09-07 22:03 UTC)

<p>You can load the STL files as segmentations and use <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#segment-comparison-module-overview">Segment Comparison module</a> to compare them. You can also subtract the segments from each other and compute volumes using <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#Segment-statistics-module-overview">Segment statistics module</a>.</p>

---
