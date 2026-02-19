---
topic_id: 14930
title: "Draw A Fixed Sized Segment"
date: 2020-12-07
url: https://discourse.slicer.org/t/14930
---

# Draw a fixed sized segment

**Topic ID**: 14930
**Date**: 2020-12-07
**URL**: https://discourse.slicer.org/t/draw-a-fixed-sized-segment/14930

---

## Post #1 by @tenzin_kunkyab (2020-12-07 22:27 UTC)

<p>Hi Andras,</p>
<p>Is there a way to make a cubic segmentation of size 2 cm by 2 cm by 2 cm (just an example) in terms of its dimension? the symmetric option in scissor effect is not giving me what I need to do.</p>
<p>thank you so much</p>
<p>best<br>
Tenzin</p>

---

## Post #2 by @lassoan (2020-12-08 01:22 UTC)

<p>If you want to work with objects of known shape&amp;size then you would normally create a model of it (for a cube you can use <code>vtkCubeSource</code>) and import that into the segmentation using <code>AddSegmentFromClosedSurfaceRepresentation</code>. See example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_histogram_of_a_segmented_region">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_histogram_of_a_segmented_region</a></p>

---
