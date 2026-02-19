---
topic_id: 24427
title: "How To Judge Whether A Point In A Model Node 3D Model"
date: 2022-07-21
url: https://discourse.slicer.org/t/24427
---

# How to judge whether a point in a model node (3d model)

**Topic ID**: 24427
**Date**: 2022-07-21
**URL**: https://discourse.slicer.org/t/how-to-judge-whether-a-point-in-a-model-node-3d-model/24427

---

## Post #1 by @1023185654 (2022-07-21 08:05 UTC)

<p>hello everyone, i suppose to judge whether a point inside or outside with 3D model, how i can do this? i tried to use vtk.vtkSelectEnclosedPoints() but it dosent work</p>

---

## Post #2 by @lassoan (2022-07-21 09:36 UTC)

<p>You can use <code>vtkImplicitPolyDataDistance</code> to get distance of a point from a surface. If the distance is negative then the point is inside the mesh. You can find a complete example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-distance-of-points-from-surface">script repository</a>.</p>
<p>For very large or complex or slightly invalid meshes <code>vtkImplicitPolyDataDistance</code> may be slow or unreliable. In this case you may consider converting the model to a labelmap volume node (using Segmentation module). This conversion is not trivial and may give slightly different result at the boundary (due to finite resolution of the image volume), but checking if a position is inside a volume is very quick and guaranteed to always succeed.</p>

---

## Post #3 by @1023185654 (2022-07-21 09:41 UTC)

<p>i got it, thanks for reply</p>

---
