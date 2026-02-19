---
topic_id: 33889
title: "Drawing An Irregular Roi In The Image"
date: 2024-01-21
url: https://discourse.slicer.org/t/33889
---

# Drawing an irregular ROI in the image

**Topic ID**: 33889
**Date**: 2024-01-21
**URL**: https://discourse.slicer.org/t/drawing-an-irregular-roi-in-the-image/33889

---

## Post #1 by @Atena (2024-01-21 06:18 UTC)

<p>I use windows 10 , and 3d slicer (5.6.1 version). To show vascular leakage in my image, I need to draw an irregular ROI instead of a square or rectangle and use these areas in artificial intelligence algorithms.<br>
can you help me?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a1ed17958ea0ef1ae6b9326aae3d32fe62b6f4e.jpeg" data-download-href="/uploads/short-url/f8MDEVMNW2yo0Aj7QWPmd89FLRQ.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a1ed17958ea0ef1ae6b9326aae3d32fe62b6f4e_2_345x228.jpeg" alt="Screenshot" data-base62-sha1="f8MDEVMNW2yo0Aj7QWPmd89FLRQ" width="345" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a1ed17958ea0ef1ae6b9326aae3d32fe62b6f4e_2_345x228.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a1ed17958ea0ef1ae6b9326aae3d32fe62b6f4e_2_517x342.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a1ed17958ea0ef1ae6b9326aae3d32fe62b6f4e_2_690x456.jpeg 2x" data-dominant-color="393534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1355×899 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-01-21 06:53 UTC)

<p>You can use segment editor to create any irregular shaped region.</p>

---

## Post #3 by @Atena (2024-01-21 07:20 UTC)

<p>it is very difficult. because vessels and leakage have a lot of elegance and the negative pixels are placed in the target volume.</p>

---

## Post #4 by @muratmaga (2024-01-21 16:35 UTC)

<p>For vessels, i believe people use curve markup, which you can turn into models and segmentations.</p>

---

## Post #5 by @Atena (2024-01-22 11:49 UTC)

<p>thank you for your response.<br>
How can I use curve markup?</p>

---

## Post #6 by @muratmaga (2024-01-22 15:49 UTC)

<p>Vessel segmentation is not something I familiar with. As I understand you use the curve tool to trace the vessel and you use the MarkupsToModels extension to convert the curve to a tube with a specific diameter. If you search the forum you can find more details.</p>

---
