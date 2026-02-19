---
topic_id: 5424
title: "Convert Dicom Rt Segmented Object Into Nifti Format"
date: 2019-01-19
url: https://discourse.slicer.org/t/5424
---

# Convert DICOM-RT segmented object into NIFTI format

**Topic ID**: 5424
**Date**: 2019-01-19
**URL**: https://discourse.slicer.org/t/convert-dicom-rt-segmented-object-into-nifti-format/5424

---

## Post #1 by @moleps_islon (2019-01-19 17:08 UTC)

<p>I have a brain MRIs where the tumor is segmented in proprietary software on the T1+C series and output into what I believe is DICOM-RT format.  I can import the DICOM directory correctly after installing the RT extension into Slicer-3D. However, so far I´ve not been able to output this segmented object as a mask (for subsequent use in my statistics program) into its own NIFTI retaining the registration to the T1+C series. I can convert the segmented object and the T1 into nifti, but the registration between the two is obviously off. Any idea how I can output these two into seperate nifti files?</p>
<p>Operating system:Mac OS X<br>
Slicer version:4.10.0<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @cpinter (2019-01-27 15:09 UTC)

<p>Sorry for the late response. If you have the registration, make sure it is applied on the segmentation before the export. You can do it in the Transforms module or the Data module (double-click in rightmost column).<br>
Let us know how it goes.</p>

---

## Post #3 by @moleps_islon (2019-01-30 20:39 UTC)

<p>Upon exporting after converting to binary labelmap everything seems to work. Thx.</p>

---
