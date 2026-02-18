# How to segment muscle in TotalSegmentator

**Topic ID**: 29425
**Date**: 2023-05-12
**URL**: https://discourse.slicer.org/t/how-to-segment-muscle-in-totalsegmentator/29425

---

## Post #1 by @jay1987 (2023-05-12 09:51 UTC)

<p>i use total segmentator to segment ct , the result is<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cb9f4899e25bf6e6f1147c98e66fff936de9e75.jpeg" alt="image" data-base62-sha1="k4VfGTyUfT6XG52R1qqiEyyPfRr" width="659" height="446"></p>
<p><strong>the doctor want to segment the muscule into the red area and the yellow area</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64e2b099b7ee9592ea42990ca60b31193e3f4be0.jpeg" data-download-href="/uploads/short-url/eotqwsuUr4R1pQ0XtKGW6Mg75ao.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64e2b099b7ee9592ea42990ca60b31193e3f4be0.jpeg" alt="image" data-base62-sha1="eotqwsuUr4R1pQ0XtKGW6Mg75ao" width="690" height="355" data-dominant-color="73705D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">950×490 34.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>use total segmentator seems can’t Meeting the needs of doctors(Maybe the steps I used were incorrect) , Is there any way to meet the needs of doctors?</p>

---

## Post #2 by @pieper (2023-05-12 19:03 UTC)

<p>I don’t know if there are any models available yet for this case.  Maybe someone can speak up if they know of any.</p>
<p>As discussed in <a href="https://discourse.slicer.org/t/anyone-know-how-to-read-analyze-objectmap-files/29074/7">this thread</a> I’m hoping we’ll be able to make a MONAI Label or nnU-Net model based on some representative segmentations, but that’s still research.</p>
<p>If anyone has lots of ground truth segmentations they want to make available that could help.</p>

---

## Post #3 by @jay1987 (2023-05-13 13:59 UTC)

<p>thank you pieper,maybe MONAI label is a good choice</p>

---
