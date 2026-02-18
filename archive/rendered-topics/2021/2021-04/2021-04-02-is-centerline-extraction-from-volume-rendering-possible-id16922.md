# Is centerline extraction from volume rendering possible?

**Topic ID**: 16922
**Date**: 2021-04-02
**URL**: https://discourse.slicer.org/t/is-centerline-extraction-from-volume-rendering-possible/16922

---

## Post #1 by @chendong9416 (2021-04-02 08:45 UTC)

<p>since segmentation will be difficult sometomes from CTA with poor quality, but they can still be well displayed in volume  rendering, thus I wonder if centerline extraction directly from volume rendering possible?</p>

---

## Post #2 by @lassoan (2021-04-02 13:06 UTC)

<p>For centerline extraction it should not be a problem that the segmented surface is noisy, but you can also apply some smoothing.</p>
<p>Volume rendering is just a display method. It can help you if you want to manually place curve points in the 3D view (and then you can move it to the center of the vessel in slice views).</p>

---
