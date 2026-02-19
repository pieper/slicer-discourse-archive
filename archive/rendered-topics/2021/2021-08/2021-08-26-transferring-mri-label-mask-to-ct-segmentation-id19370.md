---
topic_id: 19370
title: "Transferring Mri Label Mask To Ct Segmentation"
date: 2021-08-26
url: https://discourse.slicer.org/t/19370
---

# Transferring MRI label mask to CT segmentation

**Topic ID**: 19370
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/transferring-mri-label-mask-to-ct-segmentation/19370

---

## Post #1 by @SogolSadeghi (2021-08-26 15:21 UTC)

<p>Operating system:Windows, x64<br>
Slicer version: latest stable version</p>
<p>Hi slicer,<br>
I have a CT segmentation with CT as a master volume also I have MRI segmentation  with MR images as a master volume. How can I move label mask of MRI Segmentation to CT Segmentation?</p>

---

## Post #2 by @lassoan (2021-08-27 02:04 UTC)

<p>You need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">register the MRI (moving image) to the CT (fixed image)</a> and then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">apply the resulting transform to the MRI segmentation</a>.</p>

---
