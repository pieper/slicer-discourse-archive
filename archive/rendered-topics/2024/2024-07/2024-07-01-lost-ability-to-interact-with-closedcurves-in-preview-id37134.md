---
topic_id: 37134
title: "Lost Ability To Interact With Closedcurves In Preview"
date: 2024-07-01
url: https://discourse.slicer.org/t/37134
---

# Lost ability to interact with closedCurves in preview

**Topic ID**: 37134
**Date**: 2024-07-01
**URL**: https://discourse.slicer.org/t/lost-ability-to-interact-with-closedcurves-in-preview/37134

---

## Post #1 by @muratmaga (2024-07-01 21:44 UTC)

<p>In the latest previews, I cannot seem to highlight a curve by hovering over it, if the curve is drawn on a model. This breaks the ability to add points to the curve in selected regions.</p>
<p>In the latest stable (5.6.2) this works as intended (see the screenshot that the color of the curve has changed to reflect active state).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f21c75f37262222343a35e55a5cd9c6404b9ab3.jpeg" data-download-href="/uploads/short-url/bi25DqQblLjBN6nxeit36ZpGRdp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f21c75f37262222343a35e55a5cd9c6404b9ab3_2_364x500.jpeg" alt="image" data-base62-sha1="bi25DqQblLjBN6nxeit36ZpGRdp" width="364" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f21c75f37262222343a35e55a5cd9c6404b9ab3_2_364x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f21c75f37262222343a35e55a5cd9c6404b9ab3_2_546x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f21c75f37262222343a35e55a5cd9c6404b9ab3_2_728x1000.jpeg 2x" data-dominant-color="A4A454"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1166×1598 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the latest preview, this functionality works, but only if the curve is not on a model. Is this behavior change intentional?</p>

---

## Post #2 by @muratmaga (2024-07-03 00:14 UTC)

<p>any comments on this issue?</p>

---

## Post #3 by @muratmaga (2024-08-28 05:14 UTC)

<p>Following on this, with more detail. The issue persists on all preview versions I tried on mac. It doesn’t require a model. To replicate:</p>
<ol>
<li>In 3D views, draw an S-shaped on curve using 5-6 control points</li>
<li>Move the pointer across the curve slowly and notice that every time the pointer is close the curve, it get highlighted as expected</li>
<li>Now turn curve 90 degree so you are looking it from the profile. Now try the same movement with pointer, and notice that curve is impossible to highlight. Note that control points doesn’t seem to get affected from this.</li>
<li>Bring back the curve to the original position, and notice that you cannot interact with it anymore (at least not easily and consistently).</li>
</ol>
<p>This is vanilla Slicer, no extensions installed.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #4 by @pieper (2024-08-28 12:30 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> any thoughts?</p>

---

## Post #5 by @cpinter (2024-08-28 12:57 UTC)

<p>I just tried it with yesterday’s preview on Windows, and the behavior is the same as what <a class="mention" href="/u/muratmaga">@muratmaga</a> described for Mac. What is strange is that sometimes the interaction is restored after a ot of changing view, rotating, etc, but for some curves the hover highlight is broken for good (for the same Slicer session). So it is quite undeterministic, except for the part that hover does not work if viewing a curve “from the profile”.</p>

---

## Post #6 by @Sunderlandkyl (2024-08-28 13:57 UTC)

<p>I think there is some pattern to the behavior. If you place a curve on the view plane in the 3D view, then you can still interact at any point along the curve with the curve. If the camera is rotated it is only possible to interact with the curve where it intersects with the view plane.</p>
<p>Curves placed on 3D models are also not interactable except where they intersect with the view plane.</p>
<p>I think this means that it may be related to picking and/or interaction distance.<br>
I’ll start looking into the issue.</p>

---

## Post #7 by @muratmaga (2024-08-28 19:36 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="6" data-topic="37134">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>If you place a curve on the view plane in the 3D view, then you can still interact at any point along the curve with the curve.</p>
</blockquote>
</aside>
<p>This isn’t the case in 5.6.2 though. Try my workflow with 5.6.2 and trying to interact with the curve in the profile view has no complications.</p>

---

## Post #8 by @Sunderlandkyl (2024-10-30 21:11 UTC)

<p>PR created here that should fix the issue: <a href="https://github.com/Slicer/Slicer/pull/8021" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix issue preventing interacting with Markups curves by Sunderlandkyl · Pull Request #8021 · Slicer/Slicer · GitHub</a>.</p>

---
