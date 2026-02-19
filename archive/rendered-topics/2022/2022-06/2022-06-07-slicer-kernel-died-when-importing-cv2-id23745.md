---
topic_id: 23745
title: "Slicer Kernel Died When Importing Cv2"
date: 2022-06-07
url: https://discourse.slicer.org/t/23745
---

# Slicer kernel died when importing cv2

**Topic ID**: 23745
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/slicer-kernel-died-when-importing-cv2/23745

---

## Post #1 by @user4 (2022-06-07 06:47 UTC)

<p>Hi,all.I want to use opencv so I installed it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01031b9324010ce9ed0a5f29d3f5663d55994106.png" data-download-href="/uploads/short-url/8X8pH7PydhOHSwSMoC4QwfsvqK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01031b9324010ce9ed0a5f29d3f5663d55994106_2_690x127.png" alt="image" data-base62-sha1="8X8pH7PydhOHSwSMoC4QwfsvqK" width="690" height="127" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01031b9324010ce9ed0a5f29d3f5663d55994106_2_690x127.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01031b9324010ce9ed0a5f29d3f5663d55994106_2_1035x190.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01031b9324010ce9ed0a5f29d3f5663d55994106_2_1380x254.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1512×279 59.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However,when I import cv2,it takes a long time and failed in the end, as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdd18e7d2a2e88bb5b46cc4d90a3cdfdddf4375a.png" data-download-href="/uploads/short-url/r5ddjTK4JjamX33KdN1AyNQwj1M.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdd18e7d2a2e88bb5b46cc4d90a3cdfdddf4375a.png" alt="image" data-base62-sha1="r5ddjTK4JjamX33KdN1AyNQwj1M" width="690" height="155" data-dominant-color="F7F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">995×224 18.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I tried a lot of times ,it is still the same result…It only fails when I select Slicer4.11 as a kernel but it is okay when I select python3.But I have to use Slicer as a kernel for some reason.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df9179e35a27e0d65a854c7476570faeae96370b.png" alt="image" data-base62-sha1="vTM9JMu3GnGaekHpkjNfURQWJRN" width="412" height="262"></p>
<p>Is there some potential way to solve this problem?<br>
Thanks in advance for your help!</p>

---

## Post #2 by @mau_igna_06 (2022-06-07 08:58 UTC)

<p>You need to use the python interactor of Slicer</p>

---
