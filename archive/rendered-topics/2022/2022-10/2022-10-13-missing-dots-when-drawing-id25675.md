# Missing dots when drawing

**Topic ID**: 25675
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/missing-dots-when-drawing/25675

---

## Post #1 by @Leonie (2022-10-13 11:43 UTC)

<p>Slicer version: Slicer 5.0.3</p>
<p>I have a problem with the drawing function in the segment editor. I wanted to calculate the area of fat, muscle and bone by marking them and then use the tool “segment statistics”. But somehow there are some pointed lines appearing (see following picture), and I don’t know how to get rid of them.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6701001d29818f42412acce5686ef28b2cce6e45.png" data-download-href="/uploads/short-url/eHdk1e2XTNGOxrJDcl4DYg2UhSd.png?dl=1" title="3dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6701001d29818f42412acce5686ef28b2cce6e45_2_536x500.png" alt="3dslicer" data-base62-sha1="eHdk1e2XTNGOxrJDcl4DYg2UhSd" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6701001d29818f42412acce5686ef28b2cce6e45_2_536x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6701001d29818f42412acce5686ef28b2cce6e45.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6701001d29818f42412acce5686ef28b2cce6e45.png 2x" data-dominant-color="615056"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer</span><span class="informations">759×707 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe someone has an idea how to deal with this…</p>

---

## Post #2 by @lassoan (2022-10-21 03:16 UTC)

<p>The lines indicate that the slice view is not parallel with the segmentation’s axes. See more details <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">here</a>.</p>

---
