---
topic_id: 18500
title: "How To Best Measure Thigh Muscle Volume In At Least Three Di"
date: 2021-07-03
url: https://discourse.slicer.org/t/18500
---

# How to best measure thigh muscle volume in (at least) three different ways

**Topic ID**: 18500
**Date**: 2021-07-03
**URL**: https://discourse.slicer.org/t/how-to-best-measure-thigh-muscle-volume-in-at-least-three-different-ways/18500

---

## Post #1 by @LeoDoc (2021-07-03 18:20 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11</p>
<p>Hello!<br>
For my doctor’s thesis, I am measuring thigh muscle volume, including the femur, adipose tissue and vessels. In my project, I’m supposed to determine the mean value of thigh muscle volume and reference data for about 2000 (+) MRI images. So a lot measuring needs to be done in a fast and valid way.</p>
<p>There seem to be several ways how to measure the muscle volume with 3D-Slicer.<br>
I want to compare the most common three ways to see which one works the most accurate possible while also being the fastest.</p>
<p>There is a tool “fill between slices”, the “threshold-tool” and especially concerning thigh muscle volume, the literature states that it can also be calculated as if the thigh was a cylinder (so height multiplied by the Cross Sectional Area).</p>
<p>I compared the volumes between threshold and fill-between-slices by looking at the lumbar vertebra L4 (as a test) and I’m confused by the numbers I’m getting: threshold: 51.5cm^3 and fill-between-slices with 14.9 cm^3. I feel like 14.9 is more realistic but what am I doing wrong with the threshold-measurement?</p>
<p>My second question concerns the calculation of the “cylinder method” I mentioned. If I take the cross sectional area of (e.g.) L4 alone and multiply it by the height of the vertebra, the value is also nowhere near 14.9 cm^3 (it was also somewhere in the 50’s). I’m assuming I need a different way to evaluate the CSA by finding the thickness of the slice, right?</p>
<p>Are there any webinars or tutorials available to have a look at or are there clearer descriptions about how to measure each and every one of these possibilities to be able to compare them better? Or are the possibly also other ways how to measure muscle volume that I haven’t recognized yet?</p>
<p>Thank You all so much for your help and for everything you do!</p>

---

## Post #2 by @pieper (2021-07-07 16:40 UTC)

<p>You typically cannot use thresholding on MR datasets, so that could explain your volume results.  The volume calculation is done on the segmentation, so you can inspect what’s different between your methods.</p>
<p>If you have 2000 studies you will need something efficient but gives you whatever level of accuracy required for your analysis.  There are a wide range of methods, and so you need to explore the options and pick something that meets your constraints (time available, data quality, accuracy, etc).</p>

---

## Post #3 by @lassoan (2021-07-12 15:05 UTC)

<aside class="quote no-group" data-username="LeoDoc" data-post="1" data-topic="18500">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/f04885/48.png" class="avatar"> LeoDoc:</div>
<blockquote>
<p>I compared the volumes between threshold and fill-between-slices by looking at the lumbar vertebra L4 (as a test) and I’m confused by the numbers I’m getting: threshold: 51.5cm^3 and fill-between-slices with 14.9 cm^3. I feel like 14.9 is more realistic but what am I doing wrong with the threshold-measurement?</p>
</blockquote>
</aside>
<p>The volume that you get is the volume that you see. If you look at the two segment then you should be able to see that the one with the larger volume has larger cross-section and/or taller. You can attach an image if you need help with interpreting the results.</p>
<aside class="quote no-group" data-username="LeoDoc" data-post="1" data-topic="18500">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/f04885/48.png" class="avatar"> LeoDoc:</div>
<blockquote>
<p>My second question concerns the calculation of the “cylinder method” I mentioned. If I take the cross sectional area of (e.g.) L4 alone and multiply it by the height of the vertebra, the value is also nowhere near 14.9 cm^3 (it was also somewhere in the 50’s). I’m assuming I need a different way to evaluate the CSA by finding the thickness of the slice, right?</p>
</blockquote>
</aside>
<p>There is no other way to use to compute volume from cross-sections than the “cylinder method” (multiply cross-section area by height of a slice for each slice) on segmentations represented in binary labelmaps. Slicer uses this method, too.</p>
<p>Note that Segment Statistics module does not report cross-section areas. It always reports volume and surface area for the entire segment, even if the segment is very flat (because it is a single slice only). You can get segment cross-sections from “Segment Cross-Section Area” module (in Sandbox extension).</p>

---

## Post #4 by @LeoDoc (2021-09-22 05:27 UTC)

<p>Thank You guys fpr the answer! I’ll try to apply to apply it to my MRI’s!</p>
<p>Now, there is something else. I got a set of data the other day and successfully uploaded it into slicer and now it’s showing me what you can see in the picture.<br>
How do I transform this view into a 3D-picture?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca6a9daf145c771475646f000ec745dc424a52f4.jpeg" data-download-href="/uploads/short-url/sSES6umhkMY9WkwsvQBf3pcZQSo.jpeg?dl=1" title="MRI of foot to hip joint" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6a9daf145c771475646f000ec745dc424a52f4_2_690x387.jpeg" alt="MRI of foot to hip joint" data-base62-sha1="sSES6umhkMY9WkwsvQBf3pcZQSo" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6a9daf145c771475646f000ec745dc424a52f4_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6a9daf145c771475646f000ec745dc424a52f4_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca6a9daf145c771475646f000ec745dc424a52f4_2_1380x774.jpeg 2x" data-dominant-color="D0D0D0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MRI of foot to hip joint</span><span class="informations">2251×1264 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @pieper (2021-09-22 12:45 UTC)

<p>You can try the techniques shown here: <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Data_Loading_and_3D_Visualization" class="inline-onebox">Documentation/4.10/Training - Slicer Wiki</a></p>

---
