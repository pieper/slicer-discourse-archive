# Exporting labelmap in raw format

**Topic ID**: 32316
**Date**: 2023-10-19
**URL**: https://discourse.slicer.org/t/exporting-labelmap-in-raw-format/32316

---

## Post #1 by @mattiadl (2023-10-19 01:34 UTC)

<p>Hello all,<br>
I’m trying to export a binary labelmap in raw format.<br>
I have a segmentation, I press “Export visible segment to binary labelmap”.<br>
Then I click on the new labelmap and export to file, saving it as raw. But then I get an error. The same if I try .bmp. It works with tif and vtk. I report a screenshot of the error.<br>
How can I solve? I tried in many different ways.</p>
<p>Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77b8ff58eb023dc733fcdf38ecf682344507cf5d.png" data-download-href="/uploads/short-url/h57aNB7GCh42OIGyQmIUh49m32R.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77b8ff58eb023dc733fcdf38ecf682344507cf5d.png" alt="image" data-base62-sha1="h57aNB7GCh42OIGyQmIUh49m32R" width="690" height="268" data-dominant-color="E8E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">965×375 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-10-19 01:38 UTC)

<p>You can save in .nhdr format with compression disabled. That way you don’t lose any information, just the image header is stored in a separate file (*.seg.nhdr is the header file, *.raw is the raw voxel file).</p>
<p>Note that saving as .raw format makes the data unusable, as you need at least the image dimensions, origin, spacing, and axis directions to be able to reconstruct the image in 3D space. What is the motivation for saving as .raw file without an image header?</p>

---

## Post #3 by @mattiadl (2023-10-19 07:18 UTC)

<p>Hello,<br>
My ultimate goal is to create a voxel file of the patient to be used in an EM solver. The raw file will be associated with a voxel material description file containing the dielectric properties associated to the different tissues (identified by the index assigned in the raw file to the voxels belonging to each segmented tissue).<br>
Let me know if I’m not clear.</p>
<p>Thank you again!</p>

---

## Post #4 by @lassoan (2023-10-19 12:32 UTC)

<p>What is that solver? Are you sure that it cannot read the properties from any of the standard 3D volume file formats?</p>
<p>If the solver indeed can only accept a raw file then I would recommend to request from the developers to add support for a standard 3D image file format (NRRD, MetaIO, or NIFTI). Ability to load an array from a standard file format would simplify the life of users and would reduce the user support effort of the developers (as it would be straightforward to import the material properties). Until they implement this, using the .nhdr format can be a reasonable workaround.</p>

---

## Post #5 by @mattiadl (2023-10-20 08:37 UTC)

<p>Hello,<br>
the idea is to use it with CST and COMSOL.<br>
But thank you for your answer. I didn’t think about the .nhdr format.<br>
I can use the .raw file to build my .vox.<br>
I hope to be on the right path.</p>
<p>Thanks!</p>

---
