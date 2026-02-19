---
topic_id: 1975
title: "Can T Find The Stl File In Save Windov"
date: 2018-01-30
url: https://discourse.slicer.org/t/1975
---

# Can`t find the stl file in save windov

**Topic ID**: 1975
**Date**: 2018-01-30
**URL**: https://discourse.slicer.org/t/can-t-find-the-stl-file-in-save-windov/1975

---

## Post #1 by @Davinca (2018-01-30 15:28 UTC)

<p>Actual behavior:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc5d78fa63d5426b2b7929aa82e6a044f6d88866.jpeg" data-download-href="/uploads/short-url/t9TFpUoMb5VHauRkAQBdhRgSLSC.jpg?dl=1" title="STL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc5d78fa63d5426b2b7929aa82e6a044f6d88866_2_666x500.jpg" alt="STL" data-base62-sha1="t9TFpUoMb5VHauRkAQBdhRgSLSC" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc5d78fa63d5426b2b7929aa82e6a044f6d88866_2_666x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc5d78fa63d5426b2b7929aa82e6a044f6d88866_2_999x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc5d78fa63d5426b2b7929aa82e6a044f6d88866_2_1332x1000.jpg 2x" data-dominant-color="7A817E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">STL</span><span class="informations">1632×1224 1.01 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-01-30 18:38 UTC)

<p>You cannot save fiducial markers as a segmentation. STL represents a surface, not a set of points. You need to use Segment Editor module to create your segmentation, then export the segmentation into a model that you can save as STL.</p>
<aside class="quote quote-modified" data-post="1" data-topic="700">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-video-tutorial-for-segment-editor-lumbar-spine-segmentation-for-3d-printing/700">New video tutorial for Segment editor - lumbar spine segmentation for 3D printing</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is the first part of a video tutorial series that teaches how to use Segment editor. This tutorial explains how to create a 3D-printable lumbar spine segment that can be used for lumbar puncture training: 

The video tutorial was created by Hilary Lia (PerkLab, Queen’s University), with help from <a class="mention" href="/u/cpinter">@cpinter</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/ungi">@ungi</a>. 
Please post your comments here about how useful this tutorial format is, what did you like/what to improve, what topics/techniques/anatomical structures you would be int…
  </blockquote>
</aside>


---
