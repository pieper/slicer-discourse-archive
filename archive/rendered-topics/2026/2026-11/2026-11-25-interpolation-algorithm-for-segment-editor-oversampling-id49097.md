---
topic_id: 49097
title: "Interpolation algorithm for Segment Editor Oversampling"
date: 2026-11-25
url: https://discourse.slicer.org/t/49097
last_bumped: 2026-11-25T17:53:27.089Z
---

# Interpolation algorithm for Segment Editor Oversampling

**Topic ID**: 49097
**Date**: 2026-11-25
**URL**: https://discourse.slicer.org/t/interpolation-algorithm-for-segment-editor-oversampling/49097

---

## Post #1 by @Liam_Menz (2026-11-25 17:50 UTC)

<p>Hey,</p>
<p>I was wondering what the interpolation algorithm is (linear, nearest-neighbour, spline etc.) for the oversampling feature in the Segment Editor (Segmentation Geometry). I want to understand what is going on behind the scenes in a little more detail to determine the applicability of the tool.</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2026-11-25 17:53 UTC)

<p><a class="mention" href="/u/liam">@liam</a> when you are splitting voxels to make them smaller (oversampling) or merging them into larger ones (downsampling), you have to come with a mathematical method of objectively estimating what the new values in new voxels be. That’s the funciton of interpolation. For rest (such how they work, and the differences), I suggest you look interpolation functions and how they work in Wikipedia, along with image resampling.</p>

---
