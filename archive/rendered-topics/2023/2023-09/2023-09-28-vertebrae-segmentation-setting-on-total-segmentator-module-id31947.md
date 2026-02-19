---
topic_id: 31947
title: "Vertebrae Segmentation Setting On Total Segmentator Module"
date: 2023-09-28
url: https://discourse.slicer.org/t/31947
---

# Vertebrae Segmentation Setting on Total Segmentator Module

**Topic ID**: 31947
**Date**: 2023-09-28
**URL**: https://discourse.slicer.org/t/vertebrae-segmentation-setting-on-total-segmentator-module/31947

---

## Post #1 by @marcosncosta1 (2023-09-28 13:55 UTC)

<p>Hello Slicer community,</p>
<p>I am trying to segment vertebrae with the TotalSegmentator module and I was wondering if there is a setting where I can add “vertebrae segmentation” to the segmentation task so that I don’t have to run the “total” segmentation every time.<br>
Any help is appreciated.</p>

---

## Post #2 by @rbumm (2023-09-28 14:21 UTC)

<p>No, there isn’t, but it should be fairly simple to write a Python script that deletes all non-vertebra segments from your current scene.</p>

---
