---
topic_id: 2859
title: "Spatial Registration Of Meshes"
date: 2018-05-21
url: https://discourse.slicer.org/t/2859
---

# Spatial registration of meshes

**Topic ID**: 2859
**Date**: 2018-05-21
**URL**: https://discourse.slicer.org/t/spatial-registration-of-meshes/2859

---

## Post #1 by @Bio_Medical (2018-05-21 12:14 UTC)

<p>Can we perform Digital image coorelation in 3D slicer?</p>

---

## Post #2 by @pieper (2018-05-21 12:35 UTC)

<p>Can you be more specific?</p>

---

## Post #3 by @Bio_Medical (2018-05-22 04:27 UTC)

<p>Does 3D slicer provides us an opportunity to co-register two 3D models?Thats how we perform Digital image co-orelation,first we coregister two models and then calculate strain deformation(build maps on that basis).So I dont think it enables us to perform simulation but maybe there is some kind of library/module which can makes us  atleast register two models.<br>
If anyone has some idea kindly let me know.</p>

---

## Post #4 by @lassoan (2018-05-22 04:40 UTC)

<p>There are several registration modules for model registration. See this post for details: <a href="https://discourse.slicer.org/t/align-two-segments-to-each-other/2570/4?u=lassoan">align two segments to each other </a></p>

---

## Post #5 by @Bio_Medical (2018-05-22 08:00 UTC)

<p>Thanks@ lassoan for your response.I have seen the thread that you have mentioned.<br>
But apparently this ‘Model registration’ is doing registeration of two models based on segmentation(which has been done in 3d slicer i guess).<br>
I want to register two meshes actually.is this module able to do that as well?</p>

---

## Post #6 by @lassoan (2018-05-22 11:35 UTC)

<p>You can import models into a segmentation by using Segmentations module Import/Export section.</p>

---

## Post #7 by @thewtex (2018-05-23 01:23 UTC)

<p>Slicer provides <a href="https://itk.org/Doxygen/html/classitk_1_1MaskedFFTNormalizedCorrelationImageFilter.html" rel="nofollow noopener">itk::MaskedFFTNormalizedCorrelationImageFilter</a> – digital image correlation can be used to estimate translation in this case.</p>
<p>For deformation, the SlicerITKUltrasound extension provides access to <a href="https://github.com/KitwareMedical/ITKUltrasound" rel="nofollow noopener">ITKUltrasound</a>, which can compute correlation-based strain.</p>
<p>There are also <a href="https://itk.org/Doxygen/html/classitk_1_1ANTSNeighborhoodCorrelationImageToImageMetricv4.html" rel="nofollow noopener">correlation-based metrics</a> in the ITK registration framework.</p>

---

## Post #8 by @Bio_Medical (2018-05-24 04:11 UTC)

<p>How can i import my mesh.inp into slicer?<br>
I have tried to import it by Segmentations module&gt; Import but it  is not working(no dialogue box open after clicking on import).Is there any other way of doing it?<br>
I have to register two volumes(meshes) basically.<br>
I am using slicer 4.8.1.<br>
Operating System:Window 7<br>
Graphic card:intel r hd graphics (core i3)</p>

---

## Post #9 by @lassoan (2018-05-24 04:45 UTC)

<p>Loading of inp file format is not supported in Slicer. Either save the mesh in stl, ply, obj, vtp, vtk, or vtu file format instead of inp, or find a converter that can convert an inp file to one of the supported file formats.</p>

---
