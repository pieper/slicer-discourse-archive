---
topic_id: 5704
title: "Refine Brain Vessel Segmentation"
date: 2019-02-08
url: https://discourse.slicer.org/t/5704
---

# Refine brain vessel segmentation

**Topic ID**: 5704
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/refine-brain-vessel-segmentation/5704

---

## Post #1 by @albert94 (2019-02-08 20:41 UTC)

<p>Hi all,<br>
I am trying to segment cerebral vessels from CT and MR images. First I apply swiss skull stripper to the volume, and then I threhold the immediate result by Threshold Scalar Volume module. Now I get the following results<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cea9115300618529e4b2812df1c4fe73a51e7972.jpeg" data-download-href="/uploads/short-url/tucAfHITWi1CnU2ZYa3FRIJYWKS.jpeg?dl=1" title="ct" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cea9115300618529e4b2812df1c4fe73a51e7972_2_690x437.jpeg" alt="ct" data-base62-sha1="tucAfHITWi1CnU2ZYa3FRIJYWKS" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cea9115300618529e4b2812df1c4fe73a51e7972_2_690x437.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cea9115300618529e4b2812df1c4fe73a51e7972_2_1035x655.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cea9115300618529e4b2812df1c4fe73a51e7972.jpeg 2x" data-dominant-color="575770"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ct</span><span class="informations">1306×829 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But they are not good enough. Is there a way to refine this result?</p>
<p>Thank you for your advice.</p>

---

## Post #2 by @marie (2019-11-17 20:49 UTC)

<p>See here:</p><aside class="quote" data-post="2" data-topic="8536">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/problems-when-segmenting-blood-vessels-using-vmtk-threshold/8536/2">Problems when segmenting blood vessels using VMTK (threshold)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Have you tried the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/" rel="noopener nofollow ugc">“Vessel Segmentation By Subtraction” segmentation recipe</a>?
  </blockquote>
</aside>


---
