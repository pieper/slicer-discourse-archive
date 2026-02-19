---
topic_id: 40589
title: "How To Know Vertex Points Of A Segmented Model Stl"
date: 2024-12-09
url: https://discourse.slicer.org/t/40589
---

# How to know vertex points of a segmented model(stl)?

**Topic ID**: 40589
**Date**: 2024-12-09
**URL**: https://discourse.slicer.org/t/how-to-know-vertex-points-of-a-segmented-model-stl/40589

---

## Post #1 by @Puja_Ghosh (2024-12-09 18:50 UTC)

<p>I have done segmentation of a model in stl file. But I want to know how many vertices points do the stl model have on it? How can I know about the vertices points?</p>

---

## Post #2 by @mau_igna_06 (2024-12-09 20:34 UTC)

<p>In python:<br>
<code>nOfPoints = getNode('myModel').GetMesh().GetNumberOfPoints()</code></p>
<p>For the number of vertices, I guess you mean, points from the border edges of an open mesh, then you can use <a href="https://vtk.org/doc/nightly/html/classvtkFeatureEdges.html" rel="noopener nofollow ugc">this filter</a> with only the option BoundaryEdgesOn</p>
<p>HIH</p>

---

## Post #3 by @Puja_Ghosh (2024-12-09 20:42 UTC)

<p>Thank you so much for the information.<br>
I wanted to know if there is any built in feature or function in 3D Slicer for this? I know, in 3D Slicer, it allows to do targeted value meshing ( through surface toolbox). But I want to know vertex points before any targeted meshing (just after doing segmentation)? And is the filter (that you mentioned) applicable in 3D slicer directly?</p>

---
