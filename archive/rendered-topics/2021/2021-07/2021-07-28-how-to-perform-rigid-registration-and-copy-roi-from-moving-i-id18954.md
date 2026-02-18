# How to perform rigid registration, and copy roi from moving image to fixed image?

**Topic ID**: 18954
**Date**: 2021-07-28
**URL**: https://discourse.slicer.org/t/how-to-perform-rigid-registration-and-copy-roi-from-moving-image-to-fixed-image/18954

---

## Post #1 by @yuanzilong0213 (2021-07-28 00:40 UTC)

<p>Hi, everyone！I want to know how to perform rigid registration, and copy roi from moving image to fixed image? Thanks！</p>

---

## Post #2 by @lassoan (2021-08-12 04:46 UTC)

<p>If you computed a linear transform then you can apply that to a Markups ROI node. If you computed a warping transform then you specify the region of interest using segmentation and transform the segmentation.</p>

---
