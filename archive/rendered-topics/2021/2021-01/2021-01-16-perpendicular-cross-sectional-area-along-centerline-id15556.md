---
topic_id: 15556
title: "Perpendicular Cross Sectional Area Along Centerline"
date: 2021-01-16
url: https://discourse.slicer.org/t/15556
---

# perpendicular cross sectional area along centerline

**Topic ID**: 15556
**Date**: 2021-01-16
**URL**: https://discourse.slicer.org/t/perpendicular-cross-sectional-area-along-centerline/15556

---

## Post #1 by @airtech2 (2021-01-16 15:20 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I need a perpendicular cross sectional area along centerline in vessel segmentation model.</p>
<p>I can extract centerline using VMTK extension and get diameter along centerline using centerline metrics extension.</p>
<p>However, I don’t know how to automatically measure the perpendicular cross sectional area’s’ along extracted centerline.</p>
<p>It will be very useful to determine the appropriate stent size in stenotic curved vassel.</p>

---

## Post #2 by @airtech2 (2021-01-16 15:20 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:<br>
I had done segmentation of vessel and extract centerline with VMTK tool kit<br>
With centerline metrics, i was able to get diameter of vessel along centerline<br>
(Radius of inscribed sphere). However, clinically, when clinicians plans to do stent insertion, we need to know cross sectional area along to centerline to determine the size of stent.<br>
I have trouble with calculate the cross sectional area perpendicular to center line<br>
Is there any way to automatically calculate perpendicular cross sectional area along centerline ?</p>

---

## Post #4 by @lassoan (2021-01-16 15:23 UTC)

<p>You can use “Cross-section analysis” module in recent versions of SlicerVMTK (you need to install Slicer at least to the latest stable release).</p>

---

## Post #5 by @chir.set (2021-01-16 16:21 UTC)

<p>At a stenotic point, whether in curved or straight arterial part, the contrasted lumen’s surface area won’t be helpful to measure the vessel’s diameter. It will always be underestimated because, well, it is by definition decreased.</p>
<p>With the Cross-Section Analysis module, you can place a slice view at the point of interest,  perpendicular to the centerline, and measure the diameter manually. Calcifications may render this unfeasible, but the diameter downstream and upstream should be useful hints. Centerline Metrics on its own can hint similarly.</p>

---

## Post #6 by @chir.set (2021-01-16 19:34 UTC)

<p>Unless I misunderstood :</p>
<p>Class vtkVmtk/ComputationalGeometry/vtkvmtkPolyDataCenterlineSections.h computes</p>
<ul>
<li>Area</li>
<li>Min Size</li>
<li>Max Size</li>
<li>Shape</li>
<li>Closed</li>
</ul>
<p>for a centerline.</p>
<p>This file is not included anywhere, hence it does not seem to be used.</p>
<p>It has an interesting ::RequestData function, this is not public however.</p>
<p>If you can convince VMTK devs to expose these data with the 3 arrays attached to a centerline (Radius, EdgeArray, EdgePCoordArray), that would open a way to show them at every centerline point.</p>
<p>Good luck.</p>

---

## Post #7 by @lassoan (2021-01-16 21:26 UTC)

