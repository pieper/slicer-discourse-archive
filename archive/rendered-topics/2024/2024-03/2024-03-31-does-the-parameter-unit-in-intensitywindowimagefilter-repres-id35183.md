---
topic_id: 35183
title: "Does The Parameter Unit In Intensitywindowimagefilter Repres"
date: 2024-03-31
url: https://discourse.slicer.org/t/35183
---

# Does the parameter unit in IntensityWindowImageFilter represent the Hounsfield unit?

**Topic ID**: 35183
**Date**: 2024-03-31
**URL**: https://discourse.slicer.org/t/does-the-parameter-unit-in-intensitywindowimagefilter-represent-the-hounsfield-unit/35183

---

## Post #1 by @Nutchanon_Hemapattam (2024-03-31 04:41 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ec2a447fbaeab01b97d6dc822a081937f18a5c4.png" alt="image" data-base62-sha1="26zHyCBWEunpsBw8C2oraoKCmEc" width="493" height="234"></p>

---

## Post #2 by @lassoan (2024-03-31 19:25 UTC)

<p>If you load a clinical CT image from DICOM  then usually the voxel values are in Hounsfield unit. Cone-beam CT, micro-CT, pre-clinical CT scans are often not in Hounsfield units.</p>
<p>If <code>Input volume</code> voxel values are in HU, then <code>Window Minimum</code> and <code>Window Maximum</code> are in HU.</p>

---

## Post #3 by @Nutchanon_Hemapattam (2024-04-01 02:07 UTC)

<p>Thank you very much for reply.</p>

---
