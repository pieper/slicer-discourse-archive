---
topic_id: 47460
title: "2D slice draw/erase maps to adjacent slice in 3D instead of current"
date: 2026-06-25
url: https://discourse.slicer.org/t/47460
last_bumped: 2026-06-25T12:34:49.735Z
---

# 2D slice draw/erase maps to adjacent slice in 3D instead of current

**Topic ID**: 47460
**Date**: 2026-06-25
**URL**: https://discourse.slicer.org/t/2d-slice-draw-erase-maps-to-adjacent-slice-in-3d-instead-of-current/47460

---

## Post #1 by @falko76 (2026-06-25 12:34 UTC)

<p>CT scan, using Watershed or Grow from Seeds from SegmentEditorExtraEffects. Detecting a bone OK and clicking apply.<br>
Segment mapping is done and visually in 2d and 3d it looks fine, but erasing or drawing in 2d affects not current slice, but adjacent one (like shifted by 1).<br>
It is easily visible when editing first or last slice of the bone - on last slice when you are at slice when there is no more segment you edit, you can see the cursor in 3d in proper place, but when you erase that “empty” slice in 2D, in 3D it erases the content from previous slice. When you try it from other end, and strart with first slice segment, erase it (or draw, doesnt matter), it edits one slice below.</p>

---
