---
topic_id: 18338
title: "Segment Registration Is Voxelbase Registration"
date: 2021-06-25
url: https://discourse.slicer.org/t/18338
---

# Segment registration is Voxelbase registration？

**Topic ID**: 18338
**Date**: 2021-06-25
**URL**: https://discourse.slicer.org/t/segment-registration-is-voxelbase-registration/18338

---

## Post #1 by @lili-yu22 (2021-06-25 12:53 UTC)

<p>Operating system:windows<br>
Slicer version:3Dslicer4.11.20210226<br>
Expected behavior:May I ask the segment registration is the Voxelbase registration？What’s the principle of the surface registration？<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2021-06-25 17:41 UTC)

<p>Segment registration registers distance maps computed from the segments. See details in the <a href="https://github.com/SlicerRt/SegmentRegistration#segment-registration">papers listed in the extension’s documentation</a>.</p>

---
