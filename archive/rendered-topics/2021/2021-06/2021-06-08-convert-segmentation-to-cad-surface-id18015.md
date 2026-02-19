---
topic_id: 18015
title: "Convert Segmentation To Cad Surface"
date: 2021-06-08
url: https://discourse.slicer.org/t/18015
---

# Convert segmentation to CAD surface

**Topic ID**: 18015
**Date**: 2021-06-08
**URL**: https://discourse.slicer.org/t/convert-segmentation-to-cad-surface/18015

---

## Post #1 by @Aep93 (2021-06-08 15:49 UTC)

<p>Hello all,<br>
With current developments of the slice, are there any possibilities to convert a model/segmentation to a CAD file?</p>

---

## Post #2 by @lassoan (2021-06-08 16:16 UTC)

<p>Yes, you can already save a segmentation as a surface or volumetric mesh that CAD software can read. Most CAD software are not prepared to work with hundreds of thousands of cells (some of them can reverse engineer meshes up to a certain size, or can display the mesh, but cannot edit it, so you need to reverse engineer it manually, etc.).</p>
<p>What is your end goal? What CAD software do you plan to use and what operations you want to do on the meshes (3D printing patient specific models, finite-element analysis, …)?</p>

---

## Post #3 by @Aep93 (2021-06-08 17:00 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. In fact, I want to bring the segmentations to CAD software and mesh them there so that I can use them in my finite-element analysis. I know slicer has its own segmentmesher toolbox, however, it is significantly easier to mesh the CAD files (such as .iges format) in a CAD software.<br>
Do you have any ideas in this regard?</p>

---

## Post #4 by @lassoan (2021-06-08 18:15 UTC)

<p>Indeed it would greatly simplify finite-element analysis if anatomical shapes were described with parametric surfaces that are commonly used in CAD software. However, creating these geometric shapes (e.g., trimmed NURBS surfaces) from polygonal meshes is a very hard reverse engineering process - much harder than creating the finite-element meshes directly from the polygonal meshes. This topic has been discussed in the forum extensively a number of times, so you may find some more details if you search the forum.</p>
<p>What works quite well for us for biomedical simulation problems is to create a volumetric mesh from segmentation and do the simulation in FEBio Studio. It can load surface and volumetric meshes directly from Slicer, using VTK mesh file formats, and its solver is simple and robust enough for biomedical problems.</p>

---

## Post #5 by @Aep93 (2021-06-08 18:28 UTC)

<p>Thank you so much for your explanation <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
