---
topic_id: 28687
title: "How To Apply A Segmented Tumor To Other Imaging"
date: 2023-03-30
url: https://discourse.slicer.org/t/28687
---

# How to apply a segmented tumor to other imaging

**Topic ID**: 28687
**Date**: 2023-03-30
**URL**: https://discourse.slicer.org/t/how-to-apply-a-segmented-tumor-to-other-imaging/28687

---

## Post #1 by @curtis_sohn (2023-03-30 18:55 UTC)

<p>Hi, everyone.</p>
<p>I finished a tumor segmentation from T2-flair imaging and created the output as .nrrd file.<br>
Since segmenting all images is time consuming, I want to apply the nrrd file to also other image modalities. How can I do this in the 3D slicer?</p>

---

## Post #2 by @lassoan (2023-03-30 18:56 UTC)

<p>You can register the source image that you used for segmentation to any other image. You can then apply the computed transform to the segmentation.</p>

---
