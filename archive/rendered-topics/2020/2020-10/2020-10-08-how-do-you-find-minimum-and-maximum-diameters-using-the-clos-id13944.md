---
topic_id: 13944
title: "How Do You Find Minimum And Maximum Diameters Using The Clos"
date: 2020-10-08
url: https://discourse.slicer.org/t/13944
---

# How do you find minimum and maximum diameters using the closed curve function?

**Topic ID**: 13944
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/how-do-you-find-minimum-and-maximum-diameters-using-the-closed-curve-function/13944

---

## Post #1 by @Trex48 (2020-10-08 20:32 UTC)

<p>RT, I am trying to find the minimum and maximum diameters of a irregular closed curve in the shape of a circle/oval. Does anyone know how to do this via python code or another extension? Thanks!</p>

---

## Post #2 by @lassoan (2020-10-09 03:02 UTC)

<p>Have you already extracted the centerline and computed the radius values?</p>

---

## Post #3 by @chir.set (2020-10-09 06:35 UTC)

<p>I may be wrong, but I understand that <a class="mention" href="/u/trex48">@Trex48</a> is asking for metrics of a closed curve like in the below image, i.e, with respect to the center of an irregular closed curve. The latter can be more complex; perhaps the very notion of minimum and maximum diameters is not valid. Now I may have badly understood <a class="mention" href="/u/trex48">@Trex48</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2d65e91262088f83302fb3432937d3639097c5e.png" data-download-href="/uploads/short-url/u59yic6JI202r8HiFJsvdtcKtmC.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2d65e91262088f83302fb3432937d3639097c5e.png" alt="Screenshot" data-base62-sha1="u59yic6JI202r8HiFJsvdtcKtmC" width="690" height="489" data-dominant-color="030103"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">891×632 18.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Trex48 (2020-10-09 10:20 UTC)

<p>Thank you both.</p>
<p>I am simply trying to find the minimum and maximum diameter of a closed curve that has all of its points in the same plane.</p>
<p>Like for this irregular oval shape that I have below. I was able to find a python code to find its surface area but not the minimum and maximum diameter. This is why I am seeking help here. Thanks again.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c2a0abb966261db70e3fef2a095cd80d56aec48.png" data-download-href="/uploads/short-url/jZWV3wsepzd78UEVsIEOQwXBsq4.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2a0abb966261db70e3fef2a095cd80d56aec48_2_316x499.png" alt="Capture" data-base62-sha1="jZWV3wsepzd78UEVsIEOQwXBsq4" width="316" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2a0abb966261db70e3fef2a095cd80d56aec48_2_316x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2a0abb966261db70e3fef2a095cd80d56aec48_2_474x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2a0abb966261db70e3fef2a095cd80d56aec48_2_632x998.png 2x" data-dominant-color="5E5F6C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">673×1062 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-10-09 13:45 UTC)

<p>There are dozens of definition of minimum/maximum diameter for a closed curve. Would you like to use side length of oriented bounding box, diameters of best-fit ellipse, diameter of minimum inscribed/minimum circumsribed circle,…? Or min/max axis length across the centroid? Do the axes have to be orthogonal?</p>
<p>Which one do you need to compute?</p>

---

## Post #6 by @Trex48 (2020-10-09 20:23 UTC)

<p>It would be min/max diameter across the centroid, and the axes would have to be perpendicular to each other.</p>
<p>Thanks! Sorry I was not clear with this.</p>

---

## Post #7 by @lassoan (2020-10-09 22:11 UTC)

<aside class="quote no-group" data-username="Trex48" data-post="6" data-topic="13944">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/trex48/48/8381_2.png" class="avatar"> Trex48:</div>
<blockquote>
<p>min/max diameter across the centroid, and the axes would have to be perpendicular to each other</p>
</blockquote>
</aside>
<p>This would be an overconstrained specification (there is no solution except very special cases). If  the axes must be orthogonal then you need to specify a different criteria (e.g., axes of best fit ellipse).</p>

---

## Post #8 by @Trex48 (2020-10-09 22:23 UTC)

<p>I see. Thank you, I will go back and rethink about my criteria. I appreciate your insights on this.</p>

---

## Post #9 by @CNCLD_Ragama (2025-02-20 15:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="13944">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>axes of best fit ellipse).</p>
</blockquote>
</aside>
<p>i also need to know how to get this</p>

---

## Post #10 by @Deep_Learning (2025-02-21 12:33 UTC)

<p>look at PCA, Principal component analysis.</p>

---
