# JPG file stack with different spacings

**Topic ID**: 3436
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/jpg-file-stack-with-different-spacings/3436

---

## Post #1 by @Hari_Simha (2018-07-09 19:59 UTC)

<p>Hello</p>
<p>I am new to Slicer and am trying to construct a 3d volume from an image stack (jpeg or png). The application is in materials science. The spacing between the images in the stack are not the same.</p>
<p>Please advise as to how I could read this in.</p>
<p>Thanks</p>
<p>Hari</p>

---

## Post #2 by @lassoan (2018-07-10 04:44 UTC)

<p>If you read the image stack from DICOM then Slicer can create a grid (displacement field) transform that places each slice in their correct location. You can then harden the transform on the volume to create a uniformly spaced volume.</p>
<p>If you cannot get the input in DICOM format then you can adapt the <a href="https://github.com/Slicer/Slicer/blob/b2b7068e5b795706b57b5337212d5b160408e20e/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L523-L679">AcquisitionModeling</a> class of the DICOM reader to create the appropriate transform.</p>

---
