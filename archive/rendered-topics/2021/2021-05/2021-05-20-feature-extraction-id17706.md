---
topic_id: 17706
title: "Feature Extraction"
date: 2021-05-20
url: https://discourse.slicer.org/t/17706
---

# Feature Extraction

**Topic ID**: 17706
**Date**: 2021-05-20
**URL**: https://discourse.slicer.org/t/feature-extraction/17706

---

## Post #1 by @HAFSA (2021-05-20 12:02 UTC)

<p>Hey:<br>
I want to extract the radiomic features of 2D Slices. But it fails when the mask with only background is found or no tumor area. You can say blank slices .On the other hand I want to extract the feature of all slices even with no mask or tumor information. Please let me know how to do this… It will be appreciated. I know radiomic works with mask and image both.</p>

---

## Post #2 by @JoostJM (2022-01-21 10:05 UTC)

<p>The mask is needed to tell the computer from which part you want to compute features. If there is no ROI on your slice (blank slice) what then do you want to extract features from?</p>

---
