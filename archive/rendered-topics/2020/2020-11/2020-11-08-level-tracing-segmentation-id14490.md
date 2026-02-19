---
topic_id: 14490
title: "Level Tracing Segmentation"
date: 2020-11-08
url: https://discourse.slicer.org/t/14490
---

# Level tracing segmentation

**Topic ID**: 14490
**Date**: 2020-11-08
**URL**: https://discourse.slicer.org/t/level-tracing-segmentation/14490

---

## Post #1 by @sahithi (2020-11-08 14:44 UTC)

<p>Hello everyone,</p>
<p>I have a doubt regarding level tracing segmentation. Is level tracing segmentaion kind of thresholding segmentation(semi automatic) or not?</p>
<p>If it is diffrent from thresholding, can somebody please tell me what is the working principle of level tracing segmentation. I have already gone through the slicer documentation of level tracing segmentation.</p>
<p>I would really appreaciate, if somebody can share relevant papers on this topic.</p>
<p>Looking forward for the response.</p>
<p>Thank you,</p>
<p>Best Regards<br>
Sahithi</p>

---

## Post #2 by @pieper (2020-11-08 15:20 UTC)

<p>I’m not sure there’s any paper about LevelTracing.  It’s a simple concept: think of the image as an elevation map (like a mountain range) and the LevelTracing lines are like iso-contours of constant elevation.  E.g. like standing on the side of a hill and walking around the hill without going up or down until you end up back where you started.</p>

---
