# How to change slider position from top side to Right side

**Topic ID**: 21671
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/how-to-change-slider-position-from-top-side-to-right-side/21671

---

## Post #1 by @Dwij_Mistry (2022-01-28 09:46 UTC)

<p>Hi,</p>
<p>I am trying to change the slice view controller’s slider position from top side to right side of the slice view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5643d0d08d27d1a9c76efe20fd180a12cd3028a.jpeg" data-download-href="/uploads/short-url/sacOWlQ5nFpgTibPghgutr3qlJg.jpeg?dl=1" title="slider orientation change" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5643d0d08d27d1a9c76efe20fd180a12cd3028a_2_689x448.jpeg" alt="slider orientation change" data-base62-sha1="sacOWlQ5nFpgTibPghgutr3qlJg" width="689" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5643d0d08d27d1a9c76efe20fd180a12cd3028a_2_689x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5643d0d08d27d1a9c76efe20fd180a12cd3028a_2_1033x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5643d0d08d27d1a9c76efe20fd180a12cd3028a.jpeg 2x" data-dominant-color="555663"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slider orientation change</span><span class="informations">1346×874 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>as I can understand, this slice controller is coming from CTK.</p>
<p>Is there any way to make slice controller on right side?</p>

---

## Post #2 by @jamesobutler (2022-01-28 12:46 UTC)

<p>I see this type of thing was asked recently in <a href="https://discourse.slicer.org/t/how-to-change-view-controller-slider-horizontal-to-vertical/21350" class="inline-onebox">How to change view controller slider horizontal to vertical</a>.</p>
<p>Short answer is there is no easy way to implement this. There will be lots of hacking to move just the slider into a vertical orientation but leave other slice controller widgets in horizontal orientation.</p>
<p>Can you describe why you want to change the slider position? You want to change this for all slice views or only certain slice views?</p>

---

## Post #3 by @lassoan (2022-01-28 23:36 UTC)

<p>This could help in preserving the valuable vertical workspace and look more familiar to users, as slice scrolling is done with vertical scrollbar in most other software: MIMICS, ITK-Snap, Weasis, OHIF, etc. (MITK and OsiriX does not offer a scrollbar for slice browsing). So, it could worth some effort investigating this.</p>
<p>My concern would be that there would no be space for the other information that is currently in the slice view header (pin, view label, center, maximize, slider, orientation label, offset value, unit) in a vertical layout. Therefore, this information would need to be displayed over the image (again, as usual in other software). Slicer used to show this information over slice views but then moved out into the Data Probe because font rendering 10 years ago was a performance bottleneck. Nowadays probably the rendering time would not cause visible slowdowns.</p>
<p>Therefore, before we can think about moving the slider, we would need to improve corner annotations so that the slice label, offset value, etc. can be displayed there. Corner annotations are currently managed by the DataProbe scripted module in a quite messy way, so we would need to clean it up as a first step (make it more configurable, probably low-level parts into C++, etc.).</p>

---

## Post #4 by @Dwij_Mistry (2022-01-29 09:56 UTC)

<p>I am completely agreed with <a class="mention" href="/u/lassoan">@lassoan</a><br>
its easy to work with right side slider than slider on top side.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147ab08b9b003214fbb42b8661e9158bc821145d.png" data-download-href="/uploads/short-url/2VapsQjFE8MKlYrRJSUhUHfrLml.png?dl=1" title="Screenshot (65)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147ab08b9b003214fbb42b8661e9158bc821145d_2_385x500.png" alt="Screenshot (65)" data-base62-sha1="2VapsQjFE8MKlYrRJSUhUHfrLml" width="385" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147ab08b9b003214fbb42b8661e9158bc821145d_2_385x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147ab08b9b003214fbb42b8661e9158bc821145d_2_577x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147ab08b9b003214fbb42b8661e9158bc821145d.png 2x" data-dominant-color="3E3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (65)</span><span class="informations">668×867 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @jamesobutler (2022-01-29 13:10 UTC)

