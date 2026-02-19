---
topic_id: 28566
title: "Min Distance Between A Curvenode And Another Node"
date: 2023-03-24
url: https://discourse.slicer.org/t/28566
---

# Min distance between a curveNode and another node?

**Topic ID**: 28566
**Date**: 2023-03-24
**URL**: https://discourse.slicer.org/t/min-distance-between-a-curvenode-and-another-node/28566

---

## Post #1 by @pixilla (2023-03-24 20:01 UTC)

<p>Hello,<br>
I wanted to find the minimum distance between the curve (defined by a list of point in a vtkmrmlCurveNode) and other nodes which are vtkPolyData by using (I think) a vtkPolyDataDistanceFIlter. I started by created this curve node with the method where pointPositions is my list of points:<br>
curveNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsCurveNode”)<br>
slicer.util.updateMarkupsControlPointsFromArray(curveNode, pointPositions)</p>
<p>After that I’ve tried to use the vtkPolyDataDistanceFIlter:</p>
<pre><code>    distanceFilter = vtk.vtkDistancePolyDataFilter()
    curveA = curve.GetCurveWorld()
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputData(curveA)
    distanceFilter.SetInputConnection(0,obst.GetPolyDataConnection())
    distanceFilter.SetInputConnection(1,mapper.GetOutputPort())
    distanceFilter.Update()
    d = distanceFilter.GetOutput().GetPointData().GetScalars().GetRange()[0] 
</code></pre>
<p>My problem is that there is an error for the SetInputConnection of the curve part If I don’t use a mapper, and with the mapper I get a ‘nontype’ for the last line above. I’ve tried by using curve and it is not working.<br>
Is there a method to resolve the problem please?</p>

---

## Post #2 by @lassoan (2023-03-26 04:25 UTC)

<p><code>curve.GetCurveWorld()</code> returns a <code>vtkPolyData</code> object that you can set as input of a VTK filter using <code>SetInputData()</code> method.</p>
<p>Since you don’t need to implement any rendering, you can remove the lines that refer to the mapper.</p>

---
