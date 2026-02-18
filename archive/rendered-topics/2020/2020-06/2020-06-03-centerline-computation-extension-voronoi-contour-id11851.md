# Centerline Computation Extension - Voronoi Contour

**Topic ID**: 11851
**Date**: 2020-06-03
**URL**: https://discourse.slicer.org/t/centerline-computation-extension-voronoi-contour/11851

---

## Post #1 by @Madelene_Habib (2020-06-03 17:20 UTC)

<p>Operating system: 64 bit<br>
Slicer version: 3D Slicer 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am currently using the “Centerline Computation” extension to:<br>
-Import an STL (airway segment)<br>
-Create a point-cloud from the volume enclosed by STL<br>
-Select a starting and endpoint (mouth, epiglottis)<br>
-Find the path between the start and endpoints<br>
-Export quantitative data of said path</p>
<p>I have been successful in doing the above, however I wanted to ask what the Voronoi Model includes and if there is a way to acquire quantitative/qualitative data from the Centerline Computation extension of the Voronoi</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-06-03 17:22 UTC)

<p>You can find the list of all point and cell scalar in a model (vtkPolyData) in Models module’s Scalars section. I think the only useful information in there is the radius.</p>

---
