# Slicer 3D to CAD software via .stl file.

**Topic ID**: 5464
**Date**: 2019-01-22
**URL**: https://discourse.slicer.org/t/slicer-3d-to-cad-software-via-stl-file/5464

---

## Post #1 by @ColJol (2019-01-22 14:13 UTC)

<p>Operating system: Windows 10 Enterprise<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I want to export models from dicom files to CAD software using .stl file format to obtain surface models (&gt;25Mb). I have successfully modeled the appropriate structures with Slicer 3D and created .stl file, however, the resulting .stl file is much too large. How can I reduce tetrahedral size or any other way to make the output file more manageable? (5ish Mb)</p>

---

## Post #2 by @lassoan (2019-01-31 02:12 UTC)

<p>You can use Surface Toolbox module to clean up, smooth, and decimate models.</p>
<p>Most FE packages fail to import large or complex surface meshes, but they can work reliably with volumetric mesthes. You can generate volumetric mesh (VTK unstructured grid in .vtk or .vtu file format) using SegmentMesher extension directly from segmentation nodes. However, only some FE modeler can read VTK unstructured grid files directly (for example, FEBio <em>can</em> read them, but we could not find a conversion path from VTK to Comsol).</p>

---
