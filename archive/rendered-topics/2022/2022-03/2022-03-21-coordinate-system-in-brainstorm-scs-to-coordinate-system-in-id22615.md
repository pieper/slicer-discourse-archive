---
topic_id: 22615
title: "Coordinate System In Brainstorm Scs To Coordinate System In"
date: 2022-03-21
url: https://discourse.slicer.org/t/22615
---

# Coordinate system in brainstorm SCS to coordinate system in 3D Slicer

**Topic ID**: 22615
**Date**: 2022-03-21
**URL**: https://discourse.slicer.org/t/coordinate-system-in-brainstorm-scs-to-coordinate-system-in-3d-slicer/22615

---

## Post #1 by @Saima (2022-03-21 05:15 UTC)

<p>Dear Andras,<br>
I am running into problem of converting the coordinates from SCS to world coordinate system.</p>
<p>I exported the mesh from brain storm and then importing it to 3D slicer.<br>
It looks as below.</p>
<p>any idea on the transform.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4937a4f265e607e6277548d4a24ff5dd61995a8.jpeg" alt="coord" data-base62-sha1="s2Zyl5yUGIZYkdvBSQ3hy0fvREI" width="677" height="338"></p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2022-03-21 13:54 UTC)

<p>By default Slicer uses LPS coordinate system for all data exported to files (mesh point coordinates, image physical coordinate system, etc.) and it assumes LPS coordinate system by default. I would recommend to ask brainstorm developers about how you can export the model from their software to the image’s original LPS coordinate system.</p>

---
