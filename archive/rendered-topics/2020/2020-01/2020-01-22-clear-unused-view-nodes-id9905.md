# Clear unused view nodes

**Topic ID**: 9905
**Date**: 2020-01-22
**URL**: https://discourse.slicer.org/t/clear-unused-view-nodes/9905

---

## Post #1 by @rprueckl (2020-01-22 15:42 UTC)

<p>Hi,</p>
<p>I use custom layouts. I want to clear the scene from unused viewers (vtkMRMLSliceNode and vtkMRMLViewNode) (and the nodes that are associated to them (as far as i have seen: a vtkMRMLSliceCompositeNode, a vtkMRMLModelDisplayNode, vtkMRMLLinearTransformNode, and a vtkMRMLModelNode in case of a vtkMRMLSliceNode and a vtkMRMLCameraNode in case of a vtkMRMLViewNode)).<br>
How would I do that? Is there a way do detect ‘unused’ view nodes? Best would be to initially prevent the scene/application from generating the default views.<br>
Any hint is appreciated. Thanks</p>

---

## Post #2 by @lassoan (2020-01-22 15:53 UTC)

<p>You can use MappedInLayout attribute name, which is set to 0 for views that are not mapped in current layout.</p>

---
