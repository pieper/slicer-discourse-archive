# Extract Centerlines cannot work with cyclical vessels?

**Topic ID**: 24758
**Date**: 2022-08-15
**URL**: https://discourse.slicer.org/t/extract-centerlines-cannot-work-with-cyclical-vessels/24758

---

## Post #1 by @Doodads (2022-08-15 05:24 UTC)

<p>Hi, I used the Extract Centerlines tool on a Circle of Willis surface. The network is connected without an issue but the centerlines have a single vessel that it did not pass through (see image below). How do I adjust the Extract Centerlines tool to have the centerlines extracted properly?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9000d8f34161510cd47c1249fac0e7c823f926f6.png" data-download-href="/uploads/short-url/kxUzqy8B8yb3GYGsLMG62MHELpY.png?dl=1" title="Screenshot 2022-08-15 at 12.28.38 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9000d8f34161510cd47c1249fac0e7c823f926f6_2_653x500.png" alt="Screenshot 2022-08-15 at 12.28.38 PM" data-base62-sha1="kxUzqy8B8yb3GYGsLMG62MHELpY" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9000d8f34161510cd47c1249fac0e7c823f926f6_2_653x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9000d8f34161510cd47c1249fac0e7c823f926f6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9000d8f34161510cd47c1249fac0e7c823f926f6.png 2x" data-dominant-color="989AA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-08-15 at 12.28.38 PM</span><span class="informations">826×632 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-08-15 19:37 UTC)

<p>That’s correct. The “centerline extraction” method in “Extract Centerline” module computes shortest paths between source and destination points, therefore it always extracts tree(s). To process circular topology, you can add two points somewhere to break the circle or use the “network extraction” algorithm of the “Extract Centerline” module. See more information in the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/ExtractCenterline.md">VMTK Slicer extension’s documentation</a>.</p>

---
