---
topic_id: 11860
title: "Editing Roi Through Segment Editor"
date: 2020-06-04
url: https://discourse.slicer.org/t/11860
---

# Editing ROI through segment editor

**Topic ID**: 11860
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/editing-roi-through-segment-editor/11860

---

## Post #1 by @RadioQuest (2020-06-04 13:15 UTC)

<p>Hi…<br>
I am using 2D circles to draw an ROI of particular radius. However after registration , it appears to be at bit different position in the subsequent scan. Is it possible to move this ROI?<br>
I could not find the tools. Only option I could think of erasing and drawing new one.<br>
Thanks in advance. This community is really very supporting.<br>
Thanks.<br>
Kind Regards,<br>
R</p>

---

## Post #2 by @lassoan (2020-06-04 13:50 UTC)

<p>If you want segmentation to move with the registered volume, apply the computed transform to the segmentation node, too.</p>

---

## Post #3 by @RadioQuest (2020-06-08 12:40 UTC)

<p>Thank you for your reply.<br>
Can I move individual 2D circle ROI in the image?</p>

---

## Post #4 by @lassoan (2020-06-08 14:11 UTC)

<p>If you want to move a single segment only then you have to move the segment temporarily into a new segmentation, transform that segmentation, then move the segment back to the original segmentation. You can move segments between segmentations using Segmentations module.</p>

---

## Post #5 by @Alexis_Codazzi (2020-10-15 22:39 UTC)

<p>Hi eveyone!<br>
How can I make the segmentation move with the volume recorded by bspline transform?</p>

---

## Post #6 by @lassoan (2020-10-15 23:36 UTC)

<p>You can transform a segmentation the same way as any other nodes, by applying a transform to it. If you use latest Slicer Stable Release, then you can apply a transform in Data module by right-clicking on the transform column of a node and choosing the transform.</p>
<p>If you apply the same transform to an image and segmentation then they will move together whenever the transform is changed.</p>

---

## Post #7 by @Alexis_Codazzi (2020-10-16 00:18 UTC)

<p>Thank you. I want to apply Output BSpline transform to RTSTRUCT: HDR where I have segmented organs. I show screenshot.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91f881011825a907893d9f29ba40eab8366ab84f.png" data-download-href="/uploads/short-url/kPjEkbZT2gH8M7MqBtX8Web1hvx.png?dl=1" title="Sin título" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f881011825a907893d9f29ba40eab8366ab84f_2_690x387.png" alt="Sin título" data-base62-sha1="kPjEkbZT2gH8M7MqBtX8Web1hvx" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f881011825a907893d9f29ba40eab8366ab84f_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f881011825a907893d9f29ba40eab8366ab84f_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91f881011825a907893d9f29ba40eab8366ab84f.png 2x" data-dominant-color="A7A8AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título</span><span class="informations">1366×768 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-10-16 00:38 UTC)

<p>As I wrote above, right-click on the transform column and choose the transform you want to apply:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ed34de67042fe339ce1b43d902a336561e8c6c3.jpeg" data-download-href="/uploads/short-url/8XMjS902ezS2DZL1eO8aZz6DhTB.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ed34de67042fe339ce1b43d902a336561e8c6c3_2_690x350.jpeg" alt="image" data-base62-sha1="8XMjS902ezS2DZL1eO8aZz6DhTB" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ed34de67042fe339ce1b43d902a336561e8c6c3_2_690x350.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ed34de67042fe339ce1b43d902a336561e8c6c3_2_1035x525.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ed34de67042fe339ce1b43d902a336561e8c6c3.jpeg 2x" data-dominant-color="B6AE9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1044×530 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Use latest Slicer Stable Release.</p>

---

## Post #9 by @Alexis_Codazzi (2020-10-16 21:30 UTC)

<p>Thank you Andras.<br>
One last question. I use platismatch Bspline Deformable Registration with two CTs, one as a reference image and the other as a moving image, each one was segmented. After applying the deformable registration I got a deformable image as output and I need to know the change in volumes of the segments before and after applying the registration.</p>

---

## Post #10 by @lassoan (2020-10-17 01:55 UTC)

<p>After you apply a transform to the segmentation node you can compute segment volumes using Segment Statistics module.</p>

---

## Post #11 by @Alexis_Codazzi (2020-10-20 17:04 UTC)

<p>Thank You Andre  for your answer. I want to calculate the Jacobian determinant of the segments with the SlicerRegistration QA module to determine if the deformed segments got bigger or smaller after applying the deformable registration. I was able to visualize that the deformed segments are larger and the Jacobian determinant is always zero. Could it be a problem due to the ROI determined by the module?</p>

---

## Post #12 by @lassoan (2020-10-20 17:17 UTC)

<p>If you want to determine if a segment was shrunk or expanded then total volume is the most accurate and robust metric.If you are interested in local changes then you can export the segments to surfaces and use ModelToModelDistance extension.</p>
<p>I don’t know RegistrationQA module well and the authors of the extension do not seem to follow the discussions here, so you can write your question to the contact email address of this extension (<a href="https://github.com/gsi-biomotion/SlicerRegistrationQA">https://github.com/gsi-biomotion/SlicerRegistrationQA</a>) or submit an issue in the extension’s repository.</p>

---
