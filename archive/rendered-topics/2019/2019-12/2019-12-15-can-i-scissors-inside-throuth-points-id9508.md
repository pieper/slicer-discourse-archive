# Can I Scissors Inside throuth points?

**Topic ID**: 9508
**Date**: 2019-12-15
**URL**: https://discourse.slicer.org/t/can-i-scissors-inside-throuth-points/9508

---

## Post #1 by @timeanddoctor (2019-12-15 14:49 UTC)

<p>Can I Scissors Inside  throuth markupNode created myself?</p>

---

## Post #2 by @lassoan (2019-12-15 23:44 UTC)

<p>Markups node positions are defined in patient coordinates in 3D, while <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorScissorsEffect.cxx#L507-L807">input points for scissors effect</a> are specified in display coordinate system. If you have points in 3D, then you can create a cut surface using “Surface cut” effect (in SegmentEditorExtraEffects extension).</p>

---
