---
topic_id: 6904
title: "Disabling Object Transforms By Vr Controllers"
date: 2019-05-23
url: https://discourse.slicer.org/t/6904
---

# Disabling object transforms by VR controllers

**Topic ID**: 6904
**Date**: 2019-05-23
**URL**: https://discourse.slicer.org/t/disabling-object-transforms-by-vr-controllers/6904

---

## Post #1 by @drouin-simon (2019-05-23 18:56 UTC)

<p>Hi,</p>
<p>Is there a way to disable object transforms in VR, or to assign object transforms to a different button than world transform?</p>
<p>In the current implementation, it is very easy to transform an object by accident when the intent is to transform the world. This is particularly true when dealing with volume rendering, where the bounding box of the volume is usually bigger that the visible object.</p>
<p>My current workaround is to make all my objects non-selectable in subject hierarchy, but it is not very practical and has other unwanted consequences outside of VR.</p>

---

## Post #2 by @lassoan (2019-05-23 19:31 UTC)

<aside class="quote no-group" data-username="drouin-simon" data-post="1" data-topic="6904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drouin-simon/48/258_2.png" class="avatar"> drouin-simon:</div>
<blockquote>
<p>My current workaround is to make all my objects non-selectable in subject hierarchy, but it is not very practical</p>
</blockquote>
</aside>
<p>What do you mean? How would you make it more practical? Or you mean that the fact that you need to lock object is not practical? We are reworking widget event processing and part of it is to make it easy to remap interaction events to widget events.</p>
<aside class="quote no-group" data-username="drouin-simon" data-post="1" data-topic="6904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drouin-simon/48/258_2.png" class="avatar"> drouin-simon:</div>
<blockquote>
<p>unwanted consequences outside of VR</p>
</blockquote>
</aside>
<p>Selectable property is only used for virtual reality right now, so there are no other consequences.</p>

---

## Post #3 by @drouin-simon (2019-05-23 21:48 UTC)

<p>If the Selectable property is only ever used in VR, then this could be the way to go.</p>
<p>However, it doesn’t solve the case where you want an object to be selectable (so you don’t set the flag), but you want to avoid accidental selection when the user is transforming the point of view. At the moment, this happens often and it is too easy to make that mistake.</p>
<p>There are many ways to improve:</p>
<ul>
<li>Allow assignment of world and object motion to different buttons.</li>
<li>Give the user a few hundred milliseconds to press the second trigger before starting to transform.</li>
<li>Provide visual feedback when objects are selected for transforms. e.g. bounding box appears around the object.</li>
<li>Assign a button to undo the last object transform so that you don’t need to go out of VR to correct the mistake.</li>
<li>etc…</li>
</ul>

---

## Post #4 by @lassoan (2019-05-24 17:47 UTC)

<p>Thank you, all of these are good points.</p>
<aside class="quote no-group" data-username="drouin-simon" data-post="3" data-topic="6904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drouin-simon/48/258_2.png" class="avatar"> drouin-simon:</div>
<blockquote>
<p>Allow assignment of world and object motion to different buttons</p>
</blockquote>
</aside>
<p>This might already be the case - try grab and trigger buttons.</p>
<aside class="quote no-group" data-username="drouin-simon" data-post="3" data-topic="6904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drouin-simon/48/258_2.png" class="avatar"> drouin-simon:</div>
<blockquote>
<p>Provide visual feedback when objects are selected for transforms. e.g. bounding box appears around the object.</p>
</blockquote>
</aside>
<p>We plan to implement this.</p>
<aside class="quote no-group" data-username="drouin-simon" data-post="3" data-topic="6904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drouin-simon/48/258_2.png" class="avatar"> drouin-simon:</div>
<blockquote>
<p>Assign a button to undo the last object transform so that you don’t need to go out of VR to correct the mistake</p>
</blockquote>
</aside>
<p>Undo/redo infrastructure was disabled in Slicer because it was too complicated. We recently reviewed undo/redo infrastructure in Slicer and could fix it to work quite well. We could consider enabling undo/redo again.</p>

---
