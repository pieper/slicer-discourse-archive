---
topic_id: 18355
title: "Alpaca Scale Issue"
date: 2021-06-27
url: https://discourse.slicer.org/t/18355
---

# ALPACA Scale issue

**Topic ID**: 18355
**Date**: 2021-06-27
**URL**: https://discourse.slicer.org/t/alpaca-scale-issue/18355

---

## Post #1 by @seanchoi0519 (2021-06-27 16:02 UTC)

<p>I have 2 models I am aligning with ALPACA extension. They are same in size. I have clicked “skip scaling” option and only went up to “Run subsampling, run rigid alignment” stage (without CPD non-rigid registration/deformation). However, I noticed that my source model (red) has shrank in size.</p>
<p>Why is this so? and how can I prevent this happening? I’d like to keep both at the same size at all costs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2f97bcfffc58ca9670cae3592144dbaa706bb72.png" data-download-href="/uploads/short-url/pxhvmYXaIg2N8qlgmrnjr67urt0.png?dl=1" title="Screen Shot 2021-06-28 at 1.58.37 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f97bcfffc58ca9670cae3592144dbaa706bb72_2_549x500.png" alt="Screen Shot 2021-06-28 at 1.58.37 AM" data-base62-sha1="pxhvmYXaIg2N8qlgmrnjr67urt0" width="549" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f97bcfffc58ca9670cae3592144dbaa706bb72_2_549x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f97bcfffc58ca9670cae3592144dbaa706bb72_2_823x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f97bcfffc58ca9670cae3592144dbaa706bb72_2_1098x1000.png 2x" data-dominant-color="D3C9D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-28 at 1.58.37 AM</span><span class="informations">1226×1116 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The funny thing is, this only happens some of the time. Other times, the shrinkage is slightly less, and at other times, they’re nearly the same size.</p>

---

## Post #2 by @muratmaga (2021-06-27 17:11 UTC)

<p>What do you mean by same size? Are they identical models?</p>

---

## Post #3 by @seanchoi0519 (2021-06-27 20:42 UTC)

<p>Apart from the bit in the middle, yes they are identical prior to Alpaca alignment. They’ve been drilled slightly differentlt in the middle, but they are the same teeth. I’ve even used mark up functionality to detect the change in length (around 5% decrease of source model) of the red source model.</p>

---

## Post #4 by @muratmaga (2021-06-27 23:06 UTC)

<p>Can you share your data, along with the parameters you used in ALPACA?<br>
<a class="mention" href="/u/agporto">@agporto</a></p>

---

## Post #5 by @seanchoi0519 (2021-06-28 02:06 UTC)

<p>Yes here is the link: <a href="https://drive.google.com/drive/folders/19AkAwIys22NwQLzzIo9EPZ14ZKcNbXka?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">ALPACA - Google Drive</a></p>
<p>I’ve used the standard parameters with no changes, apart from skip scaling = checked. and only went up to “Run rigid alignment” stage.</p>
<p>Only the source model seems to be affected.</p>
<p>Please do have a go multiple times, as this happens only half of the time.<br>
Also when I swap the source &amp; target (target as the source, and vice versa), the issue seems to resolve …</p>

---

## Post #6 by @seanchoi0519 (2021-06-28 03:28 UTC)

<p>Here’s another variation that I got, after increasing the point adjustment density to 1.4. <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0e7a980944c07505fd8dd372c6c05a2b042141a.png" data-download-href="/uploads/short-url/w5BhNUZ8J0YE7OjiELsbcwBgCxQ.png?dl=1" title="Screen Shot 2021-06-28 at 1.27.19 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0e7a980944c07505fd8dd372c6c05a2b042141a_2_482x500.png" alt="Screen Shot 2021-06-28 at 1.27.19 PM" data-base62-sha1="w5BhNUZ8J0YE7OjiELsbcwBgCxQ" width="482" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0e7a980944c07505fd8dd372c6c05a2b042141a_2_482x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0e7a980944c07505fd8dd372c6c05a2b042141a_2_723x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0e7a980944c07505fd8dd372c6c05a2b042141a.png 2x" data-dominant-color="928BC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-28 at 1.27.19 PM</span><span class="informations">924×958 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After repeated attempt, I obtained this variation as well, with same parameters as before (this is what I’d like to achieve every time - no scaling done to source model)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c97003bcb1987f27ac963695ab65f91cbaec05a.png" data-download-href="/uploads/short-url/dd5rBw7kkmbFd8VHcv1ZP8KQcrw.png?dl=1" title="Screen Shot 2021-06-28 at 1.31.08 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c97003bcb1987f27ac963695ab65f91cbaec05a_2_525x500.png" alt="Screen Shot 2021-06-28 at 1.31.08 PM" data-base62-sha1="dd5rBw7kkmbFd8VHcv1ZP8KQcrw" width="525" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c97003bcb1987f27ac963695ab65f91cbaec05a_2_525x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c97003bcb1987f27ac963695ab65f91cbaec05a_2_787x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c97003bcb1987f27ac963695ab65f91cbaec05a.png 2x" data-dominant-color="938BC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-28 at 1.31.08 PM</span><span class="informations">894×850 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @agporto (2021-06-28 04:25 UTC)

<p>Hi Sean. Thanks for reporting this. Some recent modifications to the code have broken the scaling behavior. I will correct the source code tomorrow (and ping you).<br>
Thanks again</p>

---

## Post #8 by @seanchoi0519 (2021-06-28 04:49 UTC)

<p>No problem Prof Arthur<br>
I’m glad I could make a contribution to this awesome software.</p>

---
