---
topic_id: 48737
title: "Fine resolution scissors fill inside?"
date: 2026-11-05
url: https://discourse.slicer.org/t/48737
last_bumped: 2026-11-11T21:38:29.507Z
---

# Fine resolution scissors fill inside?

**Topic ID**: 48737
**Date**: 2026-11-05
**URL**: https://discourse.slicer.org/t/fine-resolution-scissors-fill-inside/48737

---

## Post #1 by @markcprosser (2026-11-05 21:29 UTC)

<p>Operating system: Ubuntu 22.04.5<br>
Slicer version: 5.12.4<br>
Expected behavior: Fine resolution scissor fill inside<br>
Actual behavior: Coarse resolution scissor fill inside</p>
<p>Hello,</p>
<p>I was using the 0.01mm (smallest possible) ‘paint’ on the ‘segment editor’ to colour in a feature and then realised scissors with ‘fill-inside’ and ‘free-form’ would probably be a better/faster way to do this, however while it works the resolution is much coarser than that of the 0.01mm ‘paint’ is it possible to make it this fine?</p>

---

## Post #2 by @mikebind (2026-11-11 21:38 UTC)

<p>Have you tried the “Draw” tool?  It allows you to fill in an arbitrarily drawn shape on a single slice, which sounds similar to what you are trying to accomplish using scissors (unless you want the 3D projection of the scissors tool).  In terms of resolution, all methods will be limited by the resolution of the segmentation (which is typically set at the resolution of the segmented image voxels, but could be modified using the Specify Geometry button).  A voxel of the segmentation is either included or not included in a segment, it cannot be partially included in a binary labelmap representation.</p>
<p>The documentation here may be helpful: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segment-editor" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a></p>

---
