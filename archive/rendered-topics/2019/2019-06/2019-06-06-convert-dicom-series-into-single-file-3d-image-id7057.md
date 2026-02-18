# Convert dicom series into single file-3D image

**Topic ID**: 7057
**Date**: 2019-06-06
**URL**: https://discourse.slicer.org/t/convert-dicom-series-into-single-file-3d-image/7057

---

## Post #1 by @Pooja_Virkar (2019-06-06 12:45 UTC)

<p>Hello,</p>
<p>I want to convert dicom series (89 slices) into single file of 3D image using 3D slicer. Could you please help me by providing steps to do it?</p>
<p>I want to use this 3D image for segmentation purpose in ITK.</p>

---

## Post #2 by @pieper (2019-06-06 13:54 UTC)

<p>Hi - I guess you mean just save a nifti file of your dicom?  Generally that’s just a matter <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_3D_Visualization_of_DICOM_images_for_Radiology_Applications" rel="nofollow noopener">of loading the data and saving in a new format</a>.  Or if you want a more direct path you might use <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener">dcm2niix</a>.</p>

---
