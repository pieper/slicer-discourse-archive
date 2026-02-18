# "Model Maker" mesh generation algorithm

**Topic ID**: 9401
**Date**: 2019-12-05
**URL**: https://discourse.slicer.org/t/model-maker-mesh-generation-algorithm/9401

---

## Post #1 by @Gonzalo_Rojas_Costa (2019-12-05 14:18 UTC)

<p>Operating system: Any<br>
Slicer version: 4.10.2<br>
Expected behavior: The mesh generated using “Model Maker” option, has points or triangles? Which algorithm uses “Model Maker” option?<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2019-12-05 14:22 UTC)

<p>It uses a number of VTK filters. See complete implementation here: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/ModelMaker/ModelMaker.cxx">https://github.com/Slicer/Slicer/blob/master/Modules/CLI/ModelMaker/ModelMaker.cxx</a></p>

---

## Post #3 by @Gonzalo_Rojas_Costa (2019-12-05 15:55 UTC)

<p>The mesh generated with “Model Maker” has triangles or only points?</p>

---

## Post #4 by @lassoan (2019-12-05 18:26 UTC)

<p>Model maker generates a surface mesh consisting of points and triangle cells.</p>

---
