---
topic_id: 24512
title: "Rotate A Vtkmrmlmodelnode In A Specific Direction"
date: 2022-07-27
url: https://discourse.slicer.org/t/24512
---

# Rotate a vtkMRMLModelNode() in a specific direction

**Topic ID**: 24512
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/rotate-a-vtkmrmlmodelnode-in-a-specific-direction/24512

---

## Post #1 by @mosenco (2022-07-27 02:03 UTC)

<p>I have created a <code>cylinderSource = vtk.vtkCylinderSource()</code><br>
and then a <code>cylindermodel = slicer.vtkMRMLModelNode()</code> and “linked together” with <code>cylindermodel.SetAndObservePolyData(cylinderSource.GetOutput())</code></p>
<p>then i created a <code>cylindermodelDisplay = slicer.vtkMRMLModelDisplayNode()</code> set all the colors and so on and “linked together” with<br>
<code>slicer.mrmlScene.AddNode(cylindermodelDisplay)  cylindermodel.SetAndObserveDisplayNodeID(cylindermodelDisplay.GetID())</code></p>
<p>all nice.</p>
<p>Now i have 2 points in space and between them multiple points (which i have their position) and i wanted to put all those nice cylinder in that direction between the 2 points and rotated accordingly, so it looks like a long rod.</p>
<p>i created a <code>cylinderTS = slicer.vtkMRMLTransformNode()</code> so my <code>cylindermodel</code> can associate with it later.<br>
I created a <code>cylinderTransform = vtk.vtkTransform()</code> so i can rotate my <code>cylinderTS</code> and i associated them with <code>cylinderTS.SetAndObserveMatrixTransformToParent(cylinderTransform.GetMatrix())</code></p>
<p>But i don’t know how to rotate in the same direciton of the “line” between the two points. I tried to use <code>cylinderTransform.RotateWXYZ()</code> but i don’t know the axis of rotation.</p>
<p>I had an idea.<br>
I just create a vtkline, i can associate a <code>slicer.vtkMRMLModelNode()</code> and then i can get the angle, the local axis… but i noticed that from a <code>slicer.vtkMRMLModelNode()</code> i can’t retrieve a <code>slicer.vtkMRMLTransformNode()</code> and neither a matrix4x4…</p>
<p>Someone can suggest me any ideas?</p>

---

## Post #2 by @cpinter (2022-07-27 10:59 UTC)

<p>I suggest using the line markup because it gives you a cylinder between two points.</p>
<p>Otherwise, this is a VTK / math question.</p>

---
