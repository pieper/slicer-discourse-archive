# Intersection between markups closed curve node on the plane and a line

**Topic ID**: 11281
**Date**: 2020-04-24
**URL**: https://discourse.slicer.org/t/intersection-between-markups-closed-curve-node-on-the-plane-and-a-line/11281

---

## Post #1 by @Mik (2020-04-24 06:53 UTC)

<p>Dear all,</p>
<p>There is a vtkMRMLMarkupsCurveNode on a plane and a line on the same plane (e.g. x=10.0 mm). I want to find a intersection point (or points) between the curve and the line.</p>
<p>It could be done manually (crude and inefficient). May be there is a solution in Slicer or VTK of such problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e063674ab68a82d36a4d6e87f9a69fbc5efbb503.jpeg" data-download-href="/uploads/short-url/w11Vjfr3CFinbFODYdfJAhswM8P.jpeg?dl=1" title="ClosedCureveNode_Plane_Modified" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e063674ab68a82d36a4d6e87f9a69fbc5efbb503_2_690x455.jpeg" alt="ClosedCureveNode_Plane_Modified" data-base62-sha1="w11Vjfr3CFinbFODYdfJAhswM8P" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e063674ab68a82d36a4d6e87f9a69fbc5efbb503_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e063674ab68a82d36a4d6e87f9a69fbc5efbb503_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e063674ab68a82d36a4d6e87f9a69fbc5efbb503_2_1380x910.jpeg 2x" data-dominant-color="45342C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ClosedCureveNode_Plane_Modified</span><span class="informations">1396×922 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @timeanddoctor (2020-04-24 10:38 UTC)

<p>Did you created the plane through this line(green)? If yes you can convert it to an array and get this points.</p>

---

## Post #3 by @timeanddoctor (2020-04-24 10:50 UTC)

<p>Maybe the simple way is creating two fidusions based the two intersection points in the 3d view</p>

---

## Post #4 by @Mik (2020-04-24 11:09 UTC)

<p>The green line is just an example. Initial data is a curve node (isocenter is an origin) and a line equation.</p>
<p>I will try to use <a href="https://vtk.org/doc/nightly/html/classvtkIntersectionPolyDataFilter.html" rel="nofollow noopener">vtkIntersectionPolyDataFilter</a>.</p>
<ol>
<li>Convert curve to polygon.</li>
<li>Convert line to vtkPlane.</li>
<li>Get first output from IntersectionPolyDataFilter and check for intersection points.</li>
</ol>

---

## Post #5 by @lassoan (2020-04-24 13:12 UTC)

<p>VTK locators can compute all intersection points of a polydata with a line extremely fast, for example <a href="https://vtk.org/doc/nightly/html/classvtkCellLocator.html#a027818794762a37868a3dccc53ad6e81">vtkCellLocator::IntersectWithLine</a>. You can get the curve as polydata by calling <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#af52fa681f15f117c5e003d63a88c2e9a">GetCurveWorld</a> method of the curve node.</p>

---
