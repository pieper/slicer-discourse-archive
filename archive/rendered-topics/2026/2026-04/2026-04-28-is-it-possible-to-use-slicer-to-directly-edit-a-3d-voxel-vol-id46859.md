---
topic_id: 46859
title: "Is It Possible To Use Slicer To Directly Edit A 3D Voxel Vol"
date: 2026-04-28
url: https://discourse.slicer.org/t/46859
---

# Is it possible to use Slicer to directly edit a 3D voxel volume?

**Topic ID**: 46859
**Date**: 2026-04-28
**URL**: https://discourse.slicer.org/t/is-it-possible-to-use-slicer-to-directly-edit-a-3d-voxel-volume/46859

---

## Post #1 by @PetrKryslUCSD (2026-04-28 15:33 UTC)

<p>Has this been already solved or at least discussed? Such as inserting “voxelized” primitives (sphere, cylinder, block, …) and combining them in various ways (boolean ops?).</p>

---

## Post #2 by @lassoan (2026-04-28 16:06 UTC)

<p>Yes, you can use the Segment Editor’s Mask Volume effect to paint in anything into a volume. There are several options, such as paint inside/outside and smooth edges (to keep gradients clean and smooth at the segment boundary).</p>
<p>If you have some input meshes (sphere, etc.) then you can load them as models into Slicer (or create them in Slicer using <code>Create Models</code> module in <code>SlicerIGT</code> extension) and then:</p>
<ul>
<li>Go to <code>Segment Editor</code> module and create a new segmentation</li>
<li>Go to <code>Data</code> module and drag-and-drop the model(s) into the segmentation node</li>
<li>Go to <code>Segment Editor</code> module and use <code>Mask Volume</code> effect to paint the segment into the volume</li>
</ul>

---
