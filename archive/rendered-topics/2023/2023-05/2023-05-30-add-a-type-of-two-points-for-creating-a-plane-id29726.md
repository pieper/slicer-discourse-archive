# Add a type of two points for creating a plane

**Topic ID**: 29726
**Date**: 2023-05-30
**URL**: https://discourse.slicer.org/t/add-a-type-of-two-points-for-creating-a-plane/29726

---

## Post #1 by @slicer365 (2023-05-30 14:21 UTC)

<p>It is useful to generate a midplane perpendicular to the line connecting two points. Especially for neurosurgeons.</p>
<p>Users only need to place two points to get the mirror plane of these two points</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a50e736863161a57b59480dadf1cff58f038b73f.jpeg" data-download-href="/uploads/short-url/ny9K5pWRsze5rfcMdJFicEoU3H9.jpeg?dl=1" title="1685456237720" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a50e736863161a57b59480dadf1cff58f038b73f_2_517x242.jpeg" alt="1685456237720" data-base62-sha1="ny9K5pWRsze5rfcMdJFicEoU3H9" width="517" height="242" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a50e736863161a57b59480dadf1cff58f038b73f_2_517x242.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a50e736863161a57b59480dadf1cff58f038b73f_2_775x363.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a50e736863161a57b59480dadf1cff58f038b73f_2_1034x484.jpeg 2x" data-dominant-color="888889"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1685456237720</span><span class="informations">1850×867 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-05-30 19:59 UTC)

<p>Instead of changing slice orientation, it is more common in neuroimaging to transform the image into a standard coordinate system that is aligned with axes of the brain.</p>
<p>You can do this in Slicer for example by using ACPC transform module. It aligns the brain in a standard orientation based on the AC-PC line and points in the midsagittal plane.</p>

---
