---
topic_id: 38449
title: "Computing The Outer Surface Area Of A Segment"
date: 2024-09-19
url: https://discourse.slicer.org/t/38449
---

# Computing the outer surface area of a segment

**Topic ID**: 38449
**Date**: 2024-09-19
**URL**: https://discourse.slicer.org/t/computing-the-outer-surface-area-of-a-segment/38449

---

## Post #1 by @debadrita_jana (2024-09-19 20:45 UTC)

<p>Hi!</p>
<p>I am trying to measure the surface area and volume of fossils using 3D slicer. I have segmented the scanned volumes. While I can ger the volume in mm3 very easily by using Quantification&gt; segment statistics, I need the outed surface area of the fossils.<br>
Most of the answers posted here show how to get the cross sectional area, but that’s not my desired output.</p>
<p>Can someone please help?</p>

---

## Post #2 by @lassoan (2024-09-20 05:51 UTC)

<p>You can fill internal holes in a segment by using <code>Wrap Solidify</code> effect in <code>Segment Editor</code> module (provided by <code>SurfaceWrapSolidify</code> extension).</p>

---
