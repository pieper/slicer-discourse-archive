# How to find area hit by cylindrical beam

**Topic ID**: 14566
**Date**: 2020-11-12
**URL**: https://discourse.slicer.org/t/how-to-find-area-hit-by-cylindrical-beam/14566

---

## Post #1 by @muntahi398 (2020-11-12 14:00 UTC)

<p>Hello good people,<br>
I have a structure obtained from CT. For Ramen scattering application total area hit by laser light is important as it is affecting the signal enhancement factor. In the picture red cylindrical shape defines the laser light. So, in different orientation, how much area of the 3D structure is hit by laser light needs to be calculated.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8302a43374d39635606e7bac55a5dec4e86da309.jpeg" data-download-href="/uploads/short-url/iGYcSShddPicbwAHPpcvbLSzVz3.jpeg?dl=1" title="SceneView2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8302a43374d39635606e7bac55a5dec4e86da309_2_435x500.jpeg" alt="SceneView2" data-base62-sha1="iGYcSShddPicbwAHPpcvbLSzVz3" width="435" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8302a43374d39635606e7bac55a5dec4e86da309_2_435x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8302a43374d39635606e7bac55a5dec4e86da309_2_652x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8302a43374d39635606e7bac55a5dec4e86da309.jpeg 2x" data-dominant-color="454141"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView2</span><span class="informations">743×853 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The material is opaque for laser, therefore ,only initial surface measurement  is needed. What would be the easier way to measure using structure and laser(segment  editor-&gt;draw cylinder) as 2 separate segment? It would be nice if it could be accomplished by a python script because measurement on many different points and shapes might be needed.</p>
<p>I attach sample image of interest. Thank you if someone could help me.</p>

---

## Post #2 by @lassoan (2020-11-13 15:03 UTC)

<p>In general, I would recommend Segment Editor module to compute intersection of two 3D objects. However, since in this case one of the objects (the laser beam) can be modeled very easily by an implicit function, you should be able to reliably cut the complex surface mesh with it. There are a couple of cut filters in VTK but probably <a href="https://vtk.org/doc/nightly/html/classvtkClipPolyData.html">vtkClipPolyData</a> will work well. If the cylinder is not infinitely long then you can clip the mesh with both a plane and a cylinder.</p>
<p>There are many examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> that shows how to get vtkPolyData from model nodes, process data using VTK, and set result in model nodes.</p>

---
