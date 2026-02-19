---
topic_id: 14455
title: "Volumetric Analysis Of Vertebral Bodies"
date: 2020-11-05
url: https://discourse.slicer.org/t/14455
---

# Volumetric Analysis of vertebral bodies

**Topic ID**: 14455
**Date**: 2020-11-05
**URL**: https://discourse.slicer.org/t/volumetric-analysis-of-vertebral-bodies/14455

---

## Post #1 by @Siegmund_Lang (2020-11-05 22:44 UTC)

<p>Dear 3DSlicer community,</p>
<p>I am looking  for a way to calculate the volume of vertebral bodies with a microsoft based software other than BrainLab.<br>
Do you know if there is a function in 3DSlicer to measure volume data (in cm^3)?</p>
<p>Thank you very much for your help!<br>
Cheers,<br>
Siegmund</p>

---

## Post #2 by @lassoan (2020-11-05 22:48 UTC)

<p>Yes, in Slicer you can segment vertebral bodies (or import segmentation from DICOM and all other commonly used file formats) and compute the volume. I would recommend to store the segmentation in a “segmentation” node and use “Segment statistics” module to get the volumes.</p>

---

## Post #3 by @Siegmund_Lang (2020-11-10 08:01 UTC)

<p>Dear Andras Lasso,</p>
<p>thanks a lot. After taking my first steps with 3D slicer I was finally able to segment a vertebral body in compute it´s volume as proposed by you. How ever I seem to have some methodical mistakes as the computed volume reads 2300 cm^3. This is much to high (by around the factor 100). Can you think of a reason for this problem?<br>
Thank you in advance!</p>

---

## Post #4 by @lassoan (2020-11-10 13:06 UTC)

<p>If you load the image from a clinical CT then the volume should be correct. If you exported the image to png or similar file formats that do not preserve image metadata then you need to recover the correct image spacing information from somewhere (e.g., by measuring size of an object of known size and multiplying image spacing with the scale factor).</p>

---
