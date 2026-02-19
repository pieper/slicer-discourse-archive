---
topic_id: 3524
title: "Load Segment From Matrix Of Integers"
date: 2018-07-19
url: https://discourse.slicer.org/t/3524
---

# Load segment from matrix of integers

**Topic ID**: 3524
**Date**: 2018-07-19
**URL**: https://discourse.slicer.org/t/load-segment-from-matrix-of-integers/3524

---

## Post #1 by @alessandronavacchia (2018-07-19 14:39 UTC)

<p>Hi all,</p>
<p>I have been exporting and importing segmentation masks as .stl files or other formats that describe the segmented volume as a surface mesh made of triangular elements.</p>
<p>I was wondering if it is possible to load segmentation masks described as a 3d matrix of ones and zeros, in which each element represents a voxel of the image volume (1 = included in the mask, 0 = not included).</p>
<p>Any help with this would be appreciated! Thanks!</p>
<p>Alessandro</p>

---

## Post #2 by @lassoan (2018-07-19 19:00 UTC)

<p>I think this example does exactly what you asked: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D</a></p>

---
