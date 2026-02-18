# How to add Sphere Source or other actors to Slicer Scene with UI

**Topic ID**: 26430
**Date**: 2022-11-25
**URL**: https://discourse.slicer.org/t/how-to-add-sphere-source-or-other-actors-to-slicer-scene-with-ui/26430

---

## Post #1 by @alireza (2022-11-25 04:49 UTC)

<p>Is there an easy way to add a sphere source (or polyLine) to slicer scene? I would like to try various rendering behaviours involving polyData and volume actors. First I thought I add a control point and increase its radius, but it seems like the radius has a maximum.</p>
<p>Is there any extension that let me create various actors from vtk and add them to the scene? or if there is written scripts somewhere I think that works as well.</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/653fc3d3355ade18b2a76b7f16dace6bf769c64d.jpeg" data-download-href="/uploads/short-url/erGQ60tc680ICG1CQQzHL3SnOcl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653fc3d3355ade18b2a76b7f16dace6bf769c64d_2_683x500.jpeg" alt="image" data-base62-sha1="erGQ60tc680ICG1CQQzHL3SnOcl" width="683" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653fc3d3355ade18b2a76b7f16dace6bf769c64d_2_683x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653fc3d3355ade18b2a76b7f16dace6bf769c64d_2_1024x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653fc3d3355ade18b2a76b7f16dace6bf769c64d_2_1366x1000.jpeg 2x" data-dominant-color="B2B1B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1529×1118 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-11-25 06:20 UTC)

<p>The easiest way to display a polydata is by adding a model node. There are many examples in the script repository, such as <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node">this</a>.</p>
<p>If you want to display many spheres of the same size or interactively move the sphere then markups could be used. Maybe slider in the GUI has a limited range, but programmatically you can set and size.</p>

---
