---
topic_id: 19643
title: "Selecting A Denoising Filter For A Ct"
date: 2021-09-13
url: https://discourse.slicer.org/t/19643
---

# Selecting a denoising filter for a CT

**Topic ID**: 19643
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/selecting-a-denoising-filter-for-a-ct/19643

---

## Post #1 by @mau_igna_06 (2021-09-13 12:52 UTC)

<p>In my application I need to detect spineContactPoint over a line that goes through the spine. For this I check until HU value is over 200 but this could fail because there are random sparce voxels with HU value 200 as you can see in this picture of thresholding (with 200HU lower limit):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f7286fedcc5acc7480f2a645af19b0ada01cbd0.png" alt="threshold_noisy_ct" data-base62-sha1="ksZEq3oZuHaLdBzybIUty9M0P8Q" width="411" height="284"></p>
<p>So I though I have to use a denoising filter. I tried “Gradient anisotropic diffusion” and it worked well but there are four denoising algorithms. What of these four filter is recommended for my use case? Thanks</p>

---

## Post #2 by @pieper (2021-09-13 14:21 UTC)

<p>It’s very hard to get a filter to clean up data like that reliably and there are many parameters that interact in nonlinear fashion.  You might be better off trying a segmentation filter.  <a class="mention" href="/u/lassoan">@lassoan</a> pointed to this work and said he had good results.  <a class="mention" href="/u/Ron">@Ron</a> also tested it on clinical data and reported good experience so it might work for you as well: <a href="https://deep-spine.de/">https://deep-spine.de/</a>.  There’s interest in working with this model based on <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/SpineSegmentation/">what was done at Project Week</a>.</p>

---

## Post #3 by @lassoan (2021-09-13 14:50 UTC)

<p>I agree that you need a shape model/neural network for fully automatic spine segmentation or if you want to separate vertebrae.</p>
<p>However, if you just need a clean posterior surface for creating a surgical guide then running a non-linear filter (such as a simple median filter) on the image that you showed above should be sufficient. If you need to fill internal holes then you can use <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfceWrapSolidify</a> extension for the region of interest.</p>

---

## Post #4 by @mau_igna_06 (2021-09-13 15:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="19643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, if you just need a clean posterior surface for creating a surgical guide then running a non-linear filter (such as a simple median filter) on the image that you showed above should be sufficient</p>
</blockquote>
</aside>
<p>I just need the area posterior to the spine to be denoised.<br>
Then I detect when I have the spineContactPoint checking when the HU value of the CT is above 200 over a line that goes through the spine. Then I segment the whole spine automatically using localThreshold with spineContactPoint as seed. It works well most of the times but it could fail due to noise.<br>
I just wanted to know what is the most convenient denoising filter for this use case. But I’ll use the median filter since you recommended it. Thanks</p>
<p>Edit: to give more context the line I use for bone detection comes from a planned pedicleScrew.<br>
After I segment the spine with localThreshold, I make a shell with hollow effect and the paint the guideBases using the hollowSegment as mask</p>

---
