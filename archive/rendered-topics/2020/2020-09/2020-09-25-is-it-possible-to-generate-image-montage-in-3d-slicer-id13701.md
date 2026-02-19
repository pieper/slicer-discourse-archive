---
topic_id: 13701
title: "Is It Possible To Generate Image Montage In 3D Slicer"
date: 2020-09-25
url: https://discourse.slicer.org/t/13701
---

# Is it possible to generate image montage in 3D Slicer?

**Topic ID**: 13701
**Date**: 2020-09-25
**URL**: https://discourse.slicer.org/t/is-it-possible-to-generate-image-montage-in-3d-slicer/13701

---

## Post #1 by @Vincent_C (2020-09-25 19:17 UTC)

<p>Hi all,</p>
<p>There is a tool is FSL - <a href="https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Miscvis" class="inline-onebox" rel="noopener nofollow ugc">Miscvis - FslWiki</a> - that can make a montage of multiple slices in axial, sagittal and coronal planes and output in .png format. Is there also a function like this available in Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a3d074dff44f81473d540d986cd4292b3714830.jpeg" data-download-href="/uploads/short-url/aAK5jZ2MdYMWn1t2rX0KTOBEKoo.jpeg?dl=1" title="sample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3d074dff44f81473d540d986cd4292b3714830_2_690x394.jpeg" alt="sample" data-base62-sha1="aAK5jZ2MdYMWn1t2rX0KTOBEKoo" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3d074dff44f81473d540d986cd4292b3714830_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3d074dff44f81473d540d986cd4292b3714830_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a3d074dff44f81473d540d986cd4292b3714830_2_1380x788.jpeg 2x" data-dominant-color="6A6A6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample</span><span class="informations">4658×2661 2.18 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-09-25 19:28 UTC)

<p>It is available in Screen Capture module - lightbox mode.</p>
<aside class="quote quote-modified" data-post="1" data-topic="10840">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-lightbox-contact-image-mode-in-screen-capture-module/10840">New lightbox (contact image) mode in screen capture module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A new “lightbox image” output type has been added in latest Slicer Preview Release. In this mode captured images are exported as a large grid of images: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b737f2e84e22dbe5725e57b74040dfa74fc7e38.jpeg" data-download-href="/uploads/short-url/mbbsraigdO5OdE17N7EAXim06Gk.jpeg?dl=1" title="image">[image]</a> 
Images can be exported from any views, with any animation mode, just select “Output type” → “lightbox image”. Number of columns is adjustable in Advanced section. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c7fa019c8ddd0bf1957e63551324a6e76df0fc5.jpeg" data-download-href="/uploads/short-url/mkrV8nslGxYE7hYKKQO4HxFTQHj.jpeg?dl=1" title="image">[image]</a> 
We plan to further improve this lightbox view generation in the future and retire dynamic lightbox views. Any comments and suggestions are welcome.
  </blockquote>
</aside>


---
