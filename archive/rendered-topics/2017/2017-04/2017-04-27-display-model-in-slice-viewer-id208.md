---
topic_id: 208
title: "Display Model In Slice Viewer"
date: 2017-04-27
url: https://discourse.slicer.org/t/208
---

# Display model in slice viewer

**Topic ID**: 208
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/display-model-in-slice-viewer/208

---

## Post #1 by @mag (2017-04-27 11:28 UTC)

<p>Hi, I am trying to draw a polygon on the axial viewer given the coordinates of some fiducial points. I am using a model created from a polydata object so I can easily export it for my analysis.<br>
I used this code in a scripted module and the polygon is correctly displayed in the 3D view but I don’t know how to display it in the red view as well, which is what I need. Is that possible?<br>
I’ve attached a screenshot at the end.</p>
<p>fidList = slicer.util.getNode(‘F’)<br>
if not fidList:<br>
print “No points found”<br>
return<br>
numFids = fidList.GetNumberOfFiducials()</p>
<p>points = vtk.vtkPoints()<br>
polygon = vtk.vtkPolygon()<br>
polygon.GetPointIds().SetNumberOfIds(numFids)</p>
<p>points_coords = <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
for i in range(numFids):<br>
fid_ras_coord = [0, 0, 0]<br>
fidList.GetNthFiducialPosition(i, fid_ras_coord)<br>
points.InsertNextPoint(fid_ras_coord)<br>
polygon.GetPointIds().SetId(i, i)<br>
points_coords.append(fid_ras_coord)</p>
<p>polygons = vtk.vtkCellArray()<br>
polygons.InsertNextCell(polygon)<br>
polygonPolyData = vtk.vtkPolyData()<br>
polygonPolyData.SetPoints(points)<br>
polygonPolyData.SetPolys(polygons)</p>
<p>model = slicer.vtkMRMLModelNode()<br>
model.SetAndObservePolyData(polygonPolyData)<br>
modelDisplay = slicer.vtkMRMLModelDisplayNode()</p>
<p>modelDisplay.SetColor(1, 1, 0)<br>
modelDisplay.BackfaceCullingOff()<br>
modelDisplay.SetOpacity(0.5)<br>
modelDisplay.SetPointSize(3)</p>
<p>modelDisplay.SetSliceIntersectionVisibility(True)<br>
modelDisplay.SetVisibility(True)<br>
slicer.mrmlScene.AddNode(modelDisplay)<br>
model.SetAndObserveDisplayNodeID(modelDisplay.GetID())<br>
modelDisplay.SetInputPolyDataConnection(model.GetPolyDataConnection())<br>
slicer.mrmlScene.AddNode(model)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cb7526feec9be95dfdbc9682abed55f679d5b17.jpeg" data-download-href="/uploads/short-url/k4PBUwS8mcNWmd6pyaUPL6oEzwb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb7526feec9be95dfdbc9682abed55f679d5b17_2_690x422.jpeg" alt="image" data-base62-sha1="k4PBUwS8mcNWmd6pyaUPL6oEzwb" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb7526feec9be95dfdbc9682abed55f679d5b17_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb7526feec9be95dfdbc9682abed55f679d5b17_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cb7526feec9be95dfdbc9682abed55f679d5b17_2_1380x844.jpeg 2x" data-dominant-color="3A3A46"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1513×927 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2017-04-27 12:29 UTC)

