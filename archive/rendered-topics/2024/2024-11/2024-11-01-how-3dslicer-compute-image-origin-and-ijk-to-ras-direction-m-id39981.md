---
topic_id: 39981
title: "How 3Dslicer Compute Image Origin And Ijk To Ras Direction M"
date: 2024-11-01
url: https://discourse.slicer.org/t/39981
---

# How 3DSlicer compute image origin and IJK to RAS direction matrix.

**Topic ID**: 39981
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/how-3dslicer-compute-image-origin-and-ijk-to-ras-direction-matrix/39981

---

## Post #1 by @fabiogatelli (2024-11-01 11:16 UTC)

<p>Hello everybody, this is my first topic and I have some trouble reasoning with 3Dslicer DICOM parameters extraction. I start from the beginnig. Due to research activity, my aim is to write down a python code (without slicer package) to convert a MRI DICOM series to a Nifti file and apply on it a segmentation mask through the affine matrix. I obtained my conversion and compared it with the one produced by 3DSlicer on the same DICOM series through the export to file functionality. I obtained pretty similar results, but the orientation is different. I try to explain myself better. The IJK to RAS direction matrices have both all zeros and ones on the diagonal for both the results but with different signs for the first two dimensions, while the origin has the same modules but different signs (on the first two dimensions). I don’t understand how 3DSlicer computes my same direction matrix and origin but with different signs. Moreover the segmentation is overlapping perfectly on 3DSlicer output, but not on mine. I hope you can understand what I mean. Thank a lot!</p>

---

## Post #2 by @lassoan (2024-11-01 11:33 UTC)

<aside class="quote no-group" data-username="fabiogatelli" data-post="1" data-topic="39981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/4491bb/48.png" class="avatar"> fabiogatelli:</div>
<blockquote>
<p>my aim is to write down a python code (without slicer package) to convert a MRI DICOM series to a Nifti file</p>
</blockquote>
</aside>
<p>I would not recommend to do this, because while it is extremely complex to implement this correctly for a wide range of DICOM objects, it is considered to be a solved problem. You can use Slicer for this using with or without GUI (using Python scripting), but if you don’t want to do that then another very robust and comprehensive 3D image reconstruction software is <code>dcm2niix</code>. There are many other software that works for well for some of the most common inaging protocols (such as ITK and VTK DICOM readers), but they cannot produce correct results for tilted-gantry acquisitions, non-uniform slice spacing, 4D images, etc.</p>

---

## Post #3 by @fabiogatelli (2024-11-07 08:34 UTC)

<p>Thank you for the answer. I’ll try another way.</p>

---
