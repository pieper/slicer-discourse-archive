---
topic_id: 39492
title: "Isotropic Expansion"
date: 2024-10-02
url: https://discourse.slicer.org/t/39492
---

# isotropic expansion

**Topic ID**: 39492
**Date**: 2024-10-02
**URL**: https://discourse.slicer.org/t/isotropic-expansion/39492

---

## Post #1 by @Farah_BH (2024-10-02 12:29 UTC)

<p>Hello, I’m trying to expand isotropically a ROI using grow/shrink. The problem is my voxel size is anisotropic [0.9,0.9,2.5] and I want to do a 2 mm expansion which is not possible using slicer segment editor (as shown in the image) . Also I want understand how this growing of ROIs work in 3D Slicer<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48951b717280585ae86f33fc1eac9267df83543e.png" alt="image" data-base62-sha1="am5PZtO7BwHQSTt5bIJMORVGN5A" width="468" height="215"></p>

---

## Post #2 by @lassoan (2024-10-02 12:34 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">decrease the spacing of the segmentation</a> if your current spacing is comparable or larger than the desired margin. Setting a 0.9mm isotropic spacing could make sense (that would allow exactly 1.8mm expansion), but if you want exact 2.0mm growth then you have to resample to something like 1.0mm or 0.5mm.</p>

---
