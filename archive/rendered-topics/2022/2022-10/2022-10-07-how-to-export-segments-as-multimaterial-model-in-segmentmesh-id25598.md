---
topic_id: 25598
title: "How To Export Segments As Multimaterial Model In Segmentmesh"
date: 2022-10-07
url: https://discourse.slicer.org/t/25598
---

# How to export segments as *multimaterial* model in SegmentMesher extension?

**Topic ID**: 25598
**Date**: 2022-10-07
**URL**: https://discourse.slicer.org/t/how-to-export-segments-as-multimaterial-model-in-segmentmesher-extension/25598

---

## Post #1 by @SlicerGroupie (2022-10-07 19:14 UTC)

<p>Hello,<br>
We have 4 segments of the cerebrum. When we export them as a model, it works, but it exports as a <em>single material</em> model (where the four segments get fused into one large mesh).</p>
<p>But we want to export it as a <em>multimaterial</em> model, where each segment can be specified to have a different material/color. It is possible to do this in 3D Slicer.</p>
<p>Alternatively, is it possible to export our four segments into four separate <em>single material</em> models, and then somehow combine them together correctly as a single <em>multimaterial</em> model?</p>
<p>Many thanks in advance!</p>

---

## Post #2 by @lassoan (2022-10-07 19:21 UTC)

<p>If you use “Cleaver” meshing method then you get a multimaterial model in the .vtk//vtu file. Material of each element is specified in the cell array called <code>label</code>.</p>

---
