# 3D rendering of segmentations without Slicer GUI

**Topic ID**: 44177
**Date**: 2025-08-23
**URL**: https://discourse.slicer.org/t/3d-rendering-of-segmentations-without-slicer-gui/44177

---

## Post #1 by @metabot18 (2025-08-23 02:58 UTC)

<p>Hello Slicer community.</p>
<p>Is it possible to generate 3D renderings like these by calling Slicer’s functions from a Python environment, without having to load Slicer’s GUI?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c0dfc1a64965d67597b46b856e09f7fb8662b57.jpeg" data-download-href="/uploads/short-url/jYYO6nt1hkK55cjTiAElIJLXCw7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c0dfc1a64965d67597b46b856e09f7fb8662b57_2_237x500.jpeg" alt="image" data-base62-sha1="jYYO6nt1hkK55cjTiAElIJLXCw7" width="237" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c0dfc1a64965d67597b46b856e09f7fb8662b57_2_237x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c0dfc1a64965d67597b46b856e09f7fb8662b57_2_355x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c0dfc1a64965d67597b46b856e09f7fb8662b57_2_474x1000.jpeg 2x" data-dominant-color="EAEAE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">490×1032 37.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried doing these through VTK Python, but I could not get a very smooth rendering that Slicer manages to do.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2025-08-23 14:50 UTC)

<p>There’s a long thread on rendering.  These approaches should all work with the <code>--no-main-window</code> and <code>--python-script</code> options Slicer options.</p>
<aside class="quote" data-post="47" data-topic="8880">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sdv/48/79161_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/higher-resolution-for-screen-captures-of-3d-view/8880/47">Higher resolution for screen captures of 3D view?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Has this ever been implemented? I would need to export an image series at 4x the resolution of my display.
  </blockquote>
</aside>


---
