---
topic_id: 35566
title: "Aligning Control Points Vertically"
date: 2024-04-17
url: https://discourse.slicer.org/t/35566
---

# Aligning control points vertically?

**Topic ID**: 35566
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/aligning-control-points-vertically/35566

---

## Post #1 by @CanidMorpho (2024-04-17 17:25 UTC)

<p>Is there a way to perfectly align two control points vertically? More specifically, if I place a landmark beside a tooth on a canid mandible, how can I ensure that a point I place at the bottom of the jaw is perfectly aligned with it? I’ve tried editing the R coordinate to match the previous landmark, but that tends to create a floating point that is not attached to the mesh itself.</p>

---

## Post #2 by @muratmaga (2024-04-17 19:00 UTC)

<p>Unless the axis of the scan is in line with your anatomical planes, you cannot do what you describe by simplify editing the coordinates.</p>
<p>Even than it may not be possible. Imagine a case where the body of the mandible is curving medially. A point on the lateral side of the carnassial would be on space when projected straight downwards.</p>
<p>What are you trying to achieve by doing this?</p>

---

## Post #3 by @CanidMorpho (2024-04-17 19:15 UTC)

<p>I appreciate your reply! I had considered this may be the case, but I wanted to ask in case there was some way to ensure alignment in a particular plane.</p>
<p>The original intent behind this was to recreate a landmarking protocol established by Dr. Julie Meachen [10.1002/ece3.2141] in 3D shape space, but after landmarking my own specimens in Slicer, it seems to me that using a curve anchored on anatomical landmarks to capture the shape of the mandible would make more sense. The issue then becomes the inability to export curves and control points in the same file, but that is not an insurmountable issue.</p>

---

## Post #4 by @muratmaga (2024-04-17 19:55 UTC)

<aside class="quote no-group" data-username="CanidMorpho" data-post="3" data-topic="35566">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/779978/48.png" class="avatar"> CanidMorpho:</div>
<blockquote>
<p>landmarking protocol established by Dr. Julie Meachen [10.1002/ece3.2141] in 3D shape space</p>
</blockquote>
</aside>
<p>No, those won’t work in 3D space. And they barely work for 2D (you assume you aligned all the mandibles during the photography in exactly the same way, which is a very strong assumption).</p>
<p>We have developed a lot of methods to do landmarking in 3D Slicer via SlicerMorph. Please check those: <a href="https://github.com/SlicerMorph/Tutorials">SlicerMorph/Tutorials: SlicerMorph module tutorials (github.com)</a></p>

---
