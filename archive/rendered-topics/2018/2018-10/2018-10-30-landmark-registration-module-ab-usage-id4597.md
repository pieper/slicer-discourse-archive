# Landmark registration module (ab)usage

**Topic ID**: 4597
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/landmark-registration-module-ab-usage/4597

---

## Post #1 by @zivy (2018-10-30 21:09 UTC)

<p>I would like to (ab)use the landmark registration module. I have two volumes and corresponding point pairs in each. I want to load the data and then use the landmark registration’s “Refine landmark” functionality. Is there an easy hack that will allow me to do so? Specific point file formats etc. ?</p>
<p>thanks<br>
Ziv</p>

---

## Post #2 by @lassoan (2018-10-30 21:15 UTC)

<p>I’m not sure how Refine landmark feature works, but you can register two volumes using thin-plate spline registration from two sets of landmarks using SlicerIGT extension’s Fiducial Registration Wizard module.</p>
<p>Fiducial points are stored in a csv file (using fcsv extension) in the following format:</p>
<pre><code># Markups fiducial file version = 4.10
# CoordinateSystem = 0
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
vtkMRMLMarkupsFiducialNode_0,-2.145,-49.845,-28.500,0.000,0.000,0.000,1.000,1,1,0,F-1,,
vtkMRMLMarkupsFiducialNode_1,-2.145,13.718,-52.409,0.000,0.000,0.000,1.000,1,1,0,F-2,,
vtkMRMLMarkupsFiducialNode_2,-2.145,29.463,15.236,0.000,0.000,0.000,1.000,1,1,0,F-3,,
</code></pre>
<p>id can be any string unique within the file.</p>

---

## Post #3 by @zivy (2018-10-30 21:59 UTC)

<p>Thanks for the quick reply, unfortunately this is not what I want to do.</p>
<p>Only loading points with the fcsv format doesn’t work when I need to load two sets of points (they are appended and the pairing is lost). When creating point pairs using the landmark registration module, it is able to separate the two point sets and “knows” about their correspondences.</p>
<p>I have the corresponding points in fixed and moving images but the localization of the points in the moving image is a bit off. What the “refine” option does is register a ROI from the fixed image centered on a point to an ROI centered on the corresponding point (just larger ROI). This results in improved correspondence.</p>
<p>Mostly I am interested in the Slicer GUI, so that I can quickly go over the corresponding point pairs and visually validate that they make sense (sometimes they are off, and with Slicer I can manually correct this and quickly run the ROI registration).</p>
<p>Hopefully this clarified things a bit.</p>

---

## Post #4 by @lassoan (2018-10-31 03:24 UTC)

<p>You could find the point pairs manually by going through the points using Markups module, with “Click to jump slices” enabled to find matching pairs. Then split the markup node into two markup nodes and reorder points (you can copy-paste markup points between lists).</p>
<p>Landmark registration module should find and use the two lists automatically if</p>
<ul>
<li>each list node name is corresponding volume node’s name with <em>-landmarks</em> appended; and</li>
<li>corresponding points have the same name in the two lists</li>
</ul>
<p>If for some reason the markup nodes or points not found or used then you can add points at random positions, save the scene, update point positions in the two .fcsv files, and load the scene.</p>

---

## Post #5 by @zivy (2018-10-31 18:41 UTC)

<p>Thanks. My workaround was to load the two volumes, add a dummy marker using the landmarks registration module and then save the mrml scene. I then overwrote the two fcsv files and loaded the scene back into slicer.</p>
<p>Also, this exposed a bug in the SimpleITK refinement, which should be fixed by <a href="https://github.com/pieper/LandmarkRegistration/pull/24" rel="nofollow noopener">this pull request</a>, so I believe I have paid my dues <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=6" title=":wink:" class="emoji" alt=":wink:"> .</p>

---
