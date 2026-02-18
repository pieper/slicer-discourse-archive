# How to mark paint 3d segment?

**Topic ID**: 17687
**Date**: 2021-05-19
**URL**: https://discourse.slicer.org/t/how-to-mark-paint-3d-segment/17687

---

## Post #1 by @Chintha_Siva_Prasad (2021-05-19 06:24 UTC)

<p>How can I get a portion of 3d volume by painting on it?</p>

---

## Post #2 by @lassoan (2021-05-19 12:41 UTC)

<p>You can blank out a volume outside and arbitrary region by using “Mask volume” effect in Segment Editor module. You can also crop a volume to the bounding rectangle of a segment by using “Split volume” effect (provided by SegmentEditorExtraEffects extension).</p>

---
