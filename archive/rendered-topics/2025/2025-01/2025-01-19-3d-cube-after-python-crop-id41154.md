---
topic_id: 41154
title: "3D Cube After Python Crop"
date: 2025-01-19
url: https://discourse.slicer.org/t/41154
---

# 3d cube after python crop

**Topic ID**: 41154
**Date**: 2025-01-19
**URL**: https://discourse.slicer.org/t/3d-cube-after-python-crop/41154

---

## Post #1 by @Andras_Gomori (2025-01-19 22:32 UTC)

<p>I’m working in win 10 with slicer, and in wsl.<br>
I’m using nifti files, and try to crop them. I use simple ITK for this purpose.<br>
The crop (somewhat) works, in the 2d views it is great. But in the 3d view the 3d cube works differently as I would expect. I’m unsure if it is the slicer, or the crop itself that causes problems. On R-L axis it is great, but on A-P and on the Z axis it is way off.<br>
I’ve tried the crop with and also without the reset of origin, spacing, and affine matrix.<br>
I’m lost.</p>
<p>edit2: I’m always deleting the cache in 3d slicer.</p>

---

## Post #2 by @lassoan (2025-01-20 04:36 UTC)

<p>I would recommend to use the Crop Volume module from your Python script. It can handle any volume, with any geometry, even under a warping transform, and any ROI box, even rotated, and can keep the original resolution or resample to isotropic output spacing. There is nothing particularly difficult in any of these, you just have to have a solid understanding of coordinate systems, transforms, API of resapling filters, and pay close attention when putting everything together.</p>

---

## Post #3 by @Andras_Gomori (2025-01-20 10:24 UTC)

<p>Thank you very much for the recommendation!<br>
I have been searching for exactly what the 3d cube is, without success. I’m not using the slicer from python (yet), but I’ll try.</p>

---
