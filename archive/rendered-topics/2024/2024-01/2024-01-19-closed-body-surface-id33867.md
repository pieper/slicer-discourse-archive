---
topic_id: 33867
title: "Closed Body Surface"
date: 2024-01-19
url: https://discourse.slicer.org/t/33867
---

# Closed body surface

**Topic ID**: 33867
**Date**: 2024-01-19
**URL**: https://discourse.slicer.org/t/closed-body-surface/33867

---

## Post #1 by @Miri_Trope (2024-01-19 11:23 UTC)

<p>Hello, I tried creating a visually appealing closed surface representation of the body using an MRI image of the breast. I utilized SimpleITK and implemented a custom algorithm. Unfortunately, I observed that the resulting vtk image has noticeable gaps. How can I generate a closed surface without these holes?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a77edfcf04f7dc91256ecd5dfca4b7ca071effde.png" data-download-href="/uploads/short-url/nTJyZxK6Rm0psE7LuJ9ZAkhKX5s.png?dl=1" title="Screenshot 2024-01-19 at 13.20.03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77edfcf04f7dc91256ecd5dfca4b7ca071effde_2_690x290.png" alt="Screenshot 2024-01-19 at 13.20.03" data-base62-sha1="nTJyZxK6Rm0psE7LuJ9ZAkhKX5s" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77edfcf04f7dc91256ecd5dfca4b7ca071effde_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77edfcf04f7dc91256ecd5dfca4b7ca071effde_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77edfcf04f7dc91256ecd5dfca4b7ca071effde_2_1380x580.png 2x" data-dominant-color="626269"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-01-19 at 13.20.03</span><span class="informations">1791×753 62.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rkikinis (2024-01-19 12:27 UTC)

<p>Hi<br>
Did you try to segment the <strong>entire</strong> breasts (fat, gland, skin) and then apply wrap solidify?</p><aside class="quote quote-modified" data-post="1" data-topic="11248">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248">Fill or extract cavities in segmentations using the new "Wrap Solidify" effect</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Making a segment that has fractured, discontinuous boundary and holes inside to be a simple solid object is a quite common task for segmentation. For example it is needed for creating simple solid bone models from CT images, extracting skin surface, segment thin surfaces, such as orbital bone wall, measuring brain volume, or volumes of various cavities. 
Slicer now has a tool for all this: “Wrap Solidify” Segment Editor effect, provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" rel="noopener nofollow ugc">SurfaceWrapSolidify extension</a> and contributed by Sebasti…
  </blockquote>
</aside>


---
