---
topic_id: 11366
title: "Segment Threshold"
date: 2020-04-30
url: https://discourse.slicer.org/t/11366
---

# Segment Threshold

**Topic ID**: 11366
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/segment-threshold/11366

---

## Post #1 by @Jini (2020-04-30 16:06 UTC)

<p>Hello,<br>
I scanned a object with lot of measurements and using CT. When I was segmentation this data I see that all measurements have different thresholds. Why the threshold is not same for every measurement? It’s the same object but a lot of measurement. Why is that so? it is not reproducible.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-04-30 16:08 UTC)

<p>What do you mean by “measurements”? Can you post a screenshot to illustrate your point?</p>

---

## Post #3 by @Jini (2020-04-30 16:24 UTC)

<p>I mean the experiment with measurement. But it is the same object that is scanned again and again. I scan ear from patient.</p>

---

## Post #4 by @Jini (2020-04-30 16:26 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca7e890151f3185ec8c35ea4ac33ad09bc63f00.png" alt="Untitled" data-base62-sha1="vu0MIc4VgK5lKMIS3UHz04PPp04" width="659" height="389"> the thtreshold in all segment from same object is not same.Why is so?</p>

---

## Post #5 by @lassoan (2020-04-30 16:58 UTC)

<p>Clinical scanners are usually calibrated, so you always get voxel values in Hounsfield units - the same structure always appears with the same intensity.</p>
<p>If what you refer to is actual variation in voxel values (and not just different default window/level setting) then most likely your scanner is not calibrated (e.g., may occur if you have a preclinical or CBCT system).</p>

---

## Post #6 by @Jini (2020-04-30 17:38 UTC)

<p>it is a micro ct device and the temporal bone is always taken out and put back in and scanned. Every scan we calibrated the microCT device.<br>
it may be that a software technical problem of microCT device, that the threshold is not same in all scan?</p>

---

## Post #7 by @lassoan (2020-04-30 18:53 UTC)

<p>If you need to use a different threshold value to segment the same structure on different scans then most likely this is a problem with the microCT device or how you calibrate it. For example, I would not expect that you must calibrate your device before each scan and in fact this could be responsible for the inconsistent intensity scaling between acquisitions (especially if the calibration is not done very accurately).</p>

---

## Post #8 by @lassoan (2020-05-17 14:14 UTC)

<p>2 posts were split to a new topic: <a href="/t/route-calculation-between-two-points/11590">Route calculation between two points</a></p>

---
