---
topic_id: 35351
title: "Calculate A Surface"
date: 2024-04-08
url: https://discourse.slicer.org/t/35351
---

# Calculate a surface

**Topic ID**: 35351
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/calculate-a-surface/35351

---

## Post #1 by @ILB (2024-04-08 11:40 UTC)

<p>Hi!<br>
Is there a way in which I can estimate the area of contact between the tumor and the organ?<br>
Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edb7a0ed866b8a358b97deaee7b4bdb46648ba0a.jpeg" data-download-href="/uploads/short-url/xUWA95wkhvCf9J2vwGOtjjPZTFo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edb7a0ed866b8a358b97deaee7b4bdb46648ba0a_2_553x500.jpeg" alt="image" data-base62-sha1="xUWA95wkhvCf9J2vwGOtjjPZTFo" width="553" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edb7a0ed866b8a358b97deaee7b4bdb46648ba0a_2_553x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edb7a0ed866b8a358b97deaee7b4bdb46648ba0a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edb7a0ed866b8a358b97deaee7b4bdb46648ba0a.jpeg 2x" data-dominant-color="3D2B2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">646×584 36.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @RafaelPalomar (2024-04-08 15:25 UTC)

<p>Hello <a class="mention" href="/u/ilb">@ILB</a>. In order to solve this problem I like to use both the segmentation data and the surface data (3D models). This dual representation is useful to do computations having intersections insides and outsides as a target. The approach is roughly as follows assuming you have both 3D models and segmentations of the organ and the tumor (it is possible to generate the segmentation data if you have the models too):</p>
<ol>
<li>Iterate over all points in the organ and convert the coordinates to the segmentation image space of the tumor (RASToIJK).</li>
<li>Check the value of the image for the given coordinates and if it matches the tumor label, it means that the point is organ surface AND is inside the tumor tissue.</li>
<li>Add the matching points to a new mesh. Here you could even copy the organ mesh and replace the points by a new list of points containing only the matched points.</li>
<li>Compute the surface area of the newly generated mesh.</li>
</ol>
<p>The following is an example created with synthetic data. Python script to generate all of this is also provided (parts of this script were generated using AI):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daa888df397a658457d0370b9d539bc301388a69.jpeg" data-download-href="/uploads/short-url/vclaGGagK8XWWBbm4id01UN00S5.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa888df397a658457d0370b9d539bc301388a69_2_690x411.jpeg" alt="Screenshot" data-base62-sha1="vclaGGagK8XWWBbm4id01UN00S5" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa888df397a658457d0370b9d539bc301388a69_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa888df397a658457d0370b9d539bc301388a69_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa888df397a658457d0370b9d539bc301388a69_2_1380x822.jpeg 2x" data-dominant-color="989CC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1448×864 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre data-code-wrap="python"><code class="lang-python">#!/usr/bin/env python3

import numpy as np

############################################################
## STEP 1; Generate synthetic data (two overlapping spheres)
############################################################

# Create a high-resolution sphere
sphereSource1 = vtk.vtkSphereSource()
sphereSource1.SetCenter(0, 0, 0)
sphereSource1.SetRadius(50)
sphereSource1.SetThetaResolution(100)  # Increase theta resolution
sphereSource1.SetPhiResolution(100)    # Increase phi resolution
sphereSource1.Update()

# Create another high-resolution sphere
sphereSource2 = vtk.vtkSphereSource()
sphereSource2.SetCenter(20, 20, 0) # Slightly offset to show overlapping
sphereSource2.SetRadius(30)
sphereSource2.SetThetaResolution(100)  # Increase theta resolution
sphereSource2.SetPhiResolution(100)    # Increase phi resolution
sphereSource2.Update()

# Create a model node for the first high-resolution sphere
modelNode1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
modelNode1.SetName("WhiteSphere")
modelNode1.SetAndObserveMesh(sphereSource1.GetOutput())

# Create a model display node for the first sphere (White color)
modelDisplayNode1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")
modelDisplayNode1.SetColor(1, 1, 1)  # RGB for White
modelDisplayNode1.SetOpacity(0.5)  # Semi-transparent
modelNode1.SetAndObserveDisplayNodeID(modelDisplayNode1.GetID())