<p>vtkvmtkPolyDataCenterlineSection just gives a value for each centerline section (region between two bifurcations), so it is not very useful for analyzing a single vessel branch.</p>
<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It has an interesting ::RequestData function, this is not public however.</p>
</blockquote>
</aside>
<p>RequestData is never public, that is called by the VTK filter pipeline executor.</p>
<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>If you can convince VMTK devs to expose these data with the 3 arrays attached to a centerline (Radius, EdgeArray, EdgePCoordArray), that would open a way to show them at every centerline point.</p>
</blockquote>
</aside>
<p>Most recent Slicer versions can now store and visualize scalar arrays associated with centerlines. I’ve now updated “Extract Centerline” module in SlicerVMTK to add radius array to the curve node (it will be available for Slicer Preview Release form tomorrow). This can be used to color the centerline, but it could be also used in Cross-Section analysis module to show “Diameter” in “More” section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfed824ea95bac41e571274603e4200158f284d.png" data-download-href="/uploads/short-url/zXfQtY2tdgEkbN8BSxNnQQWOdcx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfed824ea95bac41e571274603e4200158f284d_2_690x421.png" alt="image" data-base62-sha1="zXfQtY2tdgEkbN8BSxNnQQWOdcx" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfed824ea95bac41e571274603e4200158f284d_2_690x421.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfed824ea95bac41e571274603e4200158f284d_2_1035x631.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfed824ea95bac41e571274603e4200158f284d_2_1380x842.png 2x" data-dominant-color="606479"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2244×1370 466 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @chir.set (2021-01-17 08:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>vtkvmtkPolyDataCenterlineSection just gives a value for each centerline section</p>
</blockquote>
</aside>
<p>My bad is now clarified.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>to show “Diameter” in “More” section.</p>
</blockquote>
</aside>
<p>I’ll update Cross-Section Analysis module and send a PR.</p>

---

## Post #9 by @chir.set (2021-01-17 10:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Most recent Slicer versions can now store and visualize scalar arrays associated with centerlines. I’ve now updated “Extract Centerline” module in SlicerVMTK to add radius array to the curve node</p>
</blockquote>
</aside>
<p>I could not update Cross Section Analysis module to show diameters along a centerline markups curve in the same way as we do for a centerline model.</p>
<ol>
<li>
<p>Radii are available at control points only, with arrayFromMarkupsControlPointData. They are not available at curve points, could not find a function like ‘arrayFromMarkupsCurvePointData’. Control points are fewer than curve points and reslicing is performed along curve points.</p>
</li>
<li>
<p>Available radii at control points are volatile. If the scene is saved and reloaded, arrayFromMarkupsControlPointData returns None.</p>
</li>
</ol>
<p>More advanced coding might be necessary, its usefulness remains to be seen.</p>

---

## Post #10 by @lassoan (2021-01-17 14:01 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Radii are available at control points only, with arrayFromMarkupsControlPointData. They are not available at curve points, could not find a function like ‘arrayFromMarkupsCurvePointData’. Control points are fewer than curve points and reslicing is performed along curve points.</p>
</blockquote>
</aside>
<p>Extract centerline module creates curves with <code>curveNode.SetNumberOfPointsPerInterpolatingSegment(1)</code>, which means there is no difference between curve points and control points (if we set a higher number of curve points then markups module can interpolate between the control points to determine values at each curve point, but I’m not sure if this is exposed - we should have a <code>slicer.util.arrayFromMarkupsCurvePointData</code> helper function).</p>
<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Available radii at control points are volatile. If the scene is saved and reloaded, arrayFromMarkupsControlPointData returns None.</p>
</blockquote>
</aside>
<p>This seems to be a bug in markups module.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> The issue seems to be that <code>InterpolateControlPointMeasurement</code> is disabled. We should be able to fix this (write its state into the json file) but I’m wondering if we need this at all. Could interpolation be always enabled?</p>

---

## Post #11 by @cpinter (2021-01-18 11:17 UTC)

<p>I think I didn’t enable it by default for performance reasons. We can try enabling it by default and see if it becomes a problem or not.</p>
<p>Otherwise I can add this option to the json storage as you suggest.</p>

---

## Post #12 by @lassoan (2021-01-18 15:01 UTC)

<p>Probably the best would be to remove this variable and always compute the array.</p>
<p>We can improve the performance later. Probably at some point we will need to implement a delayed update mechanism: whenever something is changed then hide measurements, scalar overlays, etc. and request a measurement update; when there are no update requests for X amount of time then perform the measurement update. If really lengthy computations emerge then we may even need to implement manual update mode.</p>

---

## Post #13 by @cpinter (2021-01-18 16:25 UTC)

<p>See PR here <a href="https://github.com/Slicer/Slicer/pull/5392" class="inline-onebox">ENH: Always interpolate control point measurements in markups by cpinter · Pull Request #5392 · Slicer/Slicer · GitHub</a></p>

---

## Post #14 by @joannecallow (2021-06-24 18:23 UTC)

<p>Hello,</p>
<p>I am trying to measure cross-sectional area of slices perpendicular to the centreline of a tendon that I segmented. When I go to the cross-section analysis module, all the sections are blank and I can’t see any details about the area or other measures. I will include a picture below. How can I fix this problem?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b04c2b2a0023c603a4478fd28740ea45c4bcf1d6.png" alt="Screen Shot 2021-06-24 at 11.16.37 AM" data-base62-sha1="p9BdY1waUfqZ8fvlxlu7lkhLcEu" width="525" height="479"></p>

---

## Post #15 by @chir.set (2021-06-24 18:41 UTC)

<aside class="quote no-group" data-username="joannecallow" data-post="14" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e36b37/48.png" class="avatar"> joannecallow:</div>
<blockquote>
<p>measure cross-sectional area of slices perpendicular to the centreline</p>
</blockquote>
</aside>
<p>While it’s certainly information of interest, Centerline metrics does not have any knowledge of this area. You may alternatively use ‘Curved planar reformat’ and ‘Segment cross-section area’ modules if surrounding anatomy is not important.</p>
<aside class="quote no-group" data-username="joannecallow" data-post="14" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e36b37/48.png" class="avatar"> joannecallow:</div>
<blockquote>
<p>all the sections are blank</p>
</blockquote>
</aside>
<p>Don’t have any clue for this one.</p>

---

## Post #16 by @lassoan (2021-06-24 18:47 UTC)

<aside class="quote no-group quote-modified" data-username="chir.set" data-post="15" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<aside class="quote no-group" data-username="joannecallow" data-post="14" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e36b37/48.png" class="avatar"> joannecallow:</div>
<blockquote>
<p>all the sections are blank</p>
</blockquote>
</aside>
<p>Don’t have any clue for this one.</p>
</blockquote>
</aside>
<p>This is just a problem on macOS with the Slicer Stable Release. You can either go to menu → Edit → Application settings → Appearance and set Style → “Light Slicer”; or switch to the Slicer Preview Release, where this problem has been already fixed.</p>

---

## Post #17 by @chir.set (2021-06-24 19:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>or switch to the Slicer Preview Release</p>
</blockquote>
</aside>
<p>It would fix the display issue. However, SlicerExtension-VMTK is available for VTK8, while Slicer Preview Release is built on top of VTK9. So module ‘Centerline metrics’ won’t be available to <a class="mention" href="/u/joannecallow">@joannecallow</a>. I hope some grant kicks in soon to help porting SlicerExtension-VMTK to VTK9.</p>

---

## Post #18 by @lassoan (2021-06-24 19:05 UTC)

<p>You can run VMTK in Slicer Stable Release and load the scene in to Slicer Preview Release. VMTK update for VTK9 is already funded, we just need for <a class="mention" href="/u/jcfr">@jcfr</a> to be freed up (expected to happen any day now).</p>

---

## Post #19 by @joannecallow (2021-06-24 19:16 UTC)

<p>Thanks so much. Using ‘Curved planar reformat’ and ‘Segment cross-section area’ modules seems to have worked.</p>

---

## Post #20 by @lassoan (2021-11-25 15:55 UTC)

<p>A post was merged into an existing topic: <a href="/t/tangent-plane-to-a-centerline/20778/2">tangent plane to a centerline</a></p>

---

## Post #21 by @Tom (2022-11-30 09:24 UTC)

<p>The VMTK ”Cross-section analysis’” can compute perpendicular cross-sectional areas along a centerline, but is it possible to extract the data for all voxels comprising a given cross-section (the numerical data)? I have a segmentation of a spiralling tube-like structure and need to compute some statistics on each cross-section along the tube. I can get the centerline control points with slicer.util.arrayFromModelPointData but I need all the data points of the corresponding cross-section, ideally of the original scalar volume that was used for the segmentation.<br>
Many thanks!</p>

---

## Post #22 by @chir.set (2022-11-30 18:52 UTC)

<aside class="quote no-group" data-username="Tom" data-post="21" data-topic="15556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/3d9bf3/48.png" class="avatar"> Tom:</div>
<blockquote>
<p>is it possible to extract the data for all voxels comprising a given cross-section</p>
</blockquote>
</aside>
<p>This code snippet should give you the HU values of the <em>contour</em> points of the cross-section. Is it what you expected ?</p>
<pre><code class="lang-auto">inputVolume = slicer.util.getNode("CTA-cardio")
inputVolumeArray = slicer.util.arrayFromVolume(inputVolume)
centerlineNode = slicer.util.getNode("vtkMRMLMarkupsCurveNode1")

import CrossSectionAnalysis
csaLogic = CrossSectionAnalysis.CrossSectionAnalysisLogic()
csaLogic.setInputCenterlineNode(centerlineNode)
csaLogic.setLumenSurface(segmentation, "Segment_F")
crossSectionContour = csaLogic.computeCrossSectionPolydata(100)
crossSectionPoints = crossSectionContour.GetPoints()

# From LineProfile.py (simplified)
rasToIJK = vtk.vtkMatrix4x4()
parentToIJK = vtk.vtkMatrix4x4()
rasToParent = vtk.vtkMatrix4x4()
inputVolume.GetRASToIJKMatrix(parentToIJK)
vtk.vtkMatrix4x4.Multiply4x4(parentToIJK, rasToParent, rasToIJK)

for i in range(crossSectionPoints.GetNumberOfPoints()):
    contourPoint = crossSectionPoints.GetPoint(i)
    point_RAS = (contourPoint[0], contourPoint[1], contourPoint[2], 1)
    point_IJK = [0,0,0,1]
    rasToIJK.MultiplyPoint(point_RAS, point_IJK)
    point_IJK_int = (int(point_IJK[0]), int(point_IJK[1]), int(point_IJK[2]))
    print(inputVolumeArray[point_IJK_int])
</code></pre>

---

## Post #23 by @lassoan (2022-11-30 20:48 UTC)

<p>The original voxel array is not aligned with your spiral. If you need a voxel array then I would recommend to straighten the volume using Curved Planar Reformat module in Sandbox extension.</p>

---
