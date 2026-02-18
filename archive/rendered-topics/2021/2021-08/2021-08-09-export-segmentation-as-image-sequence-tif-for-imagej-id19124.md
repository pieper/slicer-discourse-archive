# Export segmentation as image sequence (tif. for ImageJ)

**Topic ID**: 19124
**Date**: 2021-08-09
**URL**: https://discourse.slicer.org/t/export-segmentation-as-image-sequence-tif-for-imagej/19124

---

## Post #1 by @Josefin (2021-08-09 15:12 UTC)

<p>Hi!</p>
<p>I’d like to export a segmentation as an image sequence/tif.file, that can be opened with ImageJ. The volume rendering is less important in this case, I’m mostly interested in the individual slices of the segmented volume (I imported the data as a tif.file). Is this possible to do in Slicer? I tried to convert the data into a DICOM series (using the converter tool) but didn’t manage to save only the segmentation. I never use DICOM files normally, but thought it might be easier to do the conversion from dicom → tiff…</p>
<p>Thanks!<br>
Cheers,<br>
J<br>
(Should mention I’m not a programmer, and I work with geological samples, so apologies in advance…:)).</p>

---

## Post #2 by @lassoan (2021-08-09 15:19 UTC)

<p>I would not recommend to use TIFF for storage of 3D files. TIFF has many limitations. For example, there is no standard way to specify slice spacing, image orientation, meaning of label values, etc. Instead, you can save the segmentation as usual, in .nrrd format and import that into ImageJ. If you prefer other formats (MetaImage (mha), NIFTI, …, which ImageJ might be able to load without plugins) then you can export the segmentation to labelmap node and choose that format for the labelmap in the save data window.</p>

---
