# Registration Problem: Brain T2WI to T1WI

**Topic ID**: 35922
**Date**: 2024-05-05
**URL**: https://discourse.slicer.org/t/registration-problem-brain-t2wi-to-t1wi/35922

---

## Post #1 by @lotus (2024-05-05 00:33 UTC)

<p>I have a registration problem, I want to register brain T2WI to T1WI, but the matrix and resolution of the two images are inconsistent, how should I deal with it, thank you</p>

---

## Post #2 by @pieper (2024-05-05 12:16 UTC)

<aside class="quote no-group" data-username="lotus" data-post="1" data-topic="35922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/0ea827/48.png" class="avatar"> lotus:</div>
<blockquote>
<p>matrix and resolution of the two images are inconsistent</p>
</blockquote>
</aside>
<p>That shouldn’t matter - if it’s the same subject then the normal registration tools should work very reliably.</p>

---

## Post #3 by @lotus (2024-05-25 07:44 UTC)

<p>More specifically, T2WI is a 2d image and T1WI is a 3d image. After many attempts, the registration effect is not satisfactory. I observed that on 2D T2WI images, the sagittal and coronal positions seemed to be compressed and could not be clearly displayed. How should this situation be handled</p>

---

## Post #4 by @LeidyMoraV (2024-05-25 16:00 UTC)

<p>Try with landmark registration</p>

---
