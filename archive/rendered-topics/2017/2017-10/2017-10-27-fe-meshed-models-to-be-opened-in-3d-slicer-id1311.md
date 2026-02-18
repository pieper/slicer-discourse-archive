# FE meshed models to be opened in 3D Slicer

**Topic ID**: 1311
**Date**: 2017-10-27
**URL**: https://discourse.slicer.org/t/fe-meshed-models-to-be-opened-in-3d-slicer/1311

---

## Post #1 by @HarishRRao (2017-10-27 17:54 UTC)

<p>I intend to use 3D Slicer to generate patient specific models from CT/MRI as input. I have a FE meshed model already created in LS DYNA which I want to morph so I don’t have to go through the model and mesh generating process again. Is there a way to open this meshed model in 3D Slicer?</p>
<p>Thanks and Regards,<br>
Harish R Rao</p>

---

## Post #2 by @lassoan (2017-10-27 18:56 UTC)

<p>Currently, Slicer can read volumetric meshes from VTK unstructured grid (.VTU) files only.</p>
<p>Probably the easiest for now is to load your LS-Dyna d3plot files to ParaView and from there save as .vtu file (see details here: <a href="https://www.paraview.org/Wiki/ParaView:FAQ">https://www.paraview.org/Wiki/ParaView:FAQ</a>).</p>
<p>If this additional conversion step disrupts your workflow then you can load the LS-Dyna file in Slicer using a few lines of Python code (reader=vtk.vtkLSDynaReader(), read the file, create a model node, and set the imported mesh as input).</p>

---

## Post #3 by @HarishRRao (2017-10-27 22:15 UTC)

<p>Thanks Andras, I will give this a try!</p>
<p>Also as I am new to programming, could you let me know exactly where I should include the Python code in 3D Slicer?</p>

---

## Post #4 by @lassoan (2017-10-27 23:18 UTC)

<p>The Slicer programming tutorial can get you started: <a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Programming_Tutorial">https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Programming_Tutorial</a></p>

---
