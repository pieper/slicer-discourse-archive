# Convert point cloud to surface model

**Topic ID**: 21175
**Date**: 2021-12-21
**URL**: https://discourse.slicer.org/t/convert-point-cloud-to-surface-model/21175

---

## Post #1 by @Saima (2021-12-21 06:36 UTC)

<p>Hi andras,<br>
Is there a way to convert the point cloud (4colums, x,y,z,intensity) to surface model.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2021-12-22 03:49 UTC)

<p>Is the point cloud structured (organized in a rectilinear grid by, for example acquired by a surface scanner) or the points are distributed randomly? Can you post a few screenshots?</p>
<p>VTK has all the necessary tools for this, but structured point sets, dense unorganized point sets, and sparse unorganized point sets require completely different surface reconstruction methods.</p>

---

## Post #3 by @tho (2025-06-19 13:51 UTC)

<p>Hi Andras,<br>
I have a similar question. Is there a way to convert a vtp with defined (but not coplanar) contours, to a closed surface segmentation in Slicer? I was thinking about reusing the same logic as for RTStructs planar contours reading and conversion, but not sure if this is possible, and how to process using Slicer?<br>
Thank you !</p>

---
