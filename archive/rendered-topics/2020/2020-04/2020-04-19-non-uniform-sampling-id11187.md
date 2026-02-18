# Non-uniform sampling

**Topic ID**: 11187
**Date**: 2020-04-19
**URL**: https://discourse.slicer.org/t/non-uniform-sampling/11187

---

## Post #1 by @loubna (2020-04-19 17:39 UTC)

<p>Due to the quality of scanning devices, it is possible that imaging resolution in the xyplane is higher than slicing capabilities. For example, regardless of units or precision used, imaging resolution is only accurate to the pixel, whereas slices could be two, three, or more pixels apart from each other. Such acquisitions produce non-uniform resolution data.</p>
<p>That is why, the data must be accommodated by an appropriate transformation of each input. One of the proposed solutions is to apply a scaling  transformation on anisotropic points.</p>
<p>my question how can I deal with this problem in 3D slicer using vtk filters</p>
<p>thank’s in advance</p>

---
