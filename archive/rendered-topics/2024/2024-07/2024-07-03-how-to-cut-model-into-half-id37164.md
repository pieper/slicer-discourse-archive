---
topic_id: 37164
title: "How To Cut Model Into Half"
date: 2024-07-03
url: https://discourse.slicer.org/t/37164
---

# How to cut model into half

**Topic ID**: 37164
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/how-to-cut-model-into-half/37164

---

## Post #1 by @huwqchn (2024-07-03 06:34 UTC)

<p>Hi, I’d like to know how to create a cross-section in 3D Slicer by adding multiple control points to slice a 3D model into two parts.</p>

---

## Post #2 by @huwqchn (2024-07-03 08:15 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f48ccdf4bcbd7ea41d1ccb55b2fef89293d573c.gif" alt="动画" data-base62-sha1="4sKM4U2bWD0887eLibSSk79JFOQ" width="690" height="340" class="animated"></p>

---

## Post #3 by @cpinter (2024-07-03 11:50 UTC)

<p>I don’t know how to do this using control points, but would this work for you?</p>
<ul>
<li>Use interactive slice intersections to define the plane with one of the slice views</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/583ba4b227df18a1cf10c7141190a5f847a5f83f.png" alt="image" data-base62-sha1="cAxNLtzklCQimUcVemwXI4HRRdZ" width="244" height="211"></p>
<ul>
<li>Clip the model using that slice in the Clipping Planes section of the Models module</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/887088b8a6e6ae84857a2358bc46caf561eee8a1.png" alt="image" data-base62-sha1="jt02qkJRzp3PalKuTlhHTxZH9IZ" width="533" height="202"></p>

---

## Post #4 by @huwqchn (2024-07-04 06:39 UTC)

<p>Thanks for reply. This doesn’t work for me; I don’t understand how to do it. Can you provide more detailed instructions?</p>

---
