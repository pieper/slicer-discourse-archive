---
topic_id: 4262
title: "3D Meshing Using Data Points"
date: 2018-10-02
url: https://discourse.slicer.org/t/4262
---

# 3d meshing using data points

**Topic ID**: 4262
**Date**: 2018-10-02
**URL**: https://discourse.slicer.org/t/3d-meshing-using-data-points/4262

---

## Post #1 by @Stuti_Verma (2018-10-02 19:31 UTC)

<p>I am new to the 3d slicer. I wanted to know whether I can generate the mesh from data points. Actually, I have the data points of a geometry in three-dimensional space and I want to construct the geometry using those points, followed by meshing with brick-type elements. The geometry will be used to model anisotropic material. Is it possible to generate mesh using the 3d slicer? If not, then what can be the other methods?</p>

---

## Post #2 by @lassoan (2018-10-03 01:20 UTC)

<p>Yes, you can probably do all these using VTK library, which is bundled with Slicer. For example, you can create a volumetric mesh from a set of points using <a href="https://www.vtk.org/Wiki/VTK/Examples/Cxx/Modelling/Delaunay3D">Delaunay triangulation</a>, convert the elements to a structured grid by <a href="https://www.vtk.org/doc/nightly/html/classvtkProbeFilter.html">probe filter</a>, etc.</p>

---

## Post #3 by @Stuti_Verma (2018-10-08 20:09 UTC)

<p>Thanks for reaching out. I had one more doubt. By converting the elements into structured grid, do you mean conversion of tetrahedral elements into hexahedral elements?</p>

---

## Post #4 by @lassoan (2018-10-08 20:43 UTC)

<p>I meant that using probe filter, you can fill voxels of a 3D volume with values sampled from the unstructured grid.</p>

---
