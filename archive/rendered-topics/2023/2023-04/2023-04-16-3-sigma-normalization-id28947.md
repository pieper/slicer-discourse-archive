---
topic_id: 28947
title: "3 Sigma Normalization"
date: 2023-04-16
url: https://discourse.slicer.org/t/28947
---

# -/+ 3 sigma normalization

**Topic ID**: 28947
**Date**: 2023-04-16
**URL**: https://discourse.slicer.org/t/3-sigma-normalization/28947

---

## Post #1 by @mahmood (2023-04-16 23:46 UTC)

<p>sorry<br>
I have a question. How can I apply -/+3 sigma normalization on my dicom files?<br>
Thanks</p>

---

## Post #2 by @lassoan (2023-04-16 23:57 UTC)

<p>When Slicer loads an image and window/level then uses +/- 3 sigma normalization by default for displaying the image (sets window/level so that 0.1 to 99.9% of the voxel intensities are mapped to the displayed intensity range).</p>
<p>In DICOM files very often the window/level is already specified and then that is used. If that is not what you want then you can right-click on the image and choose <code>Window/Level presets</code> → <code>Automatic</code>.</p>

---

## Post #3 by @Radiologist00 (2023-06-11 06:27 UTC)

<p>Hi,<br>
Can I then assume that my images go through -/+ 3 sigma normalization by default?<br>
How about the choice “normalize image filter”?<br>
Best wishes,</p>

---

## Post #4 by @Saima (2023-07-25 05:54 UTC)

<p>Hi andras,<br>
I want to normalise APTw image with range [-5, 5]. How can I do this?</p>
<p>regards,<br>
Saima</p>

---
