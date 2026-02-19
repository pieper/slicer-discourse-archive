---
topic_id: 21518
title: "Scalar Volume Display Widget Blue Line Missing In Histogram"
date: 2022-01-18
url: https://discourse.slicer.org/t/21518
---

# [Scalar Volume Display Widget] Blue line missing in histogram

**Topic ID**: 21518
**Date**: 2022-01-18
**URL**: https://discourse.slicer.org/t/scalar-volume-display-widget-blue-line-missing-in-histogram/21518

---

## Post #1 by @strider_hunter (2022-01-18 18:02 UTC)

<p>Hi,<br>
I have a ScalarVolume which has values in the range of [0,0.5]. When I view the histogram of this ScalarVolume, I am unable to understand it due to the missing blue line.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa5868ca17432096b4f90214af339dc912762edb.png" data-download-href="/uploads/short-url/zIEMAGfiCrRbqzmFXxsmjIQ4yZJ.png?dl=1" title="Slicer-VolumeDisplayWidget" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa5868ca17432096b4f90214af339dc912762edb_2_517x303.png" alt="Slicer-VolumeDisplayWidget" data-base62-sha1="zIEMAGfiCrRbqzmFXxsmjIQ4yZJ" width="517" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa5868ca17432096b4f90214af339dc912762edb_2_517x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa5868ca17432096b4f90214af339dc912762edb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa5868ca17432096b4f90214af339dc912762edb.png 2x" data-dominant-color="DDDDDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-VolumeDisplayWidget</span><span class="informations">722×424 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr>
<p>I have another ScalarVolume (a CT scan) with values in the range of [-1000, 2000]. When I view the histogram of this ScalarVolume, I am able to understand the histogram due to the presence of the blue line.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/315203001193f0fef32d03362d1c433d7f1f1275.png" alt="Slicer-VolumeDisplayWidget-1" data-base62-sha1="72j6wYajO2ONT3yDUREZSBNddC5" width="495" height="315"></p>
<p>Why is this happening? Is this a bug or am I incorrectly using/interpreting the histogram.</p>
<hr>
<p>I’m using Slicer 4.11.0. This question is closely related to <a href="https://discourse.slicer.org/t/qslicerscalarvolumedisplaywidget-adding-user-defined-histogram-to-this/21448">another post</a></p>

---

## Post #2 by @lassoan (2022-01-19 05:46 UTC)

<p>Bin size of 1 works well for integer-valued volumes, but for floating-point volumes the bin size need to be determined from the scalar range of the volume. The current implementation always used the bin size of 1.</p>
<p>I’ve fixed the issue now. The Slicer Preview Release that you download on 2022-01-20 or later will display the histogram correctly for floating-point volume types.</p>

---

## Post #3 by @strider_hunter (2022-01-20 09:31 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="21518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>… The Slicer Preview Release that you download on 2022-01-20 or later will display the histogram correctly for floating-point volume types …</p>
</blockquote>
</aside>
<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for this update. I am now able to view the blue line for the floating-point volumes as well.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c835dfa73cc800485ba798dc5b5d98dbc9685a71.png" alt="Slicer-FloatingPointHistogram" data-base62-sha1="sz8UUbIVlLttYyT1RhoVCE2yl0d" width="548" height="262"></p>
<p>I had a feature request regarding the colormap used in the histogram. Currently it used the “Gray” colormap for all volumes, but I use a different colormap for my volumes (i.e. WarmShade2). Is this change possible?</p>

---
