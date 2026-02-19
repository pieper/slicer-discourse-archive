---
topic_id: 21180
title: "Sequence Registration For 4D Ct"
date: 2021-12-22
url: https://discourse.slicer.org/t/21180
---

# Sequence Registration for 4D CT

**Topic ID**: 21180
**Date**: 2021-12-22
**URL**: https://discourse.slicer.org/t/sequence-registration-for-4d-ct/21180

---

## Post #1 by @Cody_Xie (2021-12-22 13:02 UTC)

<p>Dear all,</p>
<p>I have a 4D CT data set which has 8 phases, and I would like to segment the Left Ventricle for all 8 phases automatically (segment phase 0 manually, then the other 7 phases automatically). I followed the guidance given by Andras <a href="https://discourse.slicer.org/t/load-multiple-cardiac-phases-for-segmentation-virtual-reality/5214">Load multiple cardiac phases for segmentation/virtual reality</a>.</p>
<p>However, when I register in the Sequence Registration module, it gets stuck in “Registering item 7 of 8”. This process has been frozen here for more than an hour (please refer to the screenshot below). Would it be possible that you give me some support? Should you need more information, please tell me.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d2c483f484a97b26e51eda67c1385909fcde59a.jpeg" data-download-href="/uploads/short-url/mqpPTHc2yo1q6Km6yJemPoLUvxM.jpeg?dl=1" title="Slicer_Sequence Registration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2c483f484a97b26e51eda67c1385909fcde59a_2_690x306.jpeg" alt="Slicer_Sequence Registration" data-base62-sha1="mqpPTHc2yo1q6Km6yJemPoLUvxM" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2c483f484a97b26e51eda67c1385909fcde59a_2_690x306.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2c483f484a97b26e51eda67c1385909fcde59a_2_1035x459.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2c483f484a97b26e51eda67c1385909fcde59a_2_1380x612.jpeg 2x" data-dominant-color="C5C3C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Sequence Registration</span><span class="informations">1920×854 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Many thanks in advance!</p>

---

## Post #2 by @lassoan (2021-12-22 14:48 UTC)

<p>Check the application logs, but most likely you run out of memory. You can check if you find any interesting information in the application log. You can also experiment with adjusting the start/end frame index sliders to see if the slowdown/hang occurs when you reach a number of frames or at a specific frame.</p>

---

## Post #3 by @Cody_Xie (2021-12-22 18:47 UTC)

<p>Thanks Andras! That’s a very good idea, and I will have a try.</p>

---
