---
topic_id: 1820
title: "Segment Visibilities Are Not Saved In The Mrml File"
date: 2018-01-12
url: https://discourse.slicer.org/t/1820
---

# Segment visibilities are not saved in the mrml file

**Topic ID**: 1820
**Date**: 2018-01-12
**URL**: https://discourse.slicer.org/t/segment-visibilities-are-not-saved-in-the-mrml-file/1820

---

## Post #1 by @MMMPPPMMM (2018-01-12 14:39 UTC)

<p>I have a segmentation with two segments.<br>
I disable the visability of the 2nd segment in the data module.<br>
I save the scene.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c94aed85a7170ed829cc8ec22b2a8aebd22bc0c.png" data-download-href="/uploads/short-url/fuy7m3UmYK7OBEJclrG0XjJSi9m.png?dl=1" title="SlicerVisibilityBug" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c94aed85a7170ed829cc8ec22b2a8aebd22bc0c_2_598x499.png" alt="SlicerVisibilityBug" data-base62-sha1="fuy7m3UmYK7OBEJclrG0XjJSi9m" width="598" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c94aed85a7170ed829cc8ec22b2a8aebd22bc0c_2_598x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c94aed85a7170ed829cc8ec22b2a8aebd22bc0c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c94aed85a7170ed829cc8ec22b2a8aebd22bc0c.png 2x" data-dominant-color="D1D2D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerVisibilityBug</span><span class="informations">821×686 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If Ioad the scene again, both segments are visible</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df999bf0cfd888b1b899499cf387d321c9d9a24.png" data-download-href="/uploads/short-url/dplaDhAaqD34mZlUIaF0CUzkXty.png?dl=1" title="SlicerVisibilityBug2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df999bf0cfd888b1b899499cf387d321c9d9a24_2_682x500.png" alt="SlicerVisibilityBug2" data-base62-sha1="dplaDhAaqD34mZlUIaF0CUzkXty" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df999bf0cfd888b1b899499cf387d321c9d9a24_2_682x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df999bf0cfd888b1b899499cf387d321c9d9a24.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df999bf0cfd888b1b899499cf387d321c9d9a24.png 2x" data-dominant-color="C1C2C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerVisibilityBug2</span><span class="informations">851×623 87.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-01-12 15:43 UTC)

<p>Thanks for reporting this, I could reproduce it. Saving of visibility state is correct, but the information is ignored when the scene is loaded. I’ll try to fix this.</p>

---

## Post #3 by @lassoan (2018-01-13 03:40 UTC)

<p>Fix committed in revision 26831. Nightly builds are being reworked, so it may take a few days until a new nightly build is created.</p>

---

## Post #4 by @MMMPPPMMM (2018-01-17 13:19 UTC)

<p>Thank you. Seems to work.</p>
<p>But now the master volume information seems to be ignored?</p>

---

## Post #5 by @lassoan (2018-01-17 13:41 UTC)

<aside class="quote no-group" data-username="MMMPPPMMM" data-post="4" data-topic="1820">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>master volume information seems to be ignored?</p>
</blockquote>
</aside>
<p>What do you mean? What do you do, what do you expect to happen, and happens instead?</p>

---

## Post #6 by @MMMPPPMMM (2018-01-18 14:27 UTC)

<p>I have a scene with one CT volume and two segmentations.</p>
<p>I load the scene -&gt; Switch to Segment Editor -&gt; Switch to the 2nd segmentation</p>
<p>Then I have to select the master volume again, although it was previously selected before saving the scene.</p>

---

## Post #7 by @lassoan (2018-01-18 16:14 UTC)

<p>I cannot reproduce this, it all works well for me. Have you added segments to both segmentations? Can you upload the saved scene somewhere and post the link here?</p>

---
