# exporting sequence of stl files from segmentation of 4D dicom images

**Topic ID**: 29759
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/exporting-sequence-of-stl-files-from-segmentation-of-4d-dicom-images/29759

---

## Post #1 by @Sanjib_Gurung (2023-05-31 23:57 UTC)

<p>Hi, I am new to 3D slicer. I segmented a volume sequence of 4D cardiac MRI images. I need to export the sequence of segmented geometries as a sequence of stl files. Currently, I can only export an stl file at<br>
a time point at a time and cannot export the stl files at all the time instances at once. Is there a way to export the time sequence of stl files at once?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2023-06-02 23:38 UTC)

<p>You can write a few-line Python script that iterates through the sequence and exports each time point. There are examples in the script repository but if you have trouble finding them or you miss some steps then let us know.</p>

---
