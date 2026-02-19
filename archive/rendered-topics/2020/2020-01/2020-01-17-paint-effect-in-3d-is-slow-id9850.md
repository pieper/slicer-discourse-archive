---
topic_id: 9850
title: "Paint Effect In 3D Is Slow"
date: 2020-01-17
url: https://discourse.slicer.org/t/9850
---

# Paint effect in 3d is slow

**Topic ID**: 9850
**Date**: 2020-01-17
**URL**: https://discourse.slicer.org/t/paint-effect-in-3d-is-slow/9850

---

## Post #1 by @timeanddoctor (2020-01-17 12:35 UTC)

<p>Paint in 3d is too slow, but not the slice. However the speed of the paint seems be no associated with the scale of the brush. So can I paint many points(or times in 3d view) and then apply the segment just the last one?</p>

---

## Post #2 by @lassoan (2020-01-17 13:26 UTC)

<p>Paint in 3D is slower because it is often a computationally very hard task to accurately determine 3D position under the cursor. If you have volume rendering enabled or you have loaded a very complex model or segmentation then point picking in 3D view is expected to take noticeable time. What is your exact use case and how slow it is? (can you share a screen capture video?)</p>

---

## Post #3 by @timeanddoctor (2020-01-17 13:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443aab18d71fadbc5c2b6ab91ad158c8463518e1.gif" data-download-href="/uploads/short-url/9JAabKf44o8pcHLloUKXkWK3rCV.gif?dl=1" title="Video_2020-01-17_214328 (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/443aab18d71fadbc5c2b6ab91ad158c8463518e1_2_690x387.gif" alt="Video_2020-01-17_214328 (1)" data-base62-sha1="9JAabKf44o8pcHLloUKXkWK3rCV" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/443aab18d71fadbc5c2b6ab91ad158c8463518e1_2_690x387.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443aab18d71fadbc5c2b6ab91ad158c8463518e1.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443aab18d71fadbc5c2b6ab91ad158c8463518e1.gif 2x" data-dominant-color="7A7D7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Video_2020-01-17_214328 (1)</span><span class="informations">854×480 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-01-17 13:54 UTC)

<p>It seems that you have loaded a high-polygon-count model, which slows down point picking a lot. You can make it much smoother if you use decimate the model (with a decimation factor of 80-99%) using Surface Toolbox module. Alternatively, you can show the skin surface using GPU volume rendering (rendering may slow down but point picking on volume rendering should be much faster).</p>

---

## Post #5 by @timeanddoctor (2020-01-17 14:27 UTC)

<p>Thanks, lassoan, I used the Volume rendering for picking and the speed was perfecter. And another problem, what my purpose is just pick the surface points. Can I use a circle to collect the points?</p>

---

## Post #6 by @lassoan (2020-01-17 15:19 UTC)

<aside class="quote no-group" data-username="timeanddoctor" data-post="5" data-topic="9850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>And another problem, what my purpose is just pick the surface points. Can I use a circle to collect the points?</p>
</blockquote>
</aside>
<p>Please post this in a new topic and make it more clear and provide more details. I don’t know what circle you are referring to.</p>

---
