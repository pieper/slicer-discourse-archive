# Margin tool stopped reporting the pixel units

**Topic ID**: 10749
**Date**: 2020-03-19
**URL**: https://discourse.slicer.org/t/margin-tool-stopped-reporting-the-pixel-units/10749

---

## Post #1 by @muratmaga (2020-03-19 18:49 UTC)

<p>In about a month ago, Margin tool used to have a field that converted margins to actual pixel based on the voxel dimension:</p>
<p>This now disappeared, which is sort of a big deal for our use cases with sub-millimeter voxel sizes:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4638606abf206be8ff77846c41e21bdba2a4fda.png" alt="image" data-base62-sha1="nsfx4d05K5oxrF44z051Uw0FNN0" width="586" height="424"></p>

---

## Post #2 by @lassoan (2020-03-19 19:59 UTC)

<p>The actual size is still reported, below the spinbox:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc4c844459b4e7f58977f762a500f55d82d17a78.png" data-download-href="/uploads/short-url/t9jl5DBViJ3xo4kmMo9gr5OxYlW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc4c844459b4e7f58977f762a500f55d82d17a78_2_568x500.png" alt="image" data-base62-sha1="t9jl5DBViJ3xo4kmMo9gr5OxYlW" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc4c844459b4e7f58977f762a500f55d82d17a78_2_568x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc4c844459b4e7f58977f762a500f55d82d17a78_2_852x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc4c844459b4e7f58977f762a500f55d82d17a78.png 2x" data-dominant-color="F5F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">983×865 42.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you miss the size in pixels?</p>

---

## Post #3 by @muratmaga (2020-03-19 20:07 UTC)

<p>Yes, because the memory consumption seems to be tied into the how big the margin is, and it is sort uninformative just to have the millimeters…</p>

---

## Post #4 by @lassoan (2020-03-19 20:19 UTC)

<p>Execution time used to depend on margin size in pixels, but this should not be the case anymore.</p>
<p>Regardless, we could still add display of margin size in pixels. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, could you add this (just in parentheses after the mm values; in Margin, Hollow, Smoothing effects)?</p>

---

## Post #5 by @Sunderlandkyl (2020-03-25 16:27 UTC)

<p>The margin size in pixels should now be displayed in the latest release.</p>

---
