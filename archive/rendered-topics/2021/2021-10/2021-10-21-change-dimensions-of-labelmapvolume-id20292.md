# Change Dimensions of LabelMapVolume

**Topic ID**: 20292
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/change-dimensions-of-labelmapvolume/20292

---

## Post #1 by @alyssan (2021-10-21 21:22 UTC)

<p>I  have to change the dimensions of my labelmapvolume. What module do I use and how do I do this?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-10-22 01:09 UTC)

<p>If you have a specific volume that you want to match the geometry of then you can use the “Resample Scalar/Vector/DWI Volume” module. If you prefer to specify the new extent using an ROI box then you can use “Crop volume” module.</p>

---