# Create a model node for the second high-resolution sphere
modelNode2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
modelNode2.SetName("PurpleSphere")
modelNode2.SetAndObserveMesh(sphereSource2.GetOutput())

# Create a model display node for the second sphere (Purple color)
modelDisplayNode2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")
modelDisplayNode2.SetColor(0.5, 0, 0.5)  # RGB for Purple
modelDisplayNode2.SetOpacity(0.5)  # Semi-transparent
modelNode2.SetAndObserveDisplayNodeID(modelDisplayNode2.GetID())


##############################################################
## STEP 2: Convert purple sphere model to scalar volume data
##############################################################
#
# This is not really needed if one has the segmentation the 3D models derives from.
# It is also possible to do this through the 3D Slicer ui within the segmentations module
# and the volumes module

modelNode = slicer.util.getNode('PurpleSphere')

# Create a new segmentation node
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetName("PurpleSphereSegmentation")

# Import the model into the segmentation
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(modelNode, segmentationNode)
#segmentationNode.CreateClosedSurfaceRepresentation()

# Create a new label map volume node for exporting the segmentation
labelMapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
labelMapVolumeNode.SetName("LabelMapFromPurpleSphere")

# Get the segmentation's associated transform node (if any) to apply the same transform to the label map volume
transformNode = segmentationNode.GetParentTransformNode()
if transformNode:
    labelMapVolumeNode.SetAndObserveTransformNodeID(transformNode.GetID())

# Export the segmentation to the label map volume without specifying a reference volume for geometry
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelMapVolumeNode)

# Create a new scalar volume node from the label map volume node
volumeNode = slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene, labelMapVolumeNode, labelMapVolumeNode)
volumeNode.SetName("Volume")

print("Conversion to scalar volume completed.")

##############################################################
## STEP 3: Compute a new mesh with the points of the white sphere
##         intersecting the volume of the purple sphere
##############################################################
# This iterates over the points of the white spere and translates the points
# to the purple sphere volume space. If the image value of the corresponding coordinates
# is 1, then the point belongs to the white sphere AND is inside the purple sphere. Here
# we also add the points to a new mesh

# Helper function to convert RAS to IJK coordinates
def rasToIjk(pointRAS, volumeNode):
    rasToIjkMatrix = vtk.vtkMatrix4x4()
    volumeNode.GetRASToIJKMatrix(rasToIjkMatrix)
    pointIJK = [0, 0, 0, 1]  # Homogeneous coordinates
    rasToIjkMatrix.MultiplyPoint(pointRAS + (1,), pointIJK)
    return [int(pointIJK[0]), int(pointIJK[1]), int(pointIJK[2])]

modelNode = slicer.util.getNode('WhiteSphere')
volumeImageData = volumeNode.GetImageData()

# Get mesh data
mesh = modelNode.GetMesh()
points = mesh.GetPoints()
numPoints = points.GetNumberOfPoints()
numPolys = mesh.GetNumberOfCells()

# Initialize structures to hold inside points and cells
insidePointIds = []
insideCells = vtk.vtkCellArray()

# Check each point and keep those inside the volume
pointStatus = np.zeros(numPoints, dtype=bool)
for i in range(numPoints):
    pointRAS = points.GetPoint(i)
    pointIJK = rasToIjk(pointRAS, volumeNode)

    # Check if the point is inside the volume bounds
    bounds = volumeNode.GetImageData().GetExtent()
    if bounds[0] &lt;= pointIJK[0] &lt;= bounds[1] and bounds[2] &lt;= pointIJK[1] &lt;= bounds[3] and bounds[4] &lt;= pointIJK[2] &lt;= bounds[5]:
        # The point is inside, save it and its index
        if volumeImageData.GetScalarComponentAsDouble(*pointIJK, 0) == 1:
            pointStatus[i] = True
            insidePointIds.append(i)

# Map from old point indices to new ones
newIndices = {oldIndex: newIndex for newIndex, oldIndex in enumerate(insidePointIds)}

# Check each polygon to see if all its vertices are inside
for i in range(numPolys):
    cellPoints = mesh.GetCell(i).GetPointIds()
    if all(pointStatus[cellPoints.GetId(j)] for j in range(cellPoints.GetNumberOfIds())):
        newCellPointIds = [newIndices[cellPoints.GetId(j)] for j in range(cellPoints.GetNumberOfIds())]
        insideCells.InsertNextCell(len(newCellPointIds), newCellPointIds)

