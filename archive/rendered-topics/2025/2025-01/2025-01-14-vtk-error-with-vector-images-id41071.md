# VTK error with vector images

**Topic ID**: 41071
**Date**: 2025-01-14
**URL**: https://discourse.slicer.org/t/vtk-error-with-vector-images/41071

---

## Post #1 by @muratmaga (2025-01-14 06:37 UTC)

<p>When I try to set a vector image as a background volume and a scalar image as as a background volume, I get this error and slice view is messed up:<br>
<code>[VTK] The first input can have a maximum of four components</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06277dd72813b570dfaa34d7b511509f12572976.png" data-download-href="/uploads/short-url/SrtsjLmTANkqxNMennfGVjivz0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06277dd72813b570dfaa34d7b511509f12572976.png" alt="image" data-base62-sha1="SrtsjLmTANkqxNMennfGVjivz0" width="515" height="419"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">515×419 87.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The other way around works fine:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d034474665a7e621f5e725f33d67bf5a58b2696e.jpeg" data-download-href="/uploads/short-url/tHRjPuyhHUMMAM0P8zrgBcQGS7Q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d034474665a7e621f5e725f33d67bf5a58b2696e.jpeg" alt="image" data-base62-sha1="tHRjPuyhHUMMAM0P8zrgBcQGS7Q" width="544" height="392"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">544×392 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this a bug?<br>
<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @muratmaga (2025-01-14 06:41 UTC)

<p>Looking at this thread, this appears to be a know issue:</p><aside class="quote quote-modified" data-post="2" data-topic="16649">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rgb-or-rgba-rendering-of-single-2d-image-in-3d-not-working/16649/2">RGB or RGBA rendering of single 2D image in 3D not working</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    3-component RGB images appear correctly in slice views and the slices can be displayed in 3D view, too. 
4-component RGBA images are required for color volume rendering but RGBA volumes, but slice views of such volumes cannot be displayed in 3D view - see <a href="https://github.com/Slicer/Slicer/issues/4939" rel="noopener nofollow ugc">this issue</a>. If you want this to be fixed then <a href="https://discourse.slicer.org/t/about-the-feature-requests-category/30">add a vote for it</a>. If an issue gets many quotes (or needed for a funded project) then we can allocate developers to fix it. If you need it sooner and you are comfortable with C++ and the VTK library…
  </blockquote>
</aside>

<p>In that case, is there a way to convert RGBA image into RGB in Slicer?</p>

---

## Post #3 by @pieper (2025-01-14 20:44 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="41071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In that case, is there a way to convert RGBA image into RGB in Slicer?</p>
</blockquote>
</aside>
<p>With a couple lines of python you can strip away the alpha channel and then make a new volume.  I don’t think we have a module that does it though.</p>

---

## Post #4 by @muratmaga (2025-01-14 20:55 UTC)

<p>I actually managed that last night, but that turned out to be a dead end too.</p>
<p>It appears I cannot use the transparency and overlays with RGB images in slice views (I presume due to lack of alpha channel, unless it is a bug).</p>

---

## Post #5 by @pieper (2025-01-14 21:19 UTC)

<p>Color image rendering hasn’t been much of a priority, but yes, it should be possible to fix the pipelines if someone is able to dig into it.</p>

---
