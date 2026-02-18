# Set Orientation at vtkCylinderSource

**Topic ID**: 8663
**Date**: 2019-10-03
**URL**: https://discourse.slicer.org/t/set-orientation-at-vtkcylindersource/8663

---

## Post #1 by @siaeleni (2019-10-03 18:25 UTC)

<p>Hello,</p>
<p>I would like to Set Orientation/Direction to a vtkCylinderSource that I create in Slicer in python.<br>
From vtk documentation I realized that I have to set the orientation through vtkActor, but how can I display it on Slicer?</p>
<p>Here is a piece of code:</p>
<blockquote>
<p>cyl = vtk.vtkCylinderSource()<br>
cyl.SetRadius(50)<br>
cyl.SetResolution(50)<br>
cyl.SetHeight(100)</p>
<p>mapper = vtk.vtkPolyDataMapper()<br>
mapper.SetInputConnection(cyl.GetOutputPort())</p>
<p>actor = vtk.vtkActor()<br>
actor.SetOrientation(0,0,90)<br>
actor.SetMapper(mapper)</p>
<p>node = cyl.GetOutput()<br>
n = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLModelNode’, ‘Cylinder’)<br>
n.SetAndObservePolyData(node)<br>
n.CreateDefaultDisplayNodes()<br>
n.SetDisplayVisibility(True)<br>
cyl.Update()</p>
</blockquote>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-10-03 18:38 UTC)

<p>If you need to dynamically set its position/rotation then you set a parent transform to it. If you need a fixed pose then to cylinder source output you can apply a vtkTransformPolyDataFilter on set the output of that into the model node.</p>

---

## Post #3 by @siaeleni (2019-10-03 19:18 UTC)

<p>yes, I was wondering whether there is another option for dynamically setting the transformation except from SetMatrixTransformToParent. Thanks</p>

---

## Post #4 by @lassoan (2019-10-03 19:25 UTC)

<p>In your module you can keep a reference to vtkTransformPolyDataFilter and update it whenever you need. However, in general it is more useful if you don’t keep transforms private but store in MRML nodes so that other nodes and modules can use it. For example, if you just store a transform privately then you cannot easily modify or inspect current values using GUI, use it to reslice a volume, combine with other transforms, save/load with the scene, etc.</p>

---
