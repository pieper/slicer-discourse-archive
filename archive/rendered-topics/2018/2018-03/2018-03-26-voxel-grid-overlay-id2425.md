# Voxel grid overlay

**Topic ID**: 2425
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/voxel-grid-overlay/2425

---

## Post #1 by @fedorov (2018-03-26 13:56 UTC)

<p>Is it possible to toggle overlay of the voxel grid in slice views?</p>
<p>I think this is a feature that was available long time ago in Slicer 3. I think it can be quite helpful in some corner use cases (one of which I’ve just encountered!).</p>

---

## Post #2 by @pieper (2018-03-26 14:20 UTC)

<p>Yes, there was a voxel grid in Slicer3, but was never ported forward.  Mostly I find that turning off interpolation of the volume is good enough.  What’s the corner case?</p>

---

## Post #3 by @fedorov (2018-03-26 14:39 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="2425">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>What’s the corner case?</p>
</blockquote>
</aside>
<p>Counting voxels for debugging pixel data encoding.</p>

---

## Post #4 by @pieper (2018-03-26 14:55 UTC)

<p>I think the DataProbe should help.  Or if you access the volume as an array and put unique values in each voxel it could help.</p>

---

## Post #5 by @fedorov (2018-03-26 15:18 UTC)

<p>Oh, it definitely helps, and I can use the IJK reported in DataProbe for counting, I can also write a script outside of Slicer to help me. It’s by no means a stopper for me, but it is a nice feature that can be useful in some cases, and apparently was deemed helpful in Slicer 3.</p>
<p>Anyway, sounds like at the moment the answer to my original question is “no”.</p>
<p>Thanks!</p>

---
