---
topic_id: 15435
title: "Length Of Centerline Curve As Label Name In 3D View"
date: 2021-01-10
url: https://discourse.slicer.org/t/15435
---

# Length of centerline curve as label name in 3D view?

**Topic ID**: 15435
**Date**: 2021-01-10
**URL**: https://discourse.slicer.org/t/length-of-centerline-curve-as-label-name-in-3d-view/15435

---

## Post #1 by @rbumm (2021-01-10 14:15 UTC)

<p>Hi,</p>
<p>Is it possible to display a label (with name and length) of a centerline curve in 3D view?<br>
This would be very helpful for our vascular surgeons …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ea0411fd6d01329263504e63033706233a55dc7.jpeg" data-download-href="/uploads/short-url/dv6dZunb0RB5srt8aknFXkxQIon.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ea0411fd6d01329263504e63033706233a55dc7_2_690x307.jpeg" alt="image" data-base62-sha1="dv6dZunb0RB5srt8aknFXkxQIon" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ea0411fd6d01329263504e63033706233a55dc7_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ea0411fd6d01329263504e63033706233a55dc7_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ea0411fd6d01329263504e63033706233a55dc7_2_1380x614.jpeg 2x" data-dominant-color="9B9BA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×857 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-10 19:36 UTC)

<p>You can assign labels to any curve control point and display that. By default control point label display is disabled for curves because there would be many labels, so you need to enable that and probably set all other control point labels to empty.</p>
<p>It would be simpler if node name or measurements could be displayed as a label for curves (as for angles and lines). Please add a feature request for it at <a href="https://issues.slicer.org">https://issues.slicer.org</a>.</p>

---
