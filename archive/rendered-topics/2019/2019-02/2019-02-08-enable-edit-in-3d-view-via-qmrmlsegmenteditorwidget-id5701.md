# Enable "Edit in 3D View" Via qMRMLSegmentEditorWidget

**Topic ID**: 5701
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/enable-edit-in-3d-view-via-qmrmlsegmenteditorwidget/5701

---

## Post #1 by @coolsocks (2019-02-08 19:44 UTC)

<p>Hi I’m new to slicer development and I wanted to update my code to the 4.10 version. I just had a question of how to enable the “edit in 3D view” section using the qMRMLSegmentEditorWidget?</p>
<p>Thanks</p>

---

## Post #2 by @coolsocks (2019-02-08 21:32 UTC)

<p>I got to this point:<br>
self.segmentEditorWidget.setActiveEffectByName(“Erase”)<br>
effect = self.segmentEditorWidget.activeEffect()<br>
effect.setParameter(“Editin3DViews”,“1”)<br>
effect.self().onApply()<br>
But whenever I attempt to erase, it will only rotate/displace the volume.</p>

---
