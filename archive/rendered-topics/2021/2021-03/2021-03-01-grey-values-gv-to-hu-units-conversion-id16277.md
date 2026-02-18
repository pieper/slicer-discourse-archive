# Grey values (GV) to HU units conversion

**Topic ID**: 16277
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/grey-values-gv-to-hu-units-conversion/16277

---

## Post #1 by @nithin (2021-03-01 02:32 UTC)

<p>Hi,<br>
Can anyone please let me know how to view image intensity in HU units, currently, I am getting values in greyscale only?</p>
<p>Thanks &amp; Regards, <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b27a521e9d0e4521fbeb7e8c1ec41fe735e1a94.jpeg" data-download-href="/uploads/short-url/aIQKsJ6PrhYPSVZHPpJ7cvLNlOs.jpeg?dl=1" title="grey values" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b27a521e9d0e4521fbeb7e8c1ec41fe735e1a94_2_421x500.jpeg" alt="grey values" data-base62-sha1="aIQKsJ6PrhYPSVZHPpJ7cvLNlOs" width="421" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b27a521e9d0e4521fbeb7e8c1ec41fe735e1a94_2_421x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b27a521e9d0e4521fbeb7e8c1ec41fe735e1a94.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b27a521e9d0e4521fbeb7e8c1ec41fe735e1a94.jpeg 2x" data-dominant-color="EFF2F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grey values</span><span class="informations">594×704 50.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-03-01 15:53 UTC)

<p>If you load a calibrated CT, the voxel values are in Hounsfield Units (HU).</p>
<p>If you have loaded an uncalibrated CT and want to do intensity calibration in Slicer then you can use Segment Editor to create segments in regions with known HU and get voxel values using Segment Statistics module. You can then fit a line or curve to compute a function that converts voxel values to Hounsfield units.  You may find some useful information in <a href="https://discourse.slicer.org/t/bone-mineral-density-bmd-measurement-method/11010/4">this discussion</a>.</p>

---
