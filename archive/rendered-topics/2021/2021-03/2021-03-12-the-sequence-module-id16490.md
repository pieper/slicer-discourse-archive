---
topic_id: 16490
title: "The Sequence Module"
date: 2021-03-12
url: https://discourse.slicer.org/t/16490
---

# The sequence module

**Topic ID**: 16490
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/the-sequence-module/16490

---

## Post #1 by @mohammed_alshakhas (2021-03-12 07:10 UTC)

<p>im trying to use the sequence module, however I’m not successful at all .<br>
the documentation about it is not cleat at all to my level .</p>
<p>id appreciate some help and explanation</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2021-03-14 16:11 UTC)

<p>Please describe your overall goal and also specifically what you did, what you expected to happen, and what happened instead.</p>

---

## Post #3 by @mohammed_alshakhas (2021-03-15 14:50 UTC)

<p>I’m trying to experiment with making a video with slices scrolling volumes /segments</p>
<p>pretty much clueless about what do the parameters mean</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0f36c5c73abc25d5ad1d32e9f149c22477c2065.jpeg" data-download-href="/uploads/short-url/pfnz8Ilyd9SNzdtnzLH4lVisLCl.jpeg?dl=1" title="Screen Shot 2021-03-15 at 17.42.22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0f36c5c73abc25d5ad1d32e9f149c22477c2065_2_690x431.jpeg" alt="Screen Shot 2021-03-15 at 17.42.22" data-base62-sha1="pfnz8Ilyd9SNzdtnzLH4lVisLCl" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0f36c5c73abc25d5ad1d32e9f149c22477c2065_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0f36c5c73abc25d5ad1d32e9f149c22477c2065_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0f36c5c73abc25d5ad1d32e9f149c22477c2065_2_1380x862.jpeg 2x" data-dominant-color="858585"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-15 at 17.42.22</span><span class="informations">2880×1800 429 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>like in this example i made a volume render and trying to show axial/sagittal slice going through it</p>
<p>but I’m not sure about all these parameters and whats a master sequence and other sequences mean</p>

---

## Post #4 by @lassoan (2021-03-27 18:22 UTC)

<p>For a slice sweep video, the easiest is to use Screen Capture module. Choose a slice view as master view and “slice sweep” animation mode, and enable capture all views.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d0e8d4ecdf726e980d80dbd0bb1d8220fb4993.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d0e8d4ecdf726e980d80dbd0bb1d8220fb4993.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d0e8d4ecdf726e980d80dbd0bb1d8220fb4993.mp4</a>
    </source></video>
  </div><p></p>
<p>For animating volume rendering cropping and properties, you can use Animator module in SlicerMorph extension.</p>

---
