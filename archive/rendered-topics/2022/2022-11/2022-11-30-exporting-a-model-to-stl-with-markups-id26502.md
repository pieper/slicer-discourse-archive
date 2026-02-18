# Exporting a model to STL with markups

**Topic ID**: 26502
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/exporting-a-model-to-stl-with-markups/26502

---

## Post #1 by @bremsstrahlung (2022-11-30 04:36 UTC)

<p>I have a model and have a point list of markups on the model, How do i export this model to STL with the control points?</p>

---

## Post #2 by @cpinter (2022-11-30 14:07 UTC)

<p>You could use a Python snippet like this</p>
<pre><code class="lang-auto">fiducialNode = getNode('F')
import numpy as np
sphereSource = vtk.vtkSphereSource()
sphereSource.SetRadius(1)
for i in range(fiducialNode.GetNumberOfControlPoints()):
  p = np.zeros(3)
  fiducialNode.GetNthControlPointPosition(i, p)
  fiducialModel = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', f'Model_{fiducialNode.GetName()}_{i}')
  sphereSource.SetCenter(p)
  polyData = vtk.vtkPolyData()
  sphereSource.Update()
  polyData.DeepCopy(sphereSource.GetOutput())
  fiducialModel.SetAndObservePolyData(polyData)
</code></pre>
<p>Please note you’ll need to replace the name of your fiducial node (in my example it is <code>F</code>) and set the sphere radius as desired.</p>
<p>Once you have the model nodes you can append them together in Dynamic Modeler module’s Append feature, then export to STL.</p>

---

## Post #3 by @lassoan (2022-12-01 02:12 UTC)

<p>Alternatively, you can use a glyph filter like this:</p>
<pre><code class="lang-python">markup = getNode('F')
glyph = vtk.vtkSphereSource()
glyph.SetRadius(15.0)
glypher = vtk.vtkGlyph3D()
glypher.SetSourceConnection(glyph.GetOutputPort())
glypher.SetInputConnection(markup.GetCurveWorldConnection())
model = slicer.modules.models.logic().AddModel(glypher.GetOutputPort())
slicer.util.saveNode(model, "c:/tmp/something.stl")
</code></pre>

---

## Post #4 by @bremsstrahlung (2022-12-02 04:08 UTC)

<p>Both of the above mentioned solutions work perfectly, i can now export a model that has all the points on it. Thank You.<br>
Would it be possible to have the points and the model to be in different colors? When i use the Append feature in Dynamic Modeler the final Model is of all the same color, i would prefer if the points and my model where of different colours.</p>

---

## Post #5 by @bremsstrahlung (2022-12-02 05:49 UTC)

<p>Can this be extended to a curve? If my markups are in the form of a curve, can that be exported to an STL?</p>

---

## Post #6 by @lassoan (2022-12-02 15:15 UTC)

<p>Yes, it works exactly the same way for curves, just replace the glyph filter by tube filter.</p>

---
