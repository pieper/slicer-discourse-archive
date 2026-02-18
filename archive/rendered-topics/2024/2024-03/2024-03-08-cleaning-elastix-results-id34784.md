# Cleaning elastix results

**Topic ID**: 34784
**Date**: 2024-03-08
**URL**: https://discourse.slicer.org/t/cleaning-elastix-results/34784

---

## Post #1 by @Matteboo (2024-03-08 16:21 UTC)

<p>Hello,</p>
<p>I’ve been trying to use elastix to register some organs but I have a few issue.<br>
After registration, the results need “cleaning” (see picture where I registered a liver onto itself)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e2ccb7eb898a973e6ac8fbc6d1ed6911e20a22b.png" data-download-href="/uploads/short-url/mzhpBrvLPE2S04D6HAJOtM40V3d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e2ccb7eb898a973e6ac8fbc6d1ed6911e20a22b_2_690x370.png" alt="image" data-base62-sha1="mzhpBrvLPE2S04D6HAJOtM40V3d" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e2ccb7eb898a973e6ac8fbc6d1ed6911e20a22b_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e2ccb7eb898a973e6ac8fbc6d1ed6911e20a22b_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e2ccb7eb898a973e6ac8fbc6d1ed6911e20a22b.png 2x" data-dominant-color="36353E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1338×719 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I can fix it by doing some closing/dilating.</p>
<p>The issue is that I have other structure inside the organ I want to apply the transform to and I fear that my cleaning is changing the volume.</p>
<p>Has anybody encountered a similar issue ?<br>
Any tips on how to fix this ?</p>

---

## Post #2 by @lassoan (2024-03-08 20:20 UTC)

<p>A warped organ should not look like this. Do you do 3D/3D registration?</p>
<p>Did you apply the transform using Transforms module?</p>
<p>Could you please show the dispacement field (in Transforms module, visualization section) and copy the screenshot here? We would see if the field makes sense (smooth and not folding onto itself).</p>

---

## Post #3 by @Matteboo (2024-03-11 09:05 UTC)

<p>I applied the transform given by elastix using the transform module and I got good results.<br>
I don’t know why the volume given by the elastix module is different.<br>
In my project, I’m calling elastix directly (without going through slicer) and I have the same issue.<br>
Do you know what the transform modul does differently that I could implement on my side.</p>

---

## Post #4 by @lassoan (2024-03-11 12:13 UTC)

<aside class="quote no-group" data-username="Matteboo" data-post="3" data-topic="34784">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p>I don’t know why the volume given by the elastix module is different.</p>
</blockquote>
</aside>
<p>How did you make the Elastix module transform a segment? What inputs and outputs have you specified?</p>

---

## Post #5 by @Matteboo (2024-03-11 12:18 UTC)

<p>I put the same volume as input and output.<br>
It’s a the segmentation of a liver, stocked as a .nii, that I imported in slicer as a volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/946ff997975d8cdc65ea0b14bd75018e79b4f8a8.png" data-download-href="/uploads/short-url/lb8zovvVRyvC0DeTL8GDx2TWAFa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/946ff997975d8cdc65ea0b14bd75018e79b4f8a8_2_447x500.png" alt="image" data-base62-sha1="lb8zovvVRyvC0DeTL8GDx2TWAFa" width="447" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/946ff997975d8cdc65ea0b14bd75018e79b4f8a8_2_447x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/946ff997975d8cdc65ea0b14bd75018e79b4f8a8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/946ff997975d8cdc65ea0b14bd75018e79b4f8a8.png 2x" data-dominant-color="403434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">511×571 51.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I was using the output volume area on for the screenshot I provided in my first message<br>
My guess is that the transform module does some kind of pre/post processing that is absent in the elastix module.</p>

---

## Post #6 by @lassoan (2024-03-11 12:31 UTC)

<p>You cannot choose the same volume as input and output, because you cannot use a label volume directly as fixed or moving volume. The registration would not reliably converge due to large homogeneous regions in the label image. You could compute distance maps from binary images and use thise as registration inputs (this is implemented in <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#segmentation-and-binary-image-registration">Segment Registration</a>) or maybe use some special metric that includes a similar processing (but I don’t know if Elastix provides something like this).</p>

---

## Post #7 by @Matteboo (2024-03-11 13:03 UTC)

<p>I understand your point. However, in practice, Now that I apply the registration with the transform module, everything works well. I’ll look into changing my pipeline to have something more theoretically correct in the fututre.<br>
The issue didn’t seem to come from the transform in itself but from the way it is applied in the elastix module.<br>
Your advice allowed me to find a solution and highlighted potential weak point in my approach, thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @Matteboo (2024-03-15 13:59 UTC)

<p>As suggested by <a class="mention" href="/u/lassoan">@lassoan</a>, the solution to my issue was to apply the transform given by the elastix modul to my volume <strong>using the transform module</strong>.<br>
The cause of the issue seems to be transformix (the part of elastix in charge to apply the transform). The way transformix and the transform module apply the transform are different.<br>
If someone has an explanation of this difference, I’m curious to know.</p>

---
