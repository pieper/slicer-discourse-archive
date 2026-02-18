# OCT b-scan thickness is not being found on load

**Topic ID**: 32273
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/oct-b-scan-thickness-is-not-being-found-on-load/32273

---

## Post #1 by @Mark_Banghart (2023-10-17 15:09 UTC)

<p>We have a number of legacy DICOM files that we would like to view in slicer. The files load with drag and drop. The user selects volume and the OCT is displayed. The pixel dimensions for the x and y dimensions are filled in correctly in slicer. The thickness for the b-scans (z axis) is set to 1. The DICOM has the b-scan thickness in the header. I can get it with the following python code.</p>
<p>z_spacing = dcm.SharedFunctionalGroupsSequence[0].PixelMeasuresSequence[0].SliceThickness</p>
<p>Where is slicer looking for the OCT thickness? If I know where slicer is looking for it I can modify the DICOM so that they load in slicer with the b-scan thickness.<br>
Thanks<br>
Mark</p>

---

## Post #2 by @pieper (2023-10-17 17:09 UTC)

<p>Generally Slicer is only concerned with spacing between Slices, so you need to make sure the ImagePositionPatient is defined for each slice to make a volume.</p>

---
