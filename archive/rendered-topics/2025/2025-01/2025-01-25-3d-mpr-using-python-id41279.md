---
topic_id: 41279
title: "3D Mpr Using Python"
date: 2025-01-25
url: https://discourse.slicer.org/t/41279
---

# 3D MPR using Python

**Topic ID**: 41279
**Date**: 2025-01-25
**URL**: https://discourse.slicer.org/t/3d-mpr-using-python/41279

---

## Post #1 by @Eers (2025-01-25 10:55 UTC)

<p>Hi, I am trying to reformat a 3D MR volume to an oblique plane. Given new directional cosines, using sitk resampleImage filter I get the expected anatomical landmark but the view has some in-plane rotation in some cases, vertical flip with some inplane rotation in few other cases. What could be the possible reason, is there any standard way to do MPR given directional cosines using python</p>

---

## Post #2 by @lassoan (2025-01-25 11:03 UTC)

<p>There are 8 equally good options for displaying an image slice on screen (4 options for which corner is in the top-left corner; for each of these options, 2 options for slice normal direction pointing towards or away from the user). Slicer has no way of knowing which one you want, so when you show the image slice with automatic orientation setting, Slicer snaps the slice view axes to the closest image axes.</p>
<p>If you need a particular slice orientation then you can set it in the SliceToRAS matrix of the slice node. You actually don’t even need to resample the inage with SimpleITK: Slicer does this automatically when you set the SliceToRAS.</p>

---

## Post #3 by @Eers (2025-01-26 11:07 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> , can you please provide the steps to do MPR on slicer given slice orientation</p>

---
