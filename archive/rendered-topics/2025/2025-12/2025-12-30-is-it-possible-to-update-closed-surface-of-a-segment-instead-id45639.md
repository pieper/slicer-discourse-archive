---
topic_id: 45639
title: "Is It Possible To Update Closed Surface Of A Segment Instead"
date: 2025-12-30
url: https://discourse.slicer.org/t/45639
---

# Is it possible to update closed surface of a segment instead of removing closed surface when underlying vtkImageData is modified?

**Topic ID**: 45639
**Date**: 2025-12-30
**URL**: https://discourse.slicer.org/t/is-it-possible-to-update-closed-surface-of-a-segment-instead-of-removing-closed-surface-when-underlying-vtkimagedata-is-modified/45639

---

## Post #1 by @Vincent (2025-12-30 07:01 UTC)

<p>Hi,</p>
<p>I am trying to modify a segment by modifying the underlying binary label map (an instance of vtkImageData) in C++.</p>
<p>When modified() of vtkImageData is called, the closed surface of the segment is removed automatically.</p>
<p>Is it possible to update closed surface of a segment instead of removing closed surface when underlying vtkImageData is modified?</p>
<p>Thanks in advance,</p>
<p>Best regards,</p>
<p>Vincent</p>

---

## Post #2 by @lassoan (2025-12-30 15:34 UTC)

<p>If you replace the entire content of the vtkImageData then the application has no idea what has changed, so you need to recreate the closed surface representation. If you use vtkSlicerSegmentEditorLogic::ModifySegmentByLabelmap then modifications will be the minimum necessary.</p>

---
