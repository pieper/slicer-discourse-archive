# Interpolating points outside image

**Topic ID**: 14319
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/interpolating-points-outside-image/14319

---

## Post #1 by @Nadun_19 (2020-10-30 03:58 UTC)

<p>Hi I was if there are any extensions on 3dslicer that fixes these flat edges due to images being cut off there:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8d78d40e2d3d7a7f0ed1debb89c15672d680d9f.png" data-download-href="/uploads/short-url/uWgWYfojhGRNHlzKsbxkB07KzjV.png?dl=1" title="flat_surface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8d78d40e2d3d7a7f0ed1debb89c15672d680d9f_2_680x500.png" alt="flat_surface" data-base62-sha1="uWgWYfojhGRNHlzKsbxkB07KzjV" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8d78d40e2d3d7a7f0ed1debb89c15672d680d9f_2_680x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8d78d40e2d3d7a7f0ed1debb89c15672d680d9f_2_1020x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8d78d40e2d3d7a7f0ed1debb89c15672d680d9f.png 2x" data-dominant-color="434648"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">flat_surface</span><span class="informations">1300×955 89.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-10-30 04:20 UTC)

<p>You can make the segmentation region larger, using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">Specify geometry button</a> and a region of interest that is large enough to contain the full anatomy. You can then use paint and scissors effect in Segment editor to sculpt the missing parts.</p>
<p>If you find this sculpting too challenging then segment a complete volume, register it to your volume, segment the structures of interests, and import them into your segmentation. You can then use masking settings to paint over parts of the imported segments into your cropped segmentation.</p>

---
