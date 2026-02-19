---
topic_id: 3446
title: "Show Seed Points On 3D Volume"
date: 2018-07-10
url: https://discourse.slicer.org/t/3446
---

# Show seed points on 3D volume

**Topic ID**: 3446
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/show-seed-points-on-3d-volume/3446

---

## Post #1 by @anitakh1 (2018-07-10 12:43 UTC)

<p>hello. i have taken out few seed points from CT lung volume data. how can i show the seed points on 3D volume?</p>

---

## Post #2 by @lassoan (2018-07-10 15:34 UTC)

<p>Did you create seed points by painting them in Segment editor module, or added markup fiducials? Or some other way?</p>

---

## Post #3 by @anitakh1 (2018-07-11 05:08 UTC)

<p>no , i generated seed points through program in python.</p>

---

## Post #4 by @lassoan (2018-07-11 14:06 UTC)

<p>Make sure you add your markup fiducial node to the scene and create display node (by calling <code>CreateDefaultDisplayNodes</code>).</p>

---
