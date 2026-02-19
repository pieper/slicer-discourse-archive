---
topic_id: 43076
title: "Thresholding Creates Squares"
date: 2025-05-24
url: https://discourse.slicer.org/t/43076
---

# Thresholding creates squares

**Topic ID**: 43076
**Date**: 2025-05-24
**URL**: https://discourse.slicer.org/t/thresholding-creates-squares/43076

---

## Post #1 by @vivaciousviscera (2025-05-24 14:21 UTC)

<p>When I press “Apply” after setting the threshold values for my segment, it creates squares instead of smooth painted areas over my structures. Any idea on what’s going on here and how to fix this?</p>

---

## Post #2 by @lassoan (2025-05-24 14:26 UTC)

<p>By default, the segmentation rsaolutipn matches the resolution of the source image. If the resolition is low then you the appearance in slice views will be blocky. You can resample the source volume or segmentation as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---
