---
topic_id: 10210
title: "Can I Export My Segmentation As Voxels Instead Of Triangular"
date: 2020-02-12
url: https://discourse.slicer.org/t/10210
---

# Can I export my segmentation as Voxels instead of triangular/Tetrahedral Mesh?

**Topic ID**: 10210
**Date**: 2020-02-12
**URL**: https://discourse.slicer.org/t/can-i-export-my-segmentation-as-voxels-instead-of-triangular-tetrahedral-mesh/10210

---

## Post #1 by @Mohammad_Tanjib_Rahm (2020-02-12 06:57 UTC)

<p>I am segmenting some MRI data. But I see that the generated 3D model uses triangular mesh instead of voxels. Is there anyway to do this?</p>

---

## Post #2 by @Juicy (2020-02-12 07:19 UTC)

<p>You can export the segment as a labelmap which is made up of voxels using the “Segmentation” module in the “Export/import models and labelmaps” area with the settings set to “Export” and “Labelmap”.</p>
<p>Is that what you mean?</p>

---

## Post #3 by @Ilias_Paraskevas (2021-07-02 17:03 UTC)

<p>I want to ask on the same subject. How do I open the export file in MATLAB?</p>

---

## Post #4 by @lassoan (2021-07-02 17:12 UTC)

<p>If you simply save the segmentation as a .nrrd file (or export to nrrd file as <a class="mention" href="/u/juicy">@Juicy</a> described above) then you can load that file into Matlab using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">nrrdread.m</a>.</p>
<p>I would recommend to reconsider using Matlab. Nowadays you can achieve so much more with Python. Also, software development skills in Python are highly valued in both industry and academia, while Matlab is getting irrelevant in most application areas.</p>

---
