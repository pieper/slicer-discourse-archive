---
topic_id: 47661
title: "Multi slice variable intensity threshold (Grow from seeds)"
date: 2026-07-17
url: https://discourse.slicer.org/t/47661
last_bumped: 2026-07-17T21:41:54.558Z
---

# Multi slice variable intensity threshold (Grow from seeds)

**Topic ID**: 47661
**Date**: 2026-07-17
**URL**: https://discourse.slicer.org/t/multi-slice-variable-intensity-threshold-grow-from-seeds/47661

---

## Post #1 by @Sanjib_Gurung (2026-07-17 21:41 UTC)

<p>Hi,</p>
<p>I frequently use <strong>Grow from Seeds</strong> to generate 3D blood pool models from cardiovascular MRI and CT DICOM images.</p>
<p>In these datasets, the blood pool intensity (or Hounsfield Units in CT) often varies across different slices. When seed points are placed in regions with different intensity levels, especially where the intensity of adjacent tissues is similar to that of the blood pool, the resulting <strong>Grow from Seeds</strong> segmentation can leak into surrounding tissues. This requires a significant amount of manual editing to remove the unwanted portions of the segmentation mask.</p>
<p>Would it be possible to constrain the <strong>Grow from Seeds</strong> algorithm locally based on the intensity values around the nearest seed point, rather than using a global intensity model? This would be similar to applying different local intensity thresholds to different slices or regions within a slice, allowing the segmentation to better adapt to spatial variations in image intensity while reducing leakage into adjacent tissues.</p>
<p>Thanks!</p>

---
