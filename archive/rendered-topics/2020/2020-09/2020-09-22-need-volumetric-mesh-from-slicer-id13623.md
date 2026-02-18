# Need volumetric mesh from Slicer

**Topic ID**: 13623
**Date**: 2020-09-22
**URL**: https://discourse.slicer.org/t/need-volumetric-mesh-from-slicer/13623

---

## Post #1 by @masud407 (2020-09-22 16:50 UTC)

<p>Hello,<br>
I have segmented a spine CT scan data using slicer. I need to import it in to the finite element software (ANSYS or Abaqus). I need to have meshing file for this. The file I get from segmentation using slicer is in STL format which is not eligible for meshing. I tried to follow this forum:</p><aside class="quote" data-post="1" data-topic="1416">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/e95f7d/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-a-surface-mesh-to-a-volumetric-mesh-in-3d-slicer/1416">Convert a surface mesh to a volumetric mesh in 3D Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello everyone, 
When I use 3D SLICER, I only have a surface mesh in here. But, I want to do this file in a Finite Element Sofware, I need a volumetric mesh. 
Can you tell me how to convert a surface mesh to a volumetric mesh in 3DSLICER? 
Thank you so much, 
Van Sy,
  </blockquote>
</aside>
<p>
I used Cleaver 2.4 to generate the volumetric mesh. However, after the mesh, I was not able to save the file other than nrrd or obj format. What should I need to do to save the volumetric mesh file in step/iges/stl format? Please help</p>

---

## Post #2 by @lassoan (2020-09-22 18:19 UTC)

<p>You can create volumetric mesh using SegmentMesher module and save it as .vtk or .vtu format. You can then use mesh converters, such as <a href="https://github.com/nschloe/meshio">meshio</a> to convert to other formats, such as .inp that Abaqus can import.</p>

---

## Post #3 by @masud407 (2020-09-23 16:20 UTC)

<p>Hello Mr. Andras,</p>
<p>Thanks for your suggestion. I got the inp format. Do you know what other formats can meshio convert?</p>

---

## Post #4 by @lassoan (2020-09-23 17:11 UTC)

<p>See list of supported formats in its documentation: <a href="https://github.com/nschloe/meshio">https://github.com/nschloe/meshio</a></p>

---

## Post #5 by @masud407 (2020-09-24 16:33 UTC)

<p>Hello Lasso,</p>
<p>I got the volumetric mesh using meshio. Do you know if I can edit the mesh file (refining the mesh) obtained from meshio using other software hypermesh? I tried to refine the mesh in abaqus. However, as I inserted a mesh file (obtained from meshio) to the abaqus, Abaqus doesn’t permit me to edit/refine the mesh anymore.</p>

---

## Post #6 by @lassoan (2020-09-24 18:27 UTC)

<p>I don’t know what third-party software are available to remesh existing meshes, but there should be a number of them.</p>
<p>You can also change meshing parameters in Slicer to adjust the mesh resolution. You can easily specify global parameters using command-line switches (that dynamically adjust mesh resolution based on the complexity of the mesh geometry). Cleaver also allows specifying a sizing field, which should allow specifying regions where you want to have higher or lower resolution than the default.</p>

---

## Post #7 by @Abdulrahman (2020-10-12 04:51 UTC)

<p>Hi,<br>
stl files work with 3-matics software</p>

---
