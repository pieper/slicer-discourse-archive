# Changes to VTK polydata between 4.10 and 4.11

**Topic ID**: 17348
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/changes-to-vtk-polydata-between-4-10-and-4-11/17348

---

## Post #1 by @codey (2021-04-27 12:25 UTC)

<p>I have noticed that VTK meshes imported in 4.10 and 4.11 differ in their spatial location. Rotation by 180 corrects for this. I presume this is down to a different interpretation of the VTK coordinate system. between the slicer versions. Does anyone know why these are different?</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-04-27 13:30 UTC)

<p>This is probably due to the change in 4.11 in the way coordinate system of model files are handled in 3D Slicer</p>
<aside class="quote quote-modified" data-post="1" data-topic="10446">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446">Model files are now saved in LPS coordinate system</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    While Slicer uses RAS coordinate system internally, images, transforms, and markups files are stored in LPS coordinate system, because DICOM and all medical image computing software (maybe except a few very old ones) uses LPS coordinate system in files. 
However, Slicer has been still using its internal RAS coordinate system in mesh files (STL, VTK, VTP, OBJ, PLY), which <a href="https://issues.slicer.org/view.php?id=4445" rel="noopener nofollow ugc">caused issues when interfacing with third-party software</a>. 
Starting from tomorrow (Slicer-4.11.0-2020-02-26, revision 28794), …
  </blockquote>
</aside>


---
