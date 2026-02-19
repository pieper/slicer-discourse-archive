---
topic_id: 980
title: "Get Slice Thickness From Vtkmrmlscalarvolumenode"
date: 2017-08-31
url: https://discourse.slicer.org/t/980
---

# Get Slice Thickness from vtkMRMLScalarVolumeNode

**Topic ID**: 980
**Date**: 2017-08-31
**URL**: https://discourse.slicer.org/t/get-slice-thickness-from-vtkmrmlscalarvolumenode/980

---

## Post #1 by @moselhy (2017-08-31 16:30 UTC)

<p>How do I get Slice Thickness from a vtkMRMLScalarVolumeNode in Python?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2017-08-31 16:48 UTC)

<p>I guess you need this for shifting the slice view by a whole pixel in your segment editor effect. For this, you actually need the slice spacing from the slice view and not the slice spacing of the volume node (which may be arbitrarily oriented compared to the slice view plane). For this, you can use the <a href="http://apidocs.slicer.org/master/classqSlicerSegmentEditorAbstractEffect.html#a1b5cb12818e65c5dd54d4526d52f406e"><code>qSlicerSegmentEditorAbstractEffect::sliceSpacing(sliceWidget)</code> method</a>.</p>

---
