# I can't find any tools under segment editor. See the report bug below

**Topic ID**: 41913
**Date**: 2025-02-28
**URL**: https://discourse.slicer.org/t/i-cant-find-any-tools-under-segment-editor-see-the-report-bug-below/41913

---

## Post #1 by @Alou_Diakite (2025-02-28 07:59 UTC)

<p>[DEBUG][Qt] 28.02.2025 15:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[CRITICAL][Stream] 28.02.2025 15:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 28.02.2025 15:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/DELL/AppData/Local/slicer.org/Slicer 5.8.0/bin/…/lib/Slicer-5.8/qt-scripted-modules/SegmentEditor.py”, line 124, in enter<br>
[CRITICAL][Stream] 28.02.2025 15:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.selectParameterNode()<br>
[CRITICAL][Stream] 28.02.2025 15:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/DELL/AppData/Local/slicer.org/Slicer 5.8.0/bin/…/lib/Slicer-5.8/qt-scripted-modules/SegmentEditor.py”, line 87, in selectParameterNode<br>
[CRITICAL][Stream] 28.02.2025 15:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     segmentEditorNode.UnRegister(None)<br>
[CRITICAL][Stream] 28.02.2025 15:52:47 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: ‘vtkSlicerSegmentationsModuleMRMLPython.vtkMRMLSegm’ object has no attribute ‘UnRegister’</p>

---

## Post #2 by @cpinter (2025-02-28 10:48 UTC)

<p>Did you build Slicer from source code? What is your operating system?</p>

---

## Post #3 by @Alou_Diakite (2025-03-02 19:06 UTC)

<p>Hi, I am using a windows 11 and I installed the .exe file. The problem come up I installed the WMA extension. Without that extension, it works fine. Thank you</p>

---
