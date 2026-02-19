---
topic_id: 3385
title: "Transfrom To Vtk Data"
date: 2018-07-05
url: https://discourse.slicer.org/t/3385
---

# transfrom to VTK data

**Topic ID**: 3385
**Date**: 2018-07-05
**URL**: https://discourse.slicer.org/t/transfrom-to-vtk-data/3385

---

## Post #1 by @1102831521 (2018-07-05 13:17 UTC)

<p>Operating system: WIN7<br>
Slicer version: 4.8.1<br>
Expected behavior: vtkMRMLNode data transfrom to VTK data<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-07-05 13:28 UTC)

<p>Most MRML nodes store a VTK data object internally that you can retrieve with a get function (e.g., GetImageData, GetPolyData, GetTable).</p>

---
