# Assess Mesh quality in 3D Slicer

**Topic ID**: 26173
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/assess-mesh-quality-in-3d-slicer/26173

---

## Post #1 by @ZSoltani (2022-11-09 21:47 UTC)

<p>Hi all,</p>
<p>Is there anyway to check mesh quality in 3D Slicer, directly?</p>
<p>As an indirect solution, I saved the mesh in .vtk format and then imported it in Gmsh and used Statistic (below), which shows a great quality for the mesh generated using Cleaver method!</p>
<p>Thanks,<br>
Zahra</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/289a29cc4e5fc8074d0c50e7ec059e59b463ebec.png" data-download-href="/uploads/short-url/5Nbojgspelun8f0IIuuvSoT4xxq.png?dl=1" title="Screenshot from 2022-11-09 16-58-22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/289a29cc4e5fc8074d0c50e7ec059e59b463ebec_2_690x390.png" alt="Screenshot from 2022-11-09 16-58-22" data-base62-sha1="5Nbojgspelun8f0IIuuvSoT4xxq" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/289a29cc4e5fc8074d0c50e7ec059e59b463ebec_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/289a29cc4e5fc8074d0c50e7ec059e59b463ebec_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/289a29cc4e5fc8074d0c50e7ec059e59b463ebec_2_1380x780.png 2x" data-dominant-color="D1E7E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-09 16-58-22</span><span class="informations">3768×2135 1.62 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-11-10 13:05 UTC)

<p>We had a project for this years ago with an earlier version of Slicer.  Many of the classes to quantify and visualize mesh quality would probably be easy to port the current version.  Porting the UI would be harder, but something basic could probably be done without much trouble.</p>
<p><a href="https://www.slicer.org/wiki/Modules:IA_FEMesh-Documentation-3.6" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Modules:IA_FEMesh-Documentation-3.6</a></p>

---
