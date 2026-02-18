# Solid body vs. sheet body

**Topic ID**: 34982
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/solid-body-vs-sheet-body/34982

---

## Post #1 by @Marthe (2024-03-19 17:07 UTC)

<p>When I export an STL file of the ribcage I segmented from 3D Slicer CTACardio CT scan, I obtain a solid body in CAD software for further processing of the body. However, when I export an STL file of this ribcage after performing an ROI cut, I obtain a sheet body in CAD software. Is there a reason why no solid body is obtained after performing an ROI cut? Is there a solution for this?</p>
<p>Thank you in advance!</p>
<p>Kind regards</p>
<p>a motivated student and admirer of 3D slicer</p>

---

## Post #2 by @mau_igna_06 (2024-03-19 17:33 UTC)

<p>Normal meshes are 3D surfaces, like the one you obtain with Dynamic Modeler ROI cut tool. If you want a tetrahedral mesh you’ll need something like <a href="https://github.com/lassoan/SlicerSegmentMesher" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a></p>
<p>HIH</p>

---
