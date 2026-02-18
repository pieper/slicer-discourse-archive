# Can 3D slicer reach transparency in volume rendering like syngo do?

**Topic ID**: 17329
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/can-3d-slicer-reach-transparency-in-volume-rendering-like-syngo-do/17329

---

## Post #1 by @chendong9416 (2021-04-26 11:04 UTC)

<p>it is crucial for vascular surgeon to confirm the position of intimal tear in aortic dissection even in low quality CTA<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e40e8e9247ea399e44bdbd0be788ec7ff08c437e.png" data-download-href="/uploads/short-url/wxu3bgGIdHNMf0utA1lCindB0tM.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e40e8e9247ea399e44bdbd0be788ec7ff08c437e_2_395x499.png" alt="捕获" data-base62-sha1="wxu3bgGIdHNMf0utA1lCindB0tM" width="395" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e40e8e9247ea399e44bdbd0be788ec7ff08c437e_2_395x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e40e8e9247ea399e44bdbd0be788ec7ff08c437e_2_592x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e40e8e9247ea399e44bdbd0be788ec7ff08c437e.png 2x" data-dominant-color="151517"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">771×975 483 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chendong9416 (2021-04-26 11:07 UTC)

<p>3D reconstruction from segmentation in this case sure can not provide a clear view of intimal tear</p>

---

## Post #3 by @pieper (2021-04-26 14:21 UTC)

<p>It’s probably possible to get similar volume rendering from Slicer with some work.  But I would say that is a pretty high quality CTA and I would not expect you could get a rendering like that from a low quality CTA.</p>

---

## Post #4 by @lassoan (2021-04-26 22:01 UTC)

<p>It looks like a basic volume raycasting with gradient opacity mapping enabled and surrounding stuctures cropped or masked.</p>
<p>Go to volume rendering and set gradient opacity mapping function value to 0 for low values. Also define a cropping region to get rid of surrounding structures. If you need tighter (non-rectangular) cropping then you can use Segment Editor and volume masking.</p>

---

## Post #5 by @chendong9416 (2021-04-26 22:59 UTC)

<p>actually in a better quality CTA，intimal tear can be clearly seen through segmentation and adjust of transparency in 3D view，while in this case, 3D view from segmentation is a mess.</p>

---

## Post #6 by @chendong9416 (2021-04-26 23:00 UTC)

<p>thanks,I will have a try</p>

---
