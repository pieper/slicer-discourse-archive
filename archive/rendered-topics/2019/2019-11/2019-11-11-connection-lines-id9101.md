# Connection lines?

**Topic ID**: 9101
**Date**: 2019-11-11
**URL**: https://discourse.slicer.org/t/connection-lines/9101

---

## Post #1 by @a.dinauer (2019-11-11 00:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42cdb776c81b9ea30e7e7e48dd33c8fcc286f09f.jpeg" data-download-href="/uploads/short-url/9wYg3pIK7akugmMiIdOksTo19IX.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42cdb776c81b9ea30e7e7e48dd33c8fcc286f09f_2_690x388.jpeg" alt="PNG" data-base62-sha1="9wYg3pIK7akugmMiIdOksTo19IX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42cdb776c81b9ea30e7e7e48dd33c8fcc286f09f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42cdb776c81b9ea30e7e7e48dd33c8fcc286f09f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42cdb776c81b9ea30e7e7e48dd33c8fcc286f09f_2_1380x776.jpeg 2x" data-dominant-color="818185"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1920×1080 399 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hello, I have this problem with my MRI image. When I segment I get these lines. The result becomes very unclean and it happens automatically. Looks like connecting lines. Can I turn it off? I didn’t have this problem in one of 7 MRIs, but I couldn’t figure out what was different.</p>

---

## Post #2 by @lassoan (2019-11-11 02:52 UTC)

<p>This is normal behavior when image axes are not parallel with slice view axes. See detailed explanation and options for segmenting on oblique slices here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---
