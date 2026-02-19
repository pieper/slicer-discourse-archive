---
topic_id: 30525
title: "Error From Qmrmlsegmenteditorwidgetprivate"
date: 2023-07-11
url: https://discourse.slicer.org/t/30525
---

# Error from qMRMLSegmentEditorWidgetPrivate

**Topic ID**: 30525
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/error-from-qmrmlsegmenteditorwidgetprivate/30525

---

## Post #1 by @aiden.zhu (2023-07-11 16:56 UTC)

<p>Windows 10 Pro<br>
Slicer: 5.3.0–2023.07.08</p>
<p>Here I do call “Segment-editor” via python and always I do have this error associated with qMRMLSegmentEditorWidgetPrivate<br>
==&gt;<br>
[Qt] bool __cdecl qMRMLSegmentEditorWidgetPrivate::updateSelectedSegmentLabelmap(void) : Invalid segment selection</p>
<p>any suggestion how to deal with this error?</p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2023-07-13 01:22 UTC)

<p>It seems that you have not selected a segment before performing some operation that expected to have a segment selected. A fix is to select the first segment of the segmentation after you set the segmentation node in the Segment Editor widget.</p>

---
