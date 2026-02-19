---
topic_id: 24838
title: "Display Vtk Wedge In Slicer As Segmentation"
date: 2022-08-19
url: https://discourse.slicer.org/t/24838
---

# Display VTK Wedge in Slicer as Segmentation

**Topic ID**: 24838
**Date**: 2022-08-19
**URL**: https://discourse.slicer.org/t/display-vtk-wedge-in-slicer-as-segmentation/24838

---

## Post #1 by @connorh (2022-08-19 18:43 UTC)

<p>I’m trying to split a segment based on its rotational position (e.g. only getting a 15 deg wedge of the segmentation). I’m thinking the way to do this is to create a vtkWedge shape and take its intersection with the existing segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0cd42b5de958c3446a4e0c1ae6184ed7deb5dc7.jpeg" data-download-href="/uploads/short-url/mWwaaCkqXEToIM3JOSF2sXgqTWf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0cd42b5de958c3446a4e0c1ae6184ed7deb5dc7_2_274x250.jpeg" alt="image" data-base62-sha1="mWwaaCkqXEToIM3JOSF2sXgqTWf" width="274" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0cd42b5de958c3446a4e0c1ae6184ed7deb5dc7_2_274x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0cd42b5de958c3446a4e0c1ae6184ed7deb5dc7_2_411x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0cd42b5de958c3446a4e0c1ae6184ed7deb5dc7_2_548x500.jpeg 2x" data-dominant-color="9D9CA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">832×759 61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m creating a vtkWedge right now but I’m looking for something like “GetOutput()” that exists for a vtkSphere (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points" rel="noopener nofollow ugc">example</a>), so that I can assign my wedge shape to a segmentation node. Any suggestions? Here’s my existing code to create a wedge:</p>
<pre><code class="lang-auto">#Create Wedge Shape
wedge = vtk.vtkWedge()
wedge.GetPoints().SetPoint(0,0,0,0)
wedge.GetPoints().SetPoint(1,0,1,1)
wedge.GetPoints().SetPoint(2,0,1,1)
wedge.GetPoints().SetPoint(3,1,0,0)
wedge.GetPoints().SetPoint(4,1,0,1)
wedge.GetPoints().SetPoint(5,1,1,1)

#Create segmentation node from Wedge - can't figure this out

</code></pre>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2022-08-20 21:01 UTC)

<p><code>vtkWedge</code> is just a cell. You need to create a vtkPolyData, add points to it, then create a vtkWedge cell, add the point IDs to it, and then add the cell to the polydata. You can check out VTK examples for details, for example this <a href="https://kitware.github.io/vtk-examples/site/Cxx/Meshes/AddCell/">example that adds a triangle cell</a>.</p>
<p>You can create a segment from polydata using <code>AddSegmentFromClosedSurfaceRepresentation</code> as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">this example in the script repository</a>.</p>

---

## Post #3 by @connorh (2022-08-23 16:41 UTC)

<p>Hi Andras, thanks - that was very helpful - I’m close but I can’t get my wedge to work out - it seems like the vtkPolyData isn’t getting the correct faces, so from my 6 points defining the wedge, I get faces/triangles (0,1,2), (0,2,3), (0,3,4), (0,4,5) rather than my wedge shape.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcbce12b72ee62808f6bbbde2cd702d5443f2939.png" alt="image" data-base62-sha1="vuJIoIX4NToC7qslVfWT8dG5oXT" width="239" height="214"></p>
<p>Here’s my code:</p>
<pre><code class="lang-auto">modelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display

wedge = vtk.vtkWedge()
points = vtk.vtkPoints()

pt0 = np.array([0,0,0])
dx = np.array([1,0,0])
dx = np.array([0,1,0])
dx = np.array([0,0,1])

#define 6 coordinates for wedge
pts = [pt0, pt0 + dx + dy, pt0 + dx, pt0 + dz, pt0 + dx + dy + dz, pt0 + dx + dz]

for i in range(6):
  points.InsertNextPoint(pts[i])
  #slicer.modules.markups.logic().AddControlPoint(pts[i][0],pts[i][1],pts[i][2])

for i in range(6):
  wedge.GetPointIds().SetId(i,i)

wedges = vtk.vtkCellArray()
wedges.InsertNextCell(wedge)

wedgePD = vtk.vtkPolyData()
wedgePD.SetPoints(points)
wedgePD.SetPolys(wedges)
modelNode.SetAndObservePolyData(wedgePD)

# Import the model into the segmentation node
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(wedgeMN, segmentationNode)
</code></pre>
<p>I’ve also tried to manually define the faces without any impact:</p>
<pre><code class="lang-auto">faces = [5,  # number of faces
             3, 0, 1, 2,  # number of ids on face, ids
             3, 3, 5, 4,
             4, 1, 4, 5, 2,
             4, 0, 2, 5, 3,
             4, 1, 0, 3, 4]

wedge.SetFaces(faces)
wedge.Initialize()
</code></pre>
<p>Thanks for the help!</p>

---

## Post #4 by @lassoan (2022-08-23 17:10 UTC)

<p>Wedge is a volumetric cell, so it may need to be placed in a vtkUnstructuredGrid. However, I’m not sure if unstructured grid can be imported into a segmentation.</p>
<p>Overall, it may be simpler to create a wedge out of triangle cells and add them to a vtkPolyData.</p>

---

## Post #5 by @connorh (2022-08-23 18:01 UTC)

<p>Took your approach and just made wedge of triangles and it works great. Thank you!</p>

---
