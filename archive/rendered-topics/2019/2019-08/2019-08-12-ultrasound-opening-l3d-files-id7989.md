# Ultrasound opening .l3d files

**Topic ID**: 7989
**Date**: 2019-08-12
**URL**: https://discourse.slicer.org/t/ultrasound-opening-l3d-files/7989

---

## Post #1 by @Masteling (2019-08-12 18:22 UTC)

<p>I am having issues opening a file created by a BK ultrasound machine.<br>
The file extension is .l3d and it is a 3D ultrasound.</p>
<p>Any suggestions on how to open this file in Slicer?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-08-12 18:50 UTC)

<p>It is a proprietary format that Slicer cannot read. If you can get specification for the file format or reverse engineer it then we can help with writing an importer in Slicer. You may also ask BK if there is an option to save volumes in some standard format (e.g., DICOM, nrrd, mha, or nifti).</p>

---

## Post #3 by @Masteling (2024-05-06 11:20 UTC)

<p>I was wondering if there were any developments on this end, considering BK Medical was bough by GE.<br>
I got a conversion set-up to convert l3d to mhd/raw and then mrb that works well for the order version of BK machines. As we upgrade to newer machines, it stopped being reliable, and I am exploring my options for conversion for use in Slicer.</p>

---
