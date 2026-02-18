# Obtaining the curve of intersection between two polydata

**Topic ID**: 14785
**Date**: 2020-11-26
**URL**: https://discourse.slicer.org/t/obtaining-the-curve-of-intersection-between-two-polydata/14785

---

## Post #1 by @Anish_Basnet (2020-11-26 15:27 UTC)

<p>Hello everyone,<br>
Is there a function in VTK that could determine the curve of intersection between two polydatas?</p>
<p>I’d also like to obtain the points that lie in the curve(indicated by the red color in the figure below). Is it somehow possible?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da4f2c671c81b60f1671cb8ad56a8144dbc5819c.png" data-download-href="/uploads/short-url/v9fIrIDWoriKyY1Z739iY6F18vO.png?dl=1" title="1024px-Is-spherecyl5-s.svg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da4f2c671c81b60f1671cb8ad56a8144dbc5819c_2_615x500.png" alt="1024px-Is-spherecyl5-s.svg" data-base62-sha1="v9fIrIDWoriKyY1Z739iY6F18vO" width="615" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da4f2c671c81b60f1671cb8ad56a8144dbc5819c_2_615x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da4f2c671c81b60f1671cb8ad56a8144dbc5819c_2_922x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da4f2c671c81b60f1671cb8ad56a8144dbc5819c.png 2x" data-dominant-color="2D4272"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1024px-Is-spherecyl5-s.svg</span><span class="informations">1024×832 80.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-11-26 19:32 UTC)

<p>Slicer is based on <a href="http://www.vtk.org/">VTK</a> and all VTK features are available for Slicer modules and in the Python console. VTK compute intersection of surfaces, for example using <a href="https://vtk.org/doc/nightly/html/classvtkCutter.html">vtkCutter</a>. The cutting surface must be represented as an implicit surface, which a sphere or cylinder already is. If you want to cut with a surface defined by a surface mesh then you can probably convert it to an implicit function - check out the <a href="https://www.kitware.com/products/books/VTKTextbook.pdf">VTK textbook</a> and <a href="https://lorensen.github.io/VTKExamples/site/">VTK examples</a>, and if you cannot figure it out then ask on the <a href="https://discourse.vtk.org/">VTK forum</a>.</p>

---
