# Measure (part of) model volume along centerline

**Topic ID**: 26853
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/measure-part-of-model-volume-along-centerline/26853

---

## Post #1 by @SvElst (2022-12-20 15:27 UTC)

<p>Hi,<br>
I have a tubular model (segmentation of a nerve). I used the ExtracCenterline module to extract the centerline of this model and the Cross-Section Analysis module to determine the diameter and cross-sectional area along the length of the model. However, I would also like to measure the volume of (part of) the model along the centerline. E.g. measure the volume of the first 1.5 cm of the model. Is there a way to do this automatically (with code)?<br>
Any ideas would be greatly appreciated.</p>
<p>Thanks in advance!</p>
<p>Slicer version: 5.0.3</p>

---

## Post #2 by @chir.set (2022-12-20 16:49 UTC)

<aside class="quote no-group" data-username="SvElst" data-post="1" data-topic="26853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/svelst/48/17772_2.png" class="avatar"> SvElst:</div>
<blockquote>
<p>Is there a way to do this automatically (with code)?</p>
</blockquote>
</aside>
<p>It should be doable.</p>
<p>First idea coming to mind is cutting the closed surface representation of the segment at 2 points and get the resulting volume. It should not be too hard to do that in the module itself. Do you have coding experience to implement it ?</p>

---

## Post #3 by @SvElst (2022-12-21 11:46 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> thank you for your prompt response!<br>
I’m afraid I only have basic knowledge of Slicer coding. I have the RAS-coordinates of the centerline, so I can use these to define the required starting point and end-point at which the segment should be cut. However, I am not sure how the closed surface representation can be cut automatically based on these points. Which module should be used for this? Any guidance on the code for this would be greatly appreciated!</p>

---

## Post #4 by @chir.set (2022-12-21 16:01 UTC)

<aside class="quote no-group" data-username="SvElst" data-post="3" data-topic="26853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/svelst/48/17772_2.png" class="avatar"> SvElst:</div>
<blockquote>
<p>Any guidance on the code for this would be greatly appreciated!</p>
</blockquote>
</aside>
<p>Your problem might have been partly resolved with this <a href="https://github.com/chir-set/SlicerExtension-VMTK/tree/WithStenosisMeasurement3D" rel="noopener nofollow ugc">branch</a> of forked SlicerVMTK. The latter branch has a hard dependency on this <a href="https://github.com/chir-set/SlicerExtraMarkups" rel="noopener nofollow ugc">extension</a> that is awaiting approval for merge in the extension index.</p>
<p>Said branch is written to calculate arterial stenosis measurement by volume between 2 arbitrary points. It calculates volumes of an arterial wall and a lumen. In your case, you need the volume of a segment only, that of a nerve, it’s the same for Slicer, just a segment. You could have been using it for your requirements even though that branch requires a second surface that is drawn by above mentionned pending extension.</p>
<p>As for modifying Cross-section analysis module to allow volume measurements between points, it does not seem reasonable after second thought, because it would deface this module. Much is already implemented in this module already, and as the name suggests, it’s for ‘cross-section analysis’, and not volume analysis.</p>
<p>However, you may get a volume with this code. Adjust object names and point indices.</p>
<pre><code class="lang-auto">def clipBetweenPoints(centerlinePolyData, surfacePolyData, p1Index, p2Index, outputPolyData):
    centerlinePoints = centerlinePolyData.GetPoints()
    
    p1 = [ 0.0 ] * 3
    p2 = [ 0.0 ] * 3
    centerlinePoints.GetPoint(p1Index, p1)
    centerlinePoints.GetPoint(p2Index, p2)
    
    p1Neighbour = [ 0.0 ] * 3
    p2Neighbour = [ 0.0 ] * 3
    centerlinePoints.GetPoint(p1Index + 1, p1Neighbour)
    centerlinePoints.GetPoint(p2Index - 1, p2Neighbour)
    if p1Index &gt; p2Index:
        centerlinePoints.GetPoint(p1Index - 1, p1Neighbour)
        centerlinePoints.GetPoint(p2Index + 1, p2Neighbour)
    
    startNormal = [ 0.0 ] * 3
    endNormal = [ 0.0 ] * 3
    vtk.vtkMath().Subtract(p1Neighbour, p1, startNormal)
    vtk.vtkMath().Subtract(p2Neighbour, p2, endNormal);
    
    startPlane = vtk.vtkPlane()
    startPlane.SetOrigin(p1)
    startPlane.SetNormal(startNormal)
    endPlane = vtk.vtkPlane()
    endPlane.SetOrigin(p2)
    endPlane.SetNormal(endNormal)
    planes = vtk.vtkPlaneCollection()
    planes.AddItem(startPlane)
    planes.AddItem(endPlane)
    
    clipper = vtk.vtkClipClosedSurface()
    clipper.SetClippingPlanes(planes)
    clipper.SetInputData(surfacePolyData)
    clipper.Update()
    
    triangleFilter = vtk.vtkTriangleFilter()
    triangleFilter.SetInputConnection(clipper.GetOutputPort())
    triangleFilter.Update()
    outputPolyData.DeepCopy(triangleFilter.GetOutput())
    
