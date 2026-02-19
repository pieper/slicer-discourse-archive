---
topic_id: 32792
title: "How Do Various Slicers Encode The Origin For Their Coordinat"
date: 2023-11-13
url: https://discourse.slicer.org/t/32792
---

# How do various slicers encode the origin for their coordinate system?

**Topic ID**: 32792
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/how-do-various-slicers-encode-the-origin-for-their-coordinate-system/32792

---

## Post #1 by @Ahstark (2023-11-13 19:54 UTC)

<p>I am using ITK-Snap’s 3D segmentation and exporting as surface mesh. I was wondering how I could “Conserve” the approximate coordinates for a specific pixel on the original object. That way I can choose a pixel with an (X,Y,Z) coordinate and then know the respective coordinates on the surface mesh  after being imported into MATLAB</p>

---

## Post #2 by @lassoan (2023-11-13 20:53 UTC)

<p>All proper medical image computing software applications, including ITK-Snap, saves images and meshes accurately in physical coordinate system.</p>
<p>You need to be careful with mesh files, because coordinate system axis directions are not standardized. The directions are almost always LPS, but there are a few exceptions. For example, ITK-Snap is an exception, it appears to save meshes in RAS coordinate system. Therefore when you load the mesh into Slicer then you need to enable “Show options” and choose “Coordinate system: RAS”. When you load the mesh file into your software then you need to convert the mesh to the physical coordinate system of your choice (which should be LPS).</p>
<p>You can convert between voxel (IJK) and physical (LPS) coordinate systems by multiplying homogeneous coordinates using LPSToIJK 4x4 matrix. SlicerMatlabBridge’s NRRD reader computes the matrix for you, see <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">here</a>.</p>
<p>Just a not on Matlab: We developed the Slicer Matlab Bridge for Slicer more than 10 years ago. It made sense then. Nowadays, I would recommend everyone who works in medical image computing to switch to Python. Python has larger community, more libraries, more transparency, and less limitations. Matlab is also generally unaffordable outside academia, so if you develop something at a university in Matlab, it is unlikely that you can use it later when you work for a company.</p>

---

## Post #3 by @Ahstark (2023-11-13 23:40 UTC)

<p>Wow! Thank you for the amazing reply. I am still a little confused though. Let’s say I start with an image series in the LPS coordinate and then I slice it to a smaller mesh. Even if you converted the coordinates of the original image to the coordinates of the mesh, they are still distorted because the coordinate grid changed (its now smaller since the mesh is just a small part of the original image). I am wondering how I can go from a known coordinate in ITK snap, say (0,0,0) to a coordinate on the mesh. The origin of the original image is no longer contained in the mesh so (0,0,0) for ITK Snap will not be (0,0,0) for the mesh</p>
<p>Thanks again</p>

---

## Post #4 by @lassoan (2023-11-14 03:37 UTC)

<aside class="quote no-group" data-username="Ahstark" data-post="3" data-topic="32792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ahstark/48/68295_2.png" class="avatar"> Ahstark:</div>
<blockquote>
<p>I slice it to a smaller mesh</p>
</blockquote>
</aside>
<p>Images and meshes still remain in the correct physical position, regardless of how you resample or reslice. There is no distortion of any kind.</p>
<p>You convert from IJK coordinates to LPS by multiplying the <code>[I, J, K, 1]</code> vector by IJKToLPS matrix from the left. You can get point ID from physical LPS coordinates by using a locator (that can tell point ID closest to a point position).</p>

---
