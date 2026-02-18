# Tif images look washed out and have black lines

**Topic ID**: 11001
**Date**: 2020-04-05
**URL**: https://discourse.slicer.org/t/tif-images-look-washed-out-and-have-black-lines/11001

---

## Post #1 by @orchid (2020-04-05 17:15 UTC)

<p>I load tif image sequence and see the images look washed out and have strange black lines for sagittal and coronal view but not on axial view on Slicer.</p>
<p>The tiff images look fine to me.</p>
<p>Has anyone seen something like this and how do you resolve it?</p>
<p>I have windows 10 and slice 4.10.0.</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2020-04-05 17:16 UTC)

<p>Where do the images come from? Could you please post a few screenshots?</p>

---

## Post #3 by @muratmaga (2020-04-06 04:01 UTC)

<p>Check the slice spacing. Incorrect spacing in Z dimension may cause flatting of the two planes.</p>

---

## Post #4 by @orchid (2020-04-06 15:38 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a> for your quick reply.<br>
Here is the screen capture. I started to think it is not Slicer or ImageJ, but it is related to something else. I use imageJ to enhance contrast for dcom image sequence and save them as tiff images. Then use 3D slicer to load these image sequence.</p>
<ol>
<li>These images were loaded and displayed ok before but now they have some black lines .</li>
<li>New images that were processed by imagesj have color inverted and has black line like this one<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/607292a9425331eb85343ba2fd80756aa579a27b.jpeg" data-download-href="/uploads/short-url/dLdj7Ip4J3z8XWO8bsFUGoIMYfF.jpeg?dl=1" title="coronal3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/607292a9425331eb85343ba2fd80756aa579a27b_2_543x500.jpeg" alt="coronal3" data-base62-sha1="dLdj7Ip4J3z8XWO8bsFUGoIMYfF" width="543" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/607292a9425331eb85343ba2fd80756aa579a27b_2_543x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/607292a9425331eb85343ba2fd80756aa579a27b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/607292a9425331eb85343ba2fd80756aa579a27b.jpeg 2x" data-dominant-color="B2B2B2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">coronal3</span><span class="informations">582×535 39.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>
<p>Thanks,</p>

---

## Post #5 by @orchid (2020-04-06 15:40 UTC)

<p>Thank you, <a class="mention" href="/u/muratmaga">@muratmaga</a>.<br>
I checked the slice spacing. They look ok (1.0mm).</p>

---

## Post #6 by @lassoan (2020-04-06 19:32 UTC)

<p>Could you adjust the window/level a bit so that we can see what’s in the image?</p>

---

## Post #7 by @orchid (2020-04-06 23:47 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
I think after I used imageJ to enhance contrast and save images as tiff, my images were corrupted somehow. I tried to use the dcom images and load on slicer, I looks perfectly fine (no black lines in the middle like these below.</p>
<p>1.This  was preprocessed (saved as tiff image sequence) before and when loaded on Slicer, it looks like this. Image is fine, just additional black lines.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea635ce28ff8a81085972e727acc5a669f64c7c0.jpeg" alt="sagittal2" data-base62-sha1="xruBWpOJ0bdud32afRxfgrHEZGg" width="279" height="216"></p>
<ol start="2">
<li>This one was preprocessed recently (saved as tiff image sequence) and it looks like this on slicer. It looks like its rotated, and the color is reversed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f5fad1ddb8a00ba8ba7e713f46667e4a8a7751.jpeg" data-download-href="/uploads/short-url/ZzSbNML7BFQ2RJV3EGIjD4gxhf.jpeg?dl=1" title="sagittal3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06f5fad1ddb8a00ba8ba7e713f46667e4a8a7751_2_275x250.jpeg" alt="sagittal3" data-base62-sha1="ZzSbNML7BFQ2RJV3EGIjD4gxhf" width="275" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06f5fad1ddb8a00ba8ba7e713f46667e4a8a7751_2_275x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06f5fad1ddb8a00ba8ba7e713f46667e4a8a7751_2_412x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06f5fad1ddb8a00ba8ba7e713f46667e4a8a7751_2_550x500.jpeg 2x" data-dominant-color="C1C1C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sagittal3</span><span class="informations">576×522 31.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>

---

## Post #8 by @lassoan (2020-04-07 00:15 UTC)

<p>The black lines looks like beam hardening artifacts caused by very high density regions (most likely tooth fillings and/or implants).</p>

---

## Post #9 by @orchid (2020-04-07 22:05 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>. It makes sense.<br>
I will probably just skip using imageJ for those with braces like these and use dcom image as.</p>

---

## Post #10 by @lassoan (2020-04-07 22:49 UTC)

<p>ImageJ is great software but it is mainly for microscopy images. It has some very limited 3D image support but I would not recommend it for processing CT images.</p>

---

## Post #11 by @orchid (2020-04-08 23:23 UTC)

<p>I’ll keep that in mind. Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