<p>You can only see the intersection of the polydata with a slice, so the polydata has to be a 3D surface (theoretically it could be possible to have a 2D surface that is exactly aligned with the slice viewer, but in practice perfect alignment is often impossible to achieve).<br>
Fortunately, the <code>Markups to model</code> module in SlicerIGT extension does extactly that. It has several options for generating closed surface from a set of markups. It can do simple convex hull or smoothed contour with various options for making it more robust or accurate.</p>
<p>Simple quasi-planar surface generation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/d145e35e9961e306dc31b7ff1753f2118627283e.jpg" data-download-href="/uploads/short-url/tRjwC1uChtCGIEXzRDnzZVuFcAu.jpg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d145e35e9961e306dc31b7ff1753f2118627283e_2_690x441.jpg" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d145e35e9961e306dc31b7ff1753f2118627283e_2_690x441.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d145e35e9961e306dc31b7ff1753f2118627283e_2_1035x661.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d145e35e9961e306dc31b7ff1753f2118627283e_2_1380x882.jpg 2x" data-dominant-color="A19DA6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">3000×1920 925 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Smooth 3D surface generation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/f0df0ce5445878118e78fe55c6e4b443275d89ab.jpg" data-download-href="/uploads/short-url/ymQtweNeQczm8gOeT7uBfW5L1An.jpg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f0df0ce5445878118e78fe55c6e4b443275d89ab_2_690x441.jpg" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f0df0ce5445878118e78fe55c6e4b443275d89ab_2_690x441.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f0df0ce5445878118e78fe55c6e4b443275d89ab_2_1035x661.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f0df0ce5445878118e78fe55c6e4b443275d89ab_2_1380x882.jpg 2x" data-dominant-color="A29CA6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">3000×1920 969 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To generate the contours from your own module, you just need to add a vtkMRMLMarkupsToModelNode in your scene and set up its inputs and outputs. At minimum, call SetAndObserveMarkupsNodeID and SetAndObserveModelNodeID. See all methods and options at:<br>
<a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/MarkupsToModel/MRML/vtkMRMLMarkupsToModelNode.h" class="onebox" target="_blank" rel="noopener">https://github.com/SlicerIGT/SlicerIGT/blob/master/MarkupsToModel/MRML/vtkMRMLMarkupsToModelNode.h</a></p>

---

## Post #3 by @mag (2017-04-28 09:59 UTC)

<p>Thanks a lot for the reply.<br>
Now I can show the polygon in all the viewers using the IGT extension.<br>
However I could not figure out how to use vtkMRMLMarkupsToModelNode in my module. How do I set input and output?</p>
<p>Marta</p>

---

## Post #4 by @lassoan (2017-04-28 20:30 UTC)

<p>Example: drop a few fiducials and run this code</p>
<pre><code>inputMarkups = getNode('F')

outputModel = slicer.mrmlScene.AddNode(slicer.vtkMRMLModelNode())
outputModel.CreateDefaultDisplayNodes()
outputModel.GetDisplayNode().SetSliceIntersectionVisibility(True)
outputModel.GetDisplayNode().SetColor(1,0,0)

markupsToModel = slicer.mrmlScene.AddNode(slicer.vtkMRMLMarkupsToModelNode())
markupsToModel.SetAutoUpdateOutput(True)
markupsToModel.SetAndObserveModelNodeID(outputModel.GetID())
markupsToModel.SetAndObserveMarkupsNodeID(inputMarkups.GetID())</code></pre>

---

## Post #5 by @labixin (2021-02-15 15:15 UTC)

<p>Thank you. I am creating a model (closed surface) based on points using Markups to Model module. The results are satisfactory. Is there any related literatures I could refer to? (for reference when describing algorithms in the scientific paper). Hope for some suggestions. Your help is highly appreciated!</p>
<p>Crayon</p>

---

## Post #6 by @lassoan (2021-02-15 16:32 UTC)

<p>Please cite <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#how-to-cite">3D Slicer</a> and in addition you can cite:</p>
<ul>
<li><a href="https://github.com/SlicerIGT/SlicerMarkupsToModel">3D Slicer’s Markups to model extension</a></li>
<li><a href="https://vtk.org/vtk-textbook/">VTK library</a></li>
<li><a href="https://dl.acm.org/doi/pdf/10.1145/237170.237254">Butterfly subdivision method</a></li>
</ul>

---

## Post #7 by @slicer365 (2025-02-21 13:17 UTC)

<p>Based on this, how to set the model’s radius?</p>
<p>MarkupsToModel.SetTubeRadius(5)  like this ,it does not work</p>

---

## Post #8 by @cpinter (2025-02-21 13:30 UTC)

<p>That function works, but only in curve mode</p>
<pre><code class="lang-auto">markupsToModel.SetModelType(slicer.vtkMRMLMarkupsToModelNode.Curve)
</code></pre>

---
