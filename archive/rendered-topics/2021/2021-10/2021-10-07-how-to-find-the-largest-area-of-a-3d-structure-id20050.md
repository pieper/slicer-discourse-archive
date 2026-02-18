# How to find the largest area of a 3d structure

**Topic ID**: 20050
**Date**: 2021-10-07
**URL**: https://discourse.slicer.org/t/how-to-find-the-largest-area-of-a-3d-structure/20050

---

## Post #1 by @hourglassnam (2021-10-07 10:41 UTC)

<p>Hello!<br>
I wanted to know if there is any way to find a cross-section image with the largest length or area of a 3d structure, regardless of the orientation.<br>
I know I can get cross-section areas of segments and find the largest area, however, this means I have to reorientate volume properly in advance.<br>
Instead, I wanted to find the largest area of the 3d structure, then set that as the axial slice afterward.<br>
Is this possible?<br>
I have been looking all over the forum but could not find an answer to this.<br>
Any advice would be grateful.<br>
Thank you always.</p>

---

## Post #2 by @lassoan (2021-10-07 13:29 UTC)

<p>The most common way of extracting the largest cross-section is to use SlicerVMTK extensions “Extract centerline” module to automatically get a centerline of the object and then use “Cross-section analysis” module to get a plot of the maximum inscribed sphere radius across the structure and in that module you can also get the full cross-sectional area and reslice the image/segmentation, jump to minimum/maximum cross-section, etc.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11999dc146f0d4c0329c3392ea22ae619c203a16.jpeg" data-download-href="/uploads/short-url/2vHeLQsHAuChZVnOYXwaTEUf698.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11999dc146f0d4c0329c3392ea22ae619c203a16_2_690x421.jpeg" alt="image" data-base62-sha1="2vHeLQsHAuChZVnOYXwaTEUf698" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11999dc146f0d4c0329c3392ea22ae619c203a16_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11999dc146f0d4c0329c3392ea22ae619c203a16_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11999dc146f0d4c0329c3392ea22ae619c203a16_2_1380x842.jpeg 2x" data-dominant-color="575753"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1172 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is available for recent Slicer Preview Releases.</p>
<p>If you just want to explore a segment across a straight line then you can use the new <a href="https://github.com/jmhuie/Slicer-SegmentGeometry#segment-geometry">SegmentGeometry extension</a>.</p>
<p>If you need to automatically detect size of a structure then you can get oriented bounding box position, orientation, and size using Segment Statistics module. You can also use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi">this script</a> to create ROI nodes from them that you can use in Crop volumes module to resample the segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebca15647d17714a8363864e0990efbed6f283d6.jpeg" data-download-href="/uploads/short-url/xDTaoeMBL7ZRKeWtbI9fvwpqB14.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebca15647d17714a8363864e0990efbed6f283d6_2_499x500.jpeg" alt="image" data-base62-sha1="xDTaoeMBL7ZRKeWtbI9fvwpqB14" width="499" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebca15647d17714a8363864e0990efbed6f283d6_2_499x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebca15647d17714a8363864e0990efbed6f283d6_2_748x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebca15647d17714a8363864e0990efbed6f283d6_2_998x1000.jpeg 2x" data-dominant-color="9694A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1104×1105 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
