# How can I quantify the difference between two similar models after superimposing the two models?

**Topic ID**: 489
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/how-can-i-quantify-the-difference-between-two-similar-models-after-superimposing-the-two-models/489

---

## Post #1 by @Ramttoong (2017-06-13 02:36 UTC)

<p>How can I quantify the difference between two similar models after superimposing the two models?</p>

---

## Post #2 by @lassoan (2017-06-13 12:04 UTC)

<ul>
<li>For qualitative assessment (surface color coded by closest distance): install Model to model distance extension, use Model to model distance module.</li>
<li>For quantitative assessment (95th percentile of Hausdorff distance, Dice): install SlicerRT extensions, using Segmentations module import your models into a segmentation node, use Sement comparison module to compute metrics.</li>
</ul>

---
