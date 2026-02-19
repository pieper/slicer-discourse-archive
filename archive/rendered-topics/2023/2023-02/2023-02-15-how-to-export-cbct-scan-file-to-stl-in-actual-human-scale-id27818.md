---
topic_id: 27818
title: "How To Export Cbct Scan File To Stl In Actual Human Scale"
date: 2023-02-15
url: https://discourse.slicer.org/t/27818
---

# How to export CBCT scan file to stl in actual human scale

**Topic ID**: 27818
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/how-to-export-cbct-scan-file-to-stl-in-actual-human-scale/27818

---

## Post #1 by @Prameeth_Maduwantha (2023-02-15 05:34 UTC)

<p>Hi. I need to know how to get human scale dimensions values(mm, cm, feet or whatever)</p>
<p>When Afer exported the .stl file from the 3d slicer, then I imported it into the blender. And it says x:146m y:159m etc<br>
Is there any way to get the dimensions as it is from 3D slicer?</p>

---

## Post #2 by @lassoan (2023-02-15 05:35 UTC)

<p>Are the sizes in Slicer correct (e.g., that you measure using Markups module)?</p>

---

## Post #3 by @Prameeth_Maduwantha (2023-02-15 05:37 UTC)

<p>I need a way to get the sizes from slicer</p>

---

## Post #4 by @lassoan (2023-02-15 05:50 UTC)

<p>You can perform basic measurements (length, diameter, angle, etc.) in Markups module. For surface and volumetric measurements, you can segment the structures using Segment Editor module and get metrics using Segment Statistics module.</p>

---

## Post #5 by @Prameeth_Maduwantha (2023-02-15 05:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="27818">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Markups</p>
</blockquote>
</aside>
<p>Thanks a lot that worked.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/870d02b7c3339b2fe801f94fef4ebee531ecb12c.jpeg" data-download-href="/uploads/short-url/jgIkGsRXeOpuezBzWkCcHgw0gWw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870d02b7c3339b2fe801f94fef4ebee531ecb12c_2_690x455.jpeg" alt="image" data-base62-sha1="jgIkGsRXeOpuezBzWkCcHgw0gWw" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870d02b7c3339b2fe801f94fef4ebee531ecb12c_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870d02b7c3339b2fe801f94fef4ebee531ecb12c_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/870d02b7c3339b2fe801f94fef4ebee531ecb12c.jpeg 2x" data-dominant-color="4A5352"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1360×897 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
