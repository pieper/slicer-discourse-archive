---
topic_id: 13420
title: "Image Quantization Techniques"
date: 2020-09-10
url: https://discourse.slicer.org/t/13420
---

# Image quantization techniques?

**Topic ID**: 13420
**Date**: 2020-09-10
**URL**: https://discourse.slicer.org/t/image-quantization-techniques/13420

---

## Post #1 by @hherhold (2020-09-10 12:46 UTC)

<p>We recently had a new detector installed in our micro-CT machine that has resulted in significantly higher dataset sizes (from 0.5-1.0GB to 10GB). While this is really nice from a resolution and dynamic range point of view, working with big datasets has its challenges.</p>
<p>Some studies need the full dynamic range (16 bit) and just need to use a beefy computer to work with the data, or crop off areas to minimize dimensions, etc. But there are a number of studies where you only care about simple thresholds - bone vs matrix, air vs tissue, etc. For these datasets, 8 bit data would be a big space saver and would likely not impact results.</p>
<p>I’ve been looking at using some of the unu utilities (quantize, histo, etc) with the idea of establishing the range of absorbance values to best preserve dynamic range when converting to 8 bit to reduce dataset size. It seems fairly clear that this (quantization and binning techniques) is probably a well-traveled road. Can anyone provide pointers on how they’ve done similar tasks and added them to their workflow?</p>
<p>Thanks in advance!!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-09-10 13:02 UTC)

<p>“Simple filters” module offers a number of filters intensity rescaling, which can be used for compressing dynamic range of the image. Try RescaleIntensityFilter, IntensityWindowingFilter, ShiftScaleImageFilter, etc.</p>
<p>You can get the currently displayed window/level (or min/max) value from Volumes module, Display section.</p>
<p>Going from 16 bits to 8 bits is just 2x memory reduction, though, so it might not worth the trouble. If you increase spacing along each axis by 3x then you get 27x reduction.</p>

---

## Post #3 by @hherhold (2020-09-10 13:27 UTC)

<p>Ah, ok - simple filters is a great idea, thanks! 2x reduction might not seem like a lot, but it’s enough to make the data useable.</p>
<p>Dumb question - can you convert 16 bit data to 8 bit data within Slicer? I’ve always used Fiji for this…</p>

---

## Post #4 by @lassoan (2020-09-10 13:30 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="13420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>can you convert 16 bit data to 8 bit data within Slicer?</p>
</blockquote>
</aside>
<p>You can use “Cast scalar volume” module (or CastImageFilter in Simple Filters module) to change scalar type of a volume (16-bit short to 8-bit char).</p>

---

## Post #5 by @hherhold (2020-09-10 13:32 UTC)

<p>Awesome! Thanks (again), Andras!</p>

---

## Post #6 by @tsehrhardt (2020-09-13 11:33 UTC)

<p>Here is a sequence of steps to correctly convert 16bit to 8bit: <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab11_SlicerPlusPlus#rescalecast" rel="nofollow noopener">https://github.com/SlicerMorph/W_2020/tree/master/Lab11_SlicerPlusPlus#rescalecast</a></p>

---

## Post #7 by @hherhold (2020-09-13 12:38 UTC)

<p>Oh, that’s perfect! Thanks very much!</p>
<p>-Hollister</p>

---

## Post #8 by @lassoan (2020-09-13 13:29 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="6" data-topic="13420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>Here is a sequence of steps to correctly convert 16bit to 8bit</p>
</blockquote>
</aside>
<p>This is very nice! I have submitted a <a href="https://github.com/SlicerMorph/W_2020/pull/7">pull request</a> with a few minor corrections.</p>

---

## Post #9 by @lassoan (2022-05-05 16:31 UTC)

<p>A post was split to a new topic: <a href="/t/compute-volume-in-image/23288">Compute volume in image</a></p>

---
