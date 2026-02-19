---
topic_id: 10134
title: "Using Surface Cut With Curves"
date: 2020-02-06
url: https://discourse.slicer.org/t/10134
---

# Using surface cut with curves

**Topic ID**: 10134
**Date**: 2020-02-06
**URL**: https://discourse.slicer.org/t/using-surface-cut-with-curves/10134

---

## Post #1 by @muratmaga (2020-02-06 02:26 UTC)

<p>Is it possible to use Surface Cut tool with fiducials that are already placed, particularly with curve ones?</p>

---

## Post #2 by @lassoan (2020-02-06 03:19 UTC)

<p>Surface cut effect creates an enclosing surface of a point cloud, so it would not be directly applicable to a curve. How would you like to cut with a curve?</p>

---

## Post #3 by @muratmaga (2020-02-06 04:36 UTC)

<p>I was using the curves to outline the boundaries of individual cranial bones, and I thought perhaps I can use them to do the segmentations…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4c5d5031b3c9327ce1e3d2820807446cbbdec00.jpeg" data-download-href="/uploads/short-url/umh4M1nCn7nZd1qZpMS6Sz8zQaY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4c5d5031b3c9327ce1e3d2820807446cbbdec00_2_455x500.jpeg" alt="image" data-base62-sha1="umh4M1nCn7nZd1qZpMS6Sz8zQaY" width="455" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4c5d5031b3c9327ce1e3d2820807446cbbdec00_2_455x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4c5d5031b3c9327ce1e3d2820807446cbbdec00.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4c5d5031b3c9327ce1e3d2820807446cbbdec00.jpeg 2x" data-dominant-color="565569"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">518×569 86.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-02-06 04:51 UTC)

<p>In the next 6 months, we’ll implement parcellation of gray matter from curves drawn on segmented surfaces (and additional planes). It will be usable for splitting up a bone segment like the one you show above.</p>
<p>Until then, you can do this using Scissors module - see <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">Craniotomy segmentation recipe</a>.</p>
<p>You can also play with markups and see what surfaces you can get out of them using “Markups to model” extension.</p>

---

## Post #5 by @muratmaga (2020-02-06 05:14 UTC)

<p>Sounds awesome. I will test the options, thanks again.</p>

---
