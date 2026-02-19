---
topic_id: 25907
title: "About Surface Rendering Algorithm"
date: 2022-10-26
url: https://discourse.slicer.org/t/25907
---

# About Surface Rendering Algorithm

**Topic ID**: 25907
**Date**: 2022-10-26
**URL**: https://discourse.slicer.org/t/about-surface-rendering-algorithm/25907

---

## Post #1 by @wawa (2022-10-26 07:10 UTC)

<p>Hello, I tried saving surface rendering as STL file using Segment Editor module. I wonder whether the surface rendering uses the Marching Cubes algorithm or other algorithms?<br>
Thank you.</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2022-10-27 05:37 UTC)

<p>We use more modern algorithms: flying edges for isosurface extraction (tens of times faster than marching cubes when running on a multi-core CPU) and windowed sinc filter for reconstructing the continuous surface.</p>

---
