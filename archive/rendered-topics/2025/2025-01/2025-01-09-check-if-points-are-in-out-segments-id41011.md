# Check if points are in/out segments

**Topic ID**: 41011
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/check-if-points-are-in-out-segments/41011

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-01-09 08:54 UTC)

<p>Hi to everyone. A quick question for today <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>My goal is to know what points (contained in a fiducialsNode) are in/out  one segment. Like in the photo:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0a46efb3ce717f824c418cc620a7ae0f0fb6f21.png" data-download-href="/uploads/short-url/w3hfxcYw36A26s2JrpvZLnlGOch.png?dl=1" title="Captura de pantalla 2025-01-09 094830" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0a46efb3ce717f824c418cc620a7ae0f0fb6f21_2_541x500.png" alt="Captura de pantalla 2025-01-09 094830" data-base62-sha1="w3hfxcYw36A26s2JrpvZLnlGOch" width="541" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0a46efb3ce717f824c418cc620a7ae0f0fb6f21_2_541x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0a46efb3ce717f824c418cc620a7ae0f0fb6f21.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0a46efb3ce717f824c418cc620a7ae0f0fb6f21.png 2x" data-dominant-color="414757"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-01-09 094830</span><span class="informations">545×503 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At this moment I use the labelmap representation of the segment and the points in IJK coordinates. I’m wondering if exist a way to do it directly using the points in RAS coordinates and the segment.</p>
<p>Thanks.</p>

---

## Post #2 by @bserrano (2025-01-10 07:48 UTC)

<p>Hi,</p>
<p>This is a very interesting topic. I find it particularly useful for cleaning geometries and point clouds. Please let me know if you’ve managed to resolve the issue.</p>
<p>Thanks.</p>

---

## Post #3 by @chir.set (2025-01-10 08:13 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="41011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>are in/out</p>
</blockquote>
</aside>
<p>You may investigate vtkExtractEnclosedPoints and vtkSelectEnclosedPoints.</p>

---

## Post #4 by @SANTIAGO_PENDON_MING (2025-01-10 09:51 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="41011">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>vtkSelectEnclosedPoints</p>
</blockquote>
</aside>
<p>That was the solution!</p>
<p>The vtkExtractEnclosedPoints I couldn’t make it work by the way. The basic code I made is:</p>
<pre><code class="lang-auto">

segmentNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")  



segmentId = segmentNode.GetSegmentation().GetNthSegmentID(0)  
geometry = vtk.vtkPolyData()
segmentNode.GetClosedSurfaceRepresentation(segmentId, geometry)




points_array = np.load("puntos.npy")  




points = vtk.vtkPoints()
for point in points_array:
    points.InsertNextPoint(point)


pointCloud = vtk.vtkPolyData()
pointCloud.SetPoints(points)


enclosedPointsFilter = vtk.vtkSelectEnclosedPoints()
enclosedPointsFilter.SetInputData(pointCloud)
enclosedPointsFilter.SetSurfaceData(geometry)  
enclosedPointsFilter.Update()


inside_mask = []
for i in range(points.GetNumberOfPoints()):
    is_inside = enclosedPointsFilter.IsInside(i)  fuera
    inside_mask.append(is_inside)
    print(f"Point{i}: {'Inside' if is_inside else 'Outside'}")



</code></pre>

---
