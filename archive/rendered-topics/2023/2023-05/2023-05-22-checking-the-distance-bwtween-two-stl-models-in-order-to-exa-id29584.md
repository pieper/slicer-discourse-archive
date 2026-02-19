---
topic_id: 29584
title: "Checking The Distance Bwtween Two Stl Models In Order To Exa"
date: 2023-05-22
url: https://discourse.slicer.org/t/29584
---

# Checking the distance bwtween two STL models in order to exaluate the accuracy between virtual planning and actual surgery

**Topic ID**: 29584
**Date**: 2023-05-22
**URL**: https://discourse.slicer.org/t/checking-the-distance-bwtween-two-stl-models-in-order-to-exaluate-the-accuracy-between-virtual-planning-and-actual-surgery/29584

---

## Post #1 by @wael_telha (2023-05-22 14:44 UTC)

<p>hi dear all , I would like to  confirm the accuracy of my evaluation through sharing with you some of the steps I used for the measurement of accuracy between the virtual planning model and the actual post-operative model, I need your valuable opinion in this regard</p>
<ol>
<li>
<p>the first step after I did the registration between the pre-operative planning and post-operative<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf31d74a5649e6b76f2ddc64f2fccb552cb7a15b.jpeg" data-download-href="/uploads/short-url/tyVCrZFH5xPZt3Ow7tS04YSKlzt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf31d74a5649e6b76f2ddc64f2fccb552cb7a15b_2_690x388.jpeg" alt="image" data-base62-sha1="tyVCrZFH5xPZt3Ow7tS04YSKlzt" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf31d74a5649e6b76f2ddc64f2fccb552cb7a15b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf31d74a5649e6b76f2ddc64f2fccb552cb7a15b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf31d74a5649e6b76f2ddc64f2fccb552cb7a15b_2_1380x776.jpeg 2x" data-dominant-color="BCCDD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>After the registration, with the help of pick’n Point I choose the reference model, which is a post-operative model<br>
I made a point on the reference model as shown below at the area of interest to measure the distance between the same points between the two models, and later I chose  the propagate the non-mesh model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc99ab7cdab5be6bcd89335f439aa6525ea3cca.jpeg" data-download-href="/uploads/short-url/46FiSDHT5fu7G0GknxR5UX1KIyu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc99ab7cdab5be6bcd89335f439aa6525ea3cca_2_690x388.jpeg" alt="image" data-base62-sha1="46FiSDHT5fu7G0GknxR5UX1KIyu" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc99ab7cdab5be6bcd89335f439aa6525ea3cca_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc99ab7cdab5be6bcd89335f439aa6525ea3cca_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc99ab7cdab5be6bcd89335f439aa6525ea3cca_2_1380x776.jpeg 2x" data-dominant-color="B7D6E0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>then through Model to Model Distance the source model is the post-operative Model and the target model is the pre-operative model and the calculation was done<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac54076934ec343606000ef0b2cdd270ee74fc1f.jpeg" data-download-href="/uploads/short-url/oAu9G5sQ6cBYxO3MiZkyKorYBKn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac54076934ec343606000ef0b2cdd270ee74fc1f_2_690x388.jpeg" alt="image" data-base62-sha1="oAu9G5sQ6cBYxO3MiZkyKorYBKn" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac54076934ec343606000ef0b2cdd270ee74fc1f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac54076934ec343606000ef0b2cdd270ee74fc1f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac54076934ec343606000ef0b2cdd270ee74fc1f_2_1380x776.jpeg 2x" data-dominant-color="C5BFC9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>4.the fourth and last step was to get the measured value through Mesh Statistics. I chose the absolute value and X AXIS, Y, AND Z AXIS<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a32e7bdb5d2fc033988383c62023ff58de1f5d33.jpeg" data-download-href="/uploads/short-url/nhzpXRFVqusul8CcSP3XJpxSuQz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a32e7bdb5d2fc033988383c62023ff58de1f5d33_2_690x388.jpeg" alt="image" data-base62-sha1="nhzpXRFVqusul8CcSP3XJpxSuQz" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a32e7bdb5d2fc033988383c62023ff58de1f5d33_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a32e7bdb5d2fc033988383c62023ff58de1f5d33_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a32e7bdb5d2fc033988383c62023ff58de1f5d33_2_1380x776.jpeg 2x" data-dominant-color="C6BFC8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>my question is this step are accurate for measuring the distance between 2 models ?</p>

---
