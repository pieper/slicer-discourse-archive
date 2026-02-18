# Spharm.vtk vs procalign in group comparison

**Topic ID**: 2774
**Date**: 2018-05-08
**URL**: https://discourse.slicer.org/t/spharm-vtk-vs-procalign-in-group-comparison/2774

---

## Post #1 by @Olof (2018-05-08 08:58 UTC)

<p>Hi Beatriz and Martin,<br>
short question: What is the difference of using the SPHARM.vtk file and the procalign file in a group comparison … will their be big difference?  Was wondering as we check the registration looking at the color code on each SPHARM.vtk</p>

---

## Post #2 by @styner (2018-05-08 13:15 UTC)

<p>Hi Olof<br>
the *SPHARM.vtk surfaces are in the original image space and thus not aligned. The procalign surfaces have been aligned using a rigid-body Procrustes alignment.</p>
<p>If you analyze the surface coordinates, then alignment is needed and thus you should use the procalign surfaces. If you are analyzing properties like thickness, then alignment is not needed and you can use either one</p>
<p>Martin</p>

---
