---
topic_id: 28742
title: "How To Crop A Segmented Volume"
date: 2023-04-04
url: https://discourse.slicer.org/t/28742
---

# How to crop a segmented volume?

**Topic ID**: 28742
**Date**: 2023-04-04
**URL**: https://discourse.slicer.org/t/how-to-crop-a-segmented-volume/28742

---

## Post #1 by @mukund_shah (2023-04-04 08:48 UTC)

<p>Like in volume renderer we can crop a volume by  ROI ,how do I do so for a segmented volume?</p>

---

## Post #2 by @lassoan (2023-04-04 14:00 UTC)

<p>You can use “Specify geometry” button in Segment Editor module to crop and resample to a specified region of interest.</p>
<p>If you want to avoid resampling then you can export the segmentation to a labelmap node, crop using “Crop volume” module, then convert the labelmap to segmentation node.</p>
<p>If you just want to clip the segments in 3D then you can export them to models and enable clipping for the models.</p>

---

## Post #3 by @lassoan (2023-06-19 19:07 UTC)

<p>A post was split to a new topic: <a href="/t/segmenting-a-bottle-in-a-ct-scan-is-slow/30128">Segmenting a bottle in a CT scan is slow</a></p>

---
