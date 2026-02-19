---
topic_id: 16133
title: "Transforming A Volume Makes It Disappear From Views"
date: 2021-02-22
url: https://discourse.slicer.org/t/16133
---

# Transforming a volume makes it disappear from views

**Topic ID**: 16133
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/transforming-a-volume-makes-it-disappear-from-views/16133

---

## Post #1 by @kanikayad15 (2021-02-22 12:52 UTC)

<p>Currently trying to register two tiff files. Loaded them both in and set them at 50% opacity. Then I went into the transform module and tried rotating/moving one of the images, but when I move certain settings one of the images disappears off the screen (even when I revert the settings) . I scrolled out in the view screen and it looked like the two images were in completely different locations in the space. Why does this occur and how can I correct it? I’ve tried loading the images in with the centered option as well but I still run into this tissue.<br>
If it’s relevant, I’m running Version 4.11.20200930 r29402 / 002be18 on a Mac.</p>

---

## Post #2 by @lassoan (2021-02-22 12:55 UTC)

<aside class="quote no-group" data-username="kanikayad15" data-post="1" data-topic="16133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kanikayad15/48/10026_2.png" class="avatar"> kanikayad15:</div>
<blockquote>
<p>I move certain settings one of the images disappears off the screen</p>
</blockquote>
</aside>
<p>What those certain settings were?</p>
<p>You can quickly and reliably <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">register images by placing a few landmarks</a>.</p>

---

## Post #3 by @kanikayad15 (2021-02-22 16:12 UTC)

<p>It varies per image pair but any of the translation or rotation sliders (LR, PA, IS) could result in this bug.</p>

---

## Post #4 by @lassoan (2021-02-22 17:02 UTC)

<p>Probably it is not a bug, but you move your images out from the slice view’s plane. If you work with 2D images then you can only translate along 2 axes and rotate around 1 axis without moving your image out of view.</p>
<p>If you want the view plane to follow the displayed image then you can use Volume reslice driver module (in SlicerIGT extension), but for registration you are much better off with using landmarks anyway.</p>

---
