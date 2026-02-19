---
topic_id: 4130
title: "Intersection Two Models Plane And Centerlines Ct Mr"
date: 2018-09-17
url: https://discourse.slicer.org/t/4130
---

# Intersection two models (Plane and centerlines CT/MR)

**Topic ID**: 4130
**Date**: 2018-09-17
**URL**: https://discourse.slicer.org/t/intersection-two-models-plane-and-centerlines-ct-mr/4130

---

## Post #1 by @shahrokh (2018-09-17 14:12 UTC)

<p>Hi 3DSlicer users and developers</p>
<p>I’m sorry that I repeat my question in another way. I still have problem to find the points of collision.<br>
As you can see, I have three models.</p>
<p>Model 1 (CenterlinesMRI):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2535e1ece62741b0065f4334a0737027d4cec42f.png" data-download-href="/uploads/short-url/5jb6LFAlkIJCWidc8TrSVndMSzJ.png?dl=1" title="centerlines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2535e1ece62741b0065f4334a0737027d4cec42f.png" alt="centerlines" data-base62-sha1="5jb6LFAlkIJCWidc8TrSVndMSzJ" width="690" height="355" data-dominant-color="9EA1CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">centerlines</span><span class="informations">1440×741 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Model 2 (CenterlinesCT):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e0cced812fde36fcb0391ca6095fdda9742ef4e.png" data-download-href="/uploads/short-url/20i7MG24J04JOuvR1xMLqnXJXoG.png?dl=1" title="CenterlinesCT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e0cced812fde36fcb0391ca6095fdda9742ef4e.png" alt="CenterlinesCT" data-base62-sha1="20i7MG24J04JOuvR1xMLqnXJXoG" width="690" height="355" data-dominant-color="9F99CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CenterlinesCT</span><span class="informations">1440×741 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Model 2 (Plane):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6e1044fea957ccda27d99e649e09736ab4c936c.png" data-download-href="/uploads/short-url/wWrUHBpKusgcdeoBaDmUa8KGa0Q.png?dl=1" title="plane" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6e1044fea957ccda27d99e649e09736ab4c936c.png" alt="plane" data-base62-sha1="wWrUHBpKusgcdeoBaDmUa8KGa0Q" width="690" height="355" data-dominant-color="9294BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">plane</span><span class="informations">1440×741 12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I want to extract the points of collision between the centerlines (CenterlinesMRI and CenterlinesCT) and plane.</p>
<p>Two Models (CenterlinesCT+ Plane):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/469615cbb8e7c9b9652e0c98ba9b250dd7f01380.png" data-download-href="/uploads/short-url/a4qYGJR9wUzQOi4sqU2Zq3jbaog.png?dl=1" title="planeANDcenterlinesCT" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/469615cbb8e7c9b9652e0c98ba9b250dd7f01380.png" alt="planeANDcenterlinesCT" data-base62-sha1="a4qYGJR9wUzQOi4sqU2Zq3jbaog" width="690" height="355" data-dominant-color="9896C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">planeANDcenterlinesCT</span><span class="informations">1440×741 16.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Two Models (CenterlinesMR+ Plane):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9795e0caedc407d18656a35037b02d8cd1dfbe2.png" data-download-href="/uploads/short-url/zAWUWVIq5rBSYkJEyBcJJfAvENY.png?dl=1" title="planeANDcenterlines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9795e0caedc407d18656a35037b02d8cd1dfbe2.png" alt="planeANDcenterlines" data-base62-sha1="zAWUWVIq5rBSYkJEyBcJJfAvENY" width="690" height="355" data-dominant-color="9597BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">planeANDcenterlines</span><span class="informations">1440×741 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I do it using 3DSlicer modules or python programming?<br>
Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @pieper (2018-09-17 14:32 UTC)

<p>I guess you mean the intersection points between the lines and the plane? You can look at the <a href="https://www.vtk.org/doc/nightly/html/classvtkCutter.html#details">vtkCutter</a> class.  You can get the vtkPolyData from Slicer’s model nodes as input and then create a <a href="https://www.vtk.org/doc/nightly/html/classvtkPlane.html#details">plane</a> as the implicit function for cutting.</p>

---

## Post #3 by @shahrokh (2018-09-18 09:01 UTC)

<p>Dear Steve</p>
<p>Thanks a lot for you guidance. I can extract these intersection points with the following commands:</p>
<pre><code>import vtk
import os
filenameCLMergedMR = "centerlinesMergedMR.vtp";
readerCLMergedMR = vtk.vtkXMLPolyDataReader();
readerCLMergedMR.SetFileName(filenameCLMergedMR);
readerCLMergedMR.Update();
polydata = readerCLMergedMR.GetOutput();
points = polydata.GetPoints();
numPoints = readerCLMergedMR.GetNumberOfPoints();
lineCellArray = vtk.vtkCellArray();
lineCellArray.InsertNextCell(numPoints);
for i in range(0,numPoints):
 lineCellArray.InsertCellPoint(i)
linePolyData = vtk.vtkPolyData()
linePolyData.SetPoints(points)
linePolyData.SetLines(lineCellArray)

plane = vtk.vtkPlane()
plane.SetOrigin(0, 0, 0)
plane.SetNormal(0, 0, 1)

clipper = vtk.vtkClipPolyData()
clipper.SetInputConnection(readerCLMergedMR.GetOutputPort())
cutEdges = vtk.vtkCutter()
cutEdges.SetInputConnection(readerCLMergedMR.GetOutputPort())
cutEdges.SetCutFunction(plane)
cutEdges.GenerateCutScalarsOn()
cutStrips = vtk.vtkStripper()
cutStrips.SetInputConnection(cutEdges.GetOutputPort())
cutStrips.Update()
cutPoly = vtk.vtkPolyData()
cutPoly.SetPoints(cutStrips.GetOutput().GetPoints())

writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName("intersectionPoints.vtp")
writer.SetInputDataObject(cutStrips.GetOutput())
writer.Write()
</code></pre>
<p>Thanks a lot,<br>
Shahrokh</p>

---
