---
topic_id: 10322
title: "How To Superimpose Two Ct Cbcts"
date: 2020-02-18
url: https://discourse.slicer.org/t/10322
---

# How to superimpose two CT/CBCTs?

**Topic ID**: 10322
**Date**: 2020-02-18
**URL**: https://discourse.slicer.org/t/how-to-superimpose-two-ct-cbcts/10322

---

## Post #1 by @ddii (2020-02-18 04:23 UTC)

<p>How do you superimpose two scans? or even move the VR side by side?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5527a972f3a352229a1ee76bc0a754828a9d23f5.jpeg" data-download-href="/uploads/short-url/c9jyJyE8RIL2KU1xhuROnFPL6ap.jpeg?dl=1" title="compvr" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5527a972f3a352229a1ee76bc0a754828a9d23f5_2_397x500.jpeg" alt="compvr" data-base62-sha1="c9jyJyE8RIL2KU1xhuROnFPL6ap" width="397" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5527a972f3a352229a1ee76bc0a754828a9d23f5_2_397x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5527a972f3a352229a1ee76bc0a754828a9d23f5_2_595x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5527a972f3a352229a1ee76bc0a754828a9d23f5_2_794x1000.jpeg 2x" data-dominant-color="1D1A19"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">compvr</span><span class="informations">1412×1778 455 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @JanWitowski (2020-02-18 07:47 UTC)

<p>You’re looking for Registration tools. You can do the basic translation (moving) of the volume in Transforms module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9b7efea5d93379e1c86d01fb17bc75d170c39c5.png" data-download-href="/uploads/short-url/v41H4g4M39ilwSGY1ncdq1xGgRf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9b7efea5d93379e1c86d01fb17bc75d170c39c5_2_362x499.png" alt="image" data-base62-sha1="v41H4g4M39ilwSGY1ncdq1xGgRf" width="362" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9b7efea5d93379e1c86d01fb17bc75d170c39c5_2_362x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9b7efea5d93379e1c86d01fb17bc75d170c39c5_2_543x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9b7efea5d93379e1c86d01fb17bc75d170c39c5.png 2x" data-dominant-color="F4F5F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">604×833 33.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you need more precise or automatic registration, look into BRAINS or Elastix registration modules.</p>

---

## Post #3 by @lassoan (2020-02-18 13:59 UTC)

<p>You can also register volumes based on matching anatomical landmarks using SlicerIGT extension’s Fiducial Registration Wizard module.</p>

---

## Post #4 by @ddii (2020-02-24 14:06 UTC)

<p>Thank you very much! I will try that. Do you have any video tutorials that I can see?</p>

---

## Post #5 by @ddii (2020-02-24 14:07 UTC)

<p>Thank you very much! I have downloaded the extension. Would you send me the video tutorials if you have one? Thanks,</p>

---

## Post #6 by @lassoan (2020-02-25 18:53 UTC)

<p>You can find tutorials about SlicerIGT modules here: <a href="http://www.slicerigt.org/wp/user-tutorial/">http://www.slicerigt.org/wp/user-tutorial/</a></p>

---
