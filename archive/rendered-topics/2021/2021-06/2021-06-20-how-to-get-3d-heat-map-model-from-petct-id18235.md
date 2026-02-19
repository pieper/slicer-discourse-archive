---
topic_id: 18235
title: "How To Get 3D Heat Map Model From Petct"
date: 2021-06-20
url: https://discourse.slicer.org/t/18235
---

# How to get 3d heat map model from petct?

**Topic ID**: 18235
**Date**: 2021-06-20
**URL**: https://discourse.slicer.org/t/how-to-get-3d-heat-map-model-from-petct/18235

---

## Post #1 by @timeanddoctor (2021-06-20 12:41 UTC)

<p>How to get 3d heat map model from pet-ct?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31069e1d6c2dc58fb05adb4ff036f48f0853a52d.jpeg" data-download-href="/uploads/short-url/6ZHzBvgAjXa0PXN9zgBI6sEyUfX.jpeg?dl=1" title="微信图片_20210620203813" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31069e1d6c2dc58fb05adb4ff036f48f0853a52d_2_690x388.jpeg" alt="微信图片_20210620203813" data-base62-sha1="6ZHzBvgAjXa0PXN9zgBI6sEyUfX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31069e1d6c2dc58fb05adb4ff036f48f0853a52d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31069e1d6c2dc58fb05adb4ff036f48f0853a52d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31069e1d6c2dc58fb05adb4ff036f48f0853a52d_2_1380x776.jpeg 2x" data-dominant-color="8E8679"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20210620203813</span><span class="informations">1920×1080 409 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-20 21:22 UTC)

<p>If you use a recent Slicer version then you can drag-and-drop the PET volume into a 3D view to see it rendered using volume rendering.</p>
<p>However, the image above looks like thr surface of the brain, which is not visible on PET images. Has the surface segmented from MRI (or maybe CT)? Are you sure the coloring comes from PET? Do you know how the PET volume is used for coloring the surface?</p>

---
