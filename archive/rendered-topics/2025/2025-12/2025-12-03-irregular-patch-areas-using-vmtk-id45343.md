# Irregular patch areas using VMTK

**Topic ID**: 45343
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/irregular-patch-areas-using-vmtk/45343

---

## Post #1 by @svankuijk (2025-12-03 09:05 UTC)

<p>Dear all,</p>
<p>I’m experiencing some issues with surface patching in 3D Slicer (using VMTK) during the post-processing of my carotid steady-state CFD simulations.<br>
The CFD run itself appears correct; the WSS output is properly visualized in the exported Tecplot data file (see Fig. A). For post-processing, I subdivide my carotid geometry into patches by applying 16 circumferential bins with a height of 1 mm. I generate these patches separately for both the common carotid artery (CCA) and the internal carotid artery (ICA).<br>
However, two problems occur:</p>
<ul>
<li>In the ICA, some patches occasionally end up with an extremely small surface area (roughly two orders of magnitude smaller than adjacent patches). These show up as “holes’’ in the resulting .vtp file (Fig. B).</li>
<li>In the CCA, either the last or second-to-last axial row generates patches with a surface area 3–4 times larger than the other patches (Fig. C). When this occurs in the second-to-last row, the final row then exhibits extremely small patch areas again.</li>
</ul>
<p>I was wondering if anyone has experienced this before and if there is a solution for the above described problems. I’ve tried to reduce the patch height but this does not solve the problems.</p>
<p>Furthermore, I would like to know if the WSS values that correspond to the irregular patches are still reliable? Or should they be discarded or corrected?</p>
<p>Any insights or suggestions would be greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d652f8149f5cda9c8d6f82a313234102d1c2c5da.jpeg" data-download-href="/uploads/short-url/uzZWdOqjgSztNi2KJuZVscqsM9I.jpeg?dl=1" title="visualisatie voor slicer forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d652f8149f5cda9c8d6f82a313234102d1c2c5da_2_690x360.jpeg" alt="visualisatie voor slicer forum" data-base62-sha1="uzZWdOqjgSztNi2KJuZVscqsM9I" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d652f8149f5cda9c8d6f82a313234102d1c2c5da_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d652f8149f5cda9c8d6f82a313234102d1c2c5da.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d652f8149f5cda9c8d6f82a313234102d1c2c5da.jpeg 2x" data-dominant-color="A6A8B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">visualisatie voor slicer forum</span><span class="informations">874×456 73.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
