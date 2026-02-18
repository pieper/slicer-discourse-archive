# Can not segment on master volume

**Topic ID**: 29471
**Date**: 2023-05-15
**URL**: https://discourse.slicer.org/t/can-not-segment-on-master-volume/29471

---

## Post #1 by @doc-xie (2023-05-15 07:41 UTC)

<p>Hi,<br>
In SegmentEditor module, after the MRI data was loaded as scalar volume and create a new segmentation, the Threshold and Level tracing  can not be used correctly. The log messages showed that: File “/Volumes/Dashboards/Stable/Slicer-4100-build/Slicer-build/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorEffects/SegmentEditorLevelTracingEffect.py”, line 66, in processInteractionEvents</p>
<p>AttributeError: ‘module’ object has no attribute ‘qSlicerSegmentEditorAbstractEffect’ and <strong>strong text</strong>.<br>
What is the reason about this and how to solve this problem?<br>
Thanks</p>

---

## Post #2 by @pieper (2023-05-15 12:17 UTC)

<p>It looks like you have a very old version of Slicer.  Please try again with the current release (5.2.2 from <a href="http://download.slicer.org">download.slicer.org</a>) and let us know how it goes.</p>

---
