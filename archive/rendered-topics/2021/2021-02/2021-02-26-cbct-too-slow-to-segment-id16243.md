---
topic_id: 16243
title: "Cbct Too Slow To Segment"
date: 2021-02-26
url: https://discourse.slicer.org/t/16243
---

# CBCT too slow to segment

**Topic ID**: 16243
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/cbct-too-slow-to-segment/16243

---

## Post #1 by @mohammed_alshakhas (2021-02-26 15:38 UTC)

<p>i noticed that segmenting CBCT is way slower than Medical CT although the latter being way smaller in size .</p>
<p>any suggestion to make segmenting CBCT  faster ?</p>
<p>thanks</p>

---

## Post #2 by @muratmaga (2021-02-26 16:21 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="16243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>segmenting CBCT is way slower than Medical CT although the latter being way smaller</p>
</blockquote>
</aside>
<p>If what you wrote is correct, i.e., CBCT is larger than the medical ct in size, yes, that’s expected. As the size of the volume increases more computation (and memory) is necessary to do the segmentations.</p>
<p>How big is your CBCT (image dimensions and data type)?</p>

---

## Post #3 by @mohammed_alshakhas (2021-02-26 16:23 UTC)

<p>im sorry i meant medical CT is bigger</p>

---

## Post #4 by @mohammed_alshakhas (2021-02-26 16:30 UTC)

<p>its 507 by 507 , that what is mentioned in size column</p>

---
