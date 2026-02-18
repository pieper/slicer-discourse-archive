# Smoothing only in one direction

**Topic ID**: 2327
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/smoothing-only-in-one-direction/2327

---

## Post #1 by @alessandronavacchia (2018-03-15 14:34 UTC)

<p>Hi all,</p>
<p>I am trying to smooth a segmented volume with either a Median or Gaussian method. I segmented mostly in slices perpendicular to one axis because of the better resolution. When I smooth with large Kernel sizes or Standard deviations the geometry ends up changing too much, and when I smooth with smaller values I keep seeing the “slice effect” in the 3d volume (see figure below):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8412f6dc7098d42ac29ae74ebcb5b1655ed48a47.png" data-download-href="/uploads/short-url/iQnEJe7pSUHxNFQ4SyrIBnvdcG3.png?dl=1" title="smoothing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8412f6dc7098d42ac29ae74ebcb5b1655ed48a47_2_532x500.png" alt="smoothing" data-base62-sha1="iQnEJe7pSUHxNFQ4SyrIBnvdcG3" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8412f6dc7098d42ac29ae74ebcb5b1655ed48a47_2_532x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8412f6dc7098d42ac29ae74ebcb5b1655ed48a47.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8412f6dc7098d42ac29ae74ebcb5b1655ed48a47.png 2x" data-dominant-color="9796B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">smoothing</span><span class="informations">636×597 87.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I was wondering if there is any way to smooth with larger Kernel size of Standard deviation only in one direction (perpendicular to the sagittal plane in this case)? Have you ever encountered the same issue? Do you have alternative solutions?</p>
<p>Thanks!</p>
<p>Alessandro</p>

---

## Post #2 by @lassoan (2018-03-15 14:36 UTC)

<p>This shows that your input volume had highly anisotropic spacing. You should not attempt to smooth it, but instead use Crop volume module on the input volume (before segmentation) to resample using isotropic spacing option.</p>

---

## Post #3 by @alessandronavacchia (2018-03-16 14:14 UTC)

<p>Thanks Andras, that fixed it!</p>
<p>Alessandro</p>

---
