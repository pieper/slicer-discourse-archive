---
topic_id: 11002
title: "3D Visualisation Techniques From Labelmap"
date: 2020-04-05
url: https://discourse.slicer.org/t/11002
---

# 3D visualisation techniques from labelMap

**Topic ID**: 11002
**Date**: 2020-04-05
**URL**: https://discourse.slicer.org/t/3d-visualisation-techniques-from-labelmap/11002

---

## Post #1 by @loubna (2020-04-05 17:50 UTC)

<p>Hi,</p>
<p>Do you know some 3d visualisation methods to convert a label Map to 3d closed surface apart marching cubes. I need some suggestions according to your experiences please. Can you tell me some ideas or techniques ?</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-04-06 03:47 UTC)

<p>I would recommend to import your labelmap into a segmentation node. Segmentation can be displayed directly in 3D (closed surface is automatically generated and smoothed and kept up-to-date if the labelmap is edited). Slicer uses VTK’s flying edge method, which is a faster, parallelized isosurface extraction method; followed by smoothing (using vtkWindowedSincPolyDataFilter) to reduce staircase artifacts. You may also apply various smoothing and noise filtering methods on the labelmap in Segment Editor.</p>

---
