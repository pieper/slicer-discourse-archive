---
topic_id: 6388
title: "Mirroring Slicer"
date: 2019-04-04
url: https://discourse.slicer.org/t/6388
---

# mirroring Slicer

**Topic ID**: 6388
**Date**: 2019-04-04
**URL**: https://discourse.slicer.org/t/mirroring-slicer/6388

---

## Post #1 by @Ely_B (2019-04-04 02:39 UTC)

<p>Hi, I have a problem, I have to calculate the matrix that makes the centers of two mirrored images aligned. How should I proceed?</p>

---

## Post #2 by @cpinter (2019-04-04 13:14 UTC)

<p>You’ll have to move the origin in the direction of the mirroring by the size of the image (spacing*dimensions).</p>

---

## Post #3 by @lassoan (2019-04-06 04:29 UTC)

<aside class="quote no-group" data-username="Ely_B" data-post="1" data-topic="6388">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ely_b/48/3381_2.png" class="avatar"> Ely_B:</div>
<blockquote>
<p>I have to calculate the matrix that makes the centers of two mirrored images aligned</p>
</blockquote>
</aside>
<p>If you know the centerpoint then it should be easy: concatenate transforms that shifts center to the origin, apply mirroring, shift it back to the center.</p>
<p>If you don’t know the centerpoint then mark corresponding anatomical points on the two sides and compute the transform using landmark registration (e.g., SlicerIGT extension’s Fiducial registration wizard module).</p>

---
