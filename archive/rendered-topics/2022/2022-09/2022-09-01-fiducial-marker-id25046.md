# Fiducial Marker

**Topic ID**: 25046
**Date**: 2022-09-01
**URL**: https://discourse.slicer.org/t/fiducial-marker/25046

---

## Post #1 by @Mohammad (2022-09-01 20:34 UTC)

<p>Operating system: 10<br>
Slicer version: 4.6</p>
<p>Dear All,</p>
<p>I would be grateful if anyone could help me with how I can add some spherical fiducial<br>
(Green and Red spheres) (as in the below image) to my CT volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69c4be878ad469f6cf8615bec2fd12dab5f5f10a.png" alt="image" data-base62-sha1="f5FEJAuCEAlYu0FinJoM8b6nVoe" width="259" height="266"></p>

---

## Post #2 by @ebrahim (2022-09-01 21:28 UTC)

<p>One approach is to make point fiducials display as larger spheres by manipulating glyph size under “Display” in the markups module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b86a063f708e77f531a50aa32270d9cc5cb48ea7.png" data-download-href="/uploads/short-url/qjp0FwQCLhh3yZBRUbGkKTXciXB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b86a063f708e77f531a50aa32270d9cc5cb48ea7_2_690x189.png" alt="image" data-base62-sha1="qjp0FwQCLhh3yZBRUbGkKTXciXB" width="690" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b86a063f708e77f531a50aa32270d9cc5cb48ea7_2_690x189.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b86a063f708e77f531a50aa32270d9cc5cb48ea7_2_1035x283.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b86a063f708e77f531a50aa32270d9cc5cb48ea7.png 2x" data-dominant-color="C8C5D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1041×286 36.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2022-09-02 05:35 UTC)

<aside class="quote no-group" data-username="Mohammad" data-post="1" data-topic="25046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e274bd/48.png" class="avatar"> Mohammad:</div>
<blockquote>
<p>Slicer version: 4.6</p>
</blockquote>
</aside>
<p>You are also using a very outdated version of Slicer. You would do yourself a favor if you move to the current stable (5.0.3)</p>

---

## Post #4 by @Mohammad (2022-09-02 15:26 UTC)

<p>Hi.<br>
Because of some modules, I had to use this version. After trial and error, I could find how to insert these fiducials, now I need to know how can I insert some “Planes”. Please see the below images.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3451cd07a7af543ea65cfd3b46f71e0dc51cf7c9.png" alt="image" data-base62-sha1="7sQ5kT4xQAwX67Z9VuqgUcXvklH" width="262" height="258"></p>

---

## Post #5 by @lassoan (2022-09-02 21:05 UTC)

<p>The planes are computed automatically by the module from the points (and maybe also a ruler line or region of interest - ROI - box).</p>

---
