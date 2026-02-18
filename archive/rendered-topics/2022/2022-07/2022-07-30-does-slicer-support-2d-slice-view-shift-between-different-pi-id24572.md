# Does Slicer support 2d slice view shift between different pics whit mouse left key pressed and drag up and down?

**Topic ID**: 24572
**Date**: 2022-07-30
**URL**: https://discourse.slicer.org/t/does-slicer-support-2d-slice-view-shift-between-different-pics-whit-mouse-left-key-pressed-and-drag-up-and-down/24572

---

## Post #1 by @zhang_ming (2022-07-30 00:27 UTC)

<p>like radioAnt supported. we found that many doctors want to use Slicer with left mouse button pressed and drag up and down to shift betweeen  2d dicom pics.</p>

---

## Post #2 by @slicer365 (2022-07-30 06:12 UTC)

<p>Yes，this is a good ideal.</p>

---

## Post #3 by @zhang_ming (2022-07-30 12:43 UTC)

<p>yes, I wondering if we can add python code in .slicerrc.py file? that will be very convenient for doctor</p>

---

## Post #4 by @pieper (2022-07-30 14:16 UTC)

<p>This is very doable, either with some kind of code that overrides event processing, or more correctly by introducing a new mouse mode, like the window/level or fiducial placement modes.</p>
<p>At least for me, Slicer already provides a very efficient way to rapidly explore a slice stack (volume) using the <code>shift</code> key and mousing over orthogonal views.  But if people are used to other interfaces they are free to customize.</p>

---

## Post #5 by @zhang_ming (2022-07-31 02:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>At least for me, Slicer already provides a very efficient way to rapidly explore a slice stack (volume) using the <code>shift</code> key and mousing over orthogonal views. But if people are used to other interfaces they are free to customize.</p>
</blockquote>
</aside>
<p>I  want   to report a bug, using ‘shift’ and mouse moves in single max view , the pics won’t shift</p>

---

## Post #6 by @lassoan (2022-07-31 08:28 UTC)

<aside class="quote no-group" data-username="zhang_ming" data-post="5" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhang_ming/48/15790_2.png" class="avatar"> zhang_ming:</div>
<blockquote>
<p>I want to report a bug, using ‘shift’ and mouse moves in single max view , the pics won’t shift</p>
</blockquote>
</aside>
<p>Shift + mouse-move does not shift the current slice but all the others. So, when the view is maximized then you will not see any effect. You can still use the mouse wheel, cursor arrow keys, or page up/down keys to shift the current slice.</p>
<p>The reason for the different behavior is that 3D Slicer is a 3D-oriented software, so you don’t need to blindly browse slices by dragging in current view, but you can directly choose Slicer position in an orthogonal view. That said, to make slice browsing more convenient when only a single slice is displayed and to make Slicer more familiar to people who got used to use 2D-oriented image viewers, such as RadiANT, I agree that it would be a good idea to add a new mouse mode for slice browsing by left-click-and-drag.</p>

---

## Post #7 by @zhang_ming (2022-08-01 10:32 UTC)

<p>that will be great for doctors who familar with 2D dicom viewer to change to 3D Slicer, because some time they just need 2D mode for reading pics fast.</p>

---

## Post #8 by @zhang_ming (2022-08-01 10:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>a 3D-oriented software, so</p>
</blockquote>
</aside>
<p>will slicer add this left-click-and-drag shift fun in future version?</p>

---

## Post #9 by @chir.set (2022-08-01 11:38 UTC)

<aside class="quote no-group" data-username="zhang_ming" data-post="7" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhang_ming/48/15790_2.png" class="avatar"> zhang_ming:</div>
<blockquote>
<p>because some time they just need 2D mode for reading pics fast</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="zhang_ming" data-post="1" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhang_ming/48/15790_2.png" class="avatar"> zhang_ming:</div>
<blockquote>
<p>left mouse button pressed and drag up and down to shift betweeen 2d dicom pics</p>
</blockquote>
</aside>
<p>What’s wrong with the slider just at the top of each slice view widget ?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9f020320571e8c6d5cbc96ebb0420edbc1b065.png" alt="slider" data-base62-sha1="1WuSyhgKn3x5w8bH0gJhYnl30Dr" width="602" height="37"></p>
<p>The other way round :</p>
<p>If I switch to other viewing software, I would have preferred the slider bar instead, and perhaps requested it.</p>
<p>Doctors… doctors… <em>they</em> should really adapt to what’s available.</p>

---

## Post #10 by @zhang_ming (2022-08-01 12:25 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>adapt</p>
</blockquote>
</aside>
<p>LOL, I can’t agree more, but left-click-and-drag to shift is realllllly convenient</p>

---

## Post #11 by @pieper (2022-08-01 18:04 UTC)

<aside class="quote no-group" data-username="zhang_ming" data-post="8" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhang_ming/48/15790_2.png" class="avatar"> zhang_ming:</div>
<blockquote>
<p>will slicer add this left-click-and-drag shift fun in future version?</p>
</blockquote>
</aside>
<p>Probably not unless there’s a funded project that needs it or someone contributes the feature.</p>

---

## Post #12 by @zhang_ming (2022-08-02 06:56 UTC)

<p>ok，let me try, I want to contribute the feature</p>

---

## Post #13 by @zhang_ming (2022-08-09 13:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>contributes</p>
</blockquote>
</aside>
<p>I have finished this function, I will push my code this days.</p>

---

## Post #14 by @zhang_ming (2022-08-11 02:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="24572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>contributes</p>
</blockquote>
</aside>
<p>ok<br>
<a href="https://github.com/Slicer/Slicer/pull/6497/commits/e610afeff67f798fee9cc6b846254a87201eb5f7" rel="noopener nofollow ugc">Left Mouse ‘click-and-drag’ to shift between 2d pics test ok by simzhangbest · Pull Request #6497 · Slicer/Slicer (github.com)</a><br>
I have pull requsts ,but not approved, you can watch my code in the linke above, it’s not perfect, because when you use mouse to drag ,the direction changes won’t response rapidly, so is there any way to modify the function “<strong>ProcessIncDecSlice</strong>”, call for your help</p>

---

## Post #15 by @zhang_ming (2022-08-11 06:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76244ef4401ac8829e788cc10ee6866ccf1334ca.png" data-download-href="/uploads/short-url/gR88b98JHfm8aR6wJw2AsfTbilQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76244ef4401ac8829e788cc10ee6866ccf1334ca_2_690x261.png" alt="image" data-base62-sha1="gR88b98JHfm8aR6wJw2AsfTbilQ" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76244ef4401ac8829e788cc10ee6866ccf1334ca_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76244ef4401ac8829e788cc10ee6866ccf1334ca.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76244ef4401ac8829e788cc10ee6866ccf1334ca.png 2x" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">939×356 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
the key point in my code ,I think the deltaY should be caculated in other ways. can you offer me some suggestions?<br>
<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/chir.set">@chir.set</a></p>

---