<p>Interesting. I think I would find it more difficult to left-click and drag my mouse forward/backward to change slice offset then it would be to left-click and drag my mouse left/right.</p>
<p>My assumption would be that a vertical slider would discourage left-click and drag of a mouse and instead rely more on the usage of mouse scroll wheel instead?</p>

---

## Post #6 by @rbumm (2022-01-29 15:00 UTC)

<p>What we currently have in the GE PACS Centricity Universal Viewer at KSGR is (scrolling):</p>
<p>CTRL+Left mouse button hold, and move the mouse above or below “horizon”  → <br>
this keeps scrolling a CT series back and forth very nicely.</p>
<p>Sliders are vertical.</p>

---

## Post #7 by @pieper (2022-01-29 15:05 UTC)

<p>I know of other systems with ‘hot’ annotations, for example when clicking and dragging the slice offset number it becomes a slider that disappears when you release the mouse.  I like that this approach reduces clutter.  Some systems also have hot corners to bring up global or view-specific menus or toolbars.</p>

---

## Post #8 by @lassoan (2022-01-29 16:27 UTC)

<p>Hot corners and annotations are great for software that people must regularly use (e.g., clinical image review workstations), but bad for newcomers or occasional users (hard to discover the features). It is also harder to render nice GUI widgets over the image (if Qt widgets are used then there could be rendering complications; VTK or custom-designed widgets tend to look very ugly). But since most software dump a lot of information over the image, it is kind of the expected look&amp;feel in medical image viewers.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="21671">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I think I would find it more difficult to left-click and drag my mouse forward/backward to change slice offset then it would be to left-click and drag my mouse left/righ</p>
</blockquote>
</aside>
<p>For left-right direction your only option is to move your wrist, so you can easily cover large range, but it is always inaccurate. For up-down direction you first move your fingers, so it is very precise, and if needed then you lift up your wrist and can do larger range imprecise motion. So, for me vertical motion for scrolling makes sense.</p>
<hr>
<p>So, overall, moving towards more annotations over the image and vertical scrolling could be marginally better than what we have. However, I’m not sure if it is better enough to justify relearning for existing users (so vertical/horizontal scrollbar would should be an option), and would not be the highest priority among the possible usability improvements. If there are developers willing to spend some time with this and prototype a vertical scrollbar option and more DataProbe rework then we would be happy to help.</p>

---

## Post #9 by @jamesobutler (2022-01-29 16:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="21671">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For left-right direction your only option is to move your wrist, so you can easily cover large range, but it is always inaccurate. For up-down direction you first move your fingers, so it is very precise, and if needed then you lift up your wrist and can do larger range imprecise motion. So, for me vertical motion for scrolling makes sense.</p>
</blockquote>
</aside>
<p>Seems like we have a difference here. I use the slider to make large changes in slice offset in a quick scout scan type navigation. While you seem to use the Slider for precise smaller changes in offset.</p>
<p>I typically use left/right mouse click on the slice offset slider to quickly move to find objects in a volume. Then I use mouse scrolling for precise changing of offsets. It takes too long to scroll through a large volume by just doing mouse scrolling.</p>

---

## Post #10 by @lassoan (2022-01-29 17:22 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="21671">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Seems like we have a difference here. I use the slider to make large changes in slice offset in a quick scout scan type navigation. While you seem to use the Slider for precise smaller changes in offset.</p>
</blockquote>
</aside>
<p>I just compared the vertical and horizontal scrollbars. Similarly to you, I rarely use the slider, and only for quick browsing (my main method for slice browsing is Shift + mouse move).</p>
<p>I’ve played with the vertical scrollbar in Weasis and I have mixed experience: it is easy to adjust vertically in a short range and it is precise, but browsing in a larger range is tedious (especially when the slider spans the entire vertical size of the screen).</p>
<p>Familiarity for users would be still a strong driver for offering the option to users. I don’t know any other application that uses horizontal scrollbar for slice browsing.</p>

---

## Post #11 by @pieper (2022-01-29 17:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="21671">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>hard to discover the features</p>
</blockquote>
</aside>
<p>I’m going to disagree here - hot corners can be very discoverable if there’s a hover effect that gives people a clue that something could be active.  But I do agree it can be hard to make these easy to use and nice looking.</p>

---
