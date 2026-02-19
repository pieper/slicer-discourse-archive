---
topic_id: 1996
title: "Exporting A Segment Creates A Hollow 3D Model"
date: 2018-01-31
url: https://discourse.slicer.org/t/1996
---

# Exporting a segment creates a hollow 3D model

**Topic ID**: 1996
**Date**: 2018-01-31
**URL**: https://discourse.slicer.org/t/exporting-a-segment-creates-a-hollow-3d-model/1996

---

## Post #1 by @Researcher_2017 (2018-01-31 22:05 UTC)

<p>Hello,</p>
<p>I am working with the nightly version of 3D Slicer (version 4.9.0). I used the Segment Editor module to create a 3D model of a helmet (shown below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf39429e7e3936a1031f157dcdb588ef48d27453.jpeg" data-download-href="/uploads/short-url/rhDSkD64G0wAPZb8FEhRkV95DsD.jpg?dl=1" title="image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39429e7e3936a1031f157dcdb588ef48d27453_2_690x416.jpg" alt="image1" data-base62-sha1="rhDSkD64G0wAPZb8FEhRkV95DsD" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39429e7e3936a1031f157dcdb588ef48d27453_2_690x416.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39429e7e3936a1031f157dcdb588ef48d27453_2_1035x624.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf39429e7e3936a1031f157dcdb588ef48d27453_2_1380x832.jpg 2x" data-dominant-color="6B6E76"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image1</span><span class="informations">1924×1160 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when I export the segmentation as a model and save it as a PolyData (.VTK) file, the 3D model is hollow and only shows the outer surface of the segmentation. (shown below)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/0676ab1b3010d7b132cba62d543d06f1f7db9b1a.jpeg" data-download-href="/uploads/short-url/Vb6RnQMXpyTXbCsFKAEzrwe6NQ.jpg?dl=1" title="image2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0676ab1b3010d7b132cba62d543d06f1f7db9b1a_2_690x416.jpg" alt="image2" data-base62-sha1="Vb6RnQMXpyTXbCsFKAEzrwe6NQ" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0676ab1b3010d7b132cba62d543d06f1f7db9b1a_2_690x416.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0676ab1b3010d7b132cba62d543d06f1f7db9b1a_2_1035x624.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0676ab1b3010d7b132cba62d543d06f1f7db9b1a_2_1380x832.jpg 2x" data-dominant-color="696A71"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image2</span><span class="informations">1924×1160 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a way that I can produce a model that is completely filled in?</p>

---

## Post #2 by @lassoan (2018-01-31 22:56 UTC)

<p>VTK polydata is a polygonal surface mesh: the volume is defined by the enclosing surface. There is no need for elements inside.</p>
<p>What would you like to do with your model? Use it for finite-element analysis? In that case you can use Segment Mesher extension, which creates volumetric mesh (tetrahedral mesh, stored in a VTK unstructured grid) directly from segmentation.</p>

---

## Post #3 by @Researcher_2017 (2018-02-01 00:31 UTC)

<p>Thank you, I’ll try using the Segment Mesher extension. Ultimately, the goal is to print out the complete model on a 3D printer.</p>

---

## Post #4 by @lassoan (2018-02-01 01:07 UTC)

<p>For 3D printing you can only use a hollow model (surface mesh). The printer software will automatically design the fill-in pattern. See tutorial for creating 3D-printable models using Segment Editor: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---
