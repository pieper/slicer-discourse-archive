# Converting mesh data to volumetric data

**Topic ID**: 24279
**Date**: 2022-07-11
**URL**: https://discourse.slicer.org/t/converting-mesh-data-to-volumetric-data/24279

---

## Post #1 by @Andrey_Titov (2022-07-11 19:32 UTC)

<p>Hello everyone,</p>
<p>I was wondering if it is possible to use 3D Slicer to convert a triangular mesh (for example, one that has an .obj format) to a volumetric representation, and then save it to a medical volume format (for example, MINC)?</p>
<p>In other words, I want to create a voxel representation of the data from an isosurface representation, but I am not sure how to do it exactly.</p>
<p>Thank you for your help!</p>

---

## Post #2 by @muratmaga (2022-07-12 18:33 UTC)

<p>That’s very easy.</p>
<ol>
<li>Drag and drop your obj to the Slicer application window, and choose segmentation (instead of the default model).</li>
<li>After the OBJ is loaded into the scene, right click on the segmentation object and choose “Export Visible Segments as Binary Labelmaps”</li>
</ol>
<p>Obviously it wouldn’t have any intensity information, but this should give you a volumetric data.</p>

---

## Post #3 by @Andrey_Titov (2022-07-12 21:55 UTC)

<p>Ok, thank you very much! This is exactly what I need, I didn’t realize I could use segmentations for that!</p>

---
