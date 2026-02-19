---
topic_id: 1421
title: "Segment Editor Slowdown"
date: 2017-11-09
url: https://discourse.slicer.org/t/1421
---

# Segment Editor slowdown

**Topic ID**: 1421
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/segment-editor-slowdown/1421

---

## Post #1 by @Valeria_Vendries (2017-11-09 15:24 UTC)

<p>Hello,</p>
<p>I am experiencing extreme slowdowns when using segment editor. I downloaded a newer version and still get the problem.<br>
I am thinking the file may be too large, so would removing nodes of data help at all?<br>
Is there a way to remove the automatic update checkbox in the fill in the slices function? that may be another issue.<br>
Or is it possible for a bug to be going on?</p>
<p>Any help would be appreciated!</p>

---

## Post #2 by @lassoan (2017-11-09 22:01 UTC)

<p>We’ve checked this with Valeria and found out that the problem was mainly due to having too large (too high resolution) segmentation and 3D representation update for such large volume took too long time.</p>
<p>By performing these 3 steps, update after each editing operation reduced from about 10 seconds to a fraction of a second:</p>
<ul>
<li>Decrease segment resolution by 2x (resulting in reducing number of voxels by 8x): export segmentation to labelmap, resample using Crop volume, import labelmap to new segmentation</li>
<li>Disable 3D smoothing (set smoothing factor to 0)</li>
<li>Make 3D model simpler by smoothing the segment (using Smoothing effect, median method, kernel size of 9 voxels)</li>
</ul>

---
