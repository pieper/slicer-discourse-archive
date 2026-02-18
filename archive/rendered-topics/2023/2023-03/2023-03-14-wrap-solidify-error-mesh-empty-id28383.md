# Wrap Solidify error "mesh empty"

**Topic ID**: 28383
**Date**: 2023-03-14
**URL**: https://discourse.slicer.org/t/wrap-solidify-error-mesh-empty/28383

---

## Post #1 by @PixelTreason (2023-03-14 17:47 UTC)

<p>Hi, I am back again already, sorry!</p>
<p>I am trying to use wrap solidify to strip the skull of a CT and I am getting this error:<br>
“Wrap Solidify failed. Mesh has become empty during shrink-wrap iterations.”</p>
<p>I saw a post on the forums about this error from three years ago, but the answer then was to make sure they were using the stable version. As far as I know, I am already doing that. (version 5.2.2)</p>
<p>Anything else that might resolve this error? Again, I am incredibly grateful for any answers, Steve Pieper has already saved my butt once.</p>

---

## Post #2 by @PixelTreason (2023-03-14 22:43 UTC)

<p>Oh! I forgot to say, I was following the 3d Slicer segmentation recipes. Using the extensions SurfaceWrapSolidify and SegmentEditorExtraEffects.</p>

---

## Post #3 by @PixelTreason (2023-03-14 23:30 UTC)

<p>Oh my god, ignore me. I figured it out. It was my bad, entirely. I’m an idiot. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @durhame (2023-04-20 03:20 UTC)

<p>Hi, I must be making the same mistake, but I am not smart enough to figure out what I am doing wrong. I am getting this error on 5 out of 20 scans. Any advice?</p>

---

## Post #5 by @PixelTreason (2023-04-20 03:42 UTC)

<p>You can’t be doing what I did, I felt phenomenally stupid. It had already completed the task. I just thought it hadn’t because it doesn’t gray out the option so I kept clicking the button!</p>

---

## Post #6 by @lassoan (2023-04-20 03:56 UTC)

<aside class="quote no-group" data-username="durhame" data-post="4" data-topic="28383">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/839c29/48.png" class="avatar"> durhame:</div>
<blockquote>
<p>I am not smart enough to figure out what I am doing wrong. I am getting this error on 5 out of 20 scans. Any advice?</p>
</blockquote>
</aside>
<p>You can enable “Save intermediate results” option to see what goes wrong during the iterations.</p>

---
