---
topic_id: 938
title: "Major Slice Scrolling Performance Degradation With Volume Re"
date: 2017-08-24
url: https://discourse.slicer.org/t/938
---

# Major slice scrolling performance degradation with volume rendering on

**Topic ID**: 938
**Date**: 2017-08-24
**URL**: https://discourse.slicer.org/t/major-slice-scrolling-performance-degradation-with-volume-rendering-on/938

---

## Post #1 by @fedorov (2017-08-24 18:04 UTC)

<p>There appears to be order of magnitude (from ~15 ms/frame to ~150 ms/frame) degradation in slice scrolling performance when volume rendering is enabled (slice is not shown in 3d view).</p>
<p>See demo in this screencast: <a href="https://www.screencast.com/t/fJ9O9N2El">https://www.screencast.com/t/fJ9O9N2El</a></p>
<p>This was done on a mac with the latest nightly.</p>

---

## Post #2 by @jcfr (2017-08-24 18:43 UTC)

<p>Are you able to reproduce the problem when building against Qt5 ? (which will enable VTK8 and the latest OpenGL backend)</p>

---

## Post #3 by @fedorov (2017-08-24 18:47 UTC)

<p>I can try this after Friday (or Friday afternoon).</p>

---

## Post #4 by @fedorov (2017-08-24 18:48 UTC)

<p>The reason you get all those reports from me is that I am preparing for a tutorial, which I plan to dry-run tomorrow morning, and I report things as they show up … I hope this is helpful.</p>

---

## Post #5 by @jcfr (2017-08-24 19:33 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I am preparing for a tutorial, which I plan to dry-run tomorrow morning, and I report things as they show up</p>
</blockquote>
</aside>
<p>That is great. Then, we will be in good shape for the next release</p>

---

## Post #6 by @chir.set (2017-08-25 06:28 UTC)

<p>The performance drop is the same in Qt5. If ‘Quality control’ is set to maximum, it’s even more noticeable.</p>

---

## Post #7 by @lassoan (2017-08-25 13:46 UTC)

<p>I’ve entered a ticket to track the resolution of this issue:<br>
<a href="https://issues.slicer.org/view.php?id=4423" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=4423</a></p>

---
