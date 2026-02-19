---
topic_id: 40260
title: "Slices In 3D Views Are Blended With The Slice View Colour On"
date: 2024-11-19
url: https://discourse.slicer.org/t/40260
---

# Slices in 3D views are blended with the slice view colour on one side

**Topic ID**: 40260
**Date**: 2024-11-19
**URL**: https://discourse.slicer.org/t/slices-in-3d-views-are-blended-with-the-slice-view-colour-on-one-side/40260

---

## Post #1 by @chir.set (2024-11-19 09:48 UTC)

<p>Hello,</p>
<p>I just noticed this curious display. If we show  the red slice view in 3D, it looks as expected when looking from below, but is red tainted when looking from the top. That’s true for the other default slice views: normal on one side, tainted on the other side.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bf91747d12e3a402ea4accb8d0b0ffcd217c95e.gif" alt="Blended_Slice_View" data-base62-sha1="d7D7JiyJ8xVokW5Lr60dnUh41lk" width="586" height="500" class="animated"></p>
<p>Is it intended to distinguish the view point or does it need a fix?</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2024-11-19 13:40 UTC)

<p>Thanks for reporting this. I can replicate this in a recent preview build, but it doesn’t happen in 5.6.2.</p>
<p>I filed and issue: <a href="https://github.com/Slicer/Slicer/issues/8055" class="inline-onebox">Slices visible in 3D get color changes depending on view direction · Issue #8055 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @Sunderlandkyl (2024-11-19 18:51 UTC)

<p>Fixed in this PR: <a href="https://github.com/Slicer/Slicer/pull/8056" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix backface color on Slice nodes in 3D views by Sunderlandkyl · Pull Request #8056 · Slicer/Slicer · GitHub</a></p>

---

## Post #4 by @chir.set (2024-11-19 19:21 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="3" data-topic="40260">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>Fixed in this PR</p>
</blockquote>
</aside>
<p>Great, thank you.</p>
<p>[reaching 20 characters <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=14" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20">]</p>

---
