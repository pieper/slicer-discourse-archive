# How to include the aortic wall when i do auto segmentation using local threshold?

**Topic ID**: 14890
**Date**: 2020-12-05
**URL**: https://discourse.slicer.org/t/how-to-include-the-aortic-wall-when-i-do-auto-segmentation-using-local-threshold/14890

---

## Post #1 by @chendong9416 (2020-12-05 05:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cfbdbf71694438bfee196ebfcff005e6e152f27.jpeg" data-download-href="/uploads/short-url/aZ1Tpkb6i4VTyLb7WFd4yf5sgwn.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cfbdbf71694438bfee196ebfcff005e6e152f27_2_650x500.jpeg" alt="Screenshot" data-base62-sha1="aZ1Tpkb6i4VTyLb7WFd4yf5sgwn" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cfbdbf71694438bfee196ebfcff005e6e152f27_2_650x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cfbdbf71694438bfee196ebfcff005e6e152f27_2_975x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cfbdbf71694438bfee196ebfcff005e6e152f27.jpeg 2x" data-dominant-color="3E3F3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1147×882 64.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>this is a really importment step for centerline extration of aortic intramural hematoma!</p>

---

## Post #2 by @lassoan (2020-12-05 05:50 UTC)

<p>Since it seems that there are large sections where the aortic wall is not distinguishable from surrounding tissues(they have the same gray value), expert knowledge (manual segmentation) is needed to draw the contour where it is actually not visible.</p>
<p>To reduce manual segmentation time by a factor of 5-10x, you can use segment one out of every 5-10 slices and interpolate between them using “Fill between slices” effect.</p>

---

## Post #3 by @chendong9416 (2020-12-05 05:53 UTC)

<p>thanks, this hopes a lot.</p>

---
