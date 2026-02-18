# Functionality of Automatic Threshold Calculator

**Topic ID**: 19652
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/functionality-of-automatic-threshold-calculator/19652

---

## Post #1 by @alyssan (2021-09-13 20:14 UTC)

<p>Hello, I was looking at this example:<a href="https://gist.github.com/lassoan/4d0b94bda52d5b099432e424e03aa2b1" class="inline-onebox" rel="noopener nofollow ugc">Automatic endocranium segmentation from dry bone CT scan · GitHub</a><br>
I am interested in knowing how it computes the bone threshold automatically. I am trying to segment bone. Can this be used on any data?</p>

---

## Post #2 by @muratmaga (2021-09-13 20:33 UTC)

<p>It is in line 10 of the code (Otsu threshold method).<br>
There are many different types of automatic threshold calculation methods. Each with different assumption about the intensity distribution and/or how they model the data. You can interactively try one after the other and see which works best for your data.</p>

---

## Post #3 by @alyssan (2021-09-13 20:48 UTC)

<p>okay, thanks. Where can I find these?</p>

---

## Post #4 by @muratmaga (2021-09-13 21:02 UTC)

<p>segment editor → Threshold effect -&gt;Automatic threshold</p>

---

## Post #5 by @lassoan (2021-09-14 05:03 UTC)

<p>I’ve created this script before <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify/#surface-wrap-solidify">SurfaceWrapSolidify extension</a> existed. I would now recommend to use SurfaceWrapSolidify extension for automatic extraction of cavities inside a segmented bone, as it is more flexible, more robust, and more accurate. See detailed description <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/">here</a>.</p>

---
