# Saving DICOM format

**Topic ID**: 18414
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/saving-dicom-format/18414

---

## Post #1 by @refrangioni (2021-06-30 04:18 UTC)

<p>I need to segment CT images for include such images in TOMO_MC program to dosimetric simulating in MCNP .<br>
The TOMO_MC program only accept bitmap files.<br>
I think save the segmented images in DICOM format to convert in .bmp extensions, but i cant save segmented images in DICOM format.<br>
It is necessary any extension : slicerRT  or quantitativereporting ?</p>

---

## Post #2 by @lassoan (2021-06-30 04:20 UTC)

<p>Do you need to save the segmentation in DICOM Segmentation Object, DICOM RT structure set, or .bmp file format?</p>

---

## Post #3 by @refrangioni (2021-07-01 13:56 UTC)

<p>I need save in .bmp.<br>
The file must be contain the segmented slices.</p>

---

## Post #4 by @refrangioni (2021-07-05 12:13 UTC)

<p>I need the images to be in .bmp file format but if it’s difficult it can also be in dicom format as long as they contain the segmentation, then I can transform them into .bmp by another program, but the ideal is that they are in .bmp</p>

---

## Post #5 by @lassoan (2021-07-09 04:33 UTC)

<p>I would recommend to submit a feature request to the developers of TOMOT_MC to add support for more commonly used image formats (such as jpg or png).</p>
<p>In the meantime, you can save a segmentation or a volume in bmp file format as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">this example</a>. If you want to save the image in native resolution then you can get the voxels as numpy array using <code>slicer.util.arrayFromVolume</code> or <code>slicer.util.arrayFromSegmentBinaryLabelmap</code>.</p>

---

## Post #6 by @refrangioni (2021-07-10 01:53 UTC)

<p>I managed to save the segmented images in dicom format using the SlicerRT extension.<br>
I followed as recommended by Gowtham P in this forum:<br>
Right Click the segmentation node on Data Manager → Export visible segments to Binary Labelmap<br>
A new segmentation label will be created, if you right-click that you will get the option to export to DICOM, where you can add details and export your segment as a DICOM series.<br>
Need to choose RT in “select export type” item.<br>
Thank you very much!</p>

---
