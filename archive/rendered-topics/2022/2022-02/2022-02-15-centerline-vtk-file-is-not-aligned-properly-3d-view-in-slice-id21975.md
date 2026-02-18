# CenterLine.vtk file is not aligned properly 3D view in slicer4.13

**Topic ID**: 21975
**Date**: 2022-02-15
**URL**: https://discourse.slicer.org/t/centerline-vtk-file-is-not-aligned-properly-3d-view-in-slicer4-13/21975

---

## Post #1 by @Mahesh_Timmanagoudar (2022-02-15 06:42 UTC)

<p>I have generated VTK file using slicer 4.13 version.</p>
<p>The VTK file looks like below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebb363c9b20568ac5892de5c5f249e3f14d99c0e.png" alt="image" data-base62-sha1="xD6xSrAIc0We6KOYrnIgWlOsEKG" width="285" height="301"></p>
<p>If i try to display above file in 3D view means. It wont align using both LPS and RAS option.<br>
It will be like below in slicer view.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d80163b2767c5f1ce0e044d5f67d464a223b747d.jpeg" data-download-href="/uploads/short-url/uOS6QH4lTPBp2T8AhdMKm7U3K7b.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d80163b2767c5f1ce0e044d5f67d464a223b747d.jpeg" alt="image" data-base62-sha1="uOS6QH4lTPBp2T8AhdMKm7U3K7b" width="690" height="468" data-dominant-color="9EA0C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×483 46.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If i change the vtk file like below. (Removed -  SPACE=LPS) (second line of vtk file).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b93e77b45cc05a0b315531be43410cd9e6bc85f.png" alt="image" data-base62-sha1="d48kEDbXozONxrQQTnI8wHQePBJ" width="302" height="198"></p>
<p>If i try to display the above modified file in slicer using LPS option. Its properly aligning like below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd01d008ed10fa80cc1a70161885784b90ffb818.png" alt="image" data-base62-sha1="vx7p4ZuiGxL5Hvjj3qcMnTq4ty8" width="486" height="442"></p>
<p>May i know where we can modified these vtk files using code so that it will properly align?</p>
<p>Any suggestion how can i fix this problem?</p>

---

## Post #2 by @lassoan (2022-03-04 04:51 UTC)

<p>Is the input segmentation or model under a transform?</p>
<p>If you create the centerline using SlicerVMTK extension’s Extract centerline module does the centerline appear at correct position? If you save the scene and reload the scene (.mrml or .mrb file) then does the centerline appear in the correct position? If you save the centerline and the surface model and then load the files do they appear in the same position?</p>

---
