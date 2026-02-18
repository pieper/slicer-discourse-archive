# Export of voxel-true surface mesh

**Topic ID**: 8212
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/export-of-voxel-true-surface-mesh/8212

---

## Post #1 by @fabian (2019-08-28 17:39 UTC)

<p>Hi everyone! I’m new to Slicer and I apologise if this question is trivial or has been discussed elsewhere.</p>
<p>I have a segmented volume and I’d like to export the surface of this volume as an (ideally triangular) mesh (e.g. WEM). The constraint here is that I’d like each border voxel of the segmented volume to be represented as a vertex in the resulting mesh. No smoothing, no optimisation. Just the border voxel coordinates and a mesh between them that tells me which ones are adjacent (and by the by turns it into a surface model).</p>
<p>Is this reasonably doable with Slicer and if so, how?<br>
Thanks a lot!</p>

---

## Post #2 by @lassoan (2019-08-29 00:11 UTC)

<p>You can disable surface smoothing (decimatin is disabled by default) in Segment Editor, Show 3D button’s submenu.</p>
<p>If the surface mesh must follow the binary labelmap so closely then there might be cases when only non-manifold mesh can be created, causing serious issues with in further processing steps. What would you like to do with the mesh?</p>

---

## Post #3 by @fabian (2019-08-29 06:26 UTC)

<p>Thanks a lot lassoan! Appreciate the fast reply.</p>
<p>I want to use the points to simulate the acqisition of points on a physical organ surface. So I’m mainly interested in the border voxel coordinates as a point cloud (simulating a cloud of physically measured points).</p>
<p>But I’d also like to run a patch growing method on this surface, so knowing the adjacent points for each point would be super helpful. That’s where the mesh idea came from.</p>
<p>Will the serious issues you mention affect this? Or what sort of issues are you talking about? Thanks again for any advice!</p>

---

## Post #4 by @Chris_Rorden (2019-08-29 12:00 UTC)

<p>Be aware that medical images suffer from the partial volume problem, e.g. a voxel at the surface of the brain may contain a mixture of gray matter and CSF. The surface boundary voxels are necessarily far more likely to be composed of mixtures of tissues than voxels deep inside the object (e.g. a voxel in deep white matter might be 100% white matter, but voxels at the gray-white boundary will be mixtures). Methods like <a href="http://paulbourke.net/geometry/polygonise/" rel="nofollow noopener">marching cubes</a> leverage this by interpolating vertex positions. In general, this will give a more accurate shape than meshes where vertex positions are constrained to the voxel positions.</p>

---

## Post #5 by @fabian (2019-08-29 13:44 UTC)

<p>Thanks Chris! That’s a very good point that I hadn’t thought of - I’ll take it into consideration! What’s important to me is that the resolution is not changed and that no optimisation via vertex elimination or adjustment occurs. Thanks a lot for the feedback!</p>

---

## Post #6 by @lassoan (2019-08-29 14:11 UTC)

<p>Surfaces reconstructed by marching cubes (or flying edges) are very similar to those acquired by surface scanners. We used this successfully in several projects on skin, bone, and cartilage surfaces (with submillimeter residual error after registration).</p>

---

## Post #7 by @fabian (2019-09-02 14:17 UTC)

<p>Thanks lassoan! I’ll give that a try! Cheers!</p>

---
