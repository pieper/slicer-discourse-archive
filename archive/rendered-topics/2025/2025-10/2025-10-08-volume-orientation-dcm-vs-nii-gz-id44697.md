---
topic_id: 44697
title: "Volume Orientation Dcm Vs Nii Gz"
date: 2025-10-08
url: https://discourse.slicer.org/t/44697
---

# Volume orientation (dcm vs nii.gz)

**Topic ID**: 44697
**Date**: 2025-10-08
**URL**: https://discourse.slicer.org/t/volume-orientation-dcm-vs-nii-gz/44697

---

## Post #1 by @bserrano (2025-10-08 08:58 UTC)

<p>Hi all,</p>
<p>I am working with cardiac CT data in two formats: <strong>DICOM</strong> and <strong>NIfTI (.nii.gz)</strong>.</p>
<p>I am trying to automate some processes related to the placement of fiducials, but I’ve noticed an unexpected behavior:</p>
<ul>
<li>When I load a <strong>DICOM volume</strong>, the largest <strong>K index (IJK axial coordinate)</strong> corresponds to the superior end of the body (closest to the neck).</li>
<li>When I load a <strong>NIfTI (.nii.gz) volume</strong>, the superior slice has index <strong>0</strong> instead.</li>
</ul>
<p>My question is: <strong>How can I reliably determine the slice order in the K (axial) dimension, regardless of the input format?</strong></p>
<p>Thanks in advance!</p>

---

## Post #2 by @cpinter (2025-10-08 09:09 UTC)

<p>They are in a different orientation (RAS vs LPS). I suggest reading this page:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" target="_blank" rel="noopener">Coordinate systems — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There is a section about nifti on the bottom.</p>
<p>Let us know if you have further questions.</p>

---

## Post #3 by @lassoan (2025-10-09 02:24 UTC)

<blockquote>
<p>How can I reliably determine the slice order in the K (axial) dimension, regardless of the input format?</p>
</blockquote>
<p>You cannot do this independently from the input format, because for DICOM images this may be impossible. Each slice in a DICOM series has arbitrary orientation: they don’t have to be parallel, they can intersect each other, you can even have many slices at the same spatial position.</p>
<p>Many software packages can reconstruct regularly spaced 3D Cartesian volumes from the arbitrarily set of DICOM image slices. This operation may be a simple ordering of the slices, or it can be a complex non-linear reconstruction if the slices are irregularly spaced, tilted, or not parallel. The result of the 3D reconstruction is a voxel array and a homogeneous transformation matrix that maps between IJK indices of the array and the anatomical coordinate system. All you need to interpret the image data is this transformation matrix.</p>

---
