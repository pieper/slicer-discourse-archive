---
topic_id: 272
title: "Behavior Of Crop Volume Module"
date: 2017-05-05
url: https://discourse.slicer.org/t/272
---

# Behavior of crop volume module

**Topic ID**: 272
**Date**: 2017-05-05
**URL**: https://discourse.slicer.org/t/behavior-of-crop-volume-module/272

---

## Post #1 by @muratmaga (2017-05-05 18:28 UTC)

<p>Hi,</p>
<p>I used to use crop volume as a procedure to avoid having to resample volumes after I manually aligned them. It involved steps of manually creating a transformation, creating a new ROI that encompasses the full volume in its new orientation, and running the crop volume with interpolated cropping.</p>
<p>This is no longer functioning for me. Instead, when I open the resultant crop volume in, say in Fiji, I can the image data in the same orientation as the original volume. (Slicer build r25771, on linux)</p>
<p>Is there a way to get the old behavior back?</p>

---

## Post #2 by @lassoan (2017-05-05 19:01 UTC)

<p>Computation of IJK to RAS matrix had to be changed because in the old version spacing was incorrectly computed for volumes with permuted axis order (RAS spacing was taken from the IJK axes respectively; even when for example IJK was aligned with SRA axes). This led to degraded image quality for anisotropic output.</p>
<p>Does Fiji ignore image axis directions matrix?<br>
What was the direction matrix in the cropped volumes that worked for you in the past and what matrix is in the new volumes?</p>

---
