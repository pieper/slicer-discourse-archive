---
topic_id: 47193
title: "3D Slicer crashes when using the Smoother during segmentation"
date: 2026-06-01
url: https://discourse.slicer.org/t/47193
last_bumped: 2026-06-02T02:09:19.352Z
---

# 3D Slicer crashes when using the Smoother during segmentation

**Topic ID**: 47193
**Date**: 2026-06-01
**URL**: https://discourse.slicer.org/t/3d-slicer-crashes-when-using-the-smoother-during-segmentation/47193

---

## Post #1 by @Camilla (2026-06-01 13:59 UTC)

<p>3D Slicer crashes when using the Smoother during segmentation.</p>
<p>The program is ‘thinking’ for a really long time and ultimately end up not responding and I have to start over.</p>
<p>Any suggestions on why that happens?</p>
<p>I’m trying to segment the muscles of the lower leg if that may have an influence.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @ThomasVanParys (2026-06-01 14:05 UTC)

<p>perhaps your system has insufficient RAM for smoothing? Do you have a large segmentation volume? Perhaps try cropping the volume or filtering/downsampling to mitigate computational times…</p>

---

## Post #3 by @muratmaga (2026-06-02 02:09 UTC)

<aside class="quote no-group" data-username="Camilla" data-post="1" data-topic="47193">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e99b99/48.png" class="avatar"> Camilla:</div>
<blockquote>
<p>The program is ‘thinking’ for a really long time and ultimately end up not responding and I have to start over.</p>
</blockquote>
</aside>
<p>In my experience that’s almost always related to choosing a smoothing kernel size unrealistically large. Keep in mind the the smoothing kernel is specified in physical units (in mm to be precise), so if you keep it like 3x3x3mm and your voxel size 0.02mm then you will have kernel size of 150x150x150 which will stall and result in out of memory. Make sure the kernel size you specify makes sense in terms of voxel dimensions, you typically want something in the range of 2-5 voxels.</p>

---
