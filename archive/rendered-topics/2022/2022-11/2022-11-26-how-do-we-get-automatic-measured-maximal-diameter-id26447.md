# How do we get automatic measured maximal diameter?

**Topic ID**: 26447
**Date**: 2022-11-26
**URL**: https://discourse.slicer.org/t/how-do-we-get-automatic-measured-maximal-diameter/26447

---

## Post #1 by @chendong9416 (2022-11-26 05:20 UTC)

<p>After the segmentation of the aorta and centerline extraction, how can we get the maximal diameter of the aorta along the centerline curve automatically? is it available now in the 3D slicer?</p>

---

## Post #2 by @chendong9416 (2022-11-26 06:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/604503ed5d93a08ba575a66653af3cf422d5caa2.jpeg" data-download-href="/uploads/short-url/dJDHvU9HgkSgLj8Asdbr6PuxcwW.jpeg?dl=1" title="0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/604503ed5d93a08ba575a66653af3cf422d5caa2_2_690x326.jpeg" alt="0" data-base62-sha1="dJDHvU9HgkSgLj8Asdbr6PuxcwW" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/604503ed5d93a08ba575a66653af3cf422d5caa2_2_690x326.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/604503ed5d93a08ba575a66653af3cf422d5caa2_2_1035x489.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/604503ed5d93a08ba575a66653af3cf422d5caa2_2_1380x652.jpeg 2x" data-dominant-color="ABAAAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0</span><span class="informations">1920×908 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Is the circular equivalent (CE) diameter means the maximal diameter at the cross-section?</p>

---

## Post #3 by @lassoan (2022-11-26 16:03 UTC)

<aside class="quote no-group" data-username="chendong9416" data-post="1" data-topic="26447">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chendong9416:</div>
<blockquote>
<p>is it available now in the 3D slicer?</p>
</blockquote>
</aside>
<p>You can get the maximum cross-sectional area in Cross-section analysis module in VMTK extension.</p>
<aside class="quote no-group" data-username="chendong9416" data-post="2" data-topic="26447">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chendong9416:</div>
<blockquote>
<p>Is the circular equivalent (CE) diameter means the maximal diameter at the cross-section?</p>
</blockquote>
</aside>
<p>No, it is the diameter of the circle that had the same surface area that the cross-sectional area of the vessel.</p>

---

## Post #4 by @chendong9416 (2022-11-27 03:46 UTC)

<p>Thanks for your reply.</p>

---

## Post #5 by @Joe_Makoid (2024-09-27 19:16 UTC)

<p>Hello,</p>
<p>I am doing something similar as <a class="mention" href="/u/chendong9416">@chendong9416</a>. I am segmenting the entire aorta and running a centerline extraction then analyzing it in cross-section analysis module.</p>
<p>The MIS diameter and CE diameter seem to be materially different at some locations (specifically at the arch it seems). Do you know which one is more accurate? At first glance, it looks like CE is more accurate, except when you get to the arch it measures a plane that isn’t perfectly perpendicular to the centerline and therefore overestimates the true diameter.</p>
<p>Would love to know the thoughts of an expert on this!!</p>

---

## Post #6 by @lassoan (2024-10-17 05:44 UTC)

<p>Both MIS and CE diameters are accurate. They measure different properties. See some more details in this discussion:</p>
<aside class="quote" data-post="3" data-topic="38572">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joe_makoid/48/78065_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/aortic-diameter-measurement-mis-or-ce-more-accurate/38572/3">Aortic Diameter Measurement - MIS or CE more accurate?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    awesome! Thank you <a class="mention" href="/u/lassoan">@lassoan</a> 
I am sort of getting it (I think(…i guess my question is, is it possible for the CE to be “tricked” in the aortic arch and not taking a measurement that is perpendicular to the centerline? (the true aortic diameter)…is the only way to truly get the max aortic diameter to straighten it somehow? 
thanks so much!!
  </blockquote>
</aside>


---
