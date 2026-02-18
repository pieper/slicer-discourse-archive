# Image Position Tag Value different in database and volume node

**Topic ID**: 36039
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/image-position-tag-value-different-in-database-and-volume-node/36039

---

## Post #1 by @fqzhice (2024-05-10 03:10 UTC)

<p>Import a CT series to Database, Get image positon tag value in Dicom File Meta data dialog. Then load image in Slicer and check volume info in Volume node, orientation and direction value is different with tag in data base. if Export to nii.gz, tag is the the same as node.</p>
<p>Any one can help?</p>

---

## Post #2 by @lassoan (2024-05-10 05:29 UTC)

<p>There are many ways to specify the same physical location for a 3D array of voxels. It is up to the application to choose what corner of the array to use as origin and how the axes are ordered.</p>
<p>If you want your image geometry (origin, spacing, axis directions, and extents) to match the geometry of some other image then you can resample the image, using that other image as reference.</p>

---

## Post #3 by @fqzhice (2024-05-10 05:52 UTC)

<p>Thanks for your Reply!<br>
So I shall resample the volume to match th original tag value. and export to nii again</p>

---

## Post #4 by @lassoan (2024-05-10 13:26 UTC)

<p>You can load the image that you want to use the geometry of, resample the other to that, and save it.</p>
<p>I would not recommend to use NIFTI for storing CT image or segmentation. NIFTI is only for brain MRI and you may run into many problems if you use this format, mostly due to that image orientation may be stored in NIFTI files in an ambiguous way. NRRD file format is simpler yet more flexible, and it does not have this ambiguity in image orientation.</p>

---
