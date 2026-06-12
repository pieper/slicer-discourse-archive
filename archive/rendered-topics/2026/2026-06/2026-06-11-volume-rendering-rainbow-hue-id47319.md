---
topic_id: 47319
title: "Volume rendering rainbow hue?"
date: 2026-06-11
url: https://discourse.slicer.org/t/47319
last_bumped: 2026-06-11T17:17:54.123Z
---

# Volume rendering rainbow hue?

**Topic ID**: 47319
**Date**: 2026-06-11
**URL**: https://discourse.slicer.org/t/volume-rendering-rainbow-hue/47319

---

## Post #1 by @PitaChib (2026-06-11 17:05 UTC)

<p>Hi all, I’m working with a ct scanned skull, and I used the preset microCT bone 16 bit preset to display my volume. However, no matter how I toggle the intensity settings and the advanced things, this hue exists, and as I move it around, it changes patterns. Is there any way I can get rid of it? I know complete gray scale gets rid of it, but I’d like it to look bone-like, and I never encountered this issue before while doing volume rendering. Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f78f5108fe8582adddfb155e83506792bcad2a72.jpeg" data-download-href="/uploads/short-url/zk0ZlyBvPGR2jEDUKrHoVzyMlvs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f78f5108fe8582adddfb155e83506792bcad2a72_2_690x406.jpeg" alt="image" data-base62-sha1="zk0ZlyBvPGR2jEDUKrHoVzyMlvs" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f78f5108fe8582adddfb155e83506792bcad2a72_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f78f5108fe8582adddfb155e83506792bcad2a72_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f78f5108fe8582adddfb155e83506792bcad2a72_2_1380x812.jpeg 2x" data-dominant-color="B6B4B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1662×980 335 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-06-11 17:17 UTC)

<p>Your screenshot is cut, so I can’t see the full ramp. MicroCT scans are not calibrated so those presets are more of a starting point, you need to customize them. If you look at the scalar opacity Mapping then you can adjust the colors.</p>
<p>Also if you like there is now a new module in SlicerMorph to try (and if you like contribute) volume rendering properties that other people generated. It is called VRPresetHub, but it is only available with the preview versions (5.11).</p>

---
