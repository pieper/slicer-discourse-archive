---
topic_id: 18196
title: "3D Rotate And Reslice"
date: 2021-06-17
url: https://discourse.slicer.org/t/18196
---

# 3D rotate and reslice

**Topic ID**: 18196
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/3d-rotate-and-reslice/18196

---

## Post #1 by @Gisuk_Hwang (2021-06-17 22:48 UTC)

<p>I have xray tomography data, but the scanned images are not upright (a few degree tilted from z axis). I would like to rotate to make my images ‘upright’ and reslice. Can fiji do this? If so, can you tell me how to do?</p>

---

## Post #2 by @lassoan (2021-06-18 20:07 UTC)

<p>I don’t know if Fiji can do this, but 3D Slicer can. For example, you can use Crop volume module with resampling option enabled, with a non-rotated ROI box. By default the ROI box will be aligned with the rotated axes of the volume, but you can get remove that rotation (and make the ROI axis-aligned) by <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">hardening the transform on the ROI</a>.</p>

---
