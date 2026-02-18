# Drawing 3D objects

**Topic ID**: 33236
**Date**: 2023-12-05
**URL**: https://discourse.slicer.org/t/drawing-3d-objects/33236

---

## Post #1 by @Dejf (2023-12-05 16:04 UTC)

<p>Hello, I am trying to segment coronary arteries by thresholding. My idea is to draw two ovoids (or any kind of object with adjustable dimensions in every directions), the first should be bigger that a heart and second should be smaller “inside heart”. By substraction of these two ovoids I should create the mask for thresholding. Is there any way to draw these kind of 3D shaped objects? Thank you.</p>

---

## Post #2 by @chir.set (2023-12-05 16:23 UTC)

<p>The ‘Surface cut’ effect of the ‘Segment editor’ can do that. You will need to install the ‘SegmentEditorExtraEffects’ extension to obtain this effect.</p>

---
