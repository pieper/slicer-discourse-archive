# Problem with Segment Editor

**Topic ID**: 13396
**Date**: 2020-09-09
**URL**: https://discourse.slicer.org/t/problem-with-segment-editor/13396

---

## Post #1 by @doc-xie (2020-09-09 07:11 UTC)

<p>Version: 4.10.0(stable)<br>
System:MacOS<br>
In Segment Editor module, the Segment can not be performed with Draw, Level tracing or Threshold tools. The error showed as following:</p>
<p>Traceback (most recent call last):<br>
File “/Volumes/Dashboards/Stable/Slicer-4100-build/Slicer-build/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 73, in processInteractionEvents<br>
File “/Volumes/Dashboards/Stable/Slicer-4100-build/Slicer-build/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 239, in apply<br>
AttributeError: ‘module’ object has no attribute ‘qSlicerSegmentEditorAbstractEffect’</p>
<p>Traceback (most recent call last):<br>
File “/Volumes/Dashboards/Stable/Slicer-4100-build/Slicer-build/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 73, in processInteractionEvents<br>
File “/Volumes/Dashboards/Stable/Slicer-4100-build/Slicer-build/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorEffects/SegmentEditorDrawEffect.py”, line 239, in apply<br>
AttributeError: ‘module’ object has no attribute ‘qSlicerSegmentEditorAbstractEffect’</p>
<p>What it the cause for this and how to solve the problem?<br>
Best wishes,<br>
Xie</p>

---

## Post #2 by @jamesobutler (2020-09-09 11:41 UTC)

<p>The current stable is actually Slicer 4.10.2 while you are using an older version 4.10.0. There are no more bug fix releases scheduled for the 4.10.x series. Can you try and see if this issue is present by using the latest Slicer preview (4.11)? This preview version will soon become the newest stable version as Slicer 5.0.</p>

---
