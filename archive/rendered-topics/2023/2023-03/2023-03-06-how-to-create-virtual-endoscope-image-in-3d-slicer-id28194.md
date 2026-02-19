---
topic_id: 28194
title: "How To Create Virtual Endoscope Image In 3D Slicer"
date: 2023-03-06
url: https://discourse.slicer.org/t/28194
---

# How to create virtual endoscope image in 3d slicer

**Topic ID**: 28194
**Date**: 2023-03-06
**URL**: https://discourse.slicer.org/t/how-to-create-virtual-endoscope-image-in-3d-slicer/28194

---

## Post #1 by @kionde (2023-03-06 14:03 UTC)

<p>Hi,I’m a beginner of 3D slicer.I’d like to know if I can create virtual endoscope images like this in 3D slicer？Can you help me to explain the question. Thank you very much!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c25db7aa26dec4ab7f68dca1ee226f3e30d5fb7.png" data-download-href="/uploads/short-url/6iy7ilDES8REQLXPRHWI8slR4iz.png?dl=1" title="virtual endoscope" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c25db7aa26dec4ab7f68dca1ee226f3e30d5fb7_2_453x499.png" alt="virtual endoscope" data-base62-sha1="6iy7ilDES8REQLXPRHWI8slR4iz" width="453" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c25db7aa26dec4ab7f68dca1ee226f3e30d5fb7_2_453x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c25db7aa26dec4ab7f68dca1ee226f3e30d5fb7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c25db7aa26dec4ab7f68dca1ee226f3e30d5fb7.png 2x" data-dominant-color="422D2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">virtual endoscope</span><span class="informations">528×582 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @RafaelPalomar (2023-03-06 14:12 UTC)

<p>3D Slicer has an Endoscopy module (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/endoscopy.html" class="inline-onebox" rel="noopener nofollow ugc">Endoscopy — 3D Slicer documentation</a>) that can help you with this.</p>

---

## Post #3 by @kionde (2023-03-06 14:18 UTC)

<p>I’m very glad to see your reply!But this page can’t be found.</p>

---

## Post #4 by @RafaelPalomar (2023-03-06 14:26 UTC)

<p>Sorry. I edited the answer with the right link.</p>

---

## Post #5 by @kionde (2023-03-06 14:34 UTC)

<p>I tried endoscopy on my model but it turned out like this.Is there anything wrong with my model?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa585d11edabce2be8abf8a04d65b07b7948e697.jpeg" data-download-href="/uploads/short-url/zIEGvERxEAvRU3i8q8kUDJ4Eq4n.jpeg?dl=1" title="endoscopy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa585d11edabce2be8abf8a04d65b07b7948e697_2_690x412.jpeg" alt="endoscopy" data-base62-sha1="zIEGvERxEAvRU3i8q8kUDJ4Eq4n" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa585d11edabce2be8abf8a04d65b07b7948e697_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa585d11edabce2be8abf8a04d65b07b7948e697_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa585d11edabce2be8abf8a04d65b07b7948e697_2_1380x824.jpeg 2x" data-dominant-color="B0B2C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">endoscopy</span><span class="informations">1920×1148 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @RafaelPalomar (2023-03-07 07:52 UTC)

<p>From the picture I understand that you have done a sort of segmentation for the centerline and placed a fiducial. I would think you need a better way to define your fiducials along the centerline. You can try the suggestions given by <a class="mention" href="/u/lassoan">@lassoan</a> in this post (<a href="https://discourse.slicer.org/t/virtual-bronchoscopy/7468/7" class="inline-onebox">Virtual Bronchoscopy - #7 by lassoan</a>) for extraction of the centerline as a curve and giving this as an input to the Endoscopy module.</p>

---

## Post #7 by @kionde (2023-03-08 14:20 UTC)

<p>Thank you for your reply!I will keep learning and try it later.</p>

---
