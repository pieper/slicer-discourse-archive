---
topic_id: 1410
title: "Removing Dvt Scanned Dental Artifacts Scatters"
date: 2017-11-08
url: https://discourse.slicer.org/t/1410
---

# Removing DVT - Scanned dental artifacts/scatters

**Topic ID**: 1410
**Date**: 2017-11-08
**URL**: https://discourse.slicer.org/t/removing-dvt-scanned-dental-artifacts-scatters/1410

---

## Post #1 by @kamikite (2017-11-08 16:07 UTC)

<p>Hey there!</p>
<p>I want to ask, if anyone knows how or whether there is a function to reduce scatters/artifacts in the dental area. Or perhaps how to repair this areas with other programs.</p>
<p>Thanks for all helps/hint.</p>

---

## Post #2 by @lassoan (2017-11-08 16:14 UTC)

<p>You can use Segment editor module for visualizing and measuring structures that are not very well visible due to image artifacts. You may start with Thresholding effect, then cut off large artifacts using Scissors effect, remove speckles using Islands effect, and smooth results using Smoothing effect.</p>

---
