---
topic_id: 40123
title: "Why Did The Segment Created By Threshold Masking Contain Vox"
date: 2024-11-11
url: https://discourse.slicer.org/t/40123
---

# Why did the segment created by threshold masking contain voxels beyond the threshold?

**Topic ID**: 40123
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/why-did-the-segment-created-by-threshold-masking-contain-voxels-beyond-the-threshold/40123

---

## Post #1 by @qmsyylsel (2024-11-11 15:11 UTC)

<p>As the pictures shows, in Segment Editor, I painted my segment under the masking with a threshold of &gt;130. But in Segment Statistics, the minimum value of that segment was 85, which was lower than 130, the threshold I set.</p>
<p>Would it be possible for anyone to tell me why this happened? And how can I get a segment without voxels out of the range I set? Many thanks in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/870448b0d1b7501dca6e5873ff238f1dd9d112c0.jpeg" data-download-href="/uploads/short-url/jgpDtXHtbDbO68fOLpiUgNtzlfO.jpeg?dl=1" title="结果1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870448b0d1b7501dca6e5873ff238f1dd9d112c0_2_690x466.jpeg" alt="结果1" data-base62-sha1="jgpDtXHtbDbO68fOLpiUgNtzlfO" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870448b0d1b7501dca6e5873ff238f1dd9d112c0_2_690x466.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870448b0d1b7501dca6e5873ff238f1dd9d112c0_2_1035x699.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870448b0d1b7501dca6e5873ff238f1dd9d112c0_2_1380x932.jpeg 2x" data-dominant-color="C2C2C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">结果1</span><span class="informations">1396×944 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5ff789d1643be43a83c933e0b1c4173f62448c85.jpeg" data-download-href="/uploads/short-url/dGXHUbpaCkOdIFg7UYgvOGOp25L.jpeg?dl=1" title="结果2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5ff789d1643be43a83c933e0b1c4173f62448c85.jpeg" alt="结果2" data-base62-sha1="dGXHUbpaCkOdIFg7UYgvOGOp25L" width="592" height="488"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">结果2</span><span class="informations">592×488 27.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-11-11 16:59 UTC)

<p>You have multiple segments, but your table does not show from which segment the stat is coming from. Perhaps you are looking at the wrong segment?</p>

---

## Post #3 by @lassoan (2024-11-11 18:33 UTC)

<p>Minimum and maximum are extremely sensitive. Out of millions of voxels, a fraction of a single voxel can change the result. You can have uncertainties about what parts of a voxel considered to be part of segmentation when the geometry (origin, spacing, axis directions, extents) is not exactly for the same for the segmentation, the scalar volume you thresholded, and the scalar volume you chose for statistics computation.</p>
<p>If you want to use minimum and maximum values then I would recommend to make conservative estimations, for example by applying Margin effect to erode/dilate the segments to ensure voxels near the segmentation boundary are excluded/included according to your requirements.</p>
<p>I’ve also added the <a href="https://github.com/Slicer/Slicer/pull/8037">option to compute 5th and 95th percentiles</a>, which characterize the value range of a segment more robustly than minimum and maximum values.</p>

---

## Post #4 by @qmsyylsel (2024-11-15 14:30 UTC)

<p>Thanks for your reply. I double-checked and confirmed that I was looking at the same segment. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @qmsyylsel (2024-11-15 14:32 UTC)

<p>Thanks for your reply. This looks like the answer to my question and I will try your advice!</p>

---
