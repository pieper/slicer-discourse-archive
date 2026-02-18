# Smoothing without decreasing size

**Topic ID**: 4641
**Date**: 2018-11-05
**URL**: https://discourse.slicer.org/t/smoothing-without-decreasing-size/4641

---

## Post #1 by @Rea2 (2018-11-05 15:38 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1</p>
<p>I’m trying to smooth my segmented object (cartilage layers of femur and acetabulum), but it’s size is considerably reduced when doing so. Is there a way to prevent it from decreasing in size when being smoothed?</p>

---

## Post #2 by @lassoan (2018-11-05 17:27 UTC)

<p>Use Segment editor module’s Smoothing effect. All methods except Gaussian preserve original size of structures.</p>

---
