---
topic_id: 36078
title: "Misplaced Images After Volume Reconstruction"
date: 2024-05-11
url: https://discourse.slicer.org/t/36078
---

# Misplaced images after volume reconstruction

**Topic ID**: 36078
**Date**: 2024-05-11
**URL**: https://discourse.slicer.org/t/misplaced-images-after-volume-reconstruction/36078

---

## Post #1 by @Olivier (2024-05-11 06:32 UTC)

<p>Hello, I am acquiring volume data from ultrasound swipes with the IGT module. Usually the reconstruction works as expected but this time the ultrasound frames seem misplaced. Not completely, they are still grouped in 2D within an expectable area, the order seems wrong.<br>
Is there a way to address this at this stage? I tried to look into the Transforms module but couldn’t figure anything.</p>

---

## Post #2 by @Olivier (2024-10-18 10:16 UTC)

<p>Hello, I try to ask again about this because we haven’t found a solution and may loose data.</p>
<p>We have progressed though, we know that the problem comes from the fact that the marker holder was positioned in the reverse position relative to the probe (right and left are inverted). This means that the image-to-probe transform did not work as intended.</p>
<p>I am hoping that it is possible to change the transform matrix to do the volume reconstruction but couldn’t figure it out.</p>

---
