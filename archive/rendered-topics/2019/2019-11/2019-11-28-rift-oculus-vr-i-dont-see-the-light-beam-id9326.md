# Rift oculus vr I dont see the light beam

**Topic ID**: 9326
**Date**: 2019-11-28
**URL**: https://discourse.slicer.org/t/rift-oculus-vr-i-dont-see-the-light-beam/9326

---

## Post #1 by @Jmarcs (2019-11-28 17:21 UTC)

<p>hello the team<br>
my new rift oculus work in 3d slicer but the headlines doesnt work with editor segment<br>
I can move the bone with them but i cant cut or use the other tools . and i dont see the light beam. I try everything. Do you have an idea<br>
best regards!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5db1f0ca3a25e6b7bda99893a7370e12a699f6a6.png" alt="2019-11-28_18h15_19" data-base62-sha1="dmRDIQnSYcV82eZzn5De6nB0bau" width="591" height="415"></p>

---

## Post #2 by @lassoan (2019-11-28 18:19 UTC)

<p>Light beam implementation in Slicer has not been completed yet.</p>
<p>The main interaction is grabbing and moving objects. It may not seem to be a lot, but it is actually very powerful, as moving an object modifies the associated transform node. Transform nodes can be used to move all objects, such as markup nodes, which are used as inputs by many modules; you can reslice volume (using Volume Reslice Driver module in SlicerIGT extension), you can also put multiple objects under the same transform in the scene to create groups; you can exclude objects from (disable selectable attribute), etc. You can get access to current position of the headset and controllers.</p>
<p>In addition to using transforms with you can also add observers to transforms and implement your own custom behavior. This is used by one of the forum members to implement segment editing in virtual reality.</p>

---

## Post #3 by @Jmarcs (2019-11-28 19:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Transform nodes can be used to move all objects, such as markup nodes, which are used as inputs by many modules; you can reslice volume (using Volume Reslice Driver module in SlicerIGT extension), you can also put multiple objects under the same transform in the scene to create groups; you can exclude objects from (disable selectable attribute), etc. You can get access to current position of the headset and controllers.</p>
</blockquote>
</aside>
<p>do you have avideo<br>
about Transform nodes can be used to move all objects, such as markup nodes, which are used as inputs by many modules; you can reslice volume (using Volume Reslice Driver module in SlicerIGT extension), you can also put multiple objects under the same transform in the scene to create groups; you can exclude objects from (disable selectable attribute), etc. You can get access to current position of the headset and controllers.</p>

---

## Post #4 by @lassoan (2019-11-28 19:15 UTC)

<p>Here are a few demo videos:</p>
<div class="lazyYT" data-youtube-id="rG9ST6xv6vg" data-youtube-title="Collaborative surgery planning in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<div class="lazyYT" data-youtube-id="F_UBoE4FaoY" data-youtube-title="Pedicle screw insertion in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If you have any specific question about how to do something then let us know.</p>

---

## Post #5 by @Jmarcs (2019-11-28 19:18 UTC)

<p>thanks i know these videos but  i dont understand<br>
you can also put multiple objects under the same transform in the scene to create groups; you can exclude objects from (disable selectable attribute), etc.</p>

---

## Post #6 by @lassoan (2019-11-28 19:22 UTC)

<p>These are described in this section of the SlicerVirtualReality extension documentation: <a href="https://github.com/KitwareMedical/SlicerVirtualReality#transform-objects">https://github.com/KitwareMedical/SlicerVirtualReality#transform-objects</a></p>

---

## Post #7 by @Jmarcs (2019-11-28 19:24 UTC)

<p>Thanks very much for your help. Your support is better than private Software. best regards</p>

---
