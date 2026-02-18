# rebuild the surface of skull bone

**Topic ID**: 7482
**Date**: 2019-07-09
**URL**: https://discourse.slicer.org/t/rebuild-the-surface-of-skull-bone/7482

---

## Post #1 by @raylene (2019-07-09 12:10 UTC)

<p>Operating system:windows<br>
Slicer version:<br>
Expected behavior:rebuild the surface of skull bone<br>
Actual behavior:I wonder whether 3D slicer can produce all the curve data on the skull bone so I can rebuild a model based on the shape using</p>

---

## Post #2 by @pieper (2019-07-09 13:37 UTC)

<p>Sure, you can start by looking at <a href="https://www.slicer.org/wiki/Documentation/4.10/Training" rel="nofollow noopener">the tutorials</a>.</p>

---

## Post #3 by @raylene (2019-07-12 07:13 UTC)

<p>Thank you. Now I have already export the model into STL format. I wonder if I want to dig some irregular arranged  holes in the model, how can I do?</p>

---

## Post #4 by @jcfr (2019-07-12 08:08 UTC)

<p>The SurfaceToolbox module provides some functionality to cleanup and process surface models.<br>
See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SurfaceToolbox" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SurfaceToolbox</a></p>
<p>Note that we are currently working on improve the modules, see <a href="https://discourse.slicer.org/t/surface-toolbox-revamp/7113" class="inline-onebox">Surface toolbox revamp</a> and <a href="https://www.slicer.org/wiki/Documentation/Labs/Surface_Toolbox_update" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/Surface_Toolbox_update</a></p>

---

## Post #5 by @pieper (2019-07-12 12:16 UTC)

<aside class="quote no-group" data-username="raylene" data-post="3" data-topic="7482">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/439d5e/48.png" class="avatar"> raylene:</div>
<blockquote>
<p>dig some irregular arranged holes in the model</p>
</blockquote>
</aside>
<p>The Scissors tool in the Segment Editor could be just what you need for that.</p>

---

## Post #6 by @lassoan (2019-07-12 12:27 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="7482">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The Scissors tool in the Segment Editor could be just what you need for that.</p>
</blockquote>
</aside>
<p>There is a short tutorial for this: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>

---
