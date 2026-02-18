# How to copy Nodes using id?

**Topic ID**: 16572
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/how-to-copy-nodes-using-id/16572

---

## Post #1 by @akshay_pillai (2021-03-16 14:23 UTC)

<p>I want to keep multiple copies of mrml nodes so that I can operate on the copies without changing the original. Kind of like clone option from data module. Is this possible? If so how can I implement it? For example - I want to create multiple copies of a curve. Any help is appreciated. Thanks</p>

---

## Post #2 by @lassoan (2021-03-16 15:54 UTC)

<p>You can clone modules at many different levels. Data module’s clone feature uses the subject hierarchy plugin associated with the node, see example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Clone_a_node">script repository</a>.</p>

---

## Post #3 by @akshay_pillai (2021-03-19 13:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hey, I see that I can copy nodes and volumes. Is there any way I can do the same thing for segments inside segmentation nodes? This seems to only work for vtkMRMLNode or vtkMRMLVolumeNode. And segments are vtkSegment</p>

---

## Post #4 by @akshay_pillai (2021-03-19 14:16 UTC)

<p>Update: I found the answer to that here: <a href="https://discourse.slicer.org/t/how-to-programmatically-use-logical-operator-add-function-from-segment-editor/16581/2" class="inline-onebox">How to programmatically use logical operator add function from segment editor? - #2 by mikebind</a></p>

---
