# Can I show a VTK scence in 3d view?

**Topic ID**: 11390
**Date**: 2020-05-03
**URL**: https://discourse.slicer.org/t/can-i-show-a-vtk-scence-in-3d-view/11390

---

## Post #1 by @timeanddoctor (2020-05-03 14:17 UTC)

<p>I created a scence with some meshes(2 layer,such as 1st:cube,2nd:cylinder) and pictures by import vtk in slicer, I want to show it in 3D view of slicer. Can I do it  with python. Thanks!</p>

---

## Post #2 by @lassoan (2020-05-04 03:19 UTC)

<p>You can load and display a mesh file in Slicer by calling:</p>
<pre><code>slicer.modules.models.logic().AddModel("path/to/modelfile.stl")</code></pre>

---
