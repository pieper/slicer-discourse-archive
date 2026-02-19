---
topic_id: 32703
title: "Slicer Could Not Load Nifti 2"
date: 2023-11-09
url: https://discourse.slicer.org/t/32703
---

# Slicer could not load NIfTI 2

**Topic ID**: 32703
**Date**: 2023-11-09
**URL**: https://discourse.slicer.org/t/slicer-could-not-load-nifti-2/32703

---

## Post #1 by @Toru_Hironaka (2023-11-09 21:56 UTC)

<p>My Slicer version: 5.2.2 r31382. I could load NIfTI-1 file in Slicer, but I could not load my NIfTI-2 file in Slicer. Is Slicer does not support NIfTI-2 file format?</p>

---

## Post #2 by @lassoan (2023-11-09 22:02 UTC)

<p>Please try with current Slicer version (right now the latest Slicer Stable Release is Slicer-5.4.0).</p>
<p>If it does not load the file then it means that ITK library (that Slicer uses for image reading/writing) cannot read this file format or its support is not enabled in Slicer. In this case, I would recommend to ask about status of NIFTI-2 support in ITK on the <a href="https://discourse.itk.org/t/how-to-enable-nifti2-library/3397">ITK forum</a>.</p>

---

## Post #3 by @Toru_Hironaka (2023-11-09 23:28 UTC)

<p>I upgrade the latest version of Slicer 5.4.0, but I got the same problem. I will look at the ITK forum. Thanks for the link.</p>

---
