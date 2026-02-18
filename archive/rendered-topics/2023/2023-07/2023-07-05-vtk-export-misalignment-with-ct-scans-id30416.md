# .vtk export misalignment with CT scans

**Topic ID**: 30416
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/vtk-export-misalignment-with-ct-scans/30416

---

## Post #1 by @William_Kuo (2023-07-05 18:28 UTC)

<p>Hi! I have been using Slicer for a while but I am still unfamiliar with some issues.</p>
<p>When I export my CT scans as a .vtk file and reimport them into Slicer and compare them with my CT scans, they don’t align. This is a problem because when I use the .vtk files in Bonemat, they don’t align with the mesh file I generate.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4aaaf35df014016a30f448ce3bb964e9874e9bde.png" data-download-href="/uploads/short-url/aExAL5M2ucHgPM2ASPAuYfySAQC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4aaaf35df014016a30f448ce3bb964e9874e9bde_2_690x343.png" alt="image" data-base62-sha1="aExAL5M2ucHgPM2ASPAuYfySAQC" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4aaaf35df014016a30f448ce3bb964e9874e9bde_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4aaaf35df014016a30f448ce3bb964e9874e9bde_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4aaaf35df014016a30f448ce3bb964e9874e9bde.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1201×598 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried matching the images and was successful in orienting them. However, the slicer positioning in each axis was still off despite looking the same. I can keep editing these CT files, but I have dozens and it’s inconvenient to keep doing this. Is there a way to export .vtk files that match orientation in CT scans so I can use them in Bonemat without misalignment?</p>

---

## Post #2 by @pieper (2023-07-05 18:36 UTC)

<p>.vtk format doesn’t preserve the image orientation information.  If you really need to use this format for compatibility you should be able to reconstruct a valid geometry manually or ideally use tools that are aware of <a href="https://www.slicer.org/wiki/Coordinate_systems">orientations</a>.</p>

---

## Post #3 by @William_Kuo (2023-07-05 18:49 UTC)

<p>Do you have any recommendation for what tools I should use?</p>

---

## Post #4 by @pieper (2023-07-05 19:03 UTC)

<p>What are you trying to do?</p>

---

## Post #5 by @William_Kuo (2023-07-05 19:18 UTC)

<p>Utilize Bonemat Batch Processing.</p>
<p>I require a .vtk file for the CT scans. But the .vtk file doesn’t align with the CT scans. I need the .vtk file to be axis-aligned to the CT scan, so my object (a bone) can utilize Bonemat that assigns material property to the bone based on the CT scan alignment.</p>

---

## Post #6 by @pieper (2023-07-05 20:25 UTC)

<p>I don’t know if anyone here uses Bonemat (I don’t) but probably it makes assumptions about the image data (identity orientation maybe?) so you can use Slicer to resample your image data until it matches.  I see that Bonemat has a restrictive non-commercial license so I’m not interested in learning more about it, but if it’s just assigning scalars to vertices of a mesh you can easily so that with Slicer using either VTK or numpy operations.</p>

---

## Post #7 by @DaSt (2023-10-26 07:23 UTC)

<p>Hi William,</p>
<p>I am using Bonemat and have similar issues. I am not exporting VTK files, but STL files derived from a segmentation in Slicer. For some of my DICOM series I see a missalignment in Bonemat between STL derived FE meshes and the DICOM series. This happens for DICOM series where the IJK to RAS Direction Matrix is not made up of solely zeros and ones.</p>
<p>I assume that bonemat does not read the orientation from the DICOM header but sets standard orientation. However I could not find anything in the documentation regarding this so I will dig into the code. Maybe this also helps you?</p>
<p>Best,<br>
Daniel</p>

---

## Post #8 by @lassoan (2023-10-26 13:35 UTC)

<p>This error has been reported a few times here on the forum. The problem is that DICOM image import in Bonemat is implemented poorly.</p>
<p>I would recommend not to use Bonemat but instead use the corresponding features in Slicer - see more details here:</p>
<aside class="quote" data-post="9" data-topic="28289">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dicom-to-rectilinear-grid-vtk/28289/9">Dicom to rectilinear grid vtk</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    By the way, it seems that <a href="http://www.bonemat.org/downloads/Bonemat_manual.pdf">all that bonemat can do</a> you can already do in Slicer. For the parameter mapping from CT densities to mechanical properties you can use a few lines of Python code (or using <a href="https://pypi.org/project/py_bonemat_abaqus/">py_bonemat_abaqus</a>). The license of bonemat is quite restrictive and you can do so much more in Slicer that I would recommend to consider using just Slicer for your workflow.
  </blockquote>
</aside>


---

## Post #9 by @DaSt (2023-10-26 14:06 UTC)

<p>Hi Andras,</p>
<p>thank you, I will look into Slicers capability. I use Bonemat primarily because of its capability to map to Finite Element Meshes.</p>
<p>Best regards,<br>
Daniel</p>

---

## Post #10 by @lassoan (2023-10-26 19:17 UTC)

<p>Slicer can map CTs to volumetric meshes, too. You can also do all the other steps (proper DICOM image import, segmentation, create FE mesh, sample CT image at mesh point positions, etc.). The only thing that may need some work is to find out what FE mesh file formats Slicer can export, what FE mesh formats your solver can load, and if there is no common format between them then use a converter or a different exporter in Slicer.</p>

---
