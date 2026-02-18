# How to measure distance along the surface of segmented or volume rendering aorta?

**Topic ID**: 19135
**Date**: 2021-08-10
**URL**: https://discourse.slicer.org/t/how-to-measure-distance-along-the-surface-of-segmented-or-volume-rendering-aorta/19135

---

## Post #1 by @chendong9416 (2021-08-10 08:41 UTC)

<p>i want to measure distance between 2 points along the surface of aorta, how can i achieve it? thanks!</p>

---

## Post #2 by @lassoan (2021-08-10 16:49 UTC)

<p>You can create a markups curve with two endpoints and choose “Shortest distance on surface” curve type:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fb20700c334c2121b00c7c2df8a61547f8ec49.png" data-download-href="/uploads/short-url/7QnOPGKmFUtSKIQcbfAfxPNG0Od.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb20700c334c2121b00c7c2df8a61547f8ec49_2_473x500.png" alt="image" data-base62-sha1="7QnOPGKmFUtSKIQcbfAfxPNG0Od" width="473" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb20700c334c2121b00c7c2df8a61547f8ec49_2_473x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb20700c334c2121b00c7c2df8a61547f8ec49_2_709x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fb20700c334c2121b00c7c2df8a61547f8ec49_2_946x1000.png 2x" data-dominant-color="DDDDDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1218×1287 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The curve will go through the mesh points, so if the mesh resolution is low then the curve may not be smooth/straight. If you find that the curve is not good enough quality then you can subdivide the mesh to have more candidate points for the curve to go through.</p>

---

## Post #3 by @chendong9416 (2021-08-11 07:27 UTC)

<p>Dear Lassoan, in my vision (4.13.0), there is no vessel in Model Node, should i download some module?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23c7f8a955d9d777f4a676bd0b7e33881b23f30f.png" data-download-href="/uploads/short-url/56x9bbQ0s6MVoO4UraFJJzbwKKz.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23c7f8a955d9d777f4a676bd0b7e33881b23f30f.png" alt="捕获" data-base62-sha1="56x9bbQ0s6MVoO4UraFJJzbwKKz" width="430" height="500" data-dominant-color="F2F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">633×736 18.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-08-12 03:49 UTC)

<p>You can choose any model node. If you have the aorta as a segmentation node then you can export it to a model node by right-clicking on it in Data module.</p>

---

## Post #5 by @chendong9416 (2021-08-13 06:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="19135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>orta as a segmentation node then you can export it to a model node by right-clicking on it in Data module.</p>
</blockquote>
</aside>
<p>________________________Thanks</p>

---
