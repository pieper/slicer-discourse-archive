---
topic_id: 33764
title: "Shape Analysis Error"
date: 2024-01-14
url: https://discourse.slicer.org/t/33764
---

# Shape analysis error

**Topic ID**: 33764
**Date**: 2024-01-14
**URL**: https://discourse.slicer.org/t/shape-analysis-error/33764

---

## Post #1 by @anasmh101 (2024-01-14 03:00 UTC)

<p>I have problem in shape analysis module,  I am doing shape analysis for mandible condyles pre/post operative, in many cases after doing the shape analysis, the output shape population viewer show flipped models as shown in screen shot, although I made sure that the segmentation models are completely closed and no holes or gaps in the segmentations after cropping, but still get same flipped models, after many trials. I opted to make new segmentations for the condyles but still get same flipped output models after performing shape analysis<br>
( <strong>this issue happens for one sided condyles, For example,  the problem is happening for left condyles models, while right condyles models taken from the exact same mandible segmentation have no problem at all in shape analysis result)</strong><br>
what am I doing wrong or missing ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1faccbd9a15cc3ad7c9b83e3b2c4d303ea25edf1.png" data-download-href="/uploads/short-url/4wd0ZdO0XVabHICjOdfzY4EfKG5.png?dl=1" title="error in condyle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1faccbd9a15cc3ad7c9b83e3b2c4d303ea25edf1_2_690x286.png" alt="error in condyle" data-base62-sha1="4wd0ZdO0XVabHICjOdfzY4EfKG5" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1faccbd9a15cc3ad7c9b83e3b2c4d303ea25edf1_2_690x286.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1faccbd9a15cc3ad7c9b83e3b2c4d303ea25edf1_2_1035x429.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1faccbd9a15cc3ad7c9b83e3b2c4d303ea25edf1.png 2x" data-dominant-color="443440"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error in condyle</span><span class="informations">1112×462 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b.png" data-download-href="/uploads/short-url/4dTtefRTyaAa1JIsXQQMDiwKNWX.png?dl=1" title="shape analysis error2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b_2_690x281.png" alt="shape analysis error2" data-base62-sha1="4dTtefRTyaAa1JIsXQQMDiwKNWX" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b_2_1035x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9ac8e5af59c1f50cacc4ceb5f90b6fc271781b.png 2x" data-dominant-color="402F3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">shape analysis error2</span><span class="informations">1127×460 90.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @anasmh101 (2024-01-14 04:43 UTC)

<p>this is what is shown on the python console when the output of shape analysis is flipped unaligned models<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e2bf03c25ba8b0f9a2b0a48e8335f341e3f7333.png" data-download-href="/uploads/short-url/21mOYAbWb2zcfc6W4ob9Nj6fQS7.png?dl=1" title="python for error condyle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e2bf03c25ba8b0f9a2b0a48e8335f341e3f7333.png" alt="python for error condyle" data-base62-sha1="21mOYAbWb2zcfc6W4ob9Nj6fQS7" width="690" height="121" data-dominant-color="FEEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">python for error condyle</span><span class="informations">1543×272 18.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2024-01-14 06:00 UTC)

<p>You have some non-ascii characters, and extremely long file path that might cause the reported write issue. I would first try with a simpler path, without any non-english characters and see if it works.</p>

---

## Post #4 by @anasmh101 (2024-01-14 08:14 UTC)

<p>thank you for you reply, this is the python script I got with simpler path, same result flipped output models<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/893044d678fa08200eb4c06198d4577b7065fd86.png" data-download-href="/uploads/short-url/jzCPp0NSeMIambSiR3ZLl4HChHo.png?dl=1" title="python script 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/893044d678fa08200eb4c06198d4577b7065fd86.png" alt="python script 2" data-base62-sha1="jzCPp0NSeMIambSiR3ZLl4HChHo" width="690" height="94" data-dominant-color="FEF7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">python script 2</span><span class="informations">1103×151 4.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @anasmh101 (2024-01-14 08:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17f16d6326921c60e60bd851b30449244a665eff.png" data-download-href="/uploads/short-url/3pOeIC3hWRTzqsNHv2QhDLBIeir.png?dl=1" title="python script 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17f16d6326921c60e60bd851b30449244a665eff.png" alt="python script 3" data-base62-sha1="3pOeIC3hWRTzqsNHv2QhDLBIeir" width="690" height="50" data-dominant-color="FEF5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">python script 3</span><span class="informations">1876×138 7.85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @anasmh101 (2024-01-14 08:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/082314c0ed3b23df11f2535a043b5946a5ecd4b9.png" data-download-href="/uploads/short-url/19YYNs5ijNEPNxvf7cpyG7ixseJ.png?dl=1" title="pythone script 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/082314c0ed3b23df11f2535a043b5946a5ecd4b9.png" alt="pythone script 4" data-base62-sha1="19YYNs5ijNEPNxvf7cpyG7ixseJ" width="690" height="191" data-dominant-color="FEF1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pythone script 4</span><span class="informations">783×217 6.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @anasmh101 (2024-01-14 16:30 UTC)

<p>the previous shape analysis screenshots taken from slicer operated on windows, this one is done on Macbook<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/419f00c595a4c2da90fbd46e9dd5a8f45a8c2fc0.jpeg" data-download-href="/uploads/short-url/9mvHgZcekvPp2cFT8RRrRHGYqKk.jpeg?dl=1" title="WhatsApp Image 2024-01-15 at 00.05.39_d5bed559" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/419f00c595a4c2da90fbd46e9dd5a8f45a8c2fc0_2_690x431.jpeg" alt="WhatsApp Image 2024-01-15 at 00.05.39_d5bed559" data-base62-sha1="9mvHgZcekvPp2cFT8RRrRHGYqKk" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/419f00c595a4c2da90fbd46e9dd5a8f45a8c2fc0_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/419f00c595a4c2da90fbd46e9dd5a8f45a8c2fc0_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/419f00c595a4c2da90fbd46e9dd5a8f45a8c2fc0_2_1380x862.jpeg 2x" data-dominant-color="B5A7B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-01-15 at 00.05.39_d5bed559</span><span class="informations">1600×1000 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
