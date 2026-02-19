---
topic_id: 14956
title: "Inferior Dental Nerve Tracing"
date: 2020-12-09
url: https://discourse.slicer.org/t/14956
---

# Inferior dental nerve tracing

**Topic ID**: 14956
**Date**: 2020-12-09
**URL**: https://discourse.slicer.org/t/inferior-dental-nerve-tracing/14956

---

## Post #1 by @manjula (2020-12-09 09:18 UTC)

<p>I would appreciate if someone could share their ways (recipes) of segmenting the IDN Canal on CBCT and CTs.</p>
<p>What is the most balanced way (speed and accuracy) that you have found for this?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2020-12-09 14:17 UTC)

<p>So far the best method that I have found is using Draw tube effect: you step through coronal slices of the volume and mark the nerve centerpoint wherever you see it (it is enough to place a point in one of every 10-20 slices where the nerve curvature is low).</p>
<p>Probably this could be automated well using deep learning, but since the manual segmentation should not take more than 1-2 minutes, automation might not save a lot of time.</p>

---

## Post #3 by @manjula (2020-12-09 16:43 UTC)

<p>I have never tried it that way. It is good enough for planning purposes. And really works well.many thanks Prof Lasso</p>

---
