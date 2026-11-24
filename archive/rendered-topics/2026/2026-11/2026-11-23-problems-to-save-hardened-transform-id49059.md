---
topic_id: 49059
title: "Problems to save hardened transform"
date: 2026-11-23
url: https://discourse.slicer.org/t/49059
last_bumped: 2026-11-24T09:20:58.391Z
---

# Problems to save hardened transform

**Topic ID**: 49059
**Date**: 2026-11-23
**URL**: https://discourse.slicer.org/t/problems-to-save-hardened-transform/49059

---

## Post #1 by @Ugi_Mikla (2026-11-23 23:57 UTC)

<p>Hi, i opend a volume in version 5.4.0 and i intended to apply a linear transform and hardened it. when i save the hardened volume and reopened it, i find that it’s <strong>not exactly</strong> the way i wanted. Seems like I have a spatial issue or sth. i’m saving the file in .nrrd- I tried resampling the volume with the transformed and didn’t work.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=16" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20">  Thanks!</p>
<p>Eugenia</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13829d0bcf78f616313f02c0f6e6b8e688682437.jpeg" data-download-href="/uploads/short-url/2MAUpZSX4QcXjSF4mrpbI4Dux4X.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13829d0bcf78f616313f02c0f6e6b8e688682437_2_664x500.jpeg" alt="image" data-base62-sha1="2MAUpZSX4QcXjSF4mrpbI4Dux4X" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13829d0bcf78f616313f02c0f6e6b8e688682437_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13829d0bcf78f616313f02c0f6e6b8e688682437.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13829d0bcf78f616313f02c0f6e6b8e688682437.jpeg 2x" data-dominant-color="646363"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">871×655 85.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-11-24 06:12 UTC)

<aside class="quote no-group" data-username="Ugi_Mikla" data-post="1" data-topic="49059">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ugi_mikla/48/7603_2.png" class="avatar"> Ugi_Mikla:</div>
<blockquote>
<p>i opend a volume in version 5.4.0</p>
</blockquote>
</aside>
<p>As always, first you have to try with the latest stable version, 5.12.4.</p>
<p>If still replicates, please report again.</p>

---

## Post #3 by @philippepellerin (2026-11-24 09:20 UTC)

<p>Hi, did you check the orientation of the slices before hardening? You would have a different display whether you are in standard orientation or in reorientation mode. I had this issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a975b8a7b2819262597092a45cf58080922d9969.jpeg" data-download-href="/uploads/short-url/ob6Un8ZN7cQN0a9coKosAAy0mH7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a975b8a7b2819262597092a45cf58080922d9969_2_515x500.jpeg" alt="image" data-base62-sha1="ob6Un8ZN7cQN0a9coKosAAy0mH7" width="515" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a975b8a7b2819262597092a45cf58080922d9969_2_515x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a975b8a7b2819262597092a45cf58080922d9969_2_772x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a975b8a7b2819262597092a45cf58080922d9969_2_1030x1000.jpeg 2x" data-dominant-color="5B555D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1146×1112 47.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
