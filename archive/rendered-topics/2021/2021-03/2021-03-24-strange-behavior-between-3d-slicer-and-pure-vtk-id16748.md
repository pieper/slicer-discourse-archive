# Strange behavior between 3D Slicer and pure VTK

**Topic ID**: 16748
**Date**: 2021-03-24
**URL**: https://discourse.slicer.org/t/strange-behavior-between-3d-slicer-and-pure-vtk/16748

---

## Post #1 by @jackxiong (2021-03-24 13:07 UTC)

<p>Hello all,<br>
I have met a development issue here, I want to coloring different cell with different color, I have draft code with VTK(not in 3D Slicer), the code as below:</p>
<pre data-code-wrap="python"><code class="lang-python">import vtk

sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0,0,0)
sphereSource.SetRadius(60.0)
sphereSource.Update()
sphereSource = sphereSource.GetOutput() # vtkPolyData()

cellData = vtk.vtkUnsignedCharArray()
cellData.SetNumberOfComponents(3)
cellData.SetNumberOfTuples(sphereSource.GetNumberOfCells())
cellData.SetName('Colors')
for i in range(0,sphereSource.GetNumberOfCells()):
    cellData.InsertTuple(i,(255,255,255))

sphereSource.GetCellData().SetScalars(cellData)
sphereSource.Modified()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(sphereSource)
actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderWindowInteractor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
renderer.AddActor(actor)
renderer.SetBackground((1,1,1))
renderWindow.Render()
renderWindowInteractor.Start()
and the result as below photo:
![图片|302x332](upload://kU4E3fiQzwRcKBvkAUpOsobPYF0.png) 
</code></pre>
<p>Almost the same code in 3D Slicer python console:</p>
<pre data-code-wrap="python"><code class="lang-python"># Hide the cube
v = slicer.util.getNode('View1')
v.SetBoxVisible(False)

# Sphere
sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0,0,0)
sphereSource.SetRadius(60.0)
sphereSource.Update()
sphereSource = sphereSource.GetOutput() # vtkPolyData()

# Create a model with the sphere and add it to scene
modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
modelNode.SetAndObservePolyData(sphereSource)
modelNode.CreateDefaultDisplayNodes()
modelNode.SetName('My sphere')

cellData = vtk.vtkUnsignedCharArray()
cellData.SetNumberOfComponents(3)
cellData.SetNumberOfTuples(sphereSource.GetNumberOfCells())
cellData.SetName('Colors')
for i in range(0,sphereSource.GetNumberOfCells()):
    cellData.InsertTuple(i,(255.0, 255.0, 255.0))

sphereSource.GetCellData().SetScalars(cellData)
sphereSource.Modified()

# Set up coloring by selection array
#modelNode.GetDisplayNode().SetActiveScalar("Colors", vtk.vtkAssignAttribute.CELL_DATA)
modelNode.GetDisplayNode().SetAndObserveColorNodeID("")
modelNode.GetDisplayNode().SetScalarVisibility(True)
</code></pre>
<p>But the result as below photo:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb8958137b6f0e4527a54b264ff8b9534d34dcd.png" data-download-href="/uploads/short-url/defoAQQuv92Zyy4I9HPG8qlEdw9.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb8958137b6f0e4527a54b264ff8b9534d34dcd_2_504x500.png" alt="图片" data-base62-sha1="defoAQQuv92Zyy4I9HPG8qlEdw9" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cb8958137b6f0e4527a54b264ff8b9534d34dcd_2_504x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb8958137b6f0e4527a54b264ff8b9534d34dcd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb8958137b6f0e4527a54b264ff8b9534d34dcd.png 2x" data-dominant-color="6568C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">599×594 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Both code want to set all of the cells on the surface to white color (255.0, 255.0, 255.0), but I got different result, I have referenced c++ code as below link:</p>
<p><a href="https://kitware.github.io/vtk-examples/site/Cxx/PolyData/ColorCellsWithRGB/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://kitware.github.io/vtk-examples/site/Cxx/PolyData/ColorCellsWithRGB/</a></p>
<p>The result in 3D Slicer is not what I want. Am I missing something or need some extra configuration on 3D Slicer? Look forward to your kindly reply. Thanks in advance!<br>
environment:<br>
OS: Win10 x64<br>
3D Slicer version: 4.11.20200930</p>

---

## Post #2 by @lassoan (2021-03-24 13:11 UTC)

<p>You need to add back the line that you commented out (to set the active scalar); and set scalar range flag (to UseDirectMapping).</p>

---

## Post #3 by @jackxiong (2021-03-24 14:13 UTC)

<p>I have updated the code as your suggestion, it works very well. Thanks a lot for your kindly help!</p>

---
