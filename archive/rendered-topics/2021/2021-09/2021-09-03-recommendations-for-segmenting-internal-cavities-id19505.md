# Recommendations for segmenting internal cavities 

**Topic ID**: 19505
**Date**: 2021-09-03
**URL**: https://discourse.slicer.org/t/recommendations-for-segmenting-internal-cavities/19505

---

## Post #1 by @Ale (2021-09-03 21:14 UTC)

<p>Hi, I’m working with a microCT of bone osteoderms. I need to segment internal cavities and external compact bone. I started with threshold tool to segment compact bone and went successful. But the internal cavities is a lot more complex and some are connected with the exterior. I started segmenting full manually using the painting tool, but it take a LOT of time (2 - 3 days only 1 osteoderms). I’m asking for advice to follow some strategy to fill those cavities in a more automatic or semiautomatic way. Thanks in advance.</p>
<p>Below is and screenshot of the osteoderm:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/544d612a27eb0d48b1d9f0cde01b894b42f8cbf1.png" data-download-href="/uploads/short-url/c1LTkwWHityRWKJB1OTjdAyKJCp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/544d612a27eb0d48b1d9f0cde01b894b42f8cbf1.png" alt="image" data-base62-sha1="c1LTkwWHityRWKJB1OTjdAyKJCp" width="655" height="500" data-dominant-color="121212"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×821 18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-09-03 21:32 UTC)

<p>Yes, we have several automated tools that could segment these structures effortlessly. The key is to prevent leaking through small holes.</p>
<p>From a single image slice it is hard to tell which method will work the best, but I would recommend to start with trying cavity extraction using SurfaceWrapSolidify extension. See this <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/">segmentation recipe</a> for step-by-step instructions.</p>

---
