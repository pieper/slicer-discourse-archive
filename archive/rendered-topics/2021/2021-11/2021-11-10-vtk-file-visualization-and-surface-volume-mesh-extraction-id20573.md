---
topic_id: 20573
title: "Vtk File Visualization And Surface Volume Mesh Extraction"
date: 2021-11-10
url: https://discourse.slicer.org/t/20573
---

# VTK file visualization and surface/volume mesh extraction

**Topic ID**: 20573
**Date**: 2021-11-10
**URL**: https://discourse.slicer.org/t/vtk-file-visualization-and-surface-volume-mesh-extraction/20573

---

## Post #1 by @EMIL_fluidM (2021-11-10 21:37 UTC)

<p>I have a output vtk file from a program that i need to use to create a surface mesh. Some, issues i am having is loading the file in slicer shows strands of surface instead of a clean/connected surface. Changing the view to wireframe does shows lines connecting parts where there is no surface in the viewport. The missing surfaces does not appear when it is opened in paraview. As a result i am not sure if my geometry is clean or not. This is important since i need to create a mesh for my subsequent analysis.</p>
<p>This bring me to my second question. Can we create a mesh file (obj/stl) from vtk file in slicer.  I tried using the save module but the only option available to me are vtk and vtu. I visualized the vtk file through the “models” module</p>

---

## Post #2 by @lassoan (2021-11-11 02:47 UTC)

<aside class="quote no-group" data-username="EMIL_fluidM" data-post="1" data-topic="20573">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/emil_fluidm/48/13071_2.png" class="avatar"> EMIL_fluidM:</div>
<blockquote>
<p>issues i am having is loading the file in slicer shows strands of surface instead of a clean/connected surface</p>
</blockquote>
</aside>
<p>Most likely your mesh contains incorrectly oriented triangles. Older Slicer versions by default did not show backface of triangles. You can enable display of both sides in Models module / Display / 3D Display / Visible Sides → All. Current Slicer versions show both sides by default and contain many other fixes, so most likely they will show the full mesh by default.</p>
<aside class="quote no-group" data-username="EMIL_fluidM" data-post="1" data-topic="20573">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/emil_fluidm/48/13071_2.png" class="avatar"> EMIL_fluidM:</div>
<blockquote>
<p>Can we create a mesh file (obj/stl) from vtk file in slicer. I tried using the save module but the only option available to me are vtk and vtu. I visualized the vtk file through the “models” module</p>
</blockquote>
</aside>
<p>A .vtk file can contain an image, surface mesh, or volumetric mesh. If Slicer only offers to save a model in .vtk and .vtu (unstructured grid) format then it means that the model contains a volumetric mesh, which cannot be saved as a surface mesh (.stl, .obj, .ply, … formats).</p>
<p>You can convert your volumetric mesh to a surface mesh by copy-pasting this code snippet into the Python console (replace <code>Model</code> by the name of your model node):</p>
<aside class="quote" data-post="4" data-topic="10384">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/mesh-multiple-objects/10384/4">Mesh multiple objects</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can copy-paste this code to the Python console to extract the surface and put it into a new mode node. 
volMesh=getNode('Model').GetMesh()
extractSurface=vtk.vtkGeometryFilter()
extractSurface.SetInputData(volMesh)
extractSurface.Update()
slicer.modules.models.logic().AddModel(extractSurface.GetOutput())

You can extract a specific material by adding vtkThreshold filter before vtkGeometryFilter.
  </blockquote>
</aside>


---
