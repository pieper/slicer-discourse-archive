---
topic_id: 20421
title: "Segment Statistics For Each Slice Of Segmented Volume"
date: 2021-10-30
url: https://discourse.slicer.org/t/20421
---

# Segment statistics for each slice of segmented volume

**Topic ID**: 20421
**Date**: 2021-10-30
**URL**: https://discourse.slicer.org/t/segment-statistics-for-each-slice-of-segmented-volume/20421

---

## Post #1 by @Michel_Atieh (2021-10-30 12:24 UTC)

<p>Hello,<br>
to calculate the radiation dose received by the fetus during a CT exam, I need to know the mean Hounsfield Unit for each slice of my segmented volume (the uterus). However, I am only able to obtain statistics for the whole segmented volume. I need to know the same information but for each slice.<br>
Is there any way to do so?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2021-10-30 13:34 UTC)

<p>You can use the <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">SegmentGeometry extension</a> to compute average intensity in a segmentation along a chosen axis.</p>

---

## Post #3 by @Michel_Atieh (2021-10-30 20:07 UTC)

<p>Thank you for your response.<br>
I tried using SegmentGeometry, however, when I compared the mean slice brightness to the mean Hounsfield Unit of a single slice, the results were not the same.<br>
If only I could get the mean Hounsfield Unit of each slice rather than the mean Hounsfield Unit of the whole segmented volume.</p>

---

## Post #4 by @lassoan (2021-10-30 21:01 UTC)

<p>Do you need the average intensity of the entire slice or only of the part of the slice that is inside the segmented structure? Maybe you could add a screenshot to explain it.</p>

---

## Post #5 by @Michel_Atieh (2021-10-30 21:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c30225da764c4d414d408fe0a804779129bc2eb.jpeg" data-download-href="/uploads/short-url/hICkFRQOBr6Iv7PHpVKLb8Pyzcn.jpeg?dl=1" title="Screenshot1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c30225da764c4d414d408fe0a804779129bc2eb_2_690x410.jpeg" alt="Screenshot1" data-base62-sha1="hICkFRQOBr6Iv7PHpVKLb8Pyzcn" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c30225da764c4d414d408fe0a804779129bc2eb_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c30225da764c4d414d408fe0a804779129bc2eb_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c30225da764c4d414d408fe0a804779129bc2eb_2_1380x820.jpeg 2x" data-dominant-color="3B3D3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot1</span><span class="informations">1920×1142 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d329e7a4a0a65dbba1a194939e9728f1fefb0dc.png" data-download-href="/uploads/short-url/hRy8lvDmFwMMacojSRxiE4spTeA.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d329e7a4a0a65dbba1a194939e9728f1fefb0dc_2_612x500.png" alt="Screenshot" data-base62-sha1="hRy8lvDmFwMMacojSRxiE4spTeA" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d329e7a4a0a65dbba1a194939e9728f1fefb0dc_2_612x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d329e7a4a0a65dbba1a194939e9728f1fefb0dc_2_918x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d329e7a4a0a65dbba1a194939e9728f1fefb0dc_2_1224x1000.png 2x" data-dominant-color="4C4F46"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1398×1142 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have uploaded two images. The first one is showing the mean HU of the whole volume, and the second one shows the mean intensity of each slice of the volume.<br>
What I would like is to have the mean HU of each slice and not of the whole volume.</p>

---

## Post #6 by @lassoan (2021-10-31 01:42 UTC)

<p>What you show above looks correct. Mean brightness values in the table are higher because the irrelevant air voxels (with value of -1024) are excluded from the statistics.</p>
<p>The air voxels must be excluded because otherwise the computed mean intensity would depend on the bore diameter of the CT, the chosen padding value (voxel values outside the reconstructed image), patient support, table appearance (if the image acquisition software does not remove it), cropping settings, etc.</p>

---

## Post #7 by @Michel_Atieh (2021-10-31 13:18 UTC)

<p>Ok, I see what you’re saying. As a result, getting the mean HU by slice for a volume is not an option.<br>
Thank you for your responses; I appreciate your assistance.</p>

---

## Post #8 by @lassoan (2021-11-01 14:47 UTC)

<aside class="quote no-group" data-username="Michel_Atieh" data-post="7" data-topic="20421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michel_atieh/48/11133_2.png" class="avatar"> Michel_Atieh:</div>
<blockquote>
<p>mean HU by slice for a volume is not an option</p>
</blockquote>
</aside>
<p>You can easily get the mean HU for the entire image slice, it is just not a meaningful value in general.</p>

---

## Post #9 by @jmhuie (2021-11-01 20:43 UTC)

<aside class="quote no-group" data-username="Michel_Atieh" data-post="5" data-topic="20421">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michel_atieh/48/11133_2.png" class="avatar"> Michel_Atieh:</div>
<blockquote>
<p>I have uploaded two images. The first one is showing the mean HU of the whole volume, and the second one shows the mean intensity of each slice of the volume.<br>
What I would like is to have the mean HU of each slice and not of the whole volume.</p>
</blockquote>
</aside>
<p>Ah, the reason the values are different is because there was an error in the code. I forgot intensity values could be negative when working with Hounsfield units and was filtering out anything zero or below. I have fixed the issue and the update will be available tomorrow. If you have the current stable release, you should be able to update Segment Geometry through the extension manager. If you have the preview release, you’ll need to download and install tomorrow’s build.</p>

---

## Post #10 by @Michel_Atieh (2021-11-01 21:07 UTC)

<p>Thanks a lot for the update Jonathan! I will try again tomorrow then.<br>
Kind Regards</p>

---
