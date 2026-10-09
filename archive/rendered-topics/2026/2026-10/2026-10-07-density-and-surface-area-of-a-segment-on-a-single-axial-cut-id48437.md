---
topic_id: 48437
title: "Density and surface area of a segment on a single axial cut"
date: 2026-10-07
url: https://discourse.slicer.org/t/48437
last_bumped: 2026-10-08T15:59:04.267Z
---

# Density and surface area of a segment on a single axial cut

**Topic ID**: 48437
**Date**: 2026-10-07
**URL**: https://discourse.slicer.org/t/density-and-surface-area-of-a-segment-on-a-single-axial-cut/48437

---

## Post #1 by @Mahdi_H (2026-10-07 19:56 UTC)

<p>Hello everyone!</p>
<p>I am new to the 3d slicer software and its powerful features.</p>
<p>I am currently planning a research project and have been successful in running totalsegmentator to segment tissues I am interested in. I have now to get the density and surface area of the segmented tissues I generate on a single axial cut. Can anyone please provide with simple, beginner-level, instructions on how to do so?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @Esteban_Barreiro (2026-10-08 15:59 UTC)

<p>Hi! You can run “Segment Statistics” for your quantification based on label maps, the corresponding Scalar Volume and Closed Surface.<br>
documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" rel="noopener nofollow ugc">Segment statistics — 3D Slicer documentation</a><br>
Hope this help.</p>

---
