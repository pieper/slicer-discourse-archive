---
topic_id: 36994
title: "Total Segmentor Ribs Are Incomplete"
date: 2024-06-25
url: https://discourse.slicer.org/t/36994
---

# Total segmentor: ribs are incomplete

**Topic ID**: 36994
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/total-segmentor-ribs-are-incomplete/36994

---

## Post #1 by @Dex2046 (2024-06-25 01:15 UTC)

<p>hi，everyone<br>
I am using total segmentor to get all the bones from the whole body CT, but I found the ribs are imcomplete<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb3cc222223f5b9a8cadf32aa3a07f5fba517d63.png" data-download-href="/uploads/short-url/xz0nxvpyGJYzZEkyrAxaegaqhZ9.png?dl=1" title="0d1a89a494ddc78cc82e388d2d87ce2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb3cc222223f5b9a8cadf32aa3a07f5fba517d63_2_353x500.png" alt="0d1a89a494ddc78cc82e388d2d87ce2" data-base62-sha1="xz0nxvpyGJYzZEkyrAxaegaqhZ9" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb3cc222223f5b9a8cadf32aa3a07f5fba517d63_2_353x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb3cc222223f5b9a8cadf32aa3a07f5fba517d63_2_529x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb3cc222223f5b9a8cadf32aa3a07f5fba517d63.png 2x" data-dominant-color="9D9BAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0d1a89a494ddc78cc82e388d2d87ce2</span><span class="informations">573×811 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e445d3362633fb948254aa47f786c3e4aa1bb1.png" data-download-href="/uploads/short-url/2YOCx9LIdH45skgG8zMwj4HyR8d.png?dl=1" title="09d8d074b8df0f2474259d18e159a2d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14e445d3362633fb948254aa47f786c3e4aa1bb1_2_244x500.png" alt="09d8d074b8df0f2474259d18e159a2d" data-base62-sha1="2YOCx9LIdH45skgG8zMwj4HyR8d" width="244" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14e445d3362633fb948254aa47f786c3e4aa1bb1_2_244x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e445d3362633fb948254aa47f786c3e4aa1bb1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e445d3362633fb948254aa47f786c3e4aa1bb1.png 2x" data-dominant-color="9B9F9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">09d8d074b8df0f2474259d18e159a2d</span><span class="informations">275×562 93.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How could I solve this problem?</p>

---

## Post #2 by @Matteboo (2024-06-25 14:49 UTC)

<p>Hello,<br>
Two ideas:<br>
-Are you running total segmentator on fast mode ? that could explain the loss of some details<br>
-Is the segmentation correct on the slice view ? Maybe it’s a 3D visualisation issue</p>
<p>Also, the segmentation looks good enought to be corrected with some closing/opening on the spine and existing rib segmentation</p>

---

## Post #3 by @Dex2046 (2024-06-26 00:32 UTC)

<p>thank you for help<br>
1.standard mode was  used in segmentation<br>
2.segmentation missing were obvious on slice view<br>
<img src="https://emoji.discourse-cdn.com/twitter/cry.png?v=12" title=":cry:" class="emoji only-emoji" alt=":cry:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2024-06-26 12:00 UTC)

<p>As far as I’ve seen that gap is a limitation that happens consistently.  Maybe it’ll be addressed in future versions.</p>

---

## Post #5 by @Dex2046 (2024-06-27 02:51 UTC)

<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20">，waiting for new versions</p>

---

## Post #6 by @lassoan (2024-06-27 03:15 UTC)

<p>I would recommend to try other segmentation models (e.g., MONAI Auto3DSeg extension). If all models have this error then most likely the models need to be improved with better training data. If this is important for you, then you don’t have to wait for someone else to do the job, you can contribute these improvements yourself. You can contact the maintainers of these AI segmentation models to check if they are planning to work on this and if they would be willing to accept training data improvements from you (or if you can help them in any other way to improve rib segmentation).</p>

---

## Post #7 by @Dex2046 (2024-06-27 03:21 UTC)

<p>Thank you for your suggestion，I’ll try</p>

---

## Post #8 by @tsinesh (2024-06-28 11:38 UTC)

<p>Isn’t that the area where there is naturally no bone but rib cartilage?</p>

---
