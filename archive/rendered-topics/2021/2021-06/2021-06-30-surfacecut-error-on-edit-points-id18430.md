# SurfaceCut : error on edit points

**Topic ID**: 18430
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/surfacecut-error-on-edit-points/18430

---

## Post #1 by @chir.set (2021-06-30 13:55 UTC)

<p>Sorry to bother you again.</p>
<p>Editing placed points in SurfaceCut generates this error :</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “/home/user/bin/Slicer_Ext/SlicerSegmentEditorExtraEffects/SegmentEditorSurfaceCut/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py”, line 257, in onEdit<br>
self.logic.setPointsFromString(self, self.segmentMarkupNode, fPosStr)<br>
TypeError: setPointsFromString() takes 3 positional arguments but 4 were given</p>
</blockquote>
<p>Using SlicerSegmentEditorExtraEffects at 9933c4c2175.</p>
<p>Regards.</p>

---

## Post #2 by @jamesobutler (2021-06-30 14:47 UTC)

<p>This was resolved yesterday in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/pull/40" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix traceback due to incorrect number of input arguments by jamesobutler · Pull Request #40 · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a> and is available in the latest version of SegmentEditorExtraEffects that can be downloaded with the latest Slicer Preview using the ExtensionsManager.</p>

---
