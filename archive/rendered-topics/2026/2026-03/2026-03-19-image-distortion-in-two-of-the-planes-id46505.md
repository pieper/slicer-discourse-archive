---
topic_id: 46505
title: "Image Distortion In Two Of The Planes"
date: 2026-03-19
url: https://discourse.slicer.org/t/46505
---

# Image distortion in two of the planes

**Topic ID**: 46505
**Date**: 2026-03-19
**URL**: https://discourse.slicer.org/t/image-distortion-in-two-of-the-planes/46505

---

## Post #1 by @rainbow.jedi (2026-03-19 18:49 UTC)

<p>I’m very new to 3d slicer and had a lot of images to go through but on all of them 2/3 of the planes are distorted to some extent. The one I’ll try and attach here is a foot CT for context. I’m aware this problem has probably been raised before but if anyone could explain how to fix it to me like I was a 5 year old that’d be amazing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4a6e7afe8f73acf0f7166bf0378d40f7725db3c.jpeg" data-download-href="/uploads/short-url/ulcOB7sREkVbFOj7uzpd8d01H76.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4a6e7afe8f73acf0f7166bf0378d40f7725db3c_2_689x490.jpeg" alt="image" data-base62-sha1="ulcOB7sREkVbFOj7uzpd8d01H76" width="689" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4a6e7afe8f73acf0f7166bf0378d40f7725db3c_2_689x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4a6e7afe8f73acf0f7166bf0378d40f7725db3c_2_1033x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4a6e7afe8f73acf0f7166bf0378d40f7725db3c.jpeg 2x" data-dominant-color="35343E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1207×858 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-03-19 21:22 UTC)

<p>That looks like the kind of problem that can come from trying to load a directory of png files or something.  Slicer may try to guess the order but since there’s no metadata the geometry can be wrong.  You can try the <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md">ImageStacks module in SlicerMorph</a>.  If that’s not it report back with more details about the data.</p>

---
