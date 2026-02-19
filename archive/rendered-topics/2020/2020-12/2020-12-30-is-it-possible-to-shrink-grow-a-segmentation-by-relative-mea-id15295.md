---
topic_id: 15295
title: "Is It Possible To Shrink Grow A Segmentation By Relative Mea"
date: 2020-12-30
url: https://discourse.slicer.org/t/15295
---

# Is it possible to shrink/grow a segmentation by relative measure based on its volume?

**Topic ID**: 15295
**Date**: 2020-12-30
**URL**: https://discourse.slicer.org/t/is-it-possible-to-shrink-grow-a-segmentation-by-relative-measure-based-on-its-volume/15295

---

## Post #1 by @Niko_Plath (2020-12-30 15:09 UTC)

<p>Hi, I am searching for a functionality to shrink/grow a segmentation by a ratio of its volume instead of by absolute values via “Margin”.<br>
So something like “isotropic increase of volume by x%”.<br>
Any hints?<br>
Thanks in advance!</p>
<p>Operating system: WIn10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2020-12-30 22:55 UTC)

<p>You can increase/decrease volume of a segment by applying a scaling transform. You can easily compute the scaling factor from the amount of volume growth you want to achieve.</p>
<p>However, you might prefer margin growing instead of scaling, as it is more similar to tissue growth. Amount of volume increase due to margin growing depends on the shape of the segment, so you need to do a couple of iterations to find the margin that leads to the desired volume change. You can speed up computation of these iterations by a bit of Python scripting, which computes a distance map from the segment labelmap once and tries different threshold values on that.</p>

---
