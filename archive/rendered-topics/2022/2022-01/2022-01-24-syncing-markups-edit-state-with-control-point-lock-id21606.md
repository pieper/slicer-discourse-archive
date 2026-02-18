# Syncing Markups edit state with control point lock

**Topic ID**: 21606
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/syncing-markups-edit-state-with-control-point-lock/21606

---

## Post #1 by @smrolfe (2022-01-24 22:35 UTC)

<p>Currently, when a point is locked, the Control Points table can be used to change the position status. If the state is accidentally changed to edit and the cursor enters the screen, the previous position will be lost. Since the points are manually locked when a user is finalizing a point position, it would seem more consistent if the option to change the control point state is deactivated for locked points.</p>
<p>Does this seem like a reasonable change?<br>
<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/ezgimercan">@ezgimercan</a> <a class="mention" href="/u/mikebind">@mikebind</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c2361231f11cef7306641844d936b1b2aed42ab.png" data-download-href="/uploads/short-url/6isO92Sq1Mp56PoWVBsgevUrd91.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c2361231f11cef7306641844d936b1b2aed42ab_2_488x500.png" alt="image" data-base62-sha1="6isO92Sq1Mp56PoWVBsgevUrd91" width="488" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c2361231f11cef7306641844d936b1b2aed42ab_2_488x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c2361231f11cef7306641844d936b1b2aed42ab_2_732x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c2361231f11cef7306641844d936b1b2aed42ab_2_976x1000.png 2x" data-dominant-color="E1E6EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×1092 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ezgimercan (2022-01-24 23:00 UTC)

<p>I’ve never noticed this behavior but I agree, it doesn’t make sense to change the position of a markup that’s locked. Previously, locking was a surrogate for finalizing a point.</p>
<p>Another behavior we’ve noticed and my students complained about is that you cannot jump to the position of a locked point by clicking on it on 3D rendering. You need to unlock it to click and jump. Since it is easy to move the point by accident when it’s unlocked, students hesitate to unlock and click a point to jump to its position. Was this behavior intentional? If not, is it possible to change it?</p>

---

## Post #3 by @smrolfe (2022-01-24 23:21 UTC)

<p>Thanks, <a class="mention" href="/u/ezgimercan">@ezgimercan</a> I am looking into a bug in the jump interaction described in this <a href="https://discourse.slicer.org/t/markups-jump-slices-functionality-is-broken-on-preview/21602/3">thread</a> and will take a look at this behavior too. I don’t believe it’s intentional.</p>

---

## Post #4 by @jamesobutler (2022-01-24 23:26 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="1" data-topic="21606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>it would seem more consistent if the option to change the control point state is deactivated for locked points.</p>
</blockquote>
</aside>
<p>Sure that seems fine to me. To be easy to understand it should be applied in a manner where if the control point is locked, the position status (edit, skip, restore, clear) can’t be changed at all.</p>
<p>If the control point is locked:</p>
<ul>
<li>and the position is defined, you can’t call to edit any of the states (edit, skip, restore, clear)</li>
<li>and the position is undefined, you can’t call to edit any of the states (edit, skip, restore, clear)</li>
</ul>
<p>I’m not sure how you plan to show this visual either in the right-click context menu of the control points table or the position status buttons that exist above the control point table. It could be confusing if the point is locked, then someone deliberately tries to clear the state for it and then nothing happens. The nothing happening part is confusing as no indication why nothing happens.</p>

---

## Post #5 by @Saima (2023-07-11 07:40 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="21606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>s fine to me. To be easy to understand it should be applied in a mann</p>
</blockquote>
</aside>
<p>how to lock each control point programatically? any script? what is the line of code to lock each individual and not the markupnode?</p>
<p>regards,<br>
Saima</p>

---
