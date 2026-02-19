---
topic_id: 43649
title: "How To Compute Average Vertical Y Axis Distance Between Two"
date: 2025-07-08
url: https://discourse.slicer.org/t/43649
---

# how to compute average vertical (y-axis) distance between two curves in 3d space?

**Topic ID**: 43649
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/how-to-compute-average-vertical-y-axis-distance-between-two-curves-in-3d-space/43649

---

## Post #1 by @LJW (2025-07-08 12:46 UTC)

<p>hi,</p>
<p>i’m trying to find the average vertical distance (along the y-axis) between two curves in 3d space.</p>
<p>basically, i want to measure how far apart the two curves are in the y-direction — not the full 3d distance, just the offset along the y-axis. the curves are already defined, and i’d like to compute this average y-difference between them.</p>
<p>is there a good way to do this, either in 3d slicer or with python/numpy?</p>
<p>thanks a lot! any ideas would be appreciated.</p>

---

## Post #2 by @pieper (2025-07-08 21:39 UTC)

<p>Yes, you can do this in python.  Just get the points from the two curves and subtract and look at the y (axis).  If you need more detail you can resample in the markups module.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; n = getNode("OC")
&gt;&gt;&gt; arrayFromMarkupsControlPoints(n)
array([[-102.88747763,  -36.66582196,   87.48674899],
       [ -32.85996019,  -42.21678371,   87.48674899],
       [ -32.85996019, -117.36826585,   87.48674899],
       [-114.84339524, -175.86686273,   87.48674899]])
&gt;&gt;&gt; 
</code></pre>

---
