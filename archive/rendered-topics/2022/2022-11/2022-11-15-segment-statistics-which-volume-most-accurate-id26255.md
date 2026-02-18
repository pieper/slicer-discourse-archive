# Segment statistics: which volume most accurate

**Topic ID**: 26255
**Date**: 2022-11-15
**URL**: https://discourse.slicer.org/t/segment-statistics-which-volume-most-accurate/26255

---

## Post #1 by @hannahmed (2022-11-15 19:45 UTC)

<p>Hello everyone,</p>
<p>I am fairly new to 3D Slicer and have a question regarding segment statistics: I have segmented a structure from an MRI scan and want to identify the volume of it. Which volume is the most accurate/ meaningful (scalar volume, lable map volume, closed surface volume), as they all show different values?</p>
<p>I’d appreciate any help. Thank you!</p>

---

## Post #2 by @lassoan (2022-12-01 07:20 UTC)

<p>Scalar volume and labelmap volume should be the same, unless the scalar volume is smaller than the segment (then you probably want to use the labelmap based image, because the scalar volume based measurement only contain the parts inside the scalar volume).</p>
<p>Difference between labelmap and closed surface volume should be negligible, just be consistent and always the same. If you work with mostly the exported mesh then you may use the volume computed from the closed surface, otherwise you may prefer to use the labelmap based volume.</p>

---
