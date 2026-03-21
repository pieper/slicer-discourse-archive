---
topic_id: 46522
title: "Smoothing Aorta Segmentations Across Time"
date: 2026-03-20
url: https://discourse.slicer.org/t/46522
---

# Smoothing aorta segmentations across time

**Topic ID**: 46522
**Date**: 2026-03-20
**URL**: https://discourse.slicer.org/t/smoothing-aorta-segmentations-across-time/46522

---

## Post #1 by @tassiasalles (2026-03-20 18:45 UTC)

<p>Good afternoon,</p>
<p>I’m working with aorta segmentation across different cardiac frames and I was wondering if there is any way to smooth the segmentations across time (different cardiac frames) to avoid segmentations inconsistencies between time points.</p>
<p>I would appreciate any suggestions or recommendations to address this issue.</p>
<p>Thank you in advance =D</p>
<p>Tassia</p>

---

## Post #2 by @mikebind (2026-03-20 19:42 UTC)

<p>You could try using sequence registration to take one segmentation and deform it across time instead of having a separate segmentation for each frame.  This will likely result in a more consistent appearance over time because the registration will only introduce smooth deformations.</p>

---
