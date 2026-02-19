---
topic_id: 10832
title: "Volume Measurement"
date: 2020-03-25
url: https://discourse.slicer.org/t/10832
---

# Volume measurement

**Topic ID**: 10832
**Date**: 2020-03-25
**URL**: https://discourse.slicer.org/t/volume-measurement/10832

---

## Post #1 by @Sami_Fattouh (2020-03-25 15:36 UTC)

<p>hello<br>
what is the best way to measure the exact volume of a specific area</p>

---

## Post #2 by @Sam_Horvath (2020-03-25 15:51 UTC)

<p>A good flow would be to segment the area with the Segment Editor, then calculate the volume using the label map statistics in the Segment Statistics module.</p>
<p>Segment Editor: <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a><br>
Segment Statistics: <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmentstatistics.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/user_guide/module_segmentstatistics.html</a></p>

---
