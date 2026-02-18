# Painting on oblique images

**Topic ID**: 44968
**Date**: 2025-11-05
**URL**: https://discourse.slicer.org/t/painting-on-oblique-images/44968

---

## Post #1 by @Deep_Learning (2025-11-05 15:03 UTC)

<p>v5.8.1</p>
<p>sample data cta abdomen.</p>
<p>Create double oblique…</p>
<p>I have never understood this.</p>
<p>When I click with the paint tool, I do not get a circle.</p>
<p>I might understand this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e6f6524cc192c0564ceeaceb1687ece8f9c6fa9.jpeg" data-download-href="/uploads/short-url/mBA6oLmB2Q6X8038eRDI6NDiBo5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e6f6524cc192c0564ceeaceb1687ece8f9c6fa9_2_690x401.jpeg" alt="image" data-base62-sha1="mBA6oLmB2Q6X8038eRDI6NDiBo5" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e6f6524cc192c0564ceeaceb1687ece8f9c6fa9_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e6f6524cc192c0564ceeaceb1687ece8f9c6fa9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e6f6524cc192c0564ceeaceb1687ece8f9c6fa9.jpeg 2x" data-dominant-color="7C7C7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">848×493 38.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I definitely do not understand why when i drag the circle around, it fills in?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28bf0762b7eb3b46c172bef0503e5607084c4d30.jpeg" data-download-href="/uploads/short-url/5OsnkgVrT2VywzdoZv4F9oPdwpq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28bf0762b7eb3b46c172bef0503e5607084c4d30_2_690x401.jpeg" alt="image" data-base62-sha1="5OsnkgVrT2VywzdoZv4F9oPdwpq" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28bf0762b7eb3b46c172bef0503e5607084c4d30_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28bf0762b7eb3b46c172bef0503e5607084c4d30.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28bf0762b7eb3b46c172bef0503e5607084c4d30.jpeg 2x" data-dominant-color="7C7C7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">848×493 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Same behavior with and without masking.</p>

---

## Post #2 by @pieper (2025-11-05 16:05 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">
  <header class="source">

      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener">3D Slicer segmentation recipes</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener">Overview</a></h3>

  <p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Deep_Learning (2025-11-05 20:25 UTC)

<p>Thanks for the reply.</p>
<p>I was aware of this.  I’m not sure that it is the exact same issue. It may be.  This has always confused me.</p>
<p>I do not understand why when one clicks, there is one segmentation, but when one drags additional pixels are segmented.</p>
<p>I’ve been struggling with this issue for some time.  My work around was to drag the roi until it is complete.  So I am really iteratively painting away the “artifacts” without reslicing.</p>

---

## Post #4 by @cpinter (2025-11-06 09:54 UTC)

<p>When you paint an oblique slice it’s like painting this surface with a roller</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b51e9bef12e62169c8dc2180e2a44a4da2f0fa1b.jpeg" data-download-href="/uploads/short-url/pQg07eoqMWF30GtZoysR9UXLL1F.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b51e9bef12e62169c8dc2180e2a44a4da2f0fa1b_2_690x414.jpeg" alt="image" data-base62-sha1="pQg07eoqMWF30GtZoysR9UXLL1F" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b51e9bef12e62169c8dc2180e2a44a4da2f0fa1b_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b51e9bef12e62169c8dc2180e2a44a4da2f0fa1b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b51e9bef12e62169c8dc2180e2a44a4da2f0fa1b.jpeg 2x" data-dominant-color="39393F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">966×580 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>because the volume is sliced using an oblique plane.</p>
<p>Maybe we could add a thickness option to the paintbrush, but the solutions suggested by <a class="mention" href="/u/lassoan">@lassoan</a> (in the page referenced by <a class="mention" href="/u/pieper">@pieper</a>) seem to be more correct.</p>

---

## Post #5 by @chir.set (2025-11-06 11:16 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="44968">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>add a thickness option to the paintbrush</p>
</blockquote>
</aside>
<p>May be the <code>Scissors</code> effect could be used for painting in <em>most</em> cases; it already has a free-form and thickness options.</p>

---

## Post #6 by @Deep_Learning (2025-11-06 12:38 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="44968">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>When you paint an oblique slice it’s like painting this surface with a roller</p>
</blockquote>
</aside>
<p>That’s exactly it….. I guess the the irreproducibility that I was experiencing was a slight movement of the mouse.</p>
<p>Resampling is an option, but yesterday I was annotating at a bunch of angles.</p>
<p>*** One question, if i resample the volume then annotated on a specific slice, when I rotate back, won’t it have the same result?</p>
<p>I‘ve done a lot of rolling in the past.  I was annotating oblique valve planes to be subtracted from another segment and need it to be complete 3d disk.  Rolling, fill holes, etc.</p>

---

## Post #7 by @cpinter (2025-11-06 14:10 UTC)

<p>I think this is an important aspect, that you want to segment on multiple different oblique directions. In this case I don’t suggest resampling, because every time you do that, you lose some image quality (and segmentation fidelity).</p>
<p>In this case I suggest oversampling the segmentation. I just tried it and it seems to work well for oblique painting:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/632afadc43b09d7f79b9b220adf55c93006df546.png" data-download-href="/uploads/short-url/e9hlVnjoK9ncOnuEEBdrgcDMGUu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632afadc43b09d7f79b9b220adf55c93006df546_2_690x357.png" alt="image" data-base62-sha1="e9hlVnjoK9ncOnuEEBdrgcDMGUu" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632afadc43b09d7f79b9b220adf55c93006df546_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632afadc43b09d7f79b9b220adf55c93006df546_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632afadc43b09d7f79b9b220adf55c93006df546_2_1380x714.png 2x" data-dominant-color="9D9EA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1884×977 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
