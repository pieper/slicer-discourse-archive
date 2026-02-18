# Improved 3D preview during segmentation

**Topic ID**: 4795
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/improved-3d-preview-during-segmentation/4795

---

## Post #1 by @lassoan (2018-11-19 05:39 UTC)

<p>Two small but useful improvements have been made to Segment Editor module, which allows easier and faster preview of segmentation results in 3D. These features are available in latest nightly versions (2018-11-19 or later).</p>
<p><strong>1. Quick enable/disable of smoothing</strong></p>
<p>When “Show 3D” is enabled in Segment Editor, 3D surface representation is regenerated each time when a segment is modified. Most time-consuming component of surface regeneration is smoothing. Depending on the segment’s complexity, <strong>3D surface updates can be up to 10x faster with smoothing disabled</strong>.</p>
<p>We have now made it simpler to temporarily disable smoothing by clicking on the “Show 3D” button’s “down-arrow” and uncheck “Surface smoothing”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33b813aa03c3819c2a389e622bc0abb5ba366ce2.png" data-download-href="/uploads/short-url/7nwJuwaFynAnlFB2y5VEbJB0nl0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b813aa03c3819c2a389e622bc0abb5ba366ce2_2_690x336.png" alt="image" data-base62-sha1="7nwJuwaFynAnlFB2y5VEbJB0nl0" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b813aa03c3819c2a389e622bc0abb5ba366ce2_2_690x336.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b813aa03c3819c2a389e622bc0abb5ba366ce2_2_1035x504.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33b813aa03c3819c2a389e622bc0abb5ba366ce2_2_1380x672.png 2x" data-dominant-color="CFCFDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1511×737 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>2. Quick 3D preview in Grow from seeds, Fill between slices, and Watershed effects</strong></p>
<p>It has been made much simpler to preview segmentation results of Grow from seeds (and other auto-complete style effects) in 3D view, by clicking “Show 3D” button in “Display” row of effect parameters section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3b624e4c1ab9bd5a3b2ebf4a3a4069889b3e1c6.jpeg" data-download-href="/uploads/short-url/ucSZgLtYbSJOHvr43dg3njZacho.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3b624e4c1ab9bd5a3b2ebf4a3a4069889b3e1c6_2_690x419.jpeg" alt="image" data-base62-sha1="ucSZgLtYbSJOHvr43dg3njZacho" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3b624e4c1ab9bd5a3b2ebf4a3a4069889b3e1c6_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3b624e4c1ab9bd5a3b2ebf4a3a4069889b3e1c6_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3b624e4c1ab9bd5a3b2ebf4a3a4069889b3e1c6_2_1380x838.jpeg 2x" data-dominant-color="9B9A9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 653 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>“Background” segment (air, surrounding soft tissues, etc.) is detected and made transparent automatically.</p>
<p>Opacity of segments can be controlled by the slider in the same row (if the slider is towards the left then input seeds are shown; if the slider is moved to the right then resulting segmentation is shown).</p>

---
