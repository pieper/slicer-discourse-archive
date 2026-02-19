---
topic_id: 19602
title: "Add Cfd Simulation Model In Next Vmtk Version"
date: 2021-09-10
url: https://discourse.slicer.org/t/19602
---

# Add CFD simulation Model in next VMTK Version?

**Topic ID**: 19602
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/add-cfd-simulation-model-in-next-vmtk-version/19602

---

## Post #1 by @junqiangchen (2021-09-10 07:01 UTC)

<p>hi,i find SimVascular CFD simulation tool from here <a href="https://simvascular.github.io/,the" rel="noopener nofollow ugc">https://simvascular.github.io/,the</a> solver is svSolver,is there planning to add CFD model in next VMTK Version?<br>
thank you</p>

---

## Post #2 by @lassoan (2021-09-13 13:55 UTC)

<p>VMTK can generate meshes that are suitable for creating meshes and boundary conditions for CFD or FSI analysis, but no simulation engine will be implemented inside the VMTK library.</p>
<p>It would be fairly straightforward to implement a frontend for segmenting vessels, setting and running simulations and displaying results in 3D Slicer with the help of SlicerVMTK extension, but I’m not aware of anyone planning to work on this.</p>

---

## Post #3 by @junqiangchen (2021-09-14 02:53 UTC)

<p>hi,lassoan,i use vmtk generate the surface and using SimVascular CFD simulation Model to get the CFD result,so i wonder whether or not there would add CFD simulation Model in VMTK,if so,that would be great.<br>
thank you</p>

---
