---
topic_id: 25193
title: "Transform Process Question"
date: 2022-09-10
url: https://discourse.slicer.org/t/25193
---

# Transform Process question

**Topic ID**: 25193
**Date**: 2022-09-10
**URL**: https://discourse.slicer.org/t/transform-process-question/25193

---

## Post #1 by @JBeninca (2022-09-10 13:55 UTC)

<p>Hi,</p>
<p>i’ve got a problem with the IGT Transform Process module. it seems does not accept vtkMRMLTransformNode s.<br>
and the GUI does not show them. and the cursor to sellect cut-off frequency does not appear</p>
<p>has anyone had the same problem?<br>
thanks</p>

---

## Post #2 by @lassoan (2022-09-11 11:42 UTC)

<p>Probably the transform node selector n the module is not set up correctly. Does everything work as expected if you use a <code>vtkMRMLLinearTransformNode</code>?</p>

---

## Post #3 by @JBeninca (2022-09-11 12:14 UTC)

<p>yes. sorry. i didn´t choose “PROCESSING_MODE_STABILIZE”, in the selector.<br>
it seems it works ok.<br>
thanks</p>

---
