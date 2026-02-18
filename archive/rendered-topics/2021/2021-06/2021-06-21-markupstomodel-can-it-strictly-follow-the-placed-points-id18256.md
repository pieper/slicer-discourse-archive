# MarkupsToModel : can it strictly follow the placed points?

**Topic ID**: 18256
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/markupstomodel-can-it-strictly-follow-the-placed-points/18256

---

## Post #1 by @chir.set (2021-06-21 17:03 UTC)

<p>The image below show the model created by MarkupsToModel. Some points get ignored if others create a concave trajectory. The final model has always a convex surface. I suppose it’s the intended algorithm in use.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84c92e7c7f0d552c18c79fda11b96b5da948b6ec.jpeg" data-download-href="/uploads/short-url/iWG3rXMHxSkNcctR28RqGt3UI3O.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84c92e7c7f0d552c18c79fda11b96b5da948b6ec_2_674x500.jpeg" alt="Screenshot" data-base62-sha1="iWG3rXMHxSkNcctR28RqGt3UI3O" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84c92e7c7f0d552c18c79fda11b96b5da948b6ec_2_674x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84c92e7c7f0d552c18c79fda11b96b5da948b6ec_2_1011x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84c92e7c7f0d552c18c79fda11b96b5da948b6ec_2_1348x1000.jpeg 2x" data-dominant-color="191711"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1741×1291 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I wish to know if the final model can strictly be bounded by the points, creating concave surfaces too. I suppose it should be done deep in the C++ code if it’s feasible. That’s beyond my means. Please see it as a note for a further enhancement of this module.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-06-21 21:30 UTC)

<p>It is impossible to have a smooth surface and go through an arbitrary set of points, but you can get close by enabling alpha shapes algorithm. To do that, disable “Force convex output” and find a “Convexity” value that works well for your point set. See more information in the <a href="https://github.com/SlicerIGT/SlicerMarkupsToModel#closed-surfaces">module documentation</a>.</p>

---

## Post #3 by @chir.set (2021-06-23 16:30 UTC)

<p>Thanks for the reply. It would have been useful to be able to freely create a segment following anatomic boundaries. This would have been time consuming too, but at least, repeatable and precise.</p>

---

## Post #4 by @lassoan (2021-06-23 16:35 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="18256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It would have been useful to be able to freely create a segment following anatomic boundaries.</p>
</blockquote>
</aside>
<p>All the tools in Segment Editor do exactly that. For example instead of dropping markup points paint small seeds and create a complete segmentation using “Grow from seeds” effect. It supports arbitrary shapes, can segment any number of structures at once, and it even takes the underlying image into account.</p>
<p>Markups to model module is a geometric modeling tool and it is not meant to be able to represent arbitrary shapes.</p>

---
