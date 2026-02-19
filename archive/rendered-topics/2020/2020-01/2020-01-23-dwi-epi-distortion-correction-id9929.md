---
topic_id: 9929
title: "Dwi Epi Distortion Correction"
date: 2020-01-23
url: https://discourse.slicer.org/t/9929
---

# DWI EPI distortion correction

**Topic ID**: 9929
**Date**: 2020-01-23
**URL**: https://discourse.slicer.org/t/dwi-epi-distortion-correction/9929

---

## Post #1 by @Adam1122 (2020-01-23 21:43 UTC)

<p>Hello, I have an input DWI dataset and wanna perform the EPI correction (magnetic susceptibility induced distortion, geometric distortion…). Does 3D Slicer enable to perform the EPI correction?</p>
<p>Thanks a lot<br>
Regards<br>
Adam</p>

---

## Post #2 by @lassoan (2020-01-24 01:23 UTC)

<p>If you have your corrective transform as an ITK transform (grid, b-spline, thin-plate-spline or a composite of these) or as a 3D vector volume (containing dense displacement field) then you can apply that to any node, such as volumes, models, point sets, etc. using Transforms module.</p>

---

## Post #3 by @Adam1122 (2020-01-31 09:45 UTC)

<p>Thanks a lot. Please, where to obtain the corrective transform matrix on my input DWI data set. Does 3D Slicer enable to get it? Or any other program?</p>

---
