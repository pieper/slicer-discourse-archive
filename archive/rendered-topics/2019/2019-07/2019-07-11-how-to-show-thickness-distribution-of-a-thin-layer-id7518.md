# How to show thickness distribution of a thin layer

**Topic ID**: 7518
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/how-to-show-thickness-distribution-of-a-thin-layer/7518

---

## Post #1 by @11125 (2019-07-11 03:39 UTC)

<p>I have a micro-CT file of a coating. I want to demonstrate the coating thickness distribution as a color contour image. Can 3d slicer do so? Or is there a function I can get the thickness data matrix registered to the coating top surface?</p>

---

## Post #2 by @pieper (2019-07-11 14:45 UTC)

<p>I don’t think there’s anything already implemented to do that, but it wouldn’t be too much work to write something that calculates it (depends a lot on the exact properties of your data, like if you are able to easily segment the coating).  Depending on how it images in the ct you might also get a reasonable visualization with volume rendering.</p>

---

## Post #3 by @lassoan (2019-07-21 03:17 UTC)

<p>How to measure thickness of a segmented structure is described here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2735">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735/2">How to analyze the thickness of the model</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    “Thickness” is not a very well defined term for models (surface meshes), but for shell-like meshes it is probably not too difficult to estimate it robustly and accurately. 
Potential approaches: 
A. Extract medial surface and estimate thickness as 2x of distance from medial surface. There are various ways of computing these in Slicer. One possible workflow: 

Compute medial surface using Simple Filters module - BinaryThinningImageFilter.
Compute distance map using Simple Filters module - Daniels…
  </blockquote>
</aside>


---
