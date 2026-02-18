# Saved surface model is not aligned with volume when viewed in external software

**Topic ID**: 821
**Date**: 2017-08-04
**URL**: https://discourse.slicer.org/t/saved-surface-model-is-not-aligned-with-volume-when-viewed-in-external-software/821

---

## Post #1 by @fmaule (2017-08-04 13:09 UTC)

<p>Operating system: Windows 7 enterprise 64bit<br>
Slicer version:4.6.2<br>
Expected behavior:<br>
I expect to visualize in 3D space the files  .stl or .ply surfaces correctly alligned with the nifti anatomical image (on which I have segmented them with Amira).<br>
Actual behavior:<br>
I viausliaze the multiple .stl and also .ply surfaces correctly aligned among them  but when I underlie the nifti image it seems that the latter has a different origin. The 3D reconstruction is completely far away from anatomical scan.  Segmentatiom was performed with Amira on the nifti file used also in the visualization with Slicer. No dicom available.<br>
I am not allowed to segment in Slicer. But I need it for the visualization outside the company.</p>
<p>thanks for your help!<br>
f.m</p>

---

## Post #2 by @lassoan (2017-08-04 13:11 UTC)

<p>Most common issue is LPS/RAS coordinate system mismatch. See this post about how this inconsistency can be fixed:</p>
<aside class="quote quote-modified" data-post="7" data-topic="717">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dicom-and-vtk-file-orientation-issue/717/7">DICOM and VTK file orientation Issue</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Most common issue is LPS/RAS coordinate system mismatch. So, may try to convert your data from LPS to RAS coordinate system by transforming it using Transforms module by a matrix that has [-1,-1,1,1] in the diagonal: 
[image]
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2021-04-18 19:48 UTC)

<p>9 posts were split to a new topic: <a href="/t/align-3d-ultrasound-image-and-surface-model/17158">Align 3D ultrasound image and surface model</a></p>

---
