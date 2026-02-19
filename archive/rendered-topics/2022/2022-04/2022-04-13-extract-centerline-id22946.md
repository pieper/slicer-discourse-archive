---
topic_id: 22946
title: "Extract Centerline"
date: 2022-04-13
url: https://discourse.slicer.org/t/22946
---

# Extract centerline

**Topic ID**: 22946
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/extract-centerline/22946

---

## Post #1 by @canadan (2022-04-13 17:55 UTC)

<p>Can anyone tell me the basic algorithm used to extract the centerline?</p>
<p>As a side note, I heard a rumour that the current implementation does not properly handle noncubic voxels (ie voxels whose length, width and height are not all equal).</p>
<p>Thanks</p>
<p>dan</p>

---

## Post #2 by @chir.set (2022-04-13 18:35 UTC)

<aside class="quote no-group" data-username="canadan" data-post="1" data-topic="22946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/a88e4f/48.png" class="avatar"> canadan:</div>
<blockquote>
<p>I heard a rumour that the current implementation does not properly handle noncubic voxels</p>
</blockquote>
</aside>
<p>This would be doubtful, centerline extraction requires a surface model, either an MRML segmentation node or an MRML model node, not a volume node (completely unrelated).</p>

---

## Post #3 by @lassoan (2022-04-13 19:49 UTC)

<p>You can start from a volume node but you need to segment it. In case the structure of interest has a distinct intensity range then you can easily segment it out using simple thresholding. You can use this segmentation as input for centerline extraction.</p>
<p>If voxels are not cubic then that does not impact centerline extraction specifically, but it is not ideal, because it means that you have less details about the geometry along certain axes. If due to this limited resolution the diameter may be reduced to 1-2 voxels then it makes sense to oversample the volume before segmentation.</p>

---

## Post #4 by @canadan (2022-04-14 13:06 UTC)

<p>Understood. Thanks (again) Andras for explaining the situation.</p>
<p>dan</p>

---
