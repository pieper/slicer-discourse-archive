---
topic_id: 26452
title: "The Slice Views Orientation Are Not Aligned With Segmentatio"
date: 2022-11-26
url: https://discourse.slicer.org/t/26452
---

# The slice views orientation are not aligned with segmentation

**Topic ID**: 26452
**Date**: 2022-11-26
**URL**: https://discourse.slicer.org/t/the-slice-views-orientation-are-not-aligned-with-segmentation/26452

---

## Post #1 by @kylin (2022-11-26 09:23 UTC)

<p>Hi,<br>
The mask appeared in adjacent slices when I was drawing a segmentation in one slice, so I can’t draw a segmentation exactly. I know there is a button in the right side of segmentation that can solve the problem. However, I couldn’t find it today when I add a new segmentation. How to solve this problem?<br>
Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04df638e8ce347efcc3c09de05d3ef3ff4d9f450.jpeg" data-download-href="/uploads/short-url/H6w8EnRLnBX5nndz0OxgYKUhEY.jpeg?dl=1" title="微信图片_20221126171841" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04df638e8ce347efcc3c09de05d3ef3ff4d9f450_2_389x499.jpeg" alt="微信图片_20221126171841" data-base62-sha1="H6w8EnRLnBX5nndz0OxgYKUhEY" width="389" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04df638e8ce347efcc3c09de05d3ef3ff4d9f450_2_389x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04df638e8ce347efcc3c09de05d3ef3ff4d9f450_2_583x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04df638e8ce347efcc3c09de05d3ef3ff4d9f450_2_778x998.jpeg 2x" data-dominant-color="ACADAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20221126171841</span><span class="informations">1448×1860 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-11-26 16:00 UTC)

<p>By default, orientation of slice views are aligned with axes of the segmented image. The warning button is only displayed if they are not aligned.</p>

---

## Post #3 by @kylin (2022-11-27 08:34 UTC)

<p>Thank you, Lasso! It worked after I restarted the computer.</p>

---

## Post #4 by @kylin (2022-11-27 09:15 UTC)

<p>Sorry, the problem still existed when I loaded another series of MRI images. Although the warning button didn’t show up, they seemed to be not aligned. When I use the level tracing to draw a segmentation, the area with yellow border was selected automatically, but the final segmentation was the whole green area when I click the mouse, and the segmentations on adjacent slices were also affected. What was the reason for that?</p>

---

## Post #5 by @kylin (2022-11-27 09:16 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79c327f8f80535703e2909568a2912c799bdb572.jpeg" data-download-href="/uploads/short-url/hn9TqENvB1E6yI3PIPXiFpEWyBA.jpeg?dl=1" title="20221127165953" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c327f8f80535703e2909568a2912c799bdb572_2_576x500.jpeg" alt="20221127165953" data-base62-sha1="hn9TqENvB1E6yI3PIPXiFpEWyBA" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c327f8f80535703e2909568a2912c799bdb572_2_576x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c327f8f80535703e2909568a2912c799bdb572_2_864x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c327f8f80535703e2909568a2912c799bdb572_2_1152x1000.jpeg 2x" data-dominant-color="A4A4A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20221127165953</span><span class="informations">1272×1104 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2022-11-27 16:20 UTC)

<p>Please use the latest Slicer Stable Release or Slicer Preview Release and let us know if Slicer still behaves differently than you expect.</p>

---

## Post #7 by @kylin (2022-11-28 11:01 UTC)

<p>I tried the latest Stable Release version 5.0.3, but the problem happened sometimes.</p>

---

## Post #8 by @lassoan (2022-11-28 14:27 UTC)

<p>The rotate warning button appears if any of thr views are not aligned with the axes of the segmentation when you switch to any effect.</p>

---

## Post #9 by @AKue (2023-09-25 07:23 UTC)

<p>Hello!<br>
Is there a way to use “level tracing” when slice views orientation are NOT aligned with segmentation?</p>

---
