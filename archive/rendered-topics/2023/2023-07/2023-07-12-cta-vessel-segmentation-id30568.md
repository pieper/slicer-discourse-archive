---
topic_id: 30568
title: "Cta Vessel Segmentation"
date: 2023-07-12
url: https://discourse.slicer.org/t/30568
---

# CTA Vessel Segmentation

**Topic ID**: 30568
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/cta-vessel-segmentation/30568

---

## Post #1 by @Dimitrios_Rallios (2023-07-12 21:12 UTC)

<p>I am trying to extract only the arteries from brain CT-Angiography. I tried a few things (Grow from seeds, vessel segmentation module etc. ) but nothing seems to work. Even if I could only get all the vessels would be a help.</p>
<p>Any tips?</p>
<p>Best ,<br>
Dimitrios.</p>

---

## Post #2 by @chir.set (2023-07-14 08:12 UTC)

<p>The trick is to extract the brain as soft tissue first.</p>
<p>You may use HD-BET, SwissSkullStripper or TotalSegmentator for this. Once you have a masked volume, tools line FloodFilling or GrowFromSeeds may extract the arteries from a contrast enhanced CT angio with fewer artifacts. The final masked volume may require some manual editing. I found that fewer editing is required with TotalSegmentator.</p>
<p>In any case, the result will be sub-optimal. Veins have intensity ranges that are quite close to those in arteries. Further manual editing will be required.</p>
<p>If you just want to view the arteries quickly without segmenting, VolumeRendering is very good.</p>

---
