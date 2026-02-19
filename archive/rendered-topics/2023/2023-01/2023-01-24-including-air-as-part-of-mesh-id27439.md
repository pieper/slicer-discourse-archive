---
topic_id: 27439
title: "Including Air As Part Of Mesh"
date: 2023-01-24
url: https://discourse.slicer.org/t/27439
---

# Including air as part of mesh

**Topic ID**: 27439
**Date**: 2023-01-24
**URL**: https://discourse.slicer.org/t/including-air-as-part-of-mesh/27439

---

## Post #1 by @ascam (2023-01-24 12:23 UTC)

<p>Hi there.</p>
<p>I’m looking to run a FEM model of light propagation across biological tissue (including free space / pockets of air), and am using Slicer to create a volumetric mesh. I need to include air as part of the mesh. Does anyone know how to include air / free space as part of the mesh?<br>
Thanks</p>

---

## Post #2 by @lassoan (2023-01-24 12:26 UTC)

<p>If you use “Cleaver” mesher in SegmentMesher extension then it can add such background material. You can also add a background segment on Segment Editor by using any editing tool (e.g., Paint or Scissors) with choosing “outside all segments” as editable region.</p>

---
