# Runtime of SegmentMesher

**Topic ID**: 10193
**Date**: 2020-02-10
**URL**: https://discourse.slicer.org/t/runtime-of-segmentmesher/10193

---

## Post #1 by @Aep93 (2020-02-10 20:07 UTC)

<p>Hello all,<br>
Is there any way to speed up generating mesh using SegmentMesher?<br>
Is it possible to use GPU for these calculations or is it possible to run in parallel? or are there any other suggestions?<br>
Thanks for your help.</p>

---

## Post #2 by @lassoan (2020-02-11 00:28 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="1" data-topic="10193">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>Is there any way to speed up generating mesh using SegmentMesher?</p>
</blockquote>
</aside>
<p>Volumetric meshing is typically not a time-constrained task, so processing time is usually not a priority when developing meshing algorithms.</p>
<p>Cleaver2 is actually a very fast method and it is nicely configurable to balance between mesh resolution, quality, and processing time.</p>
<aside class="quote no-group" data-username="Aep93" data-post="1" data-topic="10193">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>Is it possible to use GPU for these calculations or is it possible to run in parallel? or are there any other suggestions?</p>
</blockquote>
</aside>
<p>GPU (or many-core CPU) can only make an algorithm faster if you can split the processing to many independent tasks. Unfortunately, most algorithms are sequential in nature and you need to make significant effort to redesign them to allow running some parts of it in parallel.</p>
<p>I would recommend to contact the Cleaver team about possible performance optimizations and/or do some profiling yourself and see if you can make things run faster.</p>

---

## Post #3 by @Aep93 (2020-02-11 01:50 UTC)

<p>Thank you very much for your response.</p>

---
