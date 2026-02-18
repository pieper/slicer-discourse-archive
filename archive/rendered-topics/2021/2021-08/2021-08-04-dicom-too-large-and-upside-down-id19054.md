# Dicom too large and upside down

**Topic ID**: 19054
**Date**: 2021-08-04
**URL**: https://discourse.slicer.org/t/dicom-too-large-and-upside-down/19054

---

## Post #1 by @B4D (2021-08-04 12:38 UTC)

<p>I have a problem with a dicom file. The segmentation model is very large and the dicom is upside down. I would think that this would be caused by the equipment or software used to create the dicom?<br>
The CBCT equipment is Cranex 3D and the software exporting the Dicom is Invivo<br>
Is there a method to correct this. I know how to turn the model, still a bit of a hassle. The scale though is baffling me.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acccd2e4195ed063696cd883befe8c5e0ba1126e.png" alt="dicom" data-base62-sha1="oEEXo3dsxWsjB5SLNdajiCzM4ea" width="625" height="455"></p>

---

## Post #2 by @lassoan (2021-08-04 18:35 UTC)

<p>You need to use the DICOM module to load DICOM images. We have not yet disabled DICOM loading using “Add data” dialog but <a href="https://github.com/Slicer/Slicer/issues/5726">we will do that soon</a>.</p>
<p>Unfortunately, CBCT imaging devices often create invalid DICOM files. If you find that the image size or orientation of the imported DICOM image is incorrect when you load it using DICOM module, then you may need to run your data through “DICOM Patcher” module, which fixes some known errors of CBCT scanners.</p>

---
