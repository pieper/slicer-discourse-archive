---
topic_id: 31503
title: "Interpolate Volumetric Mesh From Deformation Vector Field Im"
date: 2023-09-01
url: https://discourse.slicer.org/t/31503
---

# Interpolate volumetric mesh from deformation vector field image volume

**Topic ID**: 31503
**Date**: 2023-09-01
**URL**: https://discourse.slicer.org/t/interpolate-volumetric-mesh-from-deformation-vector-field-image-volume/31503

---

## Post #1 by @suranga (2023-09-01 10:36 UTC)

<p>Hi,</p>
<p>I have created a deformed 3D-CT version and corresponding deformation vector field (DVF) volume of a given nifti image volume (reference image 3D-CT volume) using another tool. I then extracted the liver mesh from the binary mask image volume which is obtained by segmenting the liver region from the reference image volume. Now what I want is that extract the displacement field from the deformation vector field and apply that to the mesh points so that deformed 3D-CT align with the mesh.</p>
<p>I’ve already done this with SimpleITK, but I’m curious if it’s also possible with the 3D slicer. If so, could you kindly explain the procedure to me ? Additionally, I would also like to know how to visualze the deforamtion field on mesh points with a colour map ?</p>
<p>Let’s assume I have loaded volumes below to the 3D slicer:</p>
<ul>
<li>Reference 3D-CT volume (nifti format)</li>
<li>Deformed 3D-CT volume and its corresponding deformation vector field (nifti format)</li>
<li>Reference volumetric mesh in .vtk format (extracted from the reference 3D-CT)</li>
</ul>
<p>Please note that here the deformation field is the final position of the voxel after it has been transformed, i.e. initial position of the voxel + the displacement of the voxel</p>

---

## Post #2 by @pieper (2023-09-01 16:00 UTC)

<p>That should all work fine, but storing deformation fields in nifti is sure to lead to coordinate system issues that you’ll need to sort out.  Just select Transform when loading the vector field and then you can apply it to your mesh.  Have a look at the documentation of the Transforms module.</p>

---

## Post #4 by @pieper (2023-09-04 17:38 UTC)

<p>Thanks for the extra information.</p>
<aside class="quote no-group quote-post-not-found" data-username="suranga" data-post="3" data-topic="31503">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/8491ac/48.png" class="avatar"> suranga:</div>
<blockquote>
<p>vector field in question represents the voxel’s final position after undergoing transformation</p>
</blockquote>
</aside>
<p>In this case I guess you need to subtract the original position (the physical coordinate) from the vector stored at that location.  This sounds easy enough to do as long as you know all the geometry involved.</p>
<p>Note that SimpleITK is directly available in Slicer’s python environment, so you can just use any of that code to implement the change and make a grid transform to apply to the model’s polydata.</p>

---