# Create new mesh data
newPoints = vtk.vtkPoints()
newPoints.SetNumberOfPoints(len(insidePointIds))
for newIndex, oldIndex in enumerate(insidePointIds):
    newPoints.SetPoint(newIndex, points.GetPoint(oldIndex))

newPolyData = vtk.vtkPolyData()
newPolyData.SetPoints(newPoints)
newPolyData.SetPolys(insideCells)

# Create a new model node for the resulting mesh
newModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "InsideSphereMesh")
newModelNode.SetAndObserveMesh(newPolyData)

# Optionally, set up a display node for it
displayNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")
displayNode.SetColor(0, 1, 0)  # Use green color for visibility
newModelNode.SetAndObserveDisplayNodeID(displayNode.GetID())


##############################################################
## STEP 4: Compute the surface of a mesh
##############################################################
# In this case we compute the surface of the newly generated intersection
# mesh. The area should be in squared milimeters.

# Create a triangle filter to ensure the mesh consists of triangles
triangleFilter = vtk.vtkTriangleFilter()
triangleFilter.SetInputData(newPolyData)
triangleFilter.Update()

# Calculate the surface area
massProperties = vtk.vtkMassProperties()
massProperties.SetInputData(triangleFilter.GetOutput())
massProperties.Update()

surfaceArea = massProperties.GetSurfaceArea()

print(f"The surface area of the resulting mesh is: {surfaceArea} square units")
</code></pre>

---

## Post #3 by @ILB (2024-04-09 06:15 UTC)

<p>thank you for your answer! I will try and see if it works for me. However, is there any other approach without having to introduce any script?<br>
It would be really useful.<br>
Thank you again for your time!<br>
Best wishes</p>

---

## Post #4 by @RafaelPalomar (2024-04-09 07:17 UTC)

<aside class="quote no-group" data-username="ILB" data-post="3" data-topic="35351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e9c0ed/48.png" class="avatar"> ILB:</div>
<blockquote>
<p>However, is there any other approach without having to introduce any script?</p>
</blockquote>
</aside>
<p>There might be different extensions with  all the tools to make this processing workflow possible (I’m not aware of this). Alternatively, if you want to make this more accessible, you could make your own extension and distribute it through the Slicer Extension Manager. If you follow this approach, be aware of the changes that are going to be introduced in the Extensions ecosystem (<a href="https://discourse.slicer.org/t/introduction-of-tiers-for-slicer-extensions/34870" class="inline-onebox">Introduction of "tiers" for Slicer extensions</a>)</p>

---

## Post #5 by @Matteboo (2024-04-09 08:27 UTC)

<p>I thought a little bit about this and I came up with that:<br>
area of contact= (area tumor + area organ - area of the union)/2<br>
With the union being the union of your tumor and your organ.<br>
Be carefull as this only work if your segmentation don’t overlap.<br>
(If they overlap, can you explain what you consider the area of contact)</p>
<p>You can create the union using the segment editor module<br>
Once you have the union, you can get the different area using the segment statistic module<br>
This is doable without any script</p>
<p>Don’t hesitate to ask if you have any question about this</p>

---

## Post #6 by @lassoan (2024-04-09 11:57 UTC)

<p>Nice ideas! Just adding one more method: you can use the ModelToModelDistance extension to compute distance of one model surface from the other. Then use threshold filter to keep only the region that is very close to the other model. The advantage of this method is that it works even if the segments slightly overlap or there are small gaps.</p>

---

## Post #7 by @cpinter (2024-04-09 12:49 UTC)

<p>You can also use this VTK filter:<br>
<a href="https://vtk.org/doc/nightly/html/classvtkCollisionDetectionFilter.html" class="onebox" target="_blank" rel="noopener">https://vtk.org/doc/nightly/html/classvtkCollisionDetectionFilter.html</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd76f4c9cc5b871f3de99d38f23cda32344a68d3.png" alt="image" data-base62-sha1="tjCK7GkKa4CkcseiRxLmXUL7S27" width="640" height="480"></p>

---

## Post #8 by @ILB (2024-04-10 11:55 UTC)

<p>Thank you all for so many possibilities! I will explore them all and see how they work.<br>
Best wishes</p>

---
