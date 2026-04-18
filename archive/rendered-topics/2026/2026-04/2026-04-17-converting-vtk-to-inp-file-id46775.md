---
topic_id: 46775
title: "Converting Vtk To Inp File"
date: 2026-04-17
url: https://discourse.slicer.org/t/46775
---

# Converting .vtk to .inp file

**Topic ID**: 46775
**Date**: 2026-04-17
**URL**: https://discourse.slicer.org/t/converting-vtk-to-inp-file/46775

---

## Post #1 by @Tom_F-T (2026-04-17 23:22 UTC)

<p>I am trying to make a 3D model of trabecular bone for FEA in Abaqus. I am using slicer to convert the DICOM files of the bone into a 3D model, but when i first did this the .stl file i exported from slicer was only a surface mesh and as such I couldnt assign a section to it in order to apply the material to it, and it said i needed a volumetric mesh. from research, and AI, I found that downloading my model from slicer as a .vtk file was the best idea. The issue is that Abaqus cannot open .vtk files and again from research it seems the best conversion would be to a .inp file. From these forums Ive seen that people have used the meshio package in order to do this but for some reason I am running into a wall with the conversion, presumably from what i’m writing in the python console. The most common issue I get is that it doesn’t recognise my vtk file as a vtk.<br>
Any help with this would be great, I’m pretty new at this so sorry if I am making any stupid mistakes. Thanks</p>

---

## Post #2 by @lassoan (2026-04-18 00:26 UTC)

<aside class="quote no-group" data-username="Tom_F-T" data-post="1" data-topic="46775">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tom_f-t/48/81964_2.png" class="avatar"> Tom_F-T:</div>
<blockquote>
<p>.stl file i exported from slicer was only a surface mesh</p>
</blockquote>
</aside>
<p>STL file can only store a surface mesh. For finite-element analysis you probably want to create a volumetric mesh.</p>
<p>You can use the <code>SegmentMesher</code> extension in 3D Slicer to create a volumetric mesh from a segmentation. Alternatively, you can export a surface mesh from Slicer and use fTetWild, TetGen, NetGen - or any of the hundreds of mesh generators - to create the volumetric mesh. Each mesher has different capabilities and limitations, so it is not trivial to find one that fulfills all your needs, but there are many options.</p>

---
