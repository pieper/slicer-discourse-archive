# Geometry extraction

**Topic ID**: 16113
**Date**: 2021-02-21
**URL**: https://discourse.slicer.org/t/geometry-extraction/16113

---

## Post #1 by @Sedra_Mulki (2021-02-21 03:37 UTC)

<p>Hello</p>
<p>Can I know which methods are available in 3D slicer to extract the geometry like marching cubes?</p>

---

## Post #2 by @lassoan (2021-02-21 05:40 UTC)

<p>To convert binary labelmap representation of a segmentation to closed surface, we use a faster version of marching cubes called <a href="https://vtk.org/doc/nightly/html/classvtkFlyingEdges3D.html">flying edges</a> followed by Taubin smoothing and optional decimation and surface normal computation.</p>

---
