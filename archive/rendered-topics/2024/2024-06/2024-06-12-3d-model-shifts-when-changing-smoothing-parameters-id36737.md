---
topic_id: 36737
title: "3D Model Shifts When Changing Smoothing Parameters"
date: 2024-06-12
url: https://discourse.slicer.org/t/36737
---

# 3D model shifts when changing smoothing parameters

**Topic ID**: 36737
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/3d-model-shifts-when-changing-smoothing-parameters/36737

---

## Post #1 by @ckolluru (2024-06-12 21:22 UTC)

<p>I use the grayscale model maker to create an isosurface of my volume. When I change the value of the smooth parameter from 15 to zero, the model shifts slightly in the 3D view. I’ve set the Decimate option to zero. All other parameters are defaults. Please see rendering below.</p>
<p>I’m rendering one output geometry in purple and another in red with some transparency. Viewing is set to perspective mode (default) and the camera angle was set to one of the standard directions (A-P).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1d2fcdb625d4b2f80a26c5a29766201bfc67366.jpeg" data-download-href="/uploads/short-url/yvh6MShUvw8RYtgKN9uAvR6TR3g.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d2fcdb625d4b2f80a26c5a29766201bfc67366_2_643x500.jpeg" alt="image" data-base62-sha1="yvh6MShUvw8RYtgKN9uAvR6TR3g" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d2fcdb625d4b2f80a26c5a29766201bfc67366_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d2fcdb625d4b2f80a26c5a29766201bfc67366_2_964x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1d2fcdb625d4b2f80a26c5a29766201bfc67366.jpeg 2x" data-dominant-color="9495C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1153×896 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any insights on why this is happening?</p>
<p>Thanks,<br>
Chaitanya</p>

---

## Post #2 by @pieper (2024-06-12 21:31 UTC)

<p>Try the latest versions of Slicer.  Probably you are seeing the issues described below, which have been fixed.</p>
<aside class="quote quote-modified" data-post="1" data-topic="34723">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/3ab097/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/accuracy-of-segmentation-smoothing/34723">Accuracy of segmentation smoothing</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
I am healthcare professional, a general and orthopedic surgeon with over 24 years of active experience. We have been using an FDA approved software for complex surgical planning for the past 8 years. 
However, due to its increasing cost per seat, we were looking for alternative and free solutions and came across 3D Slicer. I appreciate what Slicer’s existing features provide, and we started evaluating it just a couple of months ago. Besides the great functionalities, I have found subtle …
  </blockquote>
</aside>

<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676/20">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676/20" target="_blank" rel="noopener" title="12:57AM - 13 March 2024">VTK – 13 Mar 24</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:318/199;"><img src="https://discourse.vtk.org/uploads/default/original/2X/3/362ea1f2fd601cf9bc5b4afa8a679d59999de389.png" class="thumbnail" width="318" height="199"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676/20" target="_blank" rel="noopener">Slight offset in vtkWindowedSincPolyDataFilter if normalization is enabled</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Support</span>
        </span>
      </span>
  </div>
</div>

  <p>The fix has been integrated into VTK. To illustrate the effect of what has changed, here is the result (in red) of smoothing a bumpy surface (white), generated by the newly added smoothCylNuttall test:     Left: result when using the old Hamming...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ckolluru (2024-06-15 16:06 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, this seems to work.</p>
<p>Upgraded from version 5.6.1 r32438 to 5.6.2.</p>

---
