---
topic_id: 18962
title: "Grow From Seeds Stopped Editing During Whole Heart Segmentat"
date: 2021-07-28
url: https://discourse.slicer.org/t/18962
---

# Grow from seeds stopped editing during Whole Heart Segmentation-PerkLab

**Topic ID**: 18962
**Date**: 2021-07-28
**URL**: https://discourse.slicer.org/t/grow-from-seeds-stopped-editing-during-whole-heart-segmentation-perklab/18962

---

## Post #1 by @Dexter777 (2021-07-28 23:27 UTC)

<p>Hi, I’m working on 3dp a canine caudal vena and kidneys for a clinical simulator. To learn how to use the Grow Seeds function I downloaded data and started Iassoan’s Whole Heart Segmentation from PerkLabs.<br>
I get to the point of editing the Right Atrium and I can no longer grow seeds in the other segments. My Mask is set to Editable area: Everywhere/ Over write all. Editable intensity is unchecked. I am getting numerous error, warning messages. When I paint in other segments I see a faint brush stroke and other times nothing. What am I missing from the error/warning messages?<br>
Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c36397834427cef41c6c15d5a3b734f932a0937.jpeg" data-download-href="/uploads/short-url/hIPnFwCPdTuaFCU8m6jlBVKOmRp.jpeg?dl=1" title="Cannot change seeds.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c36397834427cef41c6c15d5a3b734f932a0937_2_690x357.jpeg" alt="Cannot change seeds.PNG" data-base62-sha1="hIPnFwCPdTuaFCU8m6jlBVKOmRp" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c36397834427cef41c6c15d5a3b734f932a0937_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c36397834427cef41c6c15d5a3b734f932a0937_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c36397834427cef41c6c15d5a3b734f932a0937_2_1380x714.jpeg 2x" data-dominant-color="C5C3C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cannot change seeds.PNG</span><span class="informations">1903×987 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Dexter777 (2021-07-29 18:53 UTC)

<p>Never mind, I think I found out it was operator error and I’m not sure auto update was working.<br>
I reloaded 4.11.20210226 and decided to segment the canine caudal vena and kidneys. It worked well.<br>
Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3df1a6170fb36893712061c0a6d524c484f0291.jpeg" data-download-href="/uploads/short-url/ueiK1zeodxSaqjPpZ14GEsUXFAd.jpeg?dl=1" title="Success_Caudal.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3df1a6170fb36893712061c0a6d524c484f0291_2_690x400.jpeg" alt="Success_Caudal.PNG" data-base62-sha1="ueiK1zeodxSaqjPpZ14GEsUXFAd" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3df1a6170fb36893712061c0a6d524c484f0291_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3df1a6170fb36893712061c0a6d524c484f0291_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3df1a6170fb36893712061c0a6d524c484f0291_2_1380x800.jpeg 2x" data-dominant-color="9B9B9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Success_Caudal.PNG</span><span class="informations">1737×1008 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
