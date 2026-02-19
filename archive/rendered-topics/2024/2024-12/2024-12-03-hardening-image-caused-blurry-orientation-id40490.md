---
topic_id: 40490
title: "Hardening Image Caused Blurry Orientation"
date: 2024-12-03
url: https://discourse.slicer.org/t/40490
---

# Hardening image caused blurry orientation

**Topic ID**: 40490
**Date**: 2024-12-03
**URL**: https://discourse.slicer.org/t/hardening-image-caused-blurry-orientation/40490

---

## Post #1 by @Dimitri_Gouvoussis (2024-12-03 13:36 UTC)

<p>Hello, I am trying to measure the density of my images and am having an issue geeting them to load properly. I am using CT scans capatured with a Bruker Skyscan 1276 micro-CT. When I load the files into 3d slicer the axial, sagittal, and coronal views load fine (see image 1) but no 3D rendering appears. I was told I could fix this issue by clicking “harden transfrom”. My 3D view did appear by clicking this but was blurry and the rest of my views became blurry as well (see image 2). How can I fix this issue or at least accurately measure the density of the white sections. Thank you for your help!</p>
<p>Image 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49689e734a464ff6aa6c8d42c8a151af2c65a88b.jpeg" data-download-href="/uploads/short-url/atp01xSILj4btX0uUjbFmPePOob.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49689e734a464ff6aa6c8d42c8a151af2c65a88b_2_690x365.jpeg" alt="image" data-base62-sha1="atp01xSILj4btX0uUjbFmPePOob" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49689e734a464ff6aa6c8d42c8a151af2c65a88b_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49689e734a464ff6aa6c8d42c8a151af2c65a88b_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49689e734a464ff6aa6c8d42c8a151af2c65a88b_2_1380x730.jpeg 2x" data-dominant-color="353438"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2236×1183 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image 2 (After Hardening Transform)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19d1926de26a0dacd94c5fd048f1d6388035d87a.png" data-download-href="/uploads/short-url/3GoWrEoxPkcjbnqakKNTnMFmNeO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19d1926de26a0dacd94c5fd048f1d6388035d87a_2_690x363.png" alt="image" data-base62-sha1="3GoWrEoxPkcjbnqakKNTnMFmNeO" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19d1926de26a0dacd94c5fd048f1d6388035d87a_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19d1926de26a0dacd94c5fd048f1d6388035d87a_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19d1926de26a0dacd94c5fd048f1d6388035d87a_2_1380x726.png 2x" data-dominant-color="313135"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2242×1182 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-12-03 15:54 UTC)

<aside class="quote no-group" data-username="Dimitri_Gouvoussis" data-post="1" data-topic="40490">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dimitri_gouvoussis/48/78608_2.png" class="avatar"> Dimitri_Gouvoussis:</div>
<blockquote>
<p>My 3D view did appear by clicking this but was blurry and the rest of my views became blurry as well</p>
</blockquote>
</aside>
<p>That’s the effect of the transform. You should look into what that is and why there is a transform. Bruker systems do not usually output in DICOM format, but image sequences like TIFF, BMP, PNG. So I suspect something went wrong wen the data got converted into DICOM from the original image sequence.</p>
<p>My suggestion is try the <code>ImageStacks</code> module in Slicermorph to import the original sequence if you can. You should not have any of these issues.</p>

---
