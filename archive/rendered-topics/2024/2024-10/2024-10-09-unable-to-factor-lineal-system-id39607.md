---
topic_id: 39607
title: "Unable To Factor Lineal System"
date: 2024-10-09
url: https://discourse.slicer.org/t/39607
---

# Unable to factor lineal system

**Topic ID**: 39607
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/unable-to-factor-lineal-system/39607

---

## Post #1 by @Sofia_Gonzalez (2024-10-09 12:09 UTC)

<p>Hello everyone, I’m trying to compute the centerline of a carotid and it’s a .stil file.<br>
Someone knows why is saying that error?<br>
Is because of the mesh?</p>

---

## Post #2 by @lassoan (2024-10-10 04:40 UTC)

<p>Yes, it is because of the mesh has invalid (or at least unexpected) geometry.</p>
<p>For example, it may be that your mesh contain the vessel wall only (thin shell) instead of the blood pool (solid). Can you post a screenshot?</p>
<p>You can fix up the mesh by loading it as Segmentation and then editing it in Segment Editor module.</p>

---

## Post #3 by @Sofia_Gonzalez (2024-10-10 07:37 UTC)

<p>Yes that’s true!! I only have my .stl the surface of my carotid. But I also have the x,y,z of the mesh and u,v,w. And I have to merge it in a one file right? Do you know how to merge the coordinates of the mesh and velocity with the surface?</p>
<p>thanksss</p>

---

## Post #4 by @lassoan (2024-10-15 23:36 UTC)

<p>I don’t know what u, v, w stores - texture coordinates, velocity vector components, …? Anyway, you cannot store any of these in a standard STL file. You can store point and cell scalars in VTK mesh file formats and Slicer can read and visualize them.</p>

---
