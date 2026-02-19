---
topic_id: 27427
title: "Fill Holes In Segment"
date: 2023-01-24
url: https://discourse.slicer.org/t/27427
---

# fill holes in segment

**Topic ID**: 27427
**Date**: 2023-01-24
**URL**: https://discourse.slicer.org/t/fill-holes-in-segment/27427

---

## Post #1 by @ManiaFG (2023-01-24 01:44 UTC)

<p>Hello! Is there any way to fill holes in each slice?<br>
I’v downloaded some modules, but no result for me.<br>
Maybe there are few ways to do this? Would like to know all of them if possible : )</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feeee4f7d2ef121916cbe8985886dec57452da7e.jpeg" data-download-href="/uploads/short-url/Anf6AZXUlOvPNKuTdOXzNsD6d3g.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feeee4f7d2ef121916cbe8985886dec57452da7e_2_690x490.jpeg" alt="Screenshot_2" data-base62-sha1="Anf6AZXUlOvPNKuTdOXzNsD6d3g" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feeee4f7d2ef121916cbe8985886dec57452da7e_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/feeee4f7d2ef121916cbe8985886dec57452da7e_2_1035x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feeee4f7d2ef121916cbe8985886dec57452da7e.jpeg 2x" data-dominant-color="4C4F50"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1198×851 74.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Operating system:win 10<br>
Slicer version:5.2.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @cpinter (2023-01-24 13:39 UTC)

<p>Segmentation is never trivial. I guess you used a relatively high threshold to minimize the noise outside of the bone. You can choose a lower threshold and then use the Islands tool to remove what you don’t need. Or you can use level tracing to fill the hole on a few slices and then join the result with Fill between slices. Also I suggest trying <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">WrapSolidify</a>, it works great filling holes.</p>

---
