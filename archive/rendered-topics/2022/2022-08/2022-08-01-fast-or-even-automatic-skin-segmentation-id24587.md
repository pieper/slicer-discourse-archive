---
topic_id: 24587
title: "Fast Or Even Automatic Skin Segmentation"
date: 2022-08-01
url: https://discourse.slicer.org/t/24587
---

# Fast or even automatic skin segmentation

**Topic ID**: 24587
**Date**: 2022-08-01
**URL**: https://discourse.slicer.org/t/fast-or-even-automatic-skin-segmentation/24587

---

## Post #1 by @user4 (2022-08-01 06:10 UTC)

<p>Hi,all.I want to do some skin segmentations on my mouse body data then create a masked volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e9a4ead28e9500ab9ab7b27b5ee4a1a89ec398.jpeg" data-download-href="/uploads/short-url/2Z0830PKY6bgOhxVdVQmCZhWLfq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14e9a4ead28e9500ab9ab7b27b5ee4a1a89ec398_2_384x500.jpeg" alt="image" data-base62-sha1="2Z0830PKY6bgOhxVdVQmCZhWLfq" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14e9a4ead28e9500ab9ab7b27b5ee4a1a89ec398_2_384x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e9a4ead28e9500ab9ab7b27b5ee4a1a89ec398.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14e9a4ead28e9500ab9ab7b27b5ee4a1a89ec398.jpeg 2x" data-dominant-color="6E6B6B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">473×615 76.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Currently I achieve my goal according to the following steps.</p>
<ol>
<li>draw several slices carefully with a fixed step,for example 5mm.In this case my mouse image is 40mm which means I need to draw eight times.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0b02c75073137a183255fa5ffbd64f759ebc5a6.jpeg" data-download-href="/uploads/short-url/yle2Gc7HAFJRJO158LmUyxefPW6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0b02c75073137a183255fa5ffbd64f759ebc5a6_2_382x375.jpeg" alt="image" data-base62-sha1="yle2Gc7HAFJRJO158LmUyxefPW6" width="382" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0b02c75073137a183255fa5ffbd64f759ebc5a6_2_382x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0b02c75073137a183255fa5ffbd64f759ebc5a6_2_573x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0b02c75073137a183255fa5ffbd64f759ebc5a6_2_764x750.jpeg 2x" data-dominant-color="61655F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1180×1156 85.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>use <em>Fill between slices</em> to expand my segmentation.</li>
<li>use <em>Mask volume</em> to create the masked volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c3cc79a7c6e6f8fc23c20802ac79f66f3f98eb5.png" data-download-href="/uploads/short-url/6jleaLPSgBtb96fQur8P6kyHTeJ.png?dl=1" title="1659332907949" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c3cc79a7c6e6f8fc23c20802ac79f66f3f98eb5_2_517x258.png" alt="1659332907949" data-base62-sha1="6jleaLPSgBtb96fQur8P6kyHTeJ" width="517" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c3cc79a7c6e6f8fc23c20802ac79f66f3f98eb5_2_517x258.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c3cc79a7c6e6f8fc23c20802ac79f66f3f98eb5_2_775x387.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c3cc79a7c6e6f8fc23c20802ac79f66f3f98eb5_2_1034x516.png 2x" data-dominant-color="8789B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1659332907949</span><span class="informations">1166×582 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>What I want is to quickly or even automatically identify the skin outline. On the one hand, it takes too long to manually segment multiple times. On the other hand, manual segmentation requires very fine drawing, and there is a high probability that there will be large errors.<br>
Are there any available machine learning or deep learning models to achieve my goal?I would love to hear some possible approaches or ideas.<br>
Thank you in advance for your help!</p>

---

## Post #2 by @liam26 (2026-01-16 00:56 UTC)

<p>Any progress on this?</p>

---

## Post #3 by @mikebind (2026-01-16 19:21 UTC)

<p>Today, I’d probably try NNInteractive (<a href="https://github.com/coendevente/SlicerNNInteractive" rel="noopener nofollow ugc">coendevente/SlicerNNInteractive: A 3D Slicer extension for efficient segmentation with nnInteractive.</a>).  It’s not totally automated, but it does a remarkably good job of 3D segmentation from relatively few interactive hints.  If that works for you, you could also use it to build up a gold standard segmentation dataset for training a fully automated segmentation network via <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/tree/main?tab=readme-ov-file#developers" rel="noopener nofollow ugc">MONAI Auto3DSeg</a>.</p>

---
