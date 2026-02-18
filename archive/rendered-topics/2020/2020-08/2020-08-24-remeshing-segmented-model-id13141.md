# Remeshing segmented model

**Topic ID**: 13141
**Date**: 2020-08-24
**URL**: https://discourse.slicer.org/t/remeshing-segmented-model/13141

---

## Post #1 by @A_Bonifacio (2020-08-24 14:25 UTC)

<p>Is it possible to remesh the surface of the segmented model specifying the element edge size (maybe using surface toolbox)?<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-08-24 14:29 UTC)

<p>There are a number of tools available for this. We need to know a bit more to be able to give advice on which approaches could work for you.</p>
<p>What is your application (3D printing, mesh editing, FEM, …)?</p>
<p>What would you like to achieve by remeshing (have uniform/adaptive element size, increase or decrease the number of elements, …)?</p>

---

## Post #3 by @A_Bonifacio (2020-08-24 14:49 UTC)

<p>Yes actually I need it for FEA and a uniform mesh should work.<br>
Do you have any suggestions?<br>
Thank you.</p>

---

## Post #4 by @lassoan (2020-08-24 15:13 UTC)

<p>You can use <a href="https://github.com/lassoan/SlicerSegmentMesher">SegmentMesher extension</a> to generate a volumetric mesh directly from an image segmentation. I would recommend to use Cleaver2 backend, as it is much more reliable than tetgen and Cleaver2 has a free license (tetgen is commercial/GPL). You have several options for controlling mesh element size - it can be enforced to be strictly uniform size or adaptive (so that you can cut down on computation time and make simulation of large deformations more robust).</p>

---
