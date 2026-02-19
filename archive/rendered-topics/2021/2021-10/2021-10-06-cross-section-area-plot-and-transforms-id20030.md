---
topic_id: 20030
title: "Cross Section Area Plot And Transforms"
date: 2021-10-06
url: https://discourse.slicer.org/t/20030
---

# Cross-section area plot and transforms

**Topic ID**: 20030
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/cross-section-area-plot-and-transforms/20030

---

## Post #1 by @hherhold (2021-10-06 01:32 UTC)

<p>Hey Andras, (<a class="mention" href="/u/lassoan">@lassoan</a>)</p>
<p>Quick question on your implementation of the cross-section area plot. I did a quick test on plotting the area of a segment, then I transformed the volume and segment (translation), and ran the same plot (row) again. I did harden the transform before re-running the plot, but I got the exact same plot, which is not what I would expect. I noticed some code to deal with transforms in the <code>run()</code> function - does this not deal with transforming the volume/segment via the transforms module?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2021-10-06 01:46 UTC)

<p>Which module are you using for measuring cross-sectional area?</p>

---

## Post #3 by @hherhold (2021-10-06 01:47 UTC)

<p>The one in the sandbox.</p>

---

## Post #4 by @lassoan (2021-10-06 02:53 UTC)

<p>Translation should not change the plot, because the x axis of the cross-section plot is in voxels.</p>
<p>You may also try the new <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">Segment Geometry extension</a>.</p>

---

## Post #5 by @hherhold (2021-10-06 10:17 UTC)

<p>I tried both translation and rotation, but didn’t see a difference in the plot. I thought translation might be easier to tell a difference because the start slice should change.</p>
<p>I’ll take a look at that extension - thanks!</p>

---

## Post #6 by @lassoan (2021-10-06 11:59 UTC)

<p>If you apply any rigid transform to the segmentation or will not change the cross-sectional area computed but the module in the sandbox. That module computes the cross-sectional area in the internal labelmap axis directions and if you apply a rigid (translarion, rotation) transform then the entire labelmap is transformed (along with the axes). You can change the segmentation node’s geometry using specify geometry button or use the Segment Geometry extension to get cross-sectional area along an arbitrary direction.</p>

---

## Post #7 by @hherhold (2021-10-06 14:13 UTC)

<p>Got it.</p>
<p>The Segment Geometry extension is excellent - thanks for the info!!</p>

---
