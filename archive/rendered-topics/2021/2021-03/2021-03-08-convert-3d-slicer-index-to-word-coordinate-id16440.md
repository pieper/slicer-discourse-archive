# Convert 3D Slicer index to word coordinate

**Topic ID**: 16440
**Date**: 2021-03-08
**URL**: https://discourse.slicer.org/t/convert-3d-slicer-index-to-word-coordinate/16440

---

## Post #1 by @maz_khansari (2021-03-08 23:19 UTC)

<p>Hi,<br>
I am trying to convert 3D Slicer index to world coordinate but not sure if I am doing it correctly.<br>
Here is the explanation from Slicer tutorial which is vague.</p>
<p>To extract the “voxel to world” transformation matrix from the NIFTI file’s header (entry: qto_xyz:1-4 ) in Matlab:</p>
<p>d=inv(M) *[ R A S 1 ]’</p>
<p>where M is the matrix and R A S are coordinates in Slicer, then d gives a vector of voxel coordinates.</p>
<p>(Solution courtesy of András Jakab, University of Debrecen</p>
<p>Particularly I am not sure where to find qto_xyz in the header. When I load nifti file in Matlab using load_untouch_nii or built-in nifti_info(‘file.nii’), there is no qto_xyz. Also it is not clear what is M matrix.<br>
Can you please guide me through this process?</p>
<p>I can extract affine matrix then multiply it with the indexes to get world coordinates. However, the issue is that the indixes that I get from Slicer is different than the one I get from BrainSuite for the exact same location.<br>
My goal is to find corresponding points (in physical unit or world coordinates) to do point-based registration.</p>
<p>Your help is very much appreciated!</p>
<p>Operating system: Windows<br>
Slicer version: 4<br>
Expected behavior: Good<br>
Actual behavior: Good</p>

---

## Post #2 by @pieper (2021-03-08 23:30 UTC)

<p>The topic of coordinate conventions in nifti and matlab are a bit beyond the scope of Slicer, since different software and script sometimes contradict each other.  For Slicer the conventions are <a href="https://www.slicer.org/wiki/Coordinate_systems">described here</a> and the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates">script repository</a> has examples to go back and forth.</p>
<p>You should be able to use Slicer with the DataProbe and Volumes module to see all the coordinate systems and matrices and then save the file in nifti, open in matlab to learn the correspondences.</p>
<aside class="quote no-group" data-username="maz_khansari" data-post="1" data-topic="16440">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maz_khansari/48/10234_2.png" class="avatar"> maz_khansari:</div>
<blockquote>
<p>Here is the explanation from Slicer tutorial which is vague</p>
</blockquote>
</aside>
<p>Can you include the link to the tutorial?  Perhaps when this gets sorted out you can suggest clarifications.</p>

---

## Post #3 by @maz_khansari (2021-03-09 00:26 UTC)

<p>Thank you for your response and pointing me to the script repository with examples.<br>
Would be happy to suggest clarification once this is sorted out.</p>
<p>Here is the link to the tutorial (bottom of the page, Relations to other software / conventions:<br>
<a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #4 by @lassoan (2021-03-09 00:29 UTC)

<p>Note that voxel coordinates are not portable between applications, because each application is free to choose how to map IJK indices to physical positions (origin of an image can be top-left, bottom left, center voxel; first index may be fastest or slowest changing index; etc.).</p>
<p>Therefore, if you want to share point positions between applications, always use physical coordinates (which is most commonly LPS in medical imaging).</p>

---
