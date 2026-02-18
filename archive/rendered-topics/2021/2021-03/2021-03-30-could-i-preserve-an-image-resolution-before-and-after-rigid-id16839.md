# Could I preserve an image resolution before and after Rigid registration?

**Topic ID**: 16839
**Date**: 2021-03-30
**URL**: https://discourse.slicer.org/t/could-i-preserve-an-image-resolution-before-and-after-rigid-registration/16839

---

## Post #1 by @Yasuhiro_TAKEDA (2021-03-30 03:17 UTC)

<p>Hi</p>
<p>I registered two head MRI images, a T2 and a CET1 image, using General Registration function with rigid.<br>
The registration was succeeded, but the output image resolution has changed.<br>
The image resolution of the CET1 image, which was the moving image, was 1×1×1.5 mm, however this has changed to 0.5×0.5×3 mm after rigid registration, which was corresponded with the image resolution of the fixed image.</p>
<p>Could I preserve an image resolution before and after Rigid registration?</p>
<p>Thank you,</p>

---

## Post #2 by @muratmaga (2021-03-30 03:40 UTC)

<p>The whole point of the image registration is to resample the moving image into the reference image’s domain. If your moving image has a lower resolution, and your reference has higher, your moving image will be matched to your reference’s one.</p>
<p>Perhaps you can reduce the resolution in your reference to match that of moving image prior to registration, and then try to register.</p>
<p>Or you take the resultant output image and use the ResampleScalarImage to bring to whatever voxel spacing you want.</p>

---

## Post #3 by @Yasuhiro_TAKEDA (2021-03-30 23:01 UTC)

<p>Thank you for your reply.</p>
<p>I misunderstood the point of image registration.</p>
<p>Actually, I often used Amira, an image processing soft from Thermo Fisher.<br>
Amira keeps a resolution before and after an image registration.</p>
<p>Is Amira an excption?</p>

---

## Post #4 by @muratmaga (2021-03-31 02:10 UTC)

<aside class="quote no-group" data-username="Yasuhiro_TAKEDA" data-post="3" data-topic="16839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yasuhiro_takeda/48/9537_2.png" class="avatar"> Yasuhiro_TAKEDA:</div>
<blockquote>
<p>Amira keeps a resolution before and after an image registration.</p>
</blockquote>
</aside>
<p>I can’t say how Amira does it, but if the reference image has a different spacing that the moving image and after registration the resultant image still preserves original image spacing, yes, I would say it is different than the image registration frameworks that I am familiar with. At least for deformable ones.</p>
<p>With rigid, you can choose to output a transform (as oppose to a new image), and then apply that affine transform to the original moving image. That shouldn’t change the image resolution.</p>

---

## Post #5 by @Yasuhiro_TAKEDA (2021-03-31 07:24 UTC)

<p>OK.<br>
I really appreciate for your help!!</p>

---
