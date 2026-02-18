# Contour target area for MLC leaf positioning calculation

**Topic ID**: 10101
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/contour-target-area-for-mlc-leaf-positioning-calculation/10101

---

## Post #1 by @Mik (2020-02-04 11:43 UTC)

<p>Operating system: linux<br>
Slicer version: Preview</p>
<p>There are 2 points which define a normal vector 0N (yellow) of the plane (green) for DICOM CT and RTSTRUCT contour data. I can calculate a perpendicular projection of each point of target contour (red) into the plane.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23923b3995e99674dcddbbec08558df3e9e07616.png" alt="image" data-base62-sha1="54G0F3YQWkoEYS02vpY3PdUtxCC" width="396" height="319"></p>
<p>Another task is to get only external points of projected data for perimeter and area calculation (picture below). The projection plane basically an isocenter plane.</p>
<p>Is there ready made vtk filter or algorithm for that purpose?</p>
<p>For example:</p>
<ol>
<li>Input - list of points coordinates on the plane (x1, y1) (x2, y2) … (xn, yn)</li>
<li>Output - vtkPolyData closed planar polygon of the perimeter, or something like that</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17dca5d33f7598ac98e9014febf0e3e9e6b5bf8b.png" alt="image" data-base62-sha1="3p5ItTtlu9fpqpNpZjk7LxbsjhN" width="538" height="306"></p>

---

## Post #2 by @Mik (2020-02-19 08:56 UTC)

<p>After some digging through the VTK examples site, i have found a <a href="https://lorensen.github.io/VTKExamples/site/Cxx/PolyData/PointsProjectedHull/" rel="nofollow noopener">solution</a> for that issue. vtkPointsProjectedHull allows to calculate convex hull of the points.</p>

---
