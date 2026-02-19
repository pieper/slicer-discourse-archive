---
topic_id: 16485
title: "Segmentation Mri Rat"
date: 2021-03-12
url: https://discourse.slicer.org/t/16485
---

# Segmentation MRI rat

**Topic ID**: 16485
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/segmentation-mri-rat/16485

---

## Post #1 by @gloria (2021-03-12 03:18 UTC)

<p>Hi</p>
<p>I want to know if for the segmentation of gray and white matter of a rat mri I need an atlas or not???</p>

---

## Post #2 by @lassoan (2021-04-14 04:38 UTC)

<p>Considering there was not response, most likely Slicer users don’t segment rat MRI using an atlas.</p>
<p>You can probably get good segmentation by using a few modules:</p>
<ul>
<li>Make the image more uniform using bias correction by “N4ITK MRI Bias Correction” module</li>
<li>Apply anisotropic smoothing to reduce noise by “Curvature anisotropic diffusion” or “Gradient anisotropic diffusion” module</li>
<li>Use SwissSkullStripper extension to extract the brain (choose a similar existing rat MRI image and corresponding brain mask as inputs)</li>
<li>Segment white and gray matter using Segment Editor (Thresholding effect, followed by Smoothing effect, using Joint smoothing method)</li>
</ul>

---
