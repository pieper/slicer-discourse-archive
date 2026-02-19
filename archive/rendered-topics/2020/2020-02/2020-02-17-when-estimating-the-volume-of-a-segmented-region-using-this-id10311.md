---
topic_id: 10311
title: "When Estimating The Volume Of A Segmented Region Using This"
date: 2020-02-17
url: https://discourse.slicer.org/t/10311
---

# When estimating the volume of a segmented region using this software, do we need to consider the gap between the slices??

**Topic ID**: 10311
**Date**: 2020-02-17
**URL**: https://discourse.slicer.org/t/when-estimating-the-volume-of-a-segmented-region-using-this-software-do-we-need-to-consider-the-gap-between-the-slices/10311

---

## Post #1 by @Eshani (2020-02-17 14:05 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2020-02-17 14:07 UTC)

<p>You get the volume of what you see. If you see a gap between slices then the volume of the gap will not be included in the segment’s volume. If you want to skip segments during segmentation to save time on segmentation then use “Fill between slices” effect to fill the gaps.</p>

---

## Post #3 by @Eshani (2020-02-21 16:42 UTC)

<p>Okay! Thank you very much.</p>

---
