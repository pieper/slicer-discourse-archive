---
topic_id: 29181
title: "Link Dual Views With Relative Camera Position"
date: 2023-04-28
url: https://discourse.slicer.org/t/29181
---

# Link dual views with relative camera position

**Topic ID**: 29181
**Date**: 2023-04-28
**URL**: https://discourse.slicer.org/t/link-dual-views-with-relative-camera-position/29181

---

## Post #1 by @muratmaga (2023-04-28 00:35 UTC)

<p>I am not sure if title explains it what I want correctly. But here is the use case:</p>
<p>I have two models with different orientations, loaded into two 3D viewers. I would like to link the views such that when I rotate right skull, I would like the other rotate in the same way. This is current not possible, and I am not sure whether it is possible to do without having to register them.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeb43190b5ce21bc52bbb412e13803cc7d75947e.jpeg" data-download-href="/uploads/short-url/y3FHsF9c3qYU9F5so6ES0DECHdY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeb43190b5ce21bc52bbb412e13803cc7d75947e_2_635x500.jpeg" alt="image" data-base62-sha1="y3FHsF9c3qYU9F5so6ES0DECHdY" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeb43190b5ce21bc52bbb412e13803cc7d75947e_2_635x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeb43190b5ce21bc52bbb412e13803cc7d75947e_2_952x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeb43190b5ce21bc52bbb412e13803cc7d75947e.jpeg 2x" data-dominant-color="A49FB5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1159×912 64.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-04-28 13:41 UTC)

<p>It might be possible to implement a relative mode in camera linkage where the delta between the two cameras is recorded at the start and then always applied to each update.  I’m not sure how much work that would take.</p>
<p>I actually think just registering the two models to be basically in the same space would be the most straightforward.  I know that is hard to do with the rotate and translate sliders or direct manipulation, but since you have landmarks on these already it should be easy to do with a landmark transform.</p>
<p>This made me think of another mode that could be helpful: we could use the camera controls to align the two models in the views and then use the difference in camera parameters to calculate a transform to apply to one of the models for registration.  That might be more intuitive than the sliders or manipulators and would work when you didn’t have landmarks.</p>

---

## Post #3 by @muratmaga (2023-04-28 14:34 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="29181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I actually think just registering the two models to be basically in the same space would be the most straightforward.</p>
</blockquote>
</aside>
<p>This example just happened to have landmarks. Most often I do not have any.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="29181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>This made me think of another mode that could be helpful: we could use the camera controls to align the two models in the views and then use the difference in camera parameters to calculate a transform to apply to one of the models for registration. That might be more intuitive than the sliders or manipulators and would work when you didn’t have landmarks.</p>
</blockquote>
</aside>
<p>Yes, something like this what I had in mind. Once I bring objects the positions I would like to keep, there would a button or a something that will lock the relative position.</p>

---

## Post #4 by @pieper (2023-04-28 14:51 UTC)

<p>This should be pretty straightforward.  Get the translations from the centers of rotation  of the two camera views, and then the rotation from the vectors from these centers of rotation back to the camera and the up vectors.  I could imagine a little module for that would be quite doable.</p>

---

## Post #5 by @tsehrhardt (2023-04-29 01:03 UTC)

<p>If it’s helpful until this gets implemented in Slicer, you can link the viewers in Meshlab.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e096d0e90803d42d874fba2e64532cd6f96ee407.jpeg" data-download-href="/uploads/short-url/w2O4FpGl1VEq8X5emz1MeoRakdh.jpeg?dl=1" title="2023-04-28_21-02-19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e096d0e90803d42d874fba2e64532cd6f96ee407_2_690x377.jpeg" alt="2023-04-28_21-02-19" data-base62-sha1="w2O4FpGl1VEq8X5emz1MeoRakdh" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e096d0e90803d42d874fba2e64532cd6f96ee407_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e096d0e90803d42d874fba2e64532cd6f96ee407_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e096d0e90803d42d874fba2e64532cd6f96ee407_2_1380x754.jpeg 2x" data-dominant-color="676693"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-28_21-02-19</span><span class="informations">3832×2096 351 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d804c80d994ab24d97dbaf79b40747790dd3e84.jpeg" data-download-href="/uploads/short-url/kbMcxLwWOO6avm8onvfIrUKneXq.jpeg?dl=1" title="2023-04-28_21-01-26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d804c80d994ab24d97dbaf79b40747790dd3e84_2_690x377.jpeg" alt="2023-04-28_21-01-26" data-base62-sha1="kbMcxLwWOO6avm8onvfIrUKneXq" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d804c80d994ab24d97dbaf79b40747790dd3e84_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d804c80d994ab24d97dbaf79b40747790dd3e84_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d804c80d994ab24d97dbaf79b40747790dd3e84_2_1380x754.jpeg 2x" data-dominant-color="605F8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-28_21-01-26</span><span class="informations">3832×2096 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @muratmaga (2024-06-22 13:42 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="5" data-topic="29181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>until this gets implemented in Slicer,</p>
</blockquote>
</aside>
<p>For posterity this functionality is now available in the QuickAlign module of SlicerMorph. <a href="https://discourse.slicer.org/t/new-module-to-manually-align-3d-views/35634" class="inline-onebox">New module to manually align 3D views</a></p>
<p>You can align and link the view for volumes, models, and pointLists.</p>

---
