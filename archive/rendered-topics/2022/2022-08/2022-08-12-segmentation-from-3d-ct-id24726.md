# Segmentation from 3D CT

**Topic ID**: 24726
**Date**: 2022-08-12
**URL**: https://discourse.slicer.org/t/segmentation-from-3d-ct/24726

---

## Post #1 by @francesca_flore (2022-08-12 10:21 UTC)

<p>Anyone know how to segment a 3D CT scan? Exist any extension to do this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56cc21d3d8acb5ee13cd244e63db17192f2e9095.jpeg" data-download-href="/uploads/short-url/cnQpDGhlXcCx17cJDn96S4HsU3H.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56cc21d3d8acb5ee13cd244e63db17192f2e9095_2_640x500.jpeg" alt="image" data-base62-sha1="cnQpDGhlXcCx17cJDn96S4HsU3H" width="640" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56cc21d3d8acb5ee13cd244e63db17192f2e9095_2_640x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56cc21d3d8acb5ee13cd244e63db17192f2e9095.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56cc21d3d8acb5ee13cd244e63db17192f2e9095.jpeg 2x" data-dominant-color="383838"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">920×718 54.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2022-08-12 13:08 UTC)

<p>Please refer to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/index.html#segmentation" rel="noopener nofollow ugc">manual</a> for an in-depth discovery of the ‘Segment editor’ in particular.</p>

---

## Post #3 by @francesca_flore (2022-08-12 13:34 UTC)

<p>The picture is not just a single view of the CT. Is a 3D view CT with a rotation of 15 degrees. So the question is if there is a way to segment directly on the 3D view. Because I have poor quality images in the different three views, instead of 3D you can see perfectly the areas that I would like to segment.</p>

---

## Post #4 by @chir.set (2022-08-12 14:29 UTC)

<aside class="quote no-group" data-username="francesca_flore" data-post="3" data-topic="24726">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/francesca_flore/48/15307_2.png" class="avatar"> francesca_flore:</div>
<blockquote>
<p>Is a 3D view CT</p>
</blockquote>
</aside>
<p>Ok, I thought you were referring to CT scan volumes usually shipped to clinicians as a pile of DICOM images.</p>
<p>The ‘3D view CT’ is foreign to me, may be someone else may be of better help here.</p>
<p>Is it possible to upload an anonymized dataset of this ‘3D view CT’ ? I would very much like to know what it is.</p>

---

## Post #5 by @mohammed_alshakhas (2022-08-13 08:45 UTC)

<p>You can’t segment a 3d images , those images are already processed .<br>
Segmentation is done for Dicom or even JPEG .  These are raw images that can be used for segmentation .</p>
<p>Look for the original volume , usually axial series and use it for segmentation</p>

---
