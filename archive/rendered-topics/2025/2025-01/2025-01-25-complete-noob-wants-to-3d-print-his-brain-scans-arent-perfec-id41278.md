---
topic_id: 41278
title: "Complete Noob Wants To 3D Print His Brain Scans Arent Perfec"
date: 2025-01-25
url: https://discourse.slicer.org/t/41278
---

# Complete noob wants to 3d print his brain. Scans aren't perfect. Help?

**Topic ID**: 41278
**Date**: 2025-01-25
**URL**: https://discourse.slicer.org/t/complete-noob-wants-to-3d-print-his-brain-scans-arent-perfect-help/41278

---

## Post #1 by @Snoochers (2025-01-25 10:54 UTC)

<p>Hi. I have DICOM files of my brain. There’s a lot of scans in there but many wouldn’t be suitable for a 3D model I think. The best scans seem to be 26 slices going ear to ear and 33 slices going top of head to bottom. I don’t seem to have any scans with several clear front to back slices.</p>
<p>Can a good 3D model be generated simply from the two planes?</p>
<p>There’s an additional issue that the two good groups of slices are from two separate scans it seems like. They’re not in the same line of data when I load it in 3D slicer. In other words, the good slices are paired with blurry slices from the two other planes.</p>
<p>If the 2 plains are enough, how can I combine them? The software seems a bit complicated and I could use some handholding. Or perhaps someone would be kind enough to do it for me if I send them the files?</p>
<p>I found a youtube video tutorial on how to extract scans for 3D printing but unfortunately the tutorial assumes good scans</p>

---

## Post #2 by @AlexBaev (2025-01-26 08:20 UTC)

<p>Can I see your DICOM? I’ve already done the head, the bones. I can look at your brain.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9045cc90687d7441601d8a0c9dddeb10fd9c4621.jpeg" data-download-href="/uploads/short-url/kAiizAsj7TFYheYlwZ2X4CfYTHb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9045cc90687d7441601d8a0c9dddeb10fd9c4621_2_690x463.jpeg" alt="image" data-base62-sha1="kAiizAsj7TFYheYlwZ2X4CfYTHb" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9045cc90687d7441601d8a0c9dddeb10fd9c4621_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9045cc90687d7441601d8a0c9dddeb10fd9c4621_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9045cc90687d7441601d8a0c9dddeb10fd9c4621.jpeg 2x" data-dominant-color="848282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1286×864 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a href="mailto:a46779935b@mail.ru">a46779935b@mail.ru</a></p>

---

## Post #3 by @Snoochers (2025-01-26 14:42 UTC)

<p>Thank you. I sent the DICOM to the listed email.</p>

---

## Post #4 by @AlexBaev (2025-01-29 08:26 UTC)

<p>good day! slices are really not enough to get a quality image. I understand that you want to combine coronal, axial and sagital to get better quality? Here is a link why this cannot be done in Slicer.</p><aside class="quote quote-modified" data-post="1" data-topic="41310">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c67d28/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-integrate-the-dicom-data-from-3-series/41310">How to integrate the dicom data from 3 series</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am trying to evaluate bone quality using the bone texture module of 3d slicer software (ver.5.6.2) from pre- and post-operative CT scans of a certain surgery. 
However, not just with 3d slicer, but I am having trouble with axial, coronal, and sagital CT images not being displayed in series. 
To be more specific, dicom data a displays axial images clearly, but the resolution of coronal and sagital images becomes very low, and with dicom data b, coronal images are displayed clearly, but t…
  </blockquote>
</aside>
<p>
Theoretically, this can be done in other 3D programs.<br>
Here is what I managed to do in Slicer = axial.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee98126e397e91e23f96a5dbcd379a4a5c3f714e.jpeg" data-download-href="/uploads/short-url/y2HrWxlmvlAaAWBzcyNxCvNry5U.jpeg?dl=1" title="02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee98126e397e91e23f96a5dbcd379a4a5c3f714e_2_622x500.jpeg" alt="02" data-base62-sha1="y2HrWxlmvlAaAWBzcyNxCvNry5U" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee98126e397e91e23f96a5dbcd379a4a5c3f714e_2_622x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee98126e397e91e23f96a5dbcd379a4a5c3f714e_2_933x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee98126e397e91e23f96a5dbcd379a4a5c3f714e.jpeg 2x" data-dominant-color="4F4F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02</span><span class="informations">1217×978 48.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Snoochers (2025-01-30 14:41 UTC)

<p>So I should forget the idea of 3D printing my brain? I thought the slices looked pretty good…</p>

---
