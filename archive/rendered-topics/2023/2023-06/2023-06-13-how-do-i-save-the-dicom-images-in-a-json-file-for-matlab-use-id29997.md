# How do I save the dicom images in a .Json file for Matlab use

**Topic ID**: 29997
**Date**: 2023-06-13
**URL**: https://discourse.slicer.org/t/how-do-i-save-the-dicom-images-in-a-json-file-for-matlab-use/29997

---

## Post #1 by @Reham (2023-06-13 02:53 UTC)

<p>Hello,<br>
After I segmented the 3D image from a set of  dicom images, I would like to save them all in a “.json” file that has all the dicom images saved to call the file in Matlab. Anyone can help in this point will be appreciated.</p>

---

## Post #2 by @lassoan (2023-06-16 14:36 UTC)

<p>I would recommend to store 3D images in standard file formats, such as nrrd. In Matlab, you can load/saved nrrd files using nrrdread.m and nrrdwrite.m scripts available <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">here</a>.</p>

---
