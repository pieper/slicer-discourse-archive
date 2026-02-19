---
topic_id: 10653
title: "Save Nrrd As Stl But Only The Outside"
date: 2020-03-12
url: https://discourse.slicer.org/t/10653
---

# Save nrrd as stl but only the outside

**Topic ID**: 10653
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/save-nrrd-as-stl-but-only-the-outside/10653

---

## Post #1 by @guido_galetto (2020-03-12 04:05 UTC)

<p>Hi! I want to save a .nrrd file as a stl, but i want only the superficial mesh. I need the skin to make a 3d orthosis.</p>
<p>THanks!</p>

---

## Post #2 by @lassoan (2020-03-12 04:08 UTC)

<p>STL file can only store a surface mesh. If your problem is that the extracted skin surface segment is not solid then either use Smoothing effect or Wrap Solidify effect (provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>).</p>

---
