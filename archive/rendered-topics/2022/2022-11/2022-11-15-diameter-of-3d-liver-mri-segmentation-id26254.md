---
topic_id: 26254
title: "Diameter Of 3D Liver Mri Segmentation"
date: 2022-11-15
url: https://discourse.slicer.org/t/26254
---

# Diameter of 3d liver mri segmentation

**Topic ID**: 26254
**Date**: 2022-11-15
**URL**: https://discourse.slicer.org/t/diameter-of-3d-liver-mri-segmentation/26254

---

## Post #1 by @hannahmed (2022-11-15 19:41 UTC)

<p>Hello everyone,</p>
<p>I am fairly new to 3d Slicer and have a question.<br>
I have successfully segmented both the tumor and liver and discovered the segment statistics module which gives me the volume of my segments. Now I need to measure the diameter of the liver and a tumor which it contains from an MRI scan. I’m not sure how to measure or calculate the exact diameter of both the irregular shaped organ and tumor. It seems to me that by placing the ruler manually the result won’t be accurate enough.</p>
<p>I’d appreciate any help or advice, thank you!</p>
<p>Operating system: Mac<br>
Slicer version: 5.0.3</p>

---

## Post #2 by @lassoan (2022-12-01 07:20 UTC)

<p>You can get the oriented bounding box size from Segment Statistics module.</p>

---
