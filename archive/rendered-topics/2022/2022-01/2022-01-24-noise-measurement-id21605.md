# Noise measurement 

**Topic ID**: 21605
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/noise-measurement/21605

---

## Post #1 by @susmita_afroz (2022-01-24 22:08 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I need help to measure noise from an image using 3D slicer. Need to compare noise from 3 images taken with different mA</p>

---

## Post #2 by @Juicy (2022-01-25 07:45 UTC)

<p>Use the segment editor to paint an area where you want to make the noise measurement. Then use the segment statistics module to get the standard deviation of the pixel values in the painted segment as a measure of the noise in the image.</p>

---

## Post #3 by @susmita_afroz (2022-01-25 21:40 UTC)

<p>Thank you very much Juicy.</p>

---
