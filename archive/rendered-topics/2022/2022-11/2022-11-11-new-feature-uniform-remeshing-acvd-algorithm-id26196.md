# New feature: Uniform remeshing (ACVD algorithm)

**Topic ID**: 26196
**Date**: 2022-11-11
**URL**: https://discourse.slicer.org/t/new-feature-uniform-remeshing-acvd-algorithm/26196

---

## Post #1 by @lassoan (2022-11-11 14:15 UTC)

<p>Models (surface meshes) exported from image segmentation often have very high point counts, which can make visualization and further editing in external software difficult.</p>
<p>Surface Toolbox module’s Decimate feature has been offering mesh simplification using quadric decimation and decimate pro algorithms, but these algorithms generate highly varying triangle sizes and shapes (depending on the curvature of the region), which is not ideal for some applications.</p>
<p>We added a new <strong>Uniform remesh</strong> option to <em>Surface toolbox</em> module in the latest Slicer Preview Release (Slicer-5.1.0-2022-11-10), which uses the ACVD algorithm (implemented in <a href="https://github.com/pyvista/pyacvd">pyacvd</a> package), which results in a smooth mesh with evenly sized, regular shape triangles.</p>
<p>Comparison of results of the new universal remeshing (ACVD) algorithm with the already existing quadric decimation algorithm on a mesh exported from segmentation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520a70a9c4f82a2e7af668955cd9e4b92e612ace.jpeg" data-download-href="/uploads/short-url/bHLwgi986jQroEK8yTE57k7vIbY.jpeg?dl=1" title="comparison-final"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520a70a9c4f82a2e7af668955cd9e4b92e612ace_2_690x345.jpeg" alt="comparison-final" data-base62-sha1="bHLwgi986jQroEK8yTE57k7vIbY" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520a70a9c4f82a2e7af668955cd9e4b92e612ace_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520a70a9c4f82a2e7af668955cd9e4b92e612ace_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520a70a9c4f82a2e7af668955cd9e4b92e612ace_2_1380x690.jpeg 2x" data-dominant-color="C4C4B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">comparison-final</span><span class="informations">1920×961 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
