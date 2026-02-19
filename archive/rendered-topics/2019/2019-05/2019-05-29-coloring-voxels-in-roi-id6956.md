---
topic_id: 6956
title: "Coloring Voxels In Roi"
date: 2019-05-29
url: https://discourse.slicer.org/t/6956
---

# Coloring voxels in ROI

**Topic ID**: 6956
**Date**: 2019-05-29
**URL**: https://discourse.slicer.org/t/coloring-voxels-in-roi/6956

---

## Post #1 by @11124 (2019-05-29 11:34 UTC)

<p>Hi!<br>
I’m writing python plugin for segmentation, using seed growing algorithm. Now, when i found voxels in ROI region, i just set intensity at -1000. Is there any possibility to color ROI voxels?</p>

---

## Post #2 by @lassoan (2019-05-29 11:35 UTC)

<p>You can assign any colors to any voxel value by creating a custom color node in the Colors module and selecting that for displaying the volume.</p>

---
