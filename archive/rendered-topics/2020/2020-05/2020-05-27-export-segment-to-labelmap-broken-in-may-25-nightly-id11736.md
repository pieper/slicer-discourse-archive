---
topic_id: 11736
title: "Export Segment To Labelmap Broken In May 25 Nightly"
date: 2020-05-27
url: https://discourse.slicer.org/t/11736
---

# Export segment to labelmap broken in May 25 nightly

**Topic ID**: 11736
**Date**: 2020-05-27
**URL**: https://discourse.slicer.org/t/export-segment-to-labelmap-broken-in-may-25-nightly/11736

---

## Post #1 by @hherhold (2020-05-27 16:18 UTC)

<p>In the last few days, exporting a segment to a labelmap stopped working. Works fine in May 21 nightly, doesn’t work in May 25 nightly (latest build, downloaded for Mac this morning).</p>
<p>I have a debug build, I’m happy to help troubleshoot.</p>
<p>Thanks!</p>
<p>Errors from the log:</p>
<p>virtual double qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(vtkIdType) const : Input item is invalid</p>
<p>GetItemDataNode: Failed to find subject hierarchy item by ID 0</p>
<p>ExportSegmentsToLabelmapNode: Failed to generate shared labelmap</p>
<p>bool qSlicerSegmentationsModuleWidget::exportFromCurrentSegmentation() :  “Failed to export segments from segmentation Segmentation to labelmap node Segmentation-Air spaces-label!\n\nMost probably the segment cannot be converted into binary labelmap representation.”</p>

---

## Post #2 by @lassoan (2020-05-27 18:17 UTC)

<p>I was able to reproduce the error. I’ll get back to you soon.</p>

---

## Post #3 by @lassoan (2020-05-27 18:47 UTC)

<p>I’ve found the problem, this is a regression due to additional error checks that we introduced a few days ago (the error is caught by the test dashboard, too, but since it was such a small change, I did not check). The problem is fixed now. Thanks for reporting!</p>

---

## Post #4 by @hherhold (2020-05-27 20:29 UTC)

<p>Awesome! Thanks!</p>
<p>-Hollister</p>

---
