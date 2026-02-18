# Slicer constantly closing after distanceFilter.Update()

**Topic ID**: 33020
**Date**: 2023-11-25
**URL**: https://discourse.slicer.org/t/slicer-constantly-closing-after-distancefilter-update/33020

---

## Post #1 by @Dayo (2023-11-25 17:52 UTC)

<p>Hello.</p>
<p>I’m trying to calculate the distance between two meshes using vtkDistancePolyDataFilter() in my extension. Below is a snippet of my code:</p>
<p>distanceFilter = vtk.vtkDistancePolyDataFilter()<br>
distanceFilter.SetInputData(0, mesh_1)<br>
distanceFilter.SetInputData(1, mesh_2)<br>
distanceFilter.SetSignedDistance(True)<br>
distanceFilter.Update()</p>
<p>But my slicer keeps closing after running the code. I suppose that “distanceFilter.Update()” might be responsible for that because it stops closing when I remove the update.</p>
<p>Is this a problem from my end or slicer bug, please?</p>
<p>Note: I’m using 3D slicer 5.4.0</p>

---

## Post #2 by @lassoan (2023-11-25 17:58 UTC)

<p>The most likely reason is that there is something wrong with the inputs.</p>
<p>Nevertheless, VTK library should display a meaningful error message explaining what is wrong with the inputs in instead of just crashing. Try with the latest Slicer Preview Release and if ytou can make that crash, too, then describe the exact steps you do to get to this error and we’ll report it to VTK developers.</p>

---

## Post #3 by @Dayo (2023-11-25 18:22 UTC)

<p>Thank you so much for your response.</p>
<p>Yes, you are right. One of my inputs was the reason for the crash.</p>
<p>I don’t know why though.</p>
<p>The defective input is a tube created with a vtkTubeFilter through a vtkLineSource.</p>
<p>I used node = getNode(“myTube”) to get the node of the tube, and node_p = node.GetPolyData() to get the polydata of the node which I then gave as input to distanceFilter.SetInputData(0, node_p).</p>
<p>So I’m not sure where the problem is.</p>

---

## Post #4 by @lassoan (2023-11-25 20:03 UTC)

<p>Maybe you need to triangulate the input, maybe even compute normals. Tube filter output is often self-intersecting, which may be a problem, too.</p>

---

## Post #5 by @Dayo (2023-11-25 20:14 UTC)

<p>Thank you for your help.</p>
<p>I will definitely try your recommendations</p>

---
