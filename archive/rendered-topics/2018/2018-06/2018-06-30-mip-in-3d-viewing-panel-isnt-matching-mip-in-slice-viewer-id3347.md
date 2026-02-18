# MIP in 3D viewing panel isn't matching MIP in slice viewer

**Topic ID**: 3347
**Date**: 2018-06-30
**URL**: https://discourse.slicer.org/t/mip-in-3d-viewing-panel-isnt-matching-mip-in-slice-viewer/3347

---

## Post #1 by @Hamburgerfinger (2018-06-30 18:09 UTC)

<p>Hi Slicers!  I’m having a little trouble understanding why, when I’m using the maximum intensity projection rendering method in the 3D viewer, the image doesn’t exactly match (it’s pretty close) a MIP generated in the slice viewer by e.g. using “MaximumProjectionImageFilter”.  The Volume Rendering “volume properties” were of course synchronized with the Volumes module, and the opacity mapping is set to 1.0 across the entire range.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3cdaeba830a89ac26bb2173d45995bff394f005.png" data-download-href="/uploads/short-url/pEC8GbkBDwhCWKe0EYtCes77kix.png?dl=1" title="MIP" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3cdaeba830a89ac26bb2173d45995bff394f005_2_349x500.png" alt="MIP" data-base62-sha1="pEC8GbkBDwhCWKe0EYtCes77kix" width="349" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3cdaeba830a89ac26bb2173d45995bff394f005_2_349x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3cdaeba830a89ac26bb2173d45995bff394f005_2_523x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3cdaeba830a89ac26bb2173d45995bff394f005_2_698x1000.png 2x" data-dominant-color="0A1021"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MIP</span><span class="informations">711×1017 87.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-06-30 22:48 UTC)

<p>There can be minor differences in how the rays are integrated (mainly step size, but maybe other small differences, such as what scalar type is used for accumulating values, etc.) or it may be just slightly different color lookup table.</p>

---
