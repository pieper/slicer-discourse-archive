---
topic_id: 6660
title: "Averaging 3D Models"
date: 2019-04-30
url: https://discourse.slicer.org/t/6660
---

# "Averaging" 3D models

**Topic ID**: 6660
**Date**: 2019-04-30
**URL**: https://discourse.slicer.org/t/averaging-3d-models/6660

---

## Post #1 by @stephan (2019-04-30 20:19 UTC)

<p>Hi,</p>
<p>I have several 3D models which are fairly similar (heart contours), but not exactly equal. I was wondering if there is a way to create the “average” model of these after registering them to each other.<br>
I found a paper which describes the theory of what I would like to accomplish (<a href="https://www.sciencedirect.com/science/article/pii/S1077314205000858" rel="nofollow noopener">https://www.sciencedirect.com/science/article/pii/S1077314205000858</a>), but I was hoping that someone could point me to a 3D Slicer extension or so where this function might already have been implemented.</p>
<p>Thank you<br>
Stephan</p>

---

## Post #2 by @lassoan (2019-05-01 05:20 UTC)

<p><a href="http://salt.slicer.org/" rel="nofollow noopener">SlicerSALT</a> extension has sophisticated shape analysis tools that should provide what you need (probably better methods than the one described in the referenced paper).</p>

---
