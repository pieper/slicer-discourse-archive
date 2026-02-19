---
topic_id: 30408
title: "Registration Ct Images With Ants Rregistration Or Elastix"
date: 2023-07-05
url: https://discourse.slicer.org/t/30408
---

# Registration CT images with Ants Rregistration or Elastix

**Topic ID**: 30408
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/registration-ct-images-with-ants-rregistration-or-elastix/30408

---

## Post #1 by @Chiararp (2023-07-05 15:04 UTC)

<p>Hi everyone,<br>
I have a problem with the registration of two abdominal CT scans. In particular, the two cases have different sizes and different characteristics that I show below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb55b5b611ed8e51773c3919293cb50f6b212675.jpeg" data-download-href="/uploads/short-url/zRptBwdbOLUEGz1SFi3ckt66Cu9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb55b5b611ed8e51773c3919293cb50f6b212675_2_690x459.jpeg" alt="image" data-base62-sha1="zRptBwdbOLUEGz1SFi3ckt66Cu9" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb55b5b611ed8e51773c3919293cb50f6b212675_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb55b5b611ed8e51773c3919293cb50f6b212675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb55b5b611ed8e51773c3919293cb50f6b212675.jpeg 2x" data-dominant-color="94A093"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">879×585 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My goal is to accurately register the two CT because I want the kidney stones (which are shown in the basal ct) inside the calyxes of the kidney (shown in the late ct).</p>
<p>When I do the registration with Elastix or ANTS registration the result is not accurate.</p>
<p>I show the segmentations of the two volumes to emphasize how the two ct are distant from each other before registration.<br>
(yellow: late, purple: basal)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73d97a38e2a7446b18d98368891e3dea1b3c100a.png" alt="image" data-base62-sha1="gwQQQqihWik3b2PwnQpVssJkkDo" width="515" height="494"><br>
Then I do the registration with Ants registration, rigid+affine (or Elastix, the final result is the same). It’s clear that the registration is not accurate. I show you how the kidney stones are outside the calyxes.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef64ccbbc7da79d33172aae959ac0a963c948d65.jpeg" data-download-href="/uploads/short-url/y9M4Po9KRcOHxNbZ04Ez0J7v4wZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef64ccbbc7da79d33172aae959ac0a963c948d65_2_527x500.jpeg" alt="image" data-base62-sha1="y9M4Po9KRcOHxNbZ04Ez0J7v4wZ" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef64ccbbc7da79d33172aae959ac0a963c948d65_2_527x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef64ccbbc7da79d33172aae959ac0a963c948d65.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef64ccbbc7da79d33172aae959ac0a963c948d65.jpeg 2x" data-dominant-color="8E94BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">577×547 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there something I’m doing wrong? Do you have any suggestions for improving my work? Do I have to do some kind of manual pre-registration?<br>
Thank you all</p>

---
