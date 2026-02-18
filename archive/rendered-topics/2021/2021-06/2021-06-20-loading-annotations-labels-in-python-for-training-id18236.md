# Loading annotations/labels in python for training

**Topic ID**: 18236
**Date**: 2021-06-20
**URL**: https://discourse.slicer.org/t/loading-annotations-labels-in-python-for-training/18236

---

## Post #1 by @Dhruba (2021-06-20 16:55 UTC)

<p>I want to load my nii.gz file and corresponding ROI annotations (.csv) in python for training purposes. I am not sure the right way to do that. Can you give me some reference code or documentation on loading annotations? Also, how can I be sure if the annotation is in the right place after loading in? Is there a way to check this?</p>

---

## Post #2 by @lassoan (2021-06-24 16:01 UTC)

<p>See specification of markups file formats <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html">here</a>.</p>
<p>All the file formats are human-readable and self-describing, so you can just save a markups (point list, line, curve, ROI, …) in Slicer and see what information is saved and how.</p>

---
