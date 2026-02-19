---
topic_id: 15635
title: "Resampling And Inflation"
date: 2021-01-22
url: https://discourse.slicer.org/t/15635
---

# Resampling and inflation

**Topic ID**: 15635
**Date**: 2021-01-22
**URL**: https://discourse.slicer.org/t/resampling-and-inflation/15635

---

## Post #1 by @Vinny (2021-01-22 22:22 UTC)

<p>Slicer version: 4.11.20200930</p>
<p>Hello all,</p>
<p>I have a target area of interest (thalamus) that has been segmented at a higher resolution (and smaller FOV) than the T1 scan.  As part of my workflow in Slicer, I resampled the target to the original T1 dimensions using the Resample Image (BRAINS) module; however, the target area inflates by a couple of voxels all around.  I’d like to export this target to a commercial Medtronic planning station and am wondering if I should export the high-resolution target or the ‘inflated’ resampled target.</p>
<p>Thanks for your help.</p>
<p>Regards,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2021-09-14 21:19 UTC)

<p>If you can import the high-resolution (more accurate) segmentation into the treatment planning system then you are better off doing that.</p>

---
