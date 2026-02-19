---
topic_id: 4665
title: "Combine 4D Sequence Volume And 3D Volume"
date: 2018-11-06
url: https://discourse.slicer.org/t/4665
---

# Combine 4D sequence volume and 3D volume

**Topic ID**: 4665
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/combine-4d-sequence-volume-and-3d-volume/4665

---

## Post #1 by @M_pavi (2018-11-06 22:55 UTC)

<p>I have been trying to combine volume sequence cardiac data and the upper half of the body  (3D volume). I want to put 4D sequence volume put into the body and fix the scene. I tried to using transform but it seems not organized. Can anyone help me to do this ?</p>

---

## Post #2 by @lassoan (2018-11-06 23:22 UTC)

<p>We would help, but it is not clear at all what would you like to do: “putting” a volume into another volume is not a well-defined operation, I don’t know what you mean by “fixing the scene”, or by “it seems not organized”.</p>
<p>Please give some context and explain the high-level goal, maybe also attach a hand-drawn or photoshopped sketch to illustrate the main concepts.</p>

---

## Post #3 by @M_pavi (2018-11-07 16:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b18a9d1ec50df9e3e8c887accea83be2d04985e1.jpeg" data-download-href="/uploads/short-url/pkBuqRSB5srUzhuwmIyaXbNtCfv.jpeg?dl=1" title="unnamed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b18a9d1ec50df9e3e8c887accea83be2d04985e1_2_375x500.jpeg" alt="unnamed" data-base62-sha1="pkBuqRSB5srUzhuwmIyaXbNtCfv" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b18a9d1ec50df9e3e8c887accea83be2d04985e1_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b18a9d1ec50df9e3e8c887accea83be2d04985e1_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b18a9d1ec50df9e3e8c887accea83be2d04985e1_2_750x1000.jpeg 2x" data-dominant-color="A09B93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unnamed</span><span class="informations">3024×4032 1.2 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you for the quick reply. Yes, I have two volume one is 3D volume and the second one is 4D volume ( Which is consists heartbeat and moving of the lungs and other organs of the upper part in the body ) This 4D volume made using sequences. The requirement is to place volume two inside the body. Eventually, the user could able to see only volume 1 but inside plays volume 2, this would be the ultimate scene.</p>

---
