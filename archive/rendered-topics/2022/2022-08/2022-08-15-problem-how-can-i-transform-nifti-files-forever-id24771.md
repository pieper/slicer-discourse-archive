---
topic_id: 24771
title: "Problem How Can I Transform Nifti Files Forever"
date: 2022-08-15
url: https://discourse.slicer.org/t/24771
---

# Problem: How can i transform nifti files forever?

**Topic ID**: 24771
**Date**: 2022-08-15
**URL**: https://discourse.slicer.org/t/problem-how-can-i-transform-nifti-files-forever/24771

---

## Post #1 by @nikkos (2022-08-15 19:18 UTC)

<p>Hello dear slicer community,</p>
<p>I have the following problem when transforming Nifti files. Because they are not transfomed correctly. My procedure is the following:</p>
<ol>
<li>I open the nifti file.</li>
<li>I go to the Transform tab , create a new linear transform and then under apply transform move the nifti from Transformable to Transform. Only then I can see what changes when I turn the rotation sliders.</li>
<li>when I have set everything so far, I go back to Data. 4.</li>
<li>then I click on the nifti and make harden Transform.</li>
<li>when I save now, it saves but when I reload it, it looks like the transform was done twice.</li>
<li>I have the same thing when i click on the eye once to hide it and then click on it again to show it.</li>
</ol>
<p>Maybe someone here can help me or knows a similar problem, thanks a lot</p>

---

## Post #2 by @pieper (2022-08-16 14:01 UTC)

<p>Check that you are configured to see the patient view rather than the image-referenced view, which you can set as described in the link below.  Note you can also volume render or make the slice views visible in 3D to see the effect of the transforms.</p>
<aside class="quote quote-modified" data-post="2" data-topic="20092">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-view-orientation-of-oblique-rotated-volumes-aligned-to-volume-or-anatomical-axes/20092/2">Slice view orientation of oblique/rotated volumes - aligned to volume or anatomical axes?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In earlier Slicer versions, slice views were initialized to be aligned with anatomical axes (as defined when the patient was scanned). In recent Slicer Preview Releases we switched to aligning slice views with voxel arrays because this seems to be what most users expect. 
You can switch between the two orientations using <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view controls</a>: 

choose an anatomical plane using the “Slice orientation” selector to align with anatomical axes
click “Rotate to volume plane” button to snap the slice pl…
  </blockquote>
</aside>

<p>As a side note, nii files are slightly lossy because they store the transform with 32bit floats while Slicer internally uses 64bit which is better preserved in formats like nrrd and dicom.  This may sound like a small detail but it can lead to visibly different results or numerical errors when comparing orientations.</p>

---
