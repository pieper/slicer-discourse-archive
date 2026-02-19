---
topic_id: 36921
title: "How To Select A Single Slice Scene From Ct Scan And Calculat"
date: 2024-06-20
url: https://discourse.slicer.org/t/36921
---

# How to select a single slice/scene from CT scan and calculate specific segmentation volume stat? 

**Topic ID**: 36921
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/how-to-select-a-single-slice-scene-from-ct-scan-and-calculate-specific-segmentation-volume-stat/36921

---

## Post #1 by @hatcher (2024-06-20 19:33 UTC)

<p>Hi all!</p>
<p>I have currently been using 3D slicer to segment sarcopenia from CT scans. I use the tissue type segmentation task on Total Segmentator Extension and look at the skeletal muscle. I was able to figure out how to calculate the volume of the segmentations in 3D slicer using Segment statistics, but I was wondering if there was a way to capture the volume statistics of the segmentation at a single slice/scene of the CT scan on 3D slicer? As I am looking at sarcopenia, I’m trying to find the volume of segmentation at a particular area of the CT scan (L3). If anyone has any suggestions or solutions or questions, I will gladly elaborate on them, and it will be greatly appreciated!</p>
<p>Thank you for your time !</p>

---

## Post #2 by @lassoan (2024-06-20 19:37 UTC)

<p>You can use the <code>Segment cross-section area</code> module in <code>Sandbox</code> extension to get cross-sectional area of each segment slice-by-slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dab2d680fb92010725335f65d8c624a147ab1d4.jpeg" data-download-href="/uploads/short-url/b55vGsGfknJDQxkzMQD1ovZZvIE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dab2d680fb92010725335f65d8c624a147ab1d4_2_690x362.jpeg" alt="image" data-base62-sha1="b55vGsGfknJDQxkzMQD1ovZZvIE" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dab2d680fb92010725335f65d8c624a147ab1d4_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dab2d680fb92010725335f65d8c624a147ab1d4_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dab2d680fb92010725335f65d8c624a147ab1d4_2_1380x724.jpeg 2x" data-dominant-color="7A7B7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1009 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @hatcher (2024-06-20 23:19 UTC)

<p>Thank you so much! I downloaded the extension and I see the segment cross section area chart display but how do I get the CT scan slices displayed in the left top corner of your image? Also, by using this module, will I be able to save a singular slice with the segmentation and be to calculate the volume from that single slice?</p>
<p>Thank you for your help and time!</p>

---

## Post #4 by @lassoan (2024-06-21 02:40 UTC)

<aside class="quote no-group" data-username="hatcher" data-post="3" data-topic="36921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/f14d63/48.png" class="avatar"> hatcher:</div>
<blockquote>
<p>how do I get the CT scan slices displayed in the left top corner of your image?</p>
</blockquote>
</aside>
<p>Click the eye icon on the side view controller (buttons at the top of slice views).</p>
<aside class="quote no-group" data-username="hatcher" data-post="3" data-topic="36921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/f14d63/48.png" class="avatar"> hatcher:</div>
<blockquote>
<p>by using this module, will I be able to save a singular slice with the segmentation and be to calculate the volume from that single slice?</p>
</blockquote>
</aside>
<p>It is much better than that. You get all the slice cross-sectional areas in a table (git can see it in Tables module or save the scene and open the table in Excel). To get the volume you multiply the surface area with the slice spacing.</p>

---

## Post #5 by @hatcher (2024-06-21 17:26 UTC)

<p>My apologies, how do I find the slice spacing? Is it the difference between the axial positions?</p>
<p>I see that the slice I’m interested in is position S -200 but is that the slice spacing?</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b02c570c0089ff84025060df0a6a0bc4399bd97d.png" data-download-href="/uploads/short-url/p8v22lucrbegaEEqXYytQk2jqzj.png?dl=1" title="Screenshot 2024-06-21 100347" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b02c570c0089ff84025060df0a6a0bc4399bd97d_2_644x500.png" alt="Screenshot 2024-06-21 100347" data-base62-sha1="p8v22lucrbegaEEqXYytQk2jqzj" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b02c570c0089ff84025060df0a6a0bc4399bd97d_2_644x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b02c570c0089ff84025060df0a6a0bc4399bd97d_2_966x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b02c570c0089ff84025060df0a6a0bc4399bd97d.png 2x" data-dominant-color="989687"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-06-21 100347</span><span class="informations">1065×826 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-06-21 18:37 UTC)

<p>You can get the origin of the volume (slice 0 position) and slice spacing (third spacing value) in <code>Volume information</code> section in <code>Volumes</code> module.</p>

---
