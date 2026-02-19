---
topic_id: 5104
title: "Calculating The Total Volume Of Organ Which Is Placed In Two"
date: 2018-12-17
url: https://discourse.slicer.org/t/5104
---

# Calculating the total volume of organ which is placed in two radiation fields

**Topic ID**: 5104
**Date**: 2018-12-17
**URL**: https://discourse.slicer.org/t/calculating-the-total-volume-of-organ-which-is-placed-in-two-radiation-fields/5104

---

## Post #1 by @aseman (2018-12-17 06:45 UTC)

<p>Slicer version:4.8.1<br>
Hi 3D slicer Experts and all<br>
I have a lung model and two radiation fields . I want to calculate the total lung volume which is irradiated in the radiation fields. My problem is that part of lung is placed in the one beam and another part is in the other beam. How can I calculate this total irradiated lung volume?<br>
<span class="hashtag-raw">#For</span> this purpose I intersected the lung model and first beam, using Segment Editor module( Logical Operators , Intersect) ; then separately , intersected the lung model with second beam (like below figure). At last I added the results of two previous steps together. Is this method true?<br>
Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f22222eaaf06890e829f9f2c1c0a1745edbaf8e.png" data-download-href="/uploads/short-url/mHL30AzGZG63m0f3sWcIw5B2QSa.png?dl=1" title="picture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f22222eaaf06890e829f9f2c1c0a1745edbaf8e_2_690x421.png" alt="picture" data-base62-sha1="mHL30AzGZG63m0f3sWcIw5B2QSa" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f22222eaaf06890e829f9f2c1c0a1745edbaf8e_2_690x421.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f22222eaaf06890e829f9f2c1c0a1745edbaf8e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f22222eaaf06890e829f9f2c1c0a1745edbaf8e.png 2x" data-dominant-color="1B1B1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture</span><span class="informations">801×489 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @aseman (2018-12-24 07:33 UTC)

<p>Hi<br>
Unfortunately, I did not receive any feedback about my question ! Can you help me and tell that the method I used , is true or not ?<br>
Thanks a lot</p>

---

## Post #3 by @lassoan (2018-12-27 06:46 UTC)

<aside class="quote no-group" data-username="aseman" data-post="1" data-topic="5104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>At last I added the results of two previous steps together. Is this method true?</p>
</blockquote>
</aside>
<p>Yes, what you described seems to be a good approach. If the segments that you created look correct in slice and 3D views then the computed volume will be correct and meaningful, too.</p>

---
