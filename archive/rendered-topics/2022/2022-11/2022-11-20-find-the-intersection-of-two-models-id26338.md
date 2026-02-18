# Find the intersection of two models

**Topic ID**: 26338
**Date**: 2022-11-20
**URL**: https://discourse.slicer.org/t/find-the-intersection-of-two-models/26338

---

## Post #1 by @TrascendentK (2022-11-20 22:34 UTC)

<p>Hi there,</p>
<p>How can i find the points in which two models (a sort of cylinder and a bar) intersect one another?<br>
i’ve tried messing up with numpy trying to search for intersections in data arrays but that doesn’t seem the right way.</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55b417c80610abf6d0d677c20f039965456fc6ba.png" data-download-href="/uploads/short-url/ceaqNwqP0E76SkrcAei36SoLf50.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55b417c80610abf6d0d677c20f039965456fc6ba_2_690x409.png" alt="image" data-base62-sha1="ceaqNwqP0E76SkrcAei36SoLf50" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55b417c80610abf6d0d677c20f039965456fc6ba_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55b417c80610abf6d0d677c20f039965456fc6ba_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55b417c80610abf6d0d677c20f039965456fc6ba_2_1380x818.png 2x" data-dominant-color="9D9FC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1646×976 39 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @nrex45 (2022-11-21 16:23 UTC)

<p>Hi there,</p>
<p>A bit convoluted but here are some code examples that might get youon the right track useing the modeltomodel distance extension:</p>
<pre><code class="lang-auto">vtkOutput = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")

parameters = {}
parameters["vtkFile1"] = preprocessedSurface
parameters["vtkFile2"] = modelNode1
parameters['distanceType'] = "absolute_closest_point"
parameters["vtkOutput"] = vtkOutput

cliNode = slicer.cli.runSync(slicer.modules.modeltomodeldistance, None, parameters)

VTKFieldData = vtkOutput.GetMesh().GetAttributesAsFieldData(0)
mesh = vtkOutput.GetMesh()

resultTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", "defaultTable")
        
for j in range(0,VTKFieldData.GetNumberOfArrays()):
    #print(VTKFieldData.)
    resultTableNode.AddColumn(VTKFieldData.GetArray(j)) 
        
resultTableNode.AddColumn(mesh.GetPoints().GetData())
        
tableStorageNode = resultTableNode.CreateDefaultStorageNode()
tableStorageNode.SetFileName("TEST.csv")
tableStorageNode.WriteData(resultTableNode)


</code></pre>
<p>Haven’t tested the code in a while but this should generate a table of the output node, where you can look at the distances and see which are below a certain threshold and assume they are touching at those points.</p>
<p>Happy to answer FU quesions, let me know.</p>

---

## Post #3 by @TrascendentK (2022-11-21 17:01 UTC)

<p>Thanks for the answer. I figured it out by myself just five minutes ago.</p>
<p>I’ll post the code, i used using ray-casting if anyone needs it.<br>
Is it accurate enough or should i implement it your way? <a class="mention" href="/u/nrex45">@nrex45</a>.</p>
<pre><code class="lang-auto">#loading the model mesh
mesh = getNode(model_name).GetMesh()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(mesh)

#defining the coords of the tube (could be any sort of line-like obj i think)
pSource = points[0]
pTarget = points[1]

#evalutaing the actual intersections
obbTree = vtk.vtkOBBTree()
obbTree.SetDataSet(mesh)
obbTree.BuildLocator()
pointsVTKintersection = vtk.vtkPoints()
code = obbTree.IntersectWithLine(pSource, pTarget, pointsVTKintersection, None)
pointsVTKIntersectionData = pointsVTKintersection.GetData()
noPointsVTKIntersection = pointsVTKIntersectionData.GetNumberOfTuples()

#dealing with the intersection points
pointsIntersection = [] #where the intersections will be stored for future usage
for index in range(noPointsVTKIntersection):
    point_of_intersection = pointsVTKIntersectionData.GetTuple3(index)
    pointsIntersection.append(point_of_intersection)
   (slicer.mrmlScene.AddNewNodeByClass( 'vtkMRMLMarkupsFiducialNode', ('Centro coronale ' +   str(index)))).AddControlPointWorld(point_of_intersection)

return pointsIntersection #note that this is present only because in my code is part of a function that returns the coords, the actual drawing of the markups happens even if you decide to don't store the point in any variable
</code></pre>

---

## Post #4 by @chir.set (2022-11-21 20:02 UTC)

<p>This method seems to find the intersection also.</p>
<pre><code class="lang-auto"># Expect console erors.
slicer.mrmlScene.RemoveNode(sphereModel)
slicer.mrmlScene.RemoveNode(cylinderModel)
slicer.mrmlScene.RemoveNode(intersectionModel_0)
slicer.mrmlScene.RemoveNode(intersectionModel_1)

cylinder = vtk.vtkCylinderSource()
cylinder.SetRadius(5.0)
cylinder.SetHeight(100.0)
cylinder.SetResolution(45)
cylinder.Update()
cylinderTriangulator = vtk.vtkTriangleFilter()
cylinderTriangulator.SetInputConnection(cylinder.GetOutputPort())
cylinderTriangulator.Update()
cylinderModel = slicer.modules.models.logic().AddModel(cylinderTriangulator.GetOutput())
cylinderModel.SetName("cylinderModel")
cylinderModel.GetDisplayNode().SetOpacity(0.2)
cylinderModel.GetDisplayNode().SetColor(1.0, 0.0, 0.0)


sphere = vtk.vtkSphereSource()
sphere.SetRadius(25.0)
sphere.SetPhiResolution(45)
sphere.SetThetaResolution(45)
sphere.Update()
sphereTriangulator = vtk.vtkTriangleFilter()
sphereTriangulator.SetInputConnection(sphere.GetOutputPort())
sphereTriangulator.Update()
sphereModel = slicer.modules.models.logic().AddModel(sphereTriangulator.GetOutput())
sphereModel.SetName("sphereModel")
sphereModel.GetDisplayNode().SetOpacity(0.2)
sphereModel.GetDisplayNode().SetColor(0.0, 1.0, 0.0)


intersector = vtk.vtkIntersectionPolyDataFilter()
intersector.SetInputConnection(0, cylinderTriangulator.GetOutputPort())
intersector.SetInputConnection(1, sphereTriangulator.GetOutputPort())
intersector.Update()

intersectionModel_0 = slicer.modules.models.logic().AddModel(intersector.GetOutputDataObject(0))
intersectionModel_0.SetName("intersectionModel_0")
intersectionModel_0.GetDisplayNode().SetColor(0.0, 0.0, 1.0)

"""
# Cylinder (first input) minus intersection
intersectionModel_1 = slicer.modules.models.logic().AddModel(intersector.GetOutputDataObject(1))
intersectionModel_1.SetName("intersectionModel_1")
intersectionModel_1.GetDisplayNode().SetColor(1.0, 1.0, 0.0)
"""
</code></pre>

---
