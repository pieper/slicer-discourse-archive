# How can I import the mesh created in comsol to the nirfast ?

**Topic ID**: 22669
**Date**: 2022-03-24
**URL**: https://discourse.slicer.org/t/how-can-i-import-the-mesh-created-in-comsol-to-the-nirfast/22669

---

## Post #1 by @dantu (2022-03-24 13:04 UTC)

<p>Operating system:window10<br>
Slicer version:2.0.0<br>
Expected behavior:use the mesh created in comsol to compete image reconstruction<br>
Actual behavior:there’s no where to import the data</p>

---

## Post #2 by @lassoan (2022-03-26 03:32 UTC)

<p>What file formats can you export from comsol?</p>

---

## Post #3 by @dantu (2022-03-28 05:37 UTC)

<p>it can impport the ‘txt’ which includes element and node, but the NIRFAST needs element,node and ‘param.’ which displays optical parameter distribution .</p>

---

## Post #4 by @lassoan (2022-03-28 12:24 UTC)

<p>Do you want to load Slicer segmentation results into comsol, or you want to load comsol simulation results into Slicer?</p>

---

## Post #5 by @dantu (2022-03-28 12:37 UTC)

<p>i want to load comsol mesh into the software ‘NIRFAST’</p>

---

## Post #6 by @lassoan (2022-03-28 13:16 UTC)

<p>Slicer can load volumetric meshes from VTK unstructured grid files (.vtk and .vtu extensions).</p>
<p><a href="https://github.com/nirfast-admin/NIRFASTSlicer/tree/v2.0.0">NIRFAST Slicer</a> (which is a customized build of Slicer with some additional modules) does not seem to have additional mesh importers.</p>
<p>Therefore, you probably need to use a mesh converter, such as <a href="https://pypi.org/project/meshio/">meshio</a> to convert comsol output mesh to vtk/vtu file.</p>

---

## Post #7 by @dantu (2022-03-28 13:32 UTC)

<p>i see! thank you very very much!    i will have a try.</p>

---
