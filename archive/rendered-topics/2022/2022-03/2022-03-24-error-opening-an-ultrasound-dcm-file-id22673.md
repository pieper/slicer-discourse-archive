---
topic_id: 22673
title: "Error Opening An Ultrasound Dcm File"
date: 2022-03-24
url: https://discourse.slicer.org/t/22673
---

# Error opening an ultrasound .dcm file

**Topic ID**: 22673
**Date**: 2022-03-24
**URL**: https://discourse.slicer.org/t/error-opening-an-ultrasound-dcm-file/22673

---

## Post #1 by @Mariano_Medina (2022-03-24 18:28 UTC)

<p>I wanted to open a .dcm file of a 3d ultrasound to do the reconstruction in 3d slicer, but when loading the file it detects error, the error message is: “Image spacing may need to be calibrated for accurate size measurements”.<br>
How can i fix this problem?<br>
thank´s</p>
<p>Slicer version: 4.13.0-2022-01-03</p>

---

## Post #2 by @lassoan (2022-03-26 03:27 UTC)

<p>This warning is displayed because the image sequence plugin can load a wide range of image types and image spacing setting is not thoroughly validated for all of them, so the user should verify it.</p>
<p>This plugin loads a 2D+time image sequence and not a 3D volume. How do you plan to reconstruct a 3D volume from it? What ultrasound system and probe did you use to acquire this data set?</p>

---
