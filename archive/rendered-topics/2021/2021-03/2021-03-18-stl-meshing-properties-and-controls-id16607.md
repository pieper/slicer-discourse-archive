# STL Meshing properties and controls

**Topic ID**: 16607
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/stl-meshing-properties-and-controls/16607

---

## Post #1 by @Nicholas.jacobson (2021-03-18 05:35 UTC)

<p>Is there a way to understand the controls for meshing to an STL file. I’d like to be able to modify edge length properties, angles, and other elements inherent to stl meshing… or at least know what they are set at by default.</p>

---

## Post #2 by @lassoan (2021-03-26 03:09 UTC)

<p>There are no such meshing parameters. During meshing of the labelmap, each voxel is converted to a triangle, therefore the number and size of triangles are dictated by the voxel size of the labelmap’s geometry. There are various mesh processing, smoothing, re-meshing algorithms to reduce number of triangles while preserving details and good mesh quality. You can try Decimation and Smoothing options in Surface toolbox. You may also try mesh processing Python packages, such as <a href="https://github.com/pyvista/pyacvd">ACVD</a>.</p>

---
