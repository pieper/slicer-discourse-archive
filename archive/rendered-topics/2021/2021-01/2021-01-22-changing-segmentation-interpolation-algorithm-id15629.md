---
topic_id: 15629
title: "Changing Segmentation Interpolation Algorithm"
date: 2021-01-22
url: https://discourse.slicer.org/t/15629
---

# Changing segmentation interpolation algorithm?

**Topic ID**: 15629
**Date**: 2021-01-22
**URL**: https://discourse.slicer.org/t/changing-segmentation-interpolation-algorithm/15629

---

## Post #1 by @Jason_Wong (2021-01-22 14:27 UTC)

<p>Hi 3D Slicer community! My current project has an image stack of 23 images with features that need to be converted into 3D models. Unfortunately, the image spacing is quite high relative, so the side and the top views appear choppy when creating segmentations.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e3aa3b1e4f0a5c057205afd3c42f102aeaa491c.png" data-download-href="/uploads/short-url/drAw1V1cFmlFiKeJBiADx3Sc7Q8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e3aa3b1e4f0a5c057205afd3c42f102aeaa491c_2_627x500.png" alt="image" data-base62-sha1="drAw1V1cFmlFiKeJBiADx3Sc7Q8" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e3aa3b1e4f0a5c057205afd3c42f102aeaa491c_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e3aa3b1e4f0a5c057205afd3c42f102aeaa491c_2_940x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e3aa3b1e4f0a5c057205afd3c42f102aeaa491c.png 2x" data-dominant-color="474E53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">950×757 85.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to change the filling from extrusions to splines? Thanks.</p>

---

## Post #2 by @lassoan (2021-01-22 14:50 UTC)

<p>It is recommended to resample highly anisotropic volumes before segmentation. See more details here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html?highlight=anisotropic#segmentation-is-not-accurate-enough" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>

---

## Post #3 by @Jason_Wong (2021-01-24 06:53 UTC)

<p>Thanks! The process seems to cause a lot of lag in my computer. Is there a way to reduce this?</p>

---

## Post #4 by @lassoan (2021-01-24 15:59 UTC)

<p>Resampling to have higher resolution can indeed hugely increase its memory usage. Spacing scale 0.5 increases memory need (and processing time) by a factor of 8x, and spacing scale of 0.2 increases it by 125x.</p>
<p>To compensate for this, crop image to the minimum necessary size. That’s why it is always recommended to use Crop volume module to resample&amp;crop the image at the same time. You can also experiment with different spacing scale factors to find one that allows segmentation with sufficient details and your computer can still handle with reasonable speed. If you regularly need to edit high-resolution segmentations then it may worth investing into adding more physical RAM to your computer and high CPU frequency (having more CPU cores does not usually help much, because most image segmentation algorithms are not parallelized).</p>

---

## Post #5 by @muratmaga (2021-01-25 00:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="15629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>because most image segmentation algorithms are not parallelized</p>
</blockquote>
</aside>
<p>Does this mean they are inherently single-threaded, or with some development effort can they be parallelized?</p>

---

## Post #6 by @lassoan (2021-01-25 02:01 UTC)

<p>Simple algorithms can be parallelized easily (they are typically already implemented as multi-threaded), while other algorithms need lots of new ideas to efficiently utilize multiple cores.</p>
<p>It depends on many factors what the performance bottleneck is in a processing workflow. The best is to do some performance profiling to see where most of the time is spent and then focus on making that very specific part of the software faster. If you identify any performance bottlenecks then let us know and we can brainstorm on possible solutions.</p>

---

## Post #7 by @Jason_Wong (2021-01-28 05:58 UTC)

<p>I’ve tried the processing on a couple slices, after changing the oversampling ratio by 2.00 for both segmentation and the volume stack. Unfortunately, I’m still not getting anything different at least in the 3d-rendering that is. Is there an order that I have to perform the oversampling in “specify geometry”? I’m also getting the message, “Failed to determine labelmap geometry from segmentation node” at the specify geometry window, not sure if that is related.</p>

---

## Post #8 by @lassoan (2021-01-28 06:02 UTC)

<aside class="quote no-group" data-username="Jason_Wong" data-post="7" data-topic="15629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jason_wong/48/9637_2.png" class="avatar"> Jason_Wong:</div>
<blockquote>
<p>Failed to determine labelmap geometry from segmentation node</p>
</blockquote>
</aside>
<p>If the segmentation node is still empty then it cannot be used as a basis for specifying geometry. You can choose any volume or you can choose a model or ROI and specify spacing.</p>
<p>If you already have non-empty segments then oversampling should work and you need to apply smoothing after increasing oversampling as described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">documentation</a>.</p>

---
