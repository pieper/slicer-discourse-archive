# Odd behavior while painting segment

**Topic ID**: 30437
**Date**: 2023-07-06
**URL**: https://discourse.slicer.org/t/odd-behavior-while-painting-segment/30437

---

## Post #1 by @Julien_D (2023-07-06 20:10 UTC)

<p>Hi all,</p>
<p>When painting a segment, there’s an odd behavior from the brush. It’s like it’s missing spots (see picture below). I have no threshold applied and the following settings. Restarting Slicer didn’t solve it. It’s the first time I encouter this. Anyone had this issue as well? I run 5.2.2 version in Windows 10.</p>
<ul>
<li>Color smudge: off</li>
<li>Editable area: Everywhere</li>
<li>Editable intensity range: off</li>
<li>Overwrite other segments: All segments</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66c965e70f161bca43f9ee370a03771780089eb7.jpeg" alt="image" data-base62-sha1="eFic6RgkoQLWx8SeW6c6vutVxK7" width="528" height="421"></p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2023-07-06 20:44 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="30397">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ba9def/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-painting-creating-triangular-artifacts/30397">Segmentation Painting creating triangular artifacts</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone! First time posting here, so apologies if this is unclear, I can provide extra details if needed, but I am currently working on my first big project in slicer segmenting cephalic glands in snake heads. The anatomical planes of the scans were not aligned with the correct axes to start off with, so I’ve done a quick transform to rotate the heads into the proper position, then resampled the scalar volume using the lanczos interpolation method. Pretty much just following the steps of thi…
  </blockquote>
</aside>


---

## Post #3 by @Julien_D (2023-07-06 20:59 UTC)

<p>Yes, that’s it, I rotated the plane and didn’t realise it changes the pixel shape while painting <img src="https://emoji.discourse-cdn.com/twitter/man_facepalming.png?v=12" title=":man_facepalming:" class="emoji" alt=":man_facepalming:" loading="lazy" width="20" height="20"></p>
<p>Thanks!</p>

---
