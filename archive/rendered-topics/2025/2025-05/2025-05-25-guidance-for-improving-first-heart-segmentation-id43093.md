# Guidance for improving first heart segmentation

**Topic ID**: 43093
**Date**: 2025-05-25
**URL**: https://discourse.slicer.org/t/guidance-for-improving-first-heart-segmentation/43093

---

## Post #1 by @Sipan_Hovsepian (2025-05-25 19:32 UTC)

<p>Dear Community<br>
This is my first attempt of heart segmentation following the tutorial (<a href="https://www.youtube.com/watch?v=BJoIexIvtGo" rel="noopener nofollow ugc">Link</a>), I found from this community.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba81210cdfa17f90ff5a4471d7914714e8a4072e.jpeg" data-download-href="/uploads/short-url/qBTsYpQuwZQfpoIJxG8lrvyLec6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba81210cdfa17f90ff5a4471d7914714e8a4072e_2_472x500.jpeg" alt="image" data-base62-sha1="qBTsYpQuwZQfpoIJxG8lrvyLec6" width="472" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba81210cdfa17f90ff5a4471d7914714e8a4072e_2_472x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba81210cdfa17f90ff5a4471d7914714e8a4072e_2_708x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba81210cdfa17f90ff5a4471d7914714e8a4072e_2_944x1000.jpeg 2x" data-dominant-color="8E89A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1083×1146 98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would greatly appreciate any feedback for improvement. (maybe increasing the number of seeds, or using some plugins, etc.)<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2025-05-25 19:33 UTC)

<p>I would recommend to try AI segmentation extensions that have heart segmentation models, such as TotalSegmentator and MONAIAuto3DSeg. You can also try NNInteractive interactive AI segmentation tool.</p>

---

## Post #3 by @Sipan_Hovsepian (2025-05-25 20:21 UTC)

<p>Thank you so much!<br>
Is there a link for a tutorial to use them?</p>

---

## Post #4 by @lassoan (2025-05-26 11:53 UTC)

<p>The documentation of each extension should contain a basic tutorial. Let me know if you cannot find them or have problems following them.</p>

---

## Post #5 by @Sipan_Hovsepian (2025-05-26 12:00 UTC)

<p>Thank you for your feedback.<br>
This is a result I got, are there ways I can make it better?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c0100946409c447550c1496b6dbf72828c24abb.jpeg" data-download-href="/uploads/short-url/fprIhbT5nYnAmN600LsHVII1TET.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c0100946409c447550c1496b6dbf72828c24abb_2_473x499.jpeg" alt="image" data-base62-sha1="fprIhbT5nYnAmN600LsHVII1TET" width="473" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c0100946409c447550c1496b6dbf72828c24abb_2_473x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c0100946409c447550c1496b6dbf72828c24abb_2_709x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c0100946409c447550c1496b6dbf72828c24abb_2_946x998.jpeg 2x" data-dominant-color="8E7D9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1174×1240 70.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @connorh (2025-05-31 10:02 UTC)

<p>The totalsegmentator extension has a high-res cardiac chambers segmentation option (license required). If it’s for academic use, I believe you can get the license quite easily and in my experience it has worked fairly well.</p>

---

## Post #7 by @Sipan_Hovsepian (2025-05-31 13:53 UTC)

<p>Thank you so much for your feedback!<br>
I tried that, but my input data was not CTA, and thus maybe the difference was not much.<br>
I would greatly appreciate if you could share an image of a result, if you got realistic one.<br>
Thanks</p>

---
