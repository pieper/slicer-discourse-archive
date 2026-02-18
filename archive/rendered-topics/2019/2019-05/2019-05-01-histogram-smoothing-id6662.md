# Histogram smoothing

**Topic ID**: 6662
**Date**: 2019-05-01
**URL**: https://discourse.slicer.org/t/histogram-smoothing/6662

---

## Post #1 by @kayarre (2019-05-01 00:30 UTC)

<p>I am doing some analysis of MRI images and am attempting to come up with a rigerous way to do image normalization.</p>
<p>I have come across papers that look at longitudinal studies of Alzheimer’s disease that use a histogram smoothing technique to evaluate the mode, or peak intensity in normal appearing white matter as a part of white stripe normalization.</p>
<p>The thing I don’t understand is the smoothing, what does smoothing a histogram give you?<br>
and how does that get implemented? It seems like they are using Kernel density estimation?</p>
<p>I am not as clued in on the these methods and would appreciate opinions on the subject.</p>
<blockquote>
<p>We then use a penalized spline smoother (<a href="https://www.sciencedirect.com/science/article/pii/S221315821400117X#bb0080" rel="noopener nofollow ugc">Ruppert et al., 2003</a>), a fully automatic smoothing technique that estimates the smoothing parameter, to estimate the mode  (the largest non-background peak)</p>
</blockquote>
<p>paper link<br>
<a href="https://www.sciencedirect.com/science/article/pii/S221315821400117X" rel="noopener nofollow ugc">https://www.sciencedirect.com/science/article/pii/S221315821400117X</a></p>

---

## Post #2 by @lassoan (2019-05-01 12:32 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="6662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>The thing I don’t understand is the smoothing, what does smoothing a histogram give you?</p>
</blockquote>
</aside>
<p>Histogram smoothing changes voxel intensities so that the histogram of voxel intensities becomes smoother or more flat. Implementation is simply replacing each voxel intensity value with a different value. The key is figure out what intensity value should be assigned to each original intensity value.</p>
<p>I usually try to avoid modifying the original images. Instead of normalizing the image with mapping intensity values with some function (which is usually a lossy operation), I use processing algorithms that do not depend on matching of image intensity values, for example register using mutual information metric (instead of sum of squared differences metric) or segment using grow-cut method (instead of global thresholding). Some kind of normalization is useful for visual comparison of images, but usually you can get good enough results by simple linear scaling/offset in the display pipeline and you don’t need to actually modify the images.</p>

---
