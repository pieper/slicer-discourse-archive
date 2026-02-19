---
topic_id: 33419
title: "A Problem About Window Leveling Mapping Issues"
date: 2023-12-17
url: https://discourse.slicer.org/t/33419
---

# A problem about  window_leveling mapping issues

**Topic ID**: 33419
**Date**: 2023-12-17
**URL**: https://discourse.slicer.org/t/a-problem-about-window-leveling-mapping-issues/33419

---

## Post #1 by @l_xx (2023-12-17 13:12 UTC)

<p>Is there any way to implement the mapping of my red arrows, and the CT displayed will still be normal? The top one was linearly mapped, but only the window level of the bone was left. What I need is the bottom result, that is Normal results.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee34ea3d4ab92d79dfa9c485ed89b967112198d2.jpeg" data-download-href="/uploads/short-url/xZh0u5jB9p6sG2KV5aXEhmtgdfI.jpeg?dl=1" title="c94597384e409dc609cc624bf85dcba" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee34ea3d4ab92d79dfa9c485ed89b967112198d2_2_690x452.jpeg" alt="c94597384e409dc609cc624bf85dcba" data-base62-sha1="xZh0u5jB9p6sG2KV5aXEhmtgdfI" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee34ea3d4ab92d79dfa9c485ed89b967112198d2_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee34ea3d4ab92d79dfa9c485ed89b967112198d2_2_1035x678.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee34ea3d4ab92d79dfa9c485ed89b967112198d2_2_1380x904.jpeg 2x" data-dominant-color="A8A9A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">c94597384e409dc609cc624bf85dcba</span><span class="informations">1461×958 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-03-17 12:01 UTC)

<p>Window/level mapping from HU to displayed range (black to white) is always done using a linear ramp function. Both CT display that you show above are normal. It is up to you what you want to emphasize (bone, soft-tissues, etc.).</p>
<p>In addition to the window/level mapping, there is an optional thresholding operation (off by default), that allows hiding part of the image that is outside the specified range.</p>

---
