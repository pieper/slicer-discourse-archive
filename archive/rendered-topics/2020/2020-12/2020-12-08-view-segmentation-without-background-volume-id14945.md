---
topic_id: 14945
title: "View Segmentation Without Background Volume"
date: 2020-12-08
url: https://discourse.slicer.org/t/14945
---

# View segmentation without background volume

**Topic ID**: 14945
**Date**: 2020-12-08
**URL**: https://discourse.slicer.org/t/view-segmentation-without-background-volume/14945

---

## Post #1 by @iboeth (2020-12-08 18:36 UTC)

<p>Hello!<br>
I put a segmentation into 3D-Slicer, but the “pictures” are not visible…<br>
I also restarted 3D-Slicer, but it is still the same. What have I done wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5bcf7eb430c2bf65dd0d31f9da137691742ef27.jpeg" data-download-href="/uploads/short-url/pVJhG7WbXeaQbqZ8WSVo7yIweQn.jpeg?dl=1" title="D7FCA3F1-6150-42B6-A0B9-A366D4ADEC03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5bcf7eb430c2bf65dd0d31f9da137691742ef27_2_690x431.jpeg" alt="D7FCA3F1-6150-42B6-A0B9-A366D4ADEC03" data-base62-sha1="pVJhG7WbXeaQbqZ8WSVo7yIweQn" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5bcf7eb430c2bf65dd0d31f9da137691742ef27_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5bcf7eb430c2bf65dd0d31f9da137691742ef27_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5bcf7eb430c2bf65dd0d31f9da137691742ef27.jpeg 2x" data-dominant-color="7A7979"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">D7FCA3F1-6150-42B6-A0B9-A366D4ADEC03</span><span class="informations">1280×800 83.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-12-08 19:39 UTC)

<p>If you don’t have a background volume then you cannot move the slice selection slider. If you don’t have a background volume then you can create one from the segmentation itself, by right-clicking on it and exporting to binary labelmap.</p>

---

## Post #3 by @iboeth (2020-12-09 11:55 UTC)

<p>Thank you very much! It works!</p>

---
