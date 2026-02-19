---
topic_id: 26167
title: "Problem With Files From New Cbct Scanner"
date: 2022-11-09
url: https://discourse.slicer.org/t/26167
---

# problem with files from new cbct scanner

**Topic ID**: 26167
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/problem-with-files-from-new-cbct-scanner/26167

---

## Post #1 by @jeroen (2022-11-09 15:12 UTC)

<p>until now no problem, but when i recieve files from a new cbct scanner en load de filles the look like de picture below? what is wrong? please help!!!</p>
<p>in the vierwer the scan is perfect, only in the 3dslicer it looks like this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c5e03b49928621af7180580113136b7eb209f73.jpeg" data-download-href="/uploads/short-url/aTzIc8WyXOWPVf8T4z1noqDt1Un.jpeg?dl=1" title="0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c5e03b49928621af7180580113136b7eb209f73_2_374x500.jpeg" alt="0" data-base62-sha1="aTzIc8WyXOWPVf8T4z1noqDt1Un" width="374" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c5e03b49928621af7180580113136b7eb209f73_2_374x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c5e03b49928621af7180580113136b7eb209f73.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c5e03b49928621af7180580113136b7eb209f73.jpeg 2x" data-dominant-color="626461"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0</span><span class="informations">476×635 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pll_llq (2022-11-09 22:18 UTC)

<p>Try to adjust the histogram. It looks like the hounsfield unit mapping to grayscale is off because artefact intensities are too high.</p>
<p>Also this might result in some compression that is done on export from the cbct machine. Some vendors like to do that nasty stuff to lock users with their proprietary viewers</p>

---

## Post #3 by @jeroen (2022-11-10 06:28 UTC)

<p>Thx! Can i adjust this in slicer, can you tell me how.</p>
<p>Grtz.</p>

---

## Post #4 by @pll_llq (2022-11-10 07:46 UTC)

<p>Start with adjusting window levels (see the documentation for details <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a>)<br>
Hopefully this should be enough for you to view the image</p>

---

## Post #5 by @jeroen (2023-01-27 16:11 UTC)

<p>sorry it took a while, but thanks for your reply. this was indeed the problem, now it works fine again! thx thx thx…</p>

---
