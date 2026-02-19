---
topic_id: 34126
title: "Importing Unstructured Point Cloud Data From Filesystem"
date: 2024-02-02
url: https://discourse.slicer.org/t/34126
---

# Importing unstructured point cloud data from filesystem

**Topic ID**: 34126
**Date**: 2024-02-02
**URL**: https://discourse.slicer.org/t/importing-unstructured-point-cloud-data-from-filesystem/34126

---

## Post #1 by @a.tamaz (2024-02-02 19:49 UTC)

<p>Hi,</p>
<p>is it possible to import unstructured point cloud data in the Slicer UI? Ideally using .ply format.</p>
<p>I have tried the following .ply and .vtk files – Slicer loads both as “Model” and shows “Number of points” as 5 in the “Models” module, but does not show any points in the 3D viewer.</p>
<pre><code class="lang-auto"># vtk DataFile Version 4.0
vtk output
ASCII
DATASET POLYDATA
POINTS 5 float
0.0 0.0 0.0
1.0 0.0 0.0
0.0 1.0 0.0
0.0 0.0 1.0
1.0 1.0 1.0
</code></pre>
<pre><code class="lang-auto">ply
format ascii 1.0
element vertex 5
property float x
property float y
property float z
end_header
0.0 0.0 0.0
1.0 0.0 0.0
0.0 1.0 0.0
0.0 0.0 1.0
1.0 1.0 1.0
</code></pre>
<p>Any help is appreciated!<br>
Tamaz</p>

---
