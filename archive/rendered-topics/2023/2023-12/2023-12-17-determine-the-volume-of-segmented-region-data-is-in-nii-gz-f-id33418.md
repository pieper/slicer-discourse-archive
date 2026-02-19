---
topic_id: 33418
title: "Determine The Volume Of Segmented Region Data Is In Nii Gz F"
date: 2023-12-17
url: https://discourse.slicer.org/t/33418
---

# Determine the volume of segmented region . Data is in .nii.gz format

**Topic ID**: 33418
**Date**: 2023-12-17
**URL**: https://discourse.slicer.org/t/determine-the-volume-of-segmented-region-data-is-in-nii-gz-format/33418

---

## Post #1 by @DivyaB_9569 (2023-12-17 00:43 UTC)

<p>How to determine the volume of segmented region? If data is in .nii.gz format.</p>

---

## Post #2 by @muratmaga (2023-12-17 05:03 UTC)

<p>If you have the segmentation in nii.gz, then load it as a segmentation and use Segment Statistics module.to calculate the metrics like volume</p>

---
