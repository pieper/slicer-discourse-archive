# Shifting problem in model slice display

**Topic ID**: 41897
**Date**: 2025-02-27
**URL**: https://discourse.slicer.org/t/shifting-problem-in-model-slice-display/41897

---

## Post #1 by @alientex (2025-02-27 10:46 UTC)

<p>Hi,</p>
<p>I created a segment and exported it into a model. When I turn on slice display visibility, I notice an extreme contour shift, as shown in the images below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8d6c7b010fb62a27387504332242d00bd3141bd.png" data-download-href="/uploads/short-url/qna19I56YW0kpVh2EXpfwXycVNr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d6c7b010fb62a27387504332242d00bd3141bd_2_345x197.png" alt="image" data-base62-sha1="qna19I56YW0kpVh2EXpfwXycVNr" width="345" height="197" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d6c7b010fb62a27387504332242d00bd3141bd_2_345x197.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d6c7b010fb62a27387504332242d00bd3141bd_2_517x295.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8d6c7b010fb62a27387504332242d00bd3141bd_2_690x394.png 2x" data-dominant-color="908984"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1527×872 38.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bced321a54f219c2b0467acaefeb70acc387f73d.png" data-download-href="/uploads/short-url/qXjX8RuY5VJkeAKaYhW4ZJTyv7f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bced321a54f219c2b0467acaefeb70acc387f73d.png" alt="image" data-base62-sha1="qXjX8RuY5VJkeAKaYhW4ZJTyv7f" width="301" height="250" data-dominant-color="997973"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×731 5.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why is this happening?</p>

---

## Post #2 by @cpinter (2025-02-27 12:37 UTC)

<p>The labelmap consists of 3D boxes, and compared to that the surface is a continuous representation. I think simply the slice position you look at is not at the center of the labelmap voxel. Btw I wouldn’t call a half voxel discrepancy extreme. It’s similar to the partial volume effect.</p>

---

## Post #3 by @MJamal (2025-03-03 06:12 UTC)

<p>I am also facing this problem. In my case, it varies from system to system. I tried checking on another system, but I didn’t see the same effect (or shifting issue) there.</p>
<p>Is it system-dependent?</p>

---

## Post #4 by @lassoan (2025-03-03 12:58 UTC)

<p>Please use the latest version of Slicer, we have managed to reduce the effect of smoothing causing slight shift.</p>
<p>If you have problems with accuracy (some details not accurately preserved) you can always work on a smaller region of interest and increase the resolution of the binary labelmap representation of the segmentation.</p>

---

## Post #5 by @MJamal (2025-03-04 09:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="41897">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Please use the latest version of Slicer, we have managed to reduce the effect of smoothing causing slight shift.</p>
</blockquote>
</aside>
<p>Could you please share the commit link for these changes? I’d like to take a look at it.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="41897">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>tpu can always work on a smaller region of interest</p>
</blockquote>
</aside>
<p>Sorry, I didn’t quite understand—what is tpu?</p>

---

## Post #6 by @lassoan (2025-03-04 12:59 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="5" data-topic="41897">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Could you please share the commit link for these changes? I’d like to take a look at it.</p>
</blockquote>
</aside>
<p>I had to make this fix at VTK level. See all the details here:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676" target="_blank" rel="noopener" title="11:34PM - 18 January 2022">VTK – 18 Jan 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/278;"><img src="https://discourse.vtk.org/uploads/default/optimized/2X/0/093f5d3b0df40b4195b4c9cf379fac8869735b30_2_1024x413.jpeg" class="thumbnail" width="690" height="278"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676" target="_blank" rel="noopener">Slight offset in vtkWindowedSincPolyDataFilter if normalization is enabled</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Support</span>
        </span>
      </span>
  </div>
</div>

  <p>When using vtkWindowedSincPolyDataFilter with NormalizeCoordinates enabled then we have found that smoothing result is slightly shifted when the bounding box of the mesh is changed. (originally reported by a 3D Slicer user here).  Example   Data...</p>

  <p>
    <span class="label1">Reading time: 4 mins 🕑</span>
      <span class="label2">Likes: 6 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="MJamal" data-post="5" data-topic="41897">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Sorry, I didn’t quite understand</p>
</blockquote>
</aside>
<p>You can reduce the ROI and increase the resolution as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>. “Specify geometry” function is described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">here</a>.</p>

---
