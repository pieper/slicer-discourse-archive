---
topic_id: 48416
title: "The calculations used for determining TbTh/ TbSp/ & Tb.N in BoneMorphometry extension?"
date: 2026-10-06
url: https://discourse.slicer.org/t/48416
last_bumped: 2026-10-06T16:14:41.697Z
---

# The calculations used for determining TbTh/ TbSp/ & Tb.N in BoneMorphometry extension?

**Topic ID**: 48416
**Date**: 2026-10-06
**URL**: https://discourse.slicer.org/t/the-calculations-used-for-determining-tbth-tbsp-tb-n-in-bonemorphometry-extension/48416

---

## Post #1 by @danielleadams098 (2026-10-06 16:14 UTC)

<p>Operating system: Mac OS 26.2<br>
Slicer version: 5.12.4<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am looking for documentation on how exactly the BoneMorphometry extension measures trabecular thickness, trabecular separation, and trabecular number. A couple months ago, I found a page on BoneTexture extension github that explained how it counted the pixels that made up the boundary of the bone (notes below)… which seemed to be a different method than that used in Fiji software - where for each voxel, the distance to the bone interface is measured and it creates a sphere that represents the trabecular thickness in that area.</p>
<p>It seems that the BoneTexture extension documentation has been rearranged recently and I cannot locate the specific calculations of these trabecular metrics. Does anyone have that information? or can tell me where it is located now?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8a2089d011e17bf0cc7ad513b9f92897e5c484b.jpeg" data-download-href="/uploads/short-url/uUqhVj3RYknVKl2VQPXjMwgrstJ.jpeg?dl=1" title="IMG_6821" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a2089d011e17bf0cc7ad513b9f92897e5c484b_2_375x500.jpeg" alt="IMG_6821" data-base62-sha1="uUqhVj3RYknVKl2VQPXjMwgrstJ" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a2089d011e17bf0cc7ad513b9f92897e5c484b_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a2089d011e17bf0cc7ad513b9f92897e5c484b_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a2089d011e17bf0cc7ad513b9f92897e5c484b_2_750x1000.jpeg 2x" data-dominant-color="B1B0AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_6821</span><span class="informations">1920×2560 474 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
