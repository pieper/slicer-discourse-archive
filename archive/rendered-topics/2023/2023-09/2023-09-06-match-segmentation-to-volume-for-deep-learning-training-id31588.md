---
topic_id: 31588
title: "Match Segmentation To Volume For Deep Learning Training"
date: 2023-09-06
url: https://discourse.slicer.org/t/31588
---

# Match segmentation to volume for deep learning training

**Topic ID**: 31588
**Date**: 2023-09-06
**URL**: https://discourse.slicer.org/t/match-segmentation-to-volume-for-deep-learning-training/31588

---

## Post #1 by @liyuaaan (2023-09-06 10:40 UTC)

<p>Hi,<br>
I have a question regarding the padding of 3d images (.nii.gz). Say my volume dimension is [512, 512,273] , my segmentation is [183, 263, 374], they have different origins and coordinates. And then, I want my segmentation to match volume for deep learning training. Any suggestions?</p>
<p>Thank you so much!!!</p>

---

## Post #2 by @pieper (2023-09-06 18:55 UTC)

<p>If you use a newer version of Slicer the exported segmentations should match the source volumes by default.</p>

---
