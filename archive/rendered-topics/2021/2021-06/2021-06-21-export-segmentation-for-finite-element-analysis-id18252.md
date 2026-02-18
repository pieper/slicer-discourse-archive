# Export segmentation for finite element analysis

**Topic ID**: 18252
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/export-segmentation-for-finite-element-analysis/18252

---

## Post #1 by @L12 (2021-06-21 14:51 UTC)

<p>Hi, I converted my segmentation to an STL file and when I open it in a 3D viewer, the images overlap and just shows one segment. How do I save the exact same thing that appeared on my 3D slicer window? I have attached both images here.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76a87370fa4fc9944658c2a5d8e864fc1ca75490.jpeg" data-download-href="/uploads/short-url/gVHffB3s97p1OFmdGC9roWp2LS0.jpeg?dl=1" title="3dviewer.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76a87370fa4fc9944658c2a5d8e864fc1ca75490_2_690x371.jpeg" alt="3dviewer.PNG" data-base62-sha1="gVHffB3s97p1OFmdGC9roWp2LS0" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76a87370fa4fc9944658c2a5d8e864fc1ca75490_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76a87370fa4fc9944658c2a5d8e864fc1ca75490_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76a87370fa4fc9944658c2a5d8e864fc1ca75490.jpeg 2x" data-dominant-color="BDBEC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dviewer.PNG</span><span class="informations">1335×719 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f48bd5834dcc29c19ec87fd3c83e035fb25d5785.png" data-download-href="/uploads/short-url/yTm5WmlMGnUex8Ca9n5Sh0l5fEN.png?dl=1" title="slicer_image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f48bd5834dcc29c19ec87fd3c83e035fb25d5785_2_690x368.png" alt="slicer_image" data-base62-sha1="yTm5WmlMGnUex8Ca9n5Sh0l5fEN" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f48bd5834dcc29c19ec87fd3c83e035fb25d5785_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f48bd5834dcc29c19ec87fd3c83e035fb25d5785_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f48bd5834dcc29c19ec87fd3c83e035fb25d5785.png 2x" data-dominant-color="ABA8B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_image</span><span class="informations">1366×730 90.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-06-21 14:57 UTC)

<p>STL file format cannot store multiple segments in a single file. If you want to have a single file that has the segments with different colors then you can export to OBJ file format, or you can use SlicerOpenAnatomy extension to export to glTF format.</p>
<p>What is your end goal? 3D printing, virtual/augmented reality visualization, quantitative analysis, …? What software do you plan to import the exported segmentation into?</p>

---

## Post #3 by @L12 (2021-06-21 14:59 UTC)

<p>End goal is to make a VR model and I would like to open it on a CAD software first, either Solidworks or Catia.</p>

---

## Post #4 by @lassoan (2021-06-21 15:07 UTC)

<p>You can open OBJ and glTF files in most VR viewers. You can also view and interact with segmentations, 3D volumes, models, etc. in 3D Slicer in virtual reality (just install SlicerVirtualReality extension and click Show in virtual reality button on the toolbar). You can combine CAD models with segmentations in Slicer using Segment Editor, Dynamic modeler, and Combine models module.</p>
<p>What would you like to simulate surgical interventions? What procedure (pedicle screw placement, cardiac valve replacement, …)?</p>

---

## Post #5 by @L12 (2021-06-21 15:14 UTC)

<p>Okay, thank you. I will try that.</p>
<p>I am just trying to simulate the mechanics of a cell.</p>

---

## Post #6 by @lassoan (2021-06-21 15:16 UTC)

<p>Do you plan to interact with the cell - e.g., apply external force using the VR controllers and use finite-element modeling to simulate physically realistic deformations?</p>

---

## Post #7 by @L12 (2021-06-21 15:20 UTC)

<p>Yes, we plan to do that!</p>

---

## Post #8 by @lassoan (2021-06-21 15:38 UTC)

<p>I think the closest to real-time FEM simulation in Slicer is what <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> has developed with <a href="https://github.com/Kitware/SMTK">smtk</a>.</p>

---

## Post #9 by @L12 (2021-06-21 15:41 UTC)

<p>I will look into that too. Thank you very much, this was helpful!</p>

---

## Post #10 by @lassoan (2021-06-21 15:47 UTC)

<p>You can also generate volumetric meshes for finite element analysis (using Segment Mesher extension). You can use these mesh files directly in <a href="https://febio.org/downloads/">FEBio Studio</a>, and you can convert the mesh by using meshio into other formats so that you can load it into other modeling software.</p>

---
