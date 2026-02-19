---
topic_id: 13514
title: "How To Create 3D Format For Fea Analysis"
date: 2020-09-16
url: https://discourse.slicer.org/t/13514
---

# How to create 3D format for FEA analysis

**Topic ID**: 13514
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/how-to-create-3d-format-for-fea-analysis/13514

---

## Post #1 by @masud407 (2020-09-16 23:58 UTC)

<p>Hello,</p>
<p>I segmented a CT data using slicer and saved the file as STP format. I would like to mesh it using HyperMesh which was unable to take that STL data. I tried to convert the STL format into STEP/IGES/SLD format using solidworks. However, it does not work too. In addition, I can’t use the STL file for Abaqus meshing too. What should I do?</p>

---

## Post #2 by @lassoan (2021-08-03 16:26 UTC)

<p>If your FEA software cannot take surface meshes then you can generate volumetric meshes (tetrahedral and wedge elements) using Segment Statistics module. Slicer can save the volumetric mesh in .vtk or .vtu format but you can convert them to other formats using <a href="https://pypi.org/project/meshio/">meshio</a>.</p>

---
