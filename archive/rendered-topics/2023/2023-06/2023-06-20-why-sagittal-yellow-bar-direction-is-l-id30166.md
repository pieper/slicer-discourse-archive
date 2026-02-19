---
topic_id: 30166
title: "Why Sagittal Yellow Bar Direction Is L"
date: 2023-06-20
url: https://discourse.slicer.org/t/30166
---

# Why sagittal yellow bar direction is "L"?

**Topic ID**: 30166
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/why-sagittal-yellow-bar-direction-is-l/30166

---

## Post #1 by @mau_igna_06 (2023-06-20 23:35 UTC)

<p>Since Slicer uses RAS coordinate system I wonder why “L” letter is used on the yellow 2D slice view bar?<br>
Shouldn’t it be “R” (and also multiply the number by -1)?<br>
I was very confused by this while analyzing some image (see picture below). Could this letter be changed?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b23ecb4f9875ed2fa1fe19e459bd0d94cf6304d5.jpeg" data-download-href="/uploads/short-url/pqPwACOvPB0gh3iHW0h7aAmkndj.jpeg?dl=1" title="Captura desde 2023-06-20 20-33-39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b23ecb4f9875ed2fa1fe19e459bd0d94cf6304d5_2_690x388.jpeg" alt="Captura desde 2023-06-20 20-33-39" data-base62-sha1="pqPwACOvPB0gh3iHW0h7aAmkndj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b23ecb4f9875ed2fa1fe19e459bd0d94cf6304d5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b23ecb4f9875ed2fa1fe19e459bd0d94cf6304d5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b23ecb4f9875ed2fa1fe19e459bd0d94cf6304d5_2_1380x776.jpeg 2x" data-dominant-color="77777D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-06-20 20-33-39</span><span class="informations">1920×1080 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2023-06-21 00:11 UTC)

<p>This post should help:</p>
<aside class="quote quote-modified" data-post="8" data-topic="29883">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/a-bit-of-confusion-about-the-slicer-coordinate-system/29883/8">A bit of confusion about the slicer coordinate system</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In Edit-&gt;Application Settings you can change whether patient right is screen left or not. 
[image] 
That work came out of the following PR if you are curious about the conversation that led to it.
  </blockquote>
</aside>


---

## Post #3 by @mau_igna_06 (2023-06-21 12:58 UTC)

<p>Yeah, it’s related but I don’t want to change the axis directions just rename “L” to “R” and (multiply the value, I mean the number, by -1) so the all the views show a letter from RAS (the coordinate system)</p>

---

## Post #4 by @lassoan (2023-06-21 18:31 UTC)

<p>Changing the letters could make sense if they referred to coordinate values. See for example how coordinate values are always positive in the Data Probe (in the lower-left corner of the screen) and we change the coordinate system axis labels as we get from one side to the other.</p>
<p>However, those letters next to the slice offset sliders are <em>not coordinate system axis labels</em>, because they are not always aligned with any particular coordinate system axes. Since often volumes are axis aligned, you commonly see a single letter there and may think that it refers to a coordinate, but the letters actually specify the direction the slice plane moves if you drag the slider to the right (and it may consists of 1, 2, or 3 letters). This direction is independent from the position of the slice and so the letters don’t change when you move the slider.</p>

---

## Post #5 by @mau_igna_06 (2023-06-21 18:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="30166">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if you drag the slider to the right (and it may consists of 1, 2, or 3 letters). This direction is independent from the position of the slice and so the letters don’t change when you move the slider.</p>
</blockquote>
</aside>
<p>Please see the tooltip below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30a5db894bbcb88693940dd9ebae0a5c93aa9ba9.png" data-download-href="/uploads/short-url/6Wmgxtt5b6AmLmLFvBuLGAfQM4x.png?dl=1" title="Captura desde 2023-06-21 15-40-08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a5db894bbcb88693940dd9ebae0a5c93aa9ba9_2_690x395.png" alt="Captura desde 2023-06-21 15-40-08" data-base62-sha1="6Wmgxtt5b6AmLmLFvBuLGAfQM4x" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a5db894bbcb88693940dd9ebae0a5c93aa9ba9_2_690x395.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a5db894bbcb88693940dd9ebae0a5c93aa9ba9_2_1035x592.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30a5db894bbcb88693940dd9ebae0a5c93aa9ba9_2_1380x790.png 2x" data-dominant-color="242529"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-06-21 15-40-08</span><span class="informations">2498×1431 35.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Although if you see the other 2D views tooltips, they are crescent to the right. And the yellow one is crescent to the left.</p>
<p>It’s true that they might not represent the RAS coordinate system, but why not make the default direction letter labels as similar to RAS as possible?</p>
<p>A clinical review workflow of different CT series would never even use reslicing but offset, pan and zoom. And this use case maybe very popular. I think first-time users would expect to see an “R” instead of an “L” on the yellow view</p>

---

## Post #6 by @lassoan (2023-06-21 19:14 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="30166">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>It’s true that they might not represent the RAS coordinate system, but why not make the default direction letter labels as similar to RAS as possible?</p>
</blockquote>
</aside>
<p>It is because by default - according to current clinical conventions - “screen right is patient left”. You can can switch to “screen right is patient right” in Application settings / Views, but this choice is uncommon.</p>
<p>If you enable display of the slice in 3D views and you move the yellow slider then the yellow slice in the 3D view moves to the same direction.</p>

---
