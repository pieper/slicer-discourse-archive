# Orientation issue loading vtk mesh

**Topic ID**: 10641
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/orientation-issue-loading-vtk-mesh/10641

---

## Post #1 by @alixchcl (2020-03-11 12:49 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.11.0 (-2020-03-03)<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi, I am trying Slicer new version, and I encounter orientation problems while reading vtk meshes. The following segmentation is supposed to match the thalamus.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bbc7b178df637ee5706dd248ab6168636afb1f4.jpeg" data-download-href="/uploads/short-url/aNZCYjWepqdfNJbI01397Q1RjuY.jpeg?dl=1" title="Slicer3D521" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bbc7b178df637ee5706dd248ab6168636afb1f4_2_658x500.jpeg" alt="Slicer3D521" data-base62-sha1="aNZCYjWepqdfNJbI01397Q1RjuY" width="658" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bbc7b178df637ee5706dd248ab6168636afb1f4_2_658x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bbc7b178df637ee5706dd248ab6168636afb1f4_2_987x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bbc7b178df637ee5706dd248ab6168636afb1f4_2_1316x1000.jpeg 2x" data-dominant-color="575763"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer3D521</span><span class="informations">1382×1049 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, one of my colleague is using Slicer version 4.11.0-2020-01-18 on Mac OS and does not encounter the same trouble, loading exactly the same files.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9af8736a46c93caec76870b82a5fbaf3eb47bb9.jpeg" data-download-href="/uploads/short-url/sMc2pHYb8tYuUsV8O60rAA2RwIp.jpeg?dl=1" title="SlicerSara" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9af8736a46c93caec76870b82a5fbaf3eb47bb9_2_503x500.jpeg" alt="SlicerSara" data-base62-sha1="sMc2pHYb8tYuUsV8O60rAA2RwIp" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9af8736a46c93caec76870b82a5fbaf3eb47bb9_2_503x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9af8736a46c93caec76870b82a5fbaf3eb47bb9_2_754x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9af8736a46c93caec76870b82a5fbaf3eb47bb9.jpeg 2x" data-dominant-color="4C4B58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerSara</span><span class="informations">813×808 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Would anyone know what is happening there ?</p>
<p>Thanks a lot in advance!</p>

---

## Post #2 by @lassoan (2020-03-11 13:37 UTC)

<p>We have updated Slicer-4.11.0 on 2020-02-26 to consistently save all data in LPS coordinate system and assume all data to be stored in LPS coordinate system by default. See details in this post:</p>
<aside class="quote quote-modified" data-post="1" data-topic="10446">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446">Model files are now saved in LPS coordinate system</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    While Slicer uses RAS coordinate system internally, images, transforms, and markups files are stored in LPS coordinate system, because DICOM and all medical image computing software (maybe except a few very old ones) uses LPS coordinate system in files. 
However, Slicer has been still using its internal RAS coordinate system in mesh files (STL, VTK, VTP, OBJ, PLY), which <a href="https://issues.slicer.org/view.php?id=4445">caused issues when interfacing with third-party software</a>. 
Starting from tomorrow (Slicer-4.11.0-2020-02-26, revision 28794), …
  </blockquote>
</aside>

<p>If you have any remaining questions or concerns then please post them here.</p>

---
