---
topic_id: 7153
title: "Moving Volume Overwritten With Brainsfit General Registratio"
date: 2019-06-13
url: https://discourse.slicer.org/t/7153
---

# Moving volume overwritten with BRAINSfit General Registration Module

**Topic ID**: 7153
**Date**: 2019-06-13
**URL**: https://discourse.slicer.org/t/moving-volume-overwritten-with-brainsfit-general-registration-module/7153

---

## Post #1 by @Eloise (2019-06-13 10:25 UTC)

<p>Hello,</p>
<p>When I use the BRAINSFit registration module, the moving volume is overwritten (i.e. transformed and resampled in the same space as the fixed volume, and similar to the output volume). Is there any way to prevent it and keep the moving volume as it is originally ?<br>
I am using the BRAINSfit module with slicer.cli.run and I am running several successive local registration using the different segments of a segmentation (ROI moving mask) but with the same fixed and moving volumes, and it is a problem if the moving volume is modified each time.<br>
Thanks for your help,</p>

---

## Post #2 by @lassoan (2019-06-13 11:36 UTC)

<p>The moving volume is not modified, just the computed transform is set as parent transform. You can remove it by calling <code>movingVolume.SetAndObserveTransformNodeID(None)</code>.</p>

---

## Post #3 by @Eloise (2019-06-19 13:42 UTC)

<p>Thanks, it solves the problem!</p>

---
