# How to visualize scipy.interpolate.rbf object in Slicer 3D view

**Topic ID**: 19632
**Date**: 2021-09-12
**URL**: https://discourse.slicer.org/t/how-to-visualize-scipy-interpolate-rbf-object-in-slicer-3d-view/19632

---

## Post #1 by @dalbenzioG (2021-09-12 17:19 UTC)

<p>Hello,</p>
<p>I am working on spline interpolation with <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.Rbf.html" rel="noopener nofollow ugc">scipy.interpolate.Rbf</a>. Is there any possibility to visualize the results from scipy.interpolate.rbf directly in Slicer 3D view?</p>
<p>My approach so far: convert NumPy array into VTK array and then into PolyData.</p>
<p>Thank you in advance!<br>
Gabriella</p>

---

## Post #2 by @pieper (2021-09-12 17:34 UTC)

<p>Going to vtk via numpy is the right way.  Depending on what you are trying to do, a vtkImageData to vtkMRMLScalarVolume might also work.</p>

---

## Post #3 by @lassoan (2021-09-12 18:37 UTC)

<p>What do you use the RBF for? For creating/interpolating curves, transforms, images, models, …?</p>
<p>There are single-line <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util">utility functions to use numpy arrays directly in MRML nodes</a>. Some functions allow you to access MRML node content as a readable/writable numpy array, so that if you update the numpy array then the displayed data update live.</p>
<p>There are also many modeling and interpolation tools in VTK that are much more sophisticated and faster than similar functions in scipy.</p>

---

## Post #4 by @dalbenzioG (2021-10-20 19:45 UTC)

<p>Hello Andras and sorry for my late reply.</p>
<p>I have been experimenting, and the natural solution for my case is the one you are suggesting, which is using a vtkKochanekSpline() for parametric interpolation of 3d data points. Here is the code I wrote:</p>
<pre><code class="lang-auto">#Load the samples model
points_file = '/home/gabriella/PycharmProjects/Exstension/SlicerFirstExtension/IsoContourRes/points20.vtk'
samples_reader = vtk.vtkPolyDataReader()
samples_reader.SetFileName(points_file)
samples_reader.Update()
mask= samples_reader.GetOutputPort()
points = samples_reader.GetOutput().GetPoints()

xSpline = vtk.vtkKochanekSpline()
ySpline = vtk.vtkKochanekSpline()
zSpline = vtk.vtkKochanekSpline()
#
spline = vtk.vtkParametricSpline()
spline.SetXSpline(xSpline)
spline.SetYSpline(ySpline)
spline.SetZSpline(zSpline)
spline.SetPoints(points)
#
functionSource = vtk.vtkParametricFunctionSource()
functionSource.SetParametricFunction(spline)
functionSource.SetUResolution(50 * numberOfPoints)
functionSource.SetVResolution(50 * numberOfPoints)
functionSource.SetWResolution(50 * numberOfPoints)
functionSource.Update()

#Setup actor and mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(functionSource.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(colors.GetColor3d("DarkSlateGrey"))
actor.GetProperty().SetLineWidth(3.0)

#  Glyph the points
# Create a polydata to store everything in
polyData = vtk.vtkPolyData()
polyData.SetPoints(points)


sphereSource = vtk.vtkSphereSource()
sphereSource.SetRadius(1)
sphereSource.Update()
sphere = sphereSource.GetOutputPort()

# glyph = vtk.vtkGlyph3D()
# glyph.SetInputConnection(mask)
# glyph.SetSourceConnection(sphere)
# glyph.ScalingOff()
# glyph.Update()

pointMapper = vtk.vtkGlyph3DMapper()
pointMapper.SetInputData(polyData)
pointMapper.SetSourceConnection(sphere)

pointActor = vtk.vtkActor()
pointActor.SetMapper(pointMapper)
pointActor.GetProperty().SetColor(colors.GetColor3d("Peacock"))

# Create the rendering window, renderer, and interactive renderer
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetWindowName("KochanekSpline")
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Add the actors to the renderer, set the background and size
renderer.AddActor(actor)
renderer.AddActor(pointActor)
renderer.SetBackground(colors.GetColor3d("Silver"))
renderWindow.SetSize(150, 150)

renderer.ResetCamera()
renderer.GetActiveCamera().Zoom(1.5)

# Interact with the data
renderWindowInteractor.Initialize()
renderWindow.Render()
renderWindowInteractor.Start()
</code></pre>
<p>But, I am not sure how to implement the same result in Slicer 3D view. Any suggestions? <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=10" title=":pray:" class="emoji" alt=":pray:"></p>

---

## Post #5 by @lassoan (2021-10-21 03:57 UTC)

<p>Probably the simplest is to use markups curves. Something like this:</p>
<pre><code class="lang-python">points_file = '/home/gabriella/PycharmProjects/Exstension/SlicerFirstExtension/IsoContourRes/points20.vtk'
samples_reader = vtk.vtkPolyDataReader()
samples_reader.SetFileName(points_file)
samples_reader.Update()

curveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
curveNode.SetCurveTypeToKochanekSpline()
curveNode.CreateDefaultDisplayNodes()
curveNode.SetControlPointPositionsWorld(samples_reader.GetOutput().GetPoints())
</code></pre>

---
