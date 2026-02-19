---
topic_id: 6524
title: "Applying Segmentation Thresholding To Cropped Area Only"
date: 2019-04-17
url: https://discourse.slicer.org/t/6524
---

# Applying segmentation/thresholding to cropped area only

**Topic ID**: 6524
**Date**: 2019-04-17
**URL**: https://discourse.slicer.org/t/applying-segmentation-thresholding-to-cropped-area-only/6524

---

## Post #1 by @tsjamo (2019-04-17 13:35 UTC)

<p>Operating system: Window<br>
Slicer version: 4.10.0</p>
<p>I have a DICOM image of the thigh, and I want to crop the image so I am left with a single “slice” from which I will then use segmentation to calculate CSA of the quadriceps. I thought I had cropped the image to my single slice of interest, but when I use thresholding to segment, it applies it to the whole stack of images.</p>
<p>How can I isolating my segmentation to the single slice I am interested in? Im not sure my cropping has applied to the sagittal and conronal views, despite me dragging the ROI box accordingly to just the area of the single slice I wanted to segment.</p>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2019-04-17 22:46 UTC)

<p>You don’t need to crop the image, just use Segment Editor’s paint or draw effect to segment a single slice. You can then get surface are by using Segment Statistics module. Both sides of the surface is included, so divide the result by 2.</p>
<p>In recent nightly versions of Slicer, we added “closed curve” markup, which will allow cross-section area computation directly from the closed curve, without segmentation. You can already define the curve but it’s area is not reported yet - the area display is expected to be ready within a few weeks.</p>

---

## Post #3 by @tsjamo (2019-04-19 08:57 UTC)

<p>Ok, thank you. So I assume I can’t use the thresholding function on a single slice, I have to paint or draw?</p>

---

## Post #4 by @lassoan (2019-04-19 18:01 UTC)

<p>If you want to fill the entire slice then you can set a large brush size and paint the entire image slice with a single click.</p>

---
