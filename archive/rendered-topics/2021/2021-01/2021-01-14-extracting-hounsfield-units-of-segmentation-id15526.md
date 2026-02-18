# Extracting Hounsfield units of segmentation

**Topic ID**: 15526
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/extracting-hounsfield-units-of-segmentation/15526

---

## Post #1 by @Tomas_Iesmantas (2021-01-14 14:57 UTC)

<p>Hi,</p>
<p>I have segmentation of the series of DICOM images (I have those images as well). I would like to output spatial coordinates of the segmentation (just lik in STL format) as well as Hounsfield units at those points.<br>
Simply put, I want an output with 4 columns: first three entries are XYZ coordinates and the fourth column is the value of HU at that location.</p>
<p>XYZ coordinates of the segmentation can be simply obtained by saving closed surface to the STL file. But how to get out the hounsfield units I cannot figure out.</p>
<p>I understand that if the cloud point is in between the slices, then HU values has to be interpolated - thats is fine.</p>
<p>Any advice?</p>
<p>Note: I’m very new to the Slicer.</p>

---
