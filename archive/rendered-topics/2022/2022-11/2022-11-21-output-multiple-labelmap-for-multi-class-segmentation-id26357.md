---
topic_id: 26357
title: "Output Multiple Labelmap For Multi Class Segmentation"
date: 2022-11-21
url: https://discourse.slicer.org/t/26357
---

# Output multiple labelmap for multi-class segmentation

**Topic ID**: 26357
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/output-multiple-labelmap-for-multi-class-segmentation/26357

---

## Post #1 by @Dolzodmaa_D (2022-11-21 20:29 UTC)

<p>How can I save the binary label maps for each class I segmented? Or is it possible to output multi-color segmentation label map?</p>

---

## Post #2 by @lassoan (2022-12-01 06:36 UTC)

<p>By default (if segments don’t overlap) the segmentation that you save (.seg.nrrd file) is a multi-color segmentation label map.</p>
<p>If you want to have each segment in a separate volume then you can show one segment at a time and use “Export to files…” feature in Segmentations module with the “Visible segments only” option enabled.</p>
<p>You can also use <a href="https://github.com/lassoan/slicerio">slicerio</a> Python package to load a .seg.nrrd in any Python environment, get the list of segments and any segment or combination of segments as numpy arrays.</p>

---
