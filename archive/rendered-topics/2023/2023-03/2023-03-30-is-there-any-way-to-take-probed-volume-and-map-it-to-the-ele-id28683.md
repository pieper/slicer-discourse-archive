---
topic_id: 28683
title: "Is There Any Way To Take Probed Volume And Map It To The Ele"
date: 2023-03-30
url: https://discourse.slicer.org/t/28683
---

# Is there any way to take probed volume and map it to the elements instead of nodes?

**Topic ID**: 28683
**Date**: 2023-03-30
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-take-probed-volume-and-map-it-to-the-elements-instead-of-nodes/28683

---

## Post #1 by @fea_99 (2023-03-30 17:20 UTC)

<p>I believe FEBio requires that the scalar data be mapped onto the elements instead of the nodes themselves, is there any way to instead probe the data onto the elements, or even move them from the nodes to the elements?</p>

---

## Post #2 by @fea_99 (2023-03-30 17:47 UTC)

<p>After a little bit of digging, I think this snippet of code is sort of what I’m looking for, but I’m not 100% sure that this is accurate as I cannot exactly verify the values.</p>
<blockquote>
<p>nameOfModel = ‘exampleName’<br>
modelNode = getNode(nameOfModel)</p>
</blockquote>
<blockquote>
<p>toCellData = vtk.vtkPointDataToCellData()<br>
toCellData.SetInputData(modelNode.GetMesh())<br>
toCellData.PassPointDataOn()<br>
toCellData.Update()</p>
</blockquote>
<blockquote>
<p>modelNode.SetAndObserveMesh(toCellData.GetOutput())</p>
</blockquote>

---

## Post #3 by @lassoan (2023-03-30 18:50 UTC)

<p>vtkPointDataToCellData computes the cell data by averaging the point data at the vertices of the cell. This is accurate enough if the cells are small enough to be considered homogeneous.</p>
<p>For future reference: correspondence between FEM and VTK terms are <code>element</code> = <code>cell</code>, <code>node</code> = <code>point</code>. So, the question was if it was possible to set cell data in a VTK mesh based on point data. (“Probe volume with model” module sets point data)</p>

---
