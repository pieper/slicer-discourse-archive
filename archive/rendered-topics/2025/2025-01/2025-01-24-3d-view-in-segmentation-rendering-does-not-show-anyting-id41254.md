---
topic_id: 41254
title: "3D View In Segmentation Rendering Does Not Show Anyting"
date: 2025-01-24
url: https://discourse.slicer.org/t/41254
---

# 3d view in segmentation rendering does not show anyting

**Topic ID**: 41254
**Date**: 2025-01-24
**URL**: https://discourse.slicer.org/t/3d-view-in-segmentation-rendering-does-not-show-anyting/41254

---

## Post #1 by @alex_He (2025-01-24 03:26 UTC)

<p>hi<br>
I tried to show the 3d view in the volume rendering module but unsucessful.  please advise and see the attached screen capture. thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e915960c4e711aa48b22a4673994e7d0b7a8fd2d.png" data-download-href="/uploads/short-url/xfXuUU9EYVmAkZIa4kx7Yc9NO5D.png?dl=1" title="3d view not showing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e915960c4e711aa48b22a4673994e7d0b7a8fd2d_2_690x372.png" alt="3d view not showing" data-base62-sha1="xfXuUU9EYVmAkZIa4kx7Yc9NO5D" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e915960c4e711aa48b22a4673994e7d0b7a8fd2d_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e915960c4e711aa48b22a4673994e7d0b7a8fd2d_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e915960c4e711aa48b22a4673994e7d0b7a8fd2d_2_1380x744.png 2x" data-dominant-color="A4A3B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d view not showing</span><span class="informations">1919×1037 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-01-24 05:01 UTC)

<p>At this point you have no segmentation to show in 3D view. Both segments are black. Point something and it should show up.</p>

---

## Post #3 by @alex_He (2025-01-24 06:03 UTC)

<p>thanks for your advise, howver i donot quite understand what you mean.<br>
I tried to switch to volume rendering but still do not get what I wanted. the solid 3d view, not the one that is shown<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eb40deb1c97c8a599f3a964b9c869ece3a771bb.png" data-download-href="/uploads/short-url/kmpz3ONJAw7skRq33DwsEgSIZw7.png?dl=1" title="volume rendering-3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb40deb1c97c8a599f3a964b9c869ece3a771bb_2_690x387.png" alt="volume rendering-3" data-base62-sha1="kmpz3ONJAw7skRq33DwsEgSIZw7" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb40deb1c97c8a599f3a964b9c869ece3a771bb_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb40deb1c97c8a599f3a964b9c869ece3a771bb_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb40deb1c97c8a599f3a964b9c869ece3a771bb_2_1380x774.png 2x" data-dominant-color="9B9AA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume rendering-3</span><span class="informations">1919×1079 432 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mohammed_alshakhas (2025-01-24 14:26 UTC)

<p>go to browser module and check if there is transform applied to volume .<br>
sometime makes 3d  not visible . it is there delete and try segmentation again</p>

---
