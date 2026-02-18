# No GetStorableNode method in vtkMRMLStorageNode

**Topic ID**: 4764
**Date**: 2018-11-14
**URL**: https://discourse.slicer.org/t/no-getstorablenode-method-in-vtkmrmlstoragenode/4764

---

## Post #1 by @Sunderlandkyl (2018-11-14 18:45 UTC)

<p>In the case of vtkMRMLDisplayNode, there is a GetDisplayableNode() method.</p>
<p>Is there any reason why there isn’t, or couldn’t be a corresponding GetStorableNode() method in vtkMRMLStorageNode?</p>

---

## Post #2 by @lassoan (2018-11-14 19:03 UTC)

<p>We should add GetStorableNode() method to vtkMRMLStorageNode(), similarly to display/displayable node. We needed it in vtkMRMLSegmentationStorageNode, too, and added GetAssociatedDataNode() then, but a general solution would be better.</p>

---

## Post #3 by @Sunderlandkyl (2018-11-14 19:15 UTC)

<p>Sounds good. See pull request here: <a href="https://github.com/Slicer/Slicer/pull/1044" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1044</a></p>

---
