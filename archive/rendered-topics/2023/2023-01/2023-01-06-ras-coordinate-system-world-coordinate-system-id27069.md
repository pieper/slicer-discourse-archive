# RAS Coordinate System & World Coordinate system

**Topic ID**: 27069
**Date**: 2023-01-06
**URL**: https://discourse.slicer.org/t/ras-coordinate-system-world-coordinate-system/27069

---

## Post #1 by @dsa934 (2023-01-06 01:15 UTC)

<p>Operating system: window 11<br>
Slicer version: 4.13.0</p>
<p>Hi, everyone<br>
I tried to mark a point on the 3d slicer through the markups tool and load the position data.</p>
<p>Here is the code I used.</p>
<p>node_mark = slicer.util.getNode(‘F’)<br>
wcs_data = arrayFromMarkupsControlPoints(node_mark, True)</p>
<p>Comparing wcs_data and node_mark shows the same coordinates.</p>
<p>I thought node_mark would belong to the RAS coordinate system and<br>
wcs_data to belong to the world coordinate system, but isn’t it like this?</p>

---

## Post #2 by @lassoan (2023-01-06 04:09 UTC)

<p>3D Slicer’s world coordinate system is the RAS coordinate system.</p>

---

## Post #3 by @dsa934 (2023-01-06 04:46 UTC)

<p>Hi Lassoan,</p>
<p>Thx for answering !</p>
<p>But I’m still confused</p>
<p>Since the python module I made that I want to extend with 3D slicer follows w.c.s (general world coordinate system), do RAS coordinates of 3D slicer refer to normal w.c.s?</p>

---

## Post #4 by @lassoan (2023-01-06 05:08 UTC)

<p>To display any node in a custom coordinate system, add a transform node, set its transform to parent matrix, and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-a-transform-to-a-transformable-node">set this transform in the transformable node</a>.</p>

---

## Post #5 by @dsa934 (2023-01-06 05:30 UTC)

<p>hum…</p>
<p>Actually, the question was whether the 3D slicer’s RAS coordinate system is the (general - people think) world coordinate system. However, if you refer to the reference of lassoan, it seems to be roughly understood. I will try and come back if successful.</p>

---

## Post #6 by @lassoan (2023-01-06 06:08 UTC)

<blockquote>
<p>the question was whether the 3D slicer’s RAS coordinate system is the (general - people think) world coordinate system</p>
</blockquote>
<p>Yes, the world coordinate system of the application is the RAS coordinate system. For example, when you load a medical image then the image is displayed so that the image origin is aligned with the world coordinate system origin; R, A, S axes of the image are the first, second, and third axis of the world coordinate system; and world coordinate system unit is millimeters.</p>

---
