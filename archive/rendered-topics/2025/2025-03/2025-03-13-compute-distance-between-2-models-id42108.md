# Compute distance between 2 models

**Topic ID**: 42108
**Date**: 2025-03-13
**URL**: https://discourse.slicer.org/t/compute-distance-between-2-models/42108

---

## Post #1 by @slicer365 (2025-03-13 16:12 UTC)

<p>I have reconstructed two 3D models in the scene. I want to convert them into point clouds and then calculate a comprehensive distance between the two models.</p>
<p>How should I achieve this? For example, if I convert each model into 10 points and also convert the other model into 10 points, then I can use the Kabsch algorithm in this case.</p>
<p>With Python script.</p>

---

## Post #2 by @ebrahim (2025-03-14 01:48 UTC)

<p>If the models are vtkPolyData, as you would get from model mrml nodes in slicer, then there are vtk filters that compute distance. E.g. hausdorff distance</p>
<pre><code class="lang-auto">import vtk
hausdorff_filter = vtk.vtkHausdorffDistancePointSetFilter()
hausdorff_filter.SetInputData(0, polydata1)
hausdorff_filter.SetInputData(1, polydata2)
hausdorff_filter.Update()
print(hausdorff_filter.GetHausdorffDistance())
</code></pre>
<p>Of course if you have the point clouds in hand then you can also write your own algorithm in python</p>

---
