---
topic_id: 47045
title: "Fill In Part Of Segment Without Adding Whole Model"
date: 2026-05-15
url: https://discourse.slicer.org/t/47045
---

# Fill in part of segment without adding whole model 

**Topic ID**: 47045
**Date**: 2026-05-15
**URL**: https://discourse.slicer.org/t/fill-in-part-of-segment-without-adding-whole-model/47045

---

## Post #1 by @akelly17 (2026-05-15 14:26 UTC)

<p>Hey all, I cannot seem to figure out how to get this section of my model to fill in (i.e: make the segment whole) without adding back the entire model. I have just figured out how the “masking” function works, and am still confused about the inter-workings of it all. Any and all help is appreciated, especially if you’re willing to dumb it down for me haha</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/006d6e9f61ec1b47081a8e8b086a55e458c52909.jpeg" data-download-href="/uploads/short-url/3MslBPoY80KGWrjTvMwrmuSkzf.jpeg?dl=1" title="IMG_4204" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/006d6e9f61ec1b47081a8e8b086a55e458c52909_2_460x500.jpeg" alt="IMG_4204" data-base62-sha1="3MslBPoY80KGWrjTvMwrmuSkzf" width="460" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/006d6e9f61ec1b47081a8e8b086a55e458c52909_2_460x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/006d6e9f61ec1b47081a8e8b086a55e458c52909_2_690x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/006d6e9f61ec1b47081a8e8b086a55e458c52909_2_920x1000.jpeg 2x" data-dominant-color="817C99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4204</span><span class="informations">1745×1895 812 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ThomasVanParys (2026-05-15 15:38 UTC)

<p>If you are working directly on a surface mesh, you can use the <code>SurfaceToolbox</code> module, and navigate to the Fill Holes function…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c95a59725d7177d67406cec3cb7bfcaaf4373c8.png" data-download-href="/uploads/short-url/6mpCMGZwt9OirQrXNt4FssQNRWM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c95a59725d7177d67406cec3cb7bfcaaf4373c8_2_517x369.png" alt="image" data-base62-sha1="6mpCMGZwt9OirQrXNt4FssQNRWM" width="517" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c95a59725d7177d67406cec3cb7bfcaaf4373c8_2_517x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c95a59725d7177d67406cec3cb7bfcaaf4373c8_2_775x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c95a59725d7177d67406cec3cb7bfcaaf4373c8_2_1034x738.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×795 95.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
