---
topic_id: 39453
title: "Best Way To Smooth Surface Of Femur Segments For Fem"
date: 2024-09-30
url: https://discourse.slicer.org/t/39453
---

# Best way to smooth surface of femur segments for FEM

**Topic ID**: 39453
**Date**: 2024-09-30
**URL**: https://discourse.slicer.org/t/best-way-to-smooth-surface-of-femur-segments-for-fem/39453

---

## Post #1 by @Struan_Gray (2024-09-30 11:28 UTC)

<p>Hi<br>
Looking for support as a newbie. I am workong on femur segmentations using totalsegmentator. I am wanting to smooth their surface for mesh and FEM analysis without corrupting the internal voxel analysis- what is the best setting to do this? And would you use Surfacewrapsolidify extension?<br>
Thanks</p>

---

## Post #2 by @lassoan (2024-09-30 11:45 UTC)

<p>If you have staircase artifacts in the output mesh then you can follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#generated-surface-contains-step-artifacts">these instructions</a>.</p>
<p>If there are some smsll segmentation errors then your can fix them by using the Paint or Scissors effects, optionally followed by Smoothing effect (either applied globally; or just in a region by clicking in views).</p>
<p>Smoothing is also applied when you generate volumetric mesh from the segmentation, for example by SegmentMesher extension.</p>

---
