---
topic_id: 32666
title: "How To Segment Intercoastal Space"
date: 2023-11-08
url: https://discourse.slicer.org/t/32666
---

# How to segment intercoastal space?

**Topic ID**: 32666
**Date**: 2023-11-08
**URL**: https://discourse.slicer.org/t/how-to-segment-intercoastal-space/32666

---

## Post #1 by @Lee_Ho_Jun (2023-11-08 10:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2eb44b365326ee744d80fd3357c6f6417407fe2.jpeg" data-download-href="/uploads/short-url/pwN35KaW763CY1vx1rHAvszI8vM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2eb44b365326ee744d80fd3357c6f6417407fe2_2_690x317.jpeg" alt="image" data-base62-sha1="pwN35KaW763CY1vx1rHAvszI8vM" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2eb44b365326ee744d80fd3357c6f6417407fe2_2_690x317.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2eb44b365326ee744d80fd3357c6f6417407fe2_2_1035x475.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2eb44b365326ee744d80fd3357c6f6417407fe2_2_1380x634.jpeg 2x" data-dominant-color="8C8783"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×884 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi. I’ want to segment the intercoastal space.<br>
You can easily segment the ribs, but segmentation of the intercoastal space (olive color in the middle image) is quite difficult. The right image is a illustration to show the cross-sectional relationship of ribs, and the intercoastal space, in the coronal plane (shown in blue lines in the middle image).<br>
If there is a way to easily connect the outermost and innermost surfaces (red lines in the middle image, and right cross sectional illustration) of the rib (numbered) models, you can segment the volume between the 2 surfaces, Then, you can subtract the ribs to segment the intercoastal space (blue area in the left image). Is this possible in Slicer?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @volkodavmyx (2023-11-10 14:08 UTC)

<p>Try “Fill between slices” tool. It helps you fill intercostal spaces automatically.</p>

---

## Post #3 by @rbumm (2023-11-11 06:22 UTC)

<p>Good idea, but does not work.</p>

---
