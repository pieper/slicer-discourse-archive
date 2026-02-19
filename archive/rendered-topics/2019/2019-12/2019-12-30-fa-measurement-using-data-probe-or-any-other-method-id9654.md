---
topic_id: 9654
title: "Fa Measurement Using Data Probe Or Any Other Method"
date: 2019-12-30
url: https://discourse.slicer.org/t/9654
---

# FA measurement using data probe or any other method

**Topic ID**: 9654
**Date**: 2019-12-30
**URL**: https://discourse.slicer.org/t/fa-measurement-using-data-probe-or-any-other-method/9654

---

## Post #1 by @HariES (2019-12-30 06:15 UTC)

<p>How to measure fractional anisotropy in roi after creating scalar maps.</p>

---

## Post #2 by @pieper (2019-12-30 14:28 UTC)

<p>Yes, just mouse of over the slice view when FA volume is visible and you can see the FA value.  Or you can segment the area of interest and use the Segment Statistics module to get mean, min, max, etc.</p>

---

## Post #3 by @HariES (2020-02-15 18:35 UTC)

<p>Dear sir</p>
<p>Thank you and some times FA value appears and sometimes not. What is the problem.<br>
Segmentation in different slices is not appearing and it accepts only one slice.</p>

---

## Post #4 by @pieper (2020-02-16 00:43 UTC)

<p>Hi - you’ll need to give more information in order for use to help you.  Maybe include screenshot or two.  Also give more details about where you got the data, what format it is in (as best you know), what you tried, what you expected, and what happened instead.</p>

---

## Post #5 by @HariES (2020-02-17 11:41 UTC)

<p>FAvalues not calculated properly. What is the error.<br>
Screenshot attached.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e177613b2b14c56c37a320972a33dc28d13a635.jpeg" data-download-href="/uploads/short-url/20EWU1bPcbOuTmXwzxXW7UR6SLr.jpeg?dl=1" title="dtifa" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e177613b2b14c56c37a320972a33dc28d13a635_2_690x366.jpeg" alt="dtifa" data-base62-sha1="20EWU1bPcbOuTmXwzxXW7UR6SLr" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e177613b2b14c56c37a320972a33dc28d13a635_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e177613b2b14c56c37a320972a33dc28d13a635_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0e177613b2b14c56c37a320972a33dc28d13a635_2_1380x732.jpeg 2x" data-dominant-color="8F8F90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dtifa</span><span class="informations">1920×1020 703 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @emma1201 (2022-03-26 07:44 UTC)

<p>Hi! Apologies for continuing this conversation. I have created an FA Scalar Map using Diffusion &gt; Quantify &gt; Diffusion Tensor Scalar Maps and can see the FA using data probe. Is this the FA per voxel?</p>
<p>I also want to find out how to get FA metrics from the Segment Statistics module – do the mean, min, max refer to the FA of the segmented area?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/156b11043dde5c26fbad89987eedc74672618873.png" alt="image" data-base62-sha1="33tpM5qjjmhrNJT8heyDTALMUqn" width="684" height="95"></p>

---

## Post #7 by @pieper (2022-03-26 14:00 UTC)

<aside class="quote no-group" data-username="emma1201" data-post="6" data-topic="9654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/9f8e36/48.png" class="avatar"> emma1201:</div>
<blockquote>
<p>see the FA using data probe. Is this the FA per voxel?</p>
</blockquote>
</aside>
<p>Yes, it is.</p>
<aside class="quote no-group" data-username="emma1201" data-post="6" data-topic="9654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/9f8e36/48.png" class="avatar"> emma1201:</div>
<blockquote>
<p>FA metrics from the Segment Statistics module – do the mean, min, max refer to the FA of the segmented area?</p>
</blockquote>
</aside>
<p>Yes again.</p>

---

## Post #8 by @emma1201 (2022-03-26 17:01 UTC)

<p>Thank you so much for the very quick reply! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
