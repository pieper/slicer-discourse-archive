---
topic_id: 22229
title: "Does Anyone Know How To Visualize Points In Ijk Coordinates"
date: 2022-03-01
url: https://discourse.slicer.org/t/22229
---

# Does anyone know how to visualize points in IJK coordinates in RAS coordinates?

**Topic ID**: 22229
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/does-anyone-know-how-to-visualize-points-in-ijk-coordinates-in-ras-coordinates/22229

---

## Post #1 by @zhuyingxinxs (2022-03-01 08:39 UTC)

<p>Once you’ve determined the coordinates of a point in IJK coordinates, how do you visualize it in RAS coordinates? Do we have to do a coordinate transformation first?</p>

---

## Post #2 by @Alex_Vergara (2022-03-01 08:44 UTC)

<p>RAS are not coordinates but rather orientation.</p>

---

## Post #3 by @ebrahim (2022-03-01 11:06 UTC)

<p>They can be thought of as a coordinate system in Slicer.</p>
<p>e.g. volume nodes have an IJK-RAS coordinate transformation<br>
and perhaps other things</p>

---

## Post #4 by @ebrahim (2022-03-01 11:12 UTC)

<p>I’m not sure what “visualize” means here, but if it’s a volume node you can use <code>GetIJKToRASMatrix</code> to go between the two coordinate systems.</p>
<p>Maybe this can help: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-markup-control-point-ras-coordinates-from-volume-voxel-coordinates" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---
