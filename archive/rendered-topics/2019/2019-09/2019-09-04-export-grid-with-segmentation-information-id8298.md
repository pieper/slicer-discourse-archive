---
topic_id: 8298
title: "Export Grid With Segmentation Information"
date: 2019-09-04
url: https://discourse.slicer.org/t/8298
---

# Export grid with segmentation information

**Topic ID**: 8298
**Date**: 2019-09-04
**URL**: https://discourse.slicer.org/t/export-grid-with-segmentation-information/8298

---

## Post #1 by @iacarr (2019-09-04 18:12 UTC)

<p>I’m looking to obtain a file with a 3D cartesian grid containing the segmentations I’ve created. I’ve worked a bit with the Segment Mesher module but have not found a way to export a simple cartesian grid of a prescribed size. Is this possible to do in 3D slicer or is there some other software I could use to do this? It seems like a simple task but I haven’t found a good way to do it.</p>

---

## Post #2 by @lassoan (2019-09-04 18:39 UTC)

<p>Segmentation is saved by default in a 3D Cartesian grid (image volume). You can change the segment geometry (origin, spacing, axis directions) by clicking on the button in Segment Editor next to the master volume selector.</p>
<p>By default segmentation is saved into a 4D volume file (each 3D volume contain a binary labelmap), but you can export it into a single 3D volume if you export the segmentation to a labelmap node first.</p>

---
