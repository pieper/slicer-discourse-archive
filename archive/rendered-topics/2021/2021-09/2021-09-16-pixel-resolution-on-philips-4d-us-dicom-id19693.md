---
topic_id: 19693
title: "Pixel Resolution On Philips 4D Us Dicom"
date: 2021-09-16
url: https://discourse.slicer.org/t/19693
---

# Pixel Resolution on Philips 4D US DICOM

**Topic ID**: 19693
**Date**: 2021-09-16
**URL**: https://discourse.slicer.org/t/pixel-resolution-on-philips-4d-us-dicom/19693

---

## Post #1 by @echo_learner (2021-09-16 03:01 UTC)

<p>Operating system: Ubuntu 16.04<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello, I’m fairly new to slicer, so I apologize if this question has been asked already. I couldn’t find the answer. Is the image spacing that is auto-populated on Volume module when you load the Philips 4D US DICOM the correct pixel resolution of the actual image? The below is a screenshot of a sample Philips 4D US DICOM I load on 3DSlicer. My question is whether the image spacing of 0.644 by 0.639 by 0.484 is unique and correct pixel resolution of the file that I uploaded. Thank you in advance for your assistance.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/899aa03bd7e19c299c7dd8f2051cdf9e3fa2eaac.png" alt="Screenshot from 2021-09-15 16-30-26" data-base62-sha1="jDiHgTfzOexSqIgZNOZL1hy8zeY" width="642" height="456"></p>

---

## Post #2 by @lassoan (2021-09-16 03:05 UTC)

<p>The image resolution is correct, it is retrieved from the DICOM file that Philips Qlab exports. The spacing values are different for each file (they depend on the transducer type and the chosen imaging parameters, such as depth, field of view, etc.). The values that you have are similar to those that we usually see in such images.</p>

---

## Post #3 by @echo_learner (2021-09-18 21:13 UTC)

<p>Thank you for the quick response!</p>

---