segmentationNode = slicer.util.getNode("Segmentation")
segmentationNode.CreateClosedSurfaceRepresentation()
segmentSurface = vtk.vtkPolyData()
segmentationNode.GetClosedSurfaceRepresentation("Segment_1", segmentSurface)

centerlineNode = slicer.util.getNode("Centerline model")
centerlinePolyData = centerlineNode.GetPolyData()

clippedPolyData = vtk.vtkPolyData()

clipBetweenPoints(centerlinePolyData, segmentSurface, 10, 50, clippedPolyData)

mp = vtk.vtkMassProperties()
mp.SetInputData(clippedPolyData)
mp.Update()
volume = mp.GetVolume()
</code></pre>

---

## Post #5 by @SvElst (2022-12-22 08:11 UTC)

<p>Thank you so much, this is really helpful! I’ll definitely try this.</p>

---

## Post #6 by @lassoan (2022-12-22 14:53 UTC)

<p>You can also use Scissors effect in Segment Editor module, or Dynamic Modeler module to cut off pieces from a segmentation or model.</p>
<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="26853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Your problem might have been partly resolved with this <a href="https://github.com/chir-set/SlicerExtension-VMTK/tree/WithStenosisMeasurement3D">branch</a> of forked SlicerVMTK. The latter branch has a hard dependency on this <a href="https://github.com/chir-set/SlicerExtraMarkups">extension</a> that is awaiting approval for merge in the extension index.</p>
</blockquote>
</aside>
<p>I’ve worked a lot on fixing SlicerExtraMarkups build errors on Windows and macOS. The problem is that private symbols are not exported to shared libraries on these operating systems, therefore storage node classes must be completely reworked in Slicer core. The redesign is complete and I have been just reviewing, simplifying, and testing the code. I hope to be able to finalize it during the next few weeks and once it is merged into Slicer core, I’ll update SlicerExtraMarkups accordingly and it can be added to the Extensions Index.</p>

---

## Post #7 by @chir.set (2022-12-22 17:54 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="26853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>… Scissors effect …Dynamic Modeler … cut off…</p>
</blockquote>
</aside>
<p>It’s indeed the simplest method, too obvious !</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="26853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>fixing SlicerExtraMarkups build errors on Windows and macOS</p>
</blockquote>
</aside>
<p>No problem, thanks for considering this work.</p>
<p>Just out of curiosity, how is it different here with core markups ? Everything is public/protected in the storage node classes, as templated from ROI storage node.</p>

---

## Post #8 by @lassoan (2022-12-22 18:35 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="26853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Just out of curiosity, how is it different here with core markups ? Everything is public/protected in the storage node classes, as templated from ROI storage node.</p>
</blockquote>
</aside>
<p>Private symbols are visible within the library, so the private methods are all usable for classes in Slicer core, but not outside, in other modules. We knew that it was not a nice design when we implemented it, but decided to release the feature and improve it later.</p>

---
