# Interactively change the nodes of mesh

**Topic ID**: 18361
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/interactively-change-the-nodes-of-mesh/18361

---

## Post #1 by @Aep93 (2021-06-28 02:10 UTC)

<p>Hello all,<br>
Consider a mesh that is created with the segmentmesher module. For some reason, I want to change the locations of a few nodes in the created volumetric mesh to make my mesh more smooth. How can I do it? Is it possible to do it interactively?<br>
So my question is this: are there any ways to change the location of specific nodes of a model (that is created with segmentmesher) in the slicer?</p>

---

## Post #2 by @lassoan (2021-06-28 15:25 UTC)

<p>You would need to add a short Python code snippet to be able to do this. First you need to find the point that you want to modify (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-scalar-values-at-surface-of-a-model">as shown in this example</a>) and then make the point move to the position where you move a control point of markups fiducial node (similarly to how a VTK filter input is updated from a markups node in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">this example</a>).</p>

---

## Post #3 by @Aep93 (2021-06-28 15:39 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I think this process takes some time for all nodes. Instead, is it possible to smooth a model that is created with segmentmesher?<br>
I have tried playing with cleaver elements for this; however, it did not help as increasing the quality of mesh will make the mesh finer and I do not want it.<br>
Therefore I think it is very helpful if I can find a way to smooth my mesh in the slicer.</p>

---

## Post #4 by @lassoan (2021-06-28 15:54 UTC)

<p>There are many ways to smooth the input segmentation (for example, using Smoothing effect). You can also make segment mesher output smoother by adjusting meshing parameters. These should be sufficient to make the mesh smooth enough, but if you want further adjustments then you can try if there are smoothing filters in VTK that can be applied to unstructured grids (volumetric meshes).</p>

---

## Post #5 by @Aep93 (2021-06-28 16:04 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. When I use the smoothing module and apply it to a model that is created with the segmentmesher, the output model is empty. Is it because the effects in the smoothing module cannot be applied to the unstructured grids?</p>

---

## Post #6 by @lassoan (2021-06-28 21:35 UTC)

<p>Which smoothing module do you mean?</p>

---

## Post #7 by @Aep93 (2021-06-29 02:54 UTC)

<p>I attach a screenshot of the module that I use here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a30d8314adbc7567ba45fc801a4d3f41e615be7.png" data-download-href="/uploads/short-url/f9pgafrYv1EXRlcjv2zC9Hvvpnp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a30d8314adbc7567ba45fc801a4d3f41e615be7_2_524x500.png" alt="image" data-base62-sha1="f9pgafrYv1EXRlcjv2zC9Hvvpnp" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a30d8314adbc7567ba45fc801a4d3f41e615be7_2_524x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a30d8314adbc7567ba45fc801a4d3f41e615be7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a30d8314adbc7567ba45fc801a4d3f41e615be7.png 2x" data-dominant-color="E9EAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">641×611 58.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks</p>

---

## Post #8 by @lassoan (2021-06-29 04:36 UTC)

<p>This module only supports polygonal mesh (vtkPolyData), not volumetric mesh (vtkUnstructuredGrid). If you don’t get recommendations here about what methods you can use for smoothing unstructured grids then I would recommend to ask it on the <a href="https://discourse.vtk.org/">VTK forum</a> (include the link to your post here and also come back and report if you hear any useful advice there).</p>

---

## Post #9 by @Aep93 (2021-06-29 14:33 UTC)

<p>OK, <a class="mention" href="/u/lassoan">@lassoan</a>. I will post it there. Thanks.</p>

---
