# SetPosition of ellipsoid

**Topic ID**: 2721
**Date**: 2018-04-27
**URL**: https://discourse.slicer.org/t/setposition-of-ellipsoid/2721

---

## Post #1 by @Frederic (2018-04-27 16:15 UTC)

<p>Hi all,<br>
I have write a little script to draw on slicer an ellipsoid.<br>
However, I do not know how to set the position (center), could you please help me?<br>
Thanks in advance.</p>
<p>The code</p>
<blockquote>
<p>ellips = vtk.vtkParametricEllipsoid()<br>
ellips.SetXRadius(40.0)<br>
ellips.SetYRadius(10.0)<br>
ellips.SetZRadius(15.0)<br>
ellipsSource = vtk.vtkParametricFunctionSource()<br>
ellipsSource.SetParametricFunction(ellips)<br>
ellipsSource.Update()<br>
modelsLogic = slicer.modules.models.logic()<br>
model = modelsLogic.AddModel(ellipsSource.GetOutput())<br>
model.SetName(‘ellipse_1’)<br>
model.GetDisplayNode().SetSliceIntersectionVisibility(True)<br>
model.GetDisplayNode().SetSliceIntersectionThickness(3)</p>
</blockquote>
<p>from this code:</p>
<blockquote>
<p>ellipsoid = vtk.vtkParametricEllipsoid()<br>
ellipsoid.SetXRadius(1)<br>
ellipsoid.SetYRadius(0.75)<br>
ellipsoid.SetZRadius(0.5)<br>
ellipsoidSource = vtk.vtkParametricFunctionSource()<br>
ellipsoidSource.SetParametricFunction(ellipsoid)<br>
ellipsoidSource.SetScalarModeToZ()<br>
ellipsoidMapper = vtk.vtkPolyDataMapper()<br>
ellipsoidMapper.SetInputConnection(ellipsoidSource.GetOutputPort())<br>
ellipsoidMapper.SetScalarRange(-0.5, 0.5)<br>
ellipsoidActor = vtk.vtkActor()<br>
ellipsoidActor.SetMapper(ellipsoidMapper)<br>
ellipsoidActor.SetPosition(8, -12, 0)<br>
ellipsoidActor.SetScale(1.5, 1.5, 1.5)</p>
</blockquote>

---

## Post #2 by @lassoan (2018-04-27 20:14 UTC)

<p>You can add these lines to apply a transform to the model node:</p>
<pre><code>transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
model.SetAndObserveTransformNodeID(transformNode.GetID())
transform = vtk.vtkTransform()
transform.Translate(8, -12, 0)
transform.Scale(1.5, 1.5, 1.5)
transformNode.SetMatrixTransformToParent(transform.GetMatrix())
</code></pre>
<p>Note that you can go to Transforms module and use the sliders to edit your transform.</p>

---

## Post #3 by @Frederic (2018-04-30 12:30 UTC)

<p>Once again, thanks Andras.</p>

---
