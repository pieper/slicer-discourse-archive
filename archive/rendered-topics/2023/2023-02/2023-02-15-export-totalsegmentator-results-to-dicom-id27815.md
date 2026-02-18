# Export TotalSegmentator results to DICOM

**Topic ID**: 27815
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/export-totalsegmentator-results-to-dicom/27815

---

## Post #1 by @LipTeck_Chew (2023-02-15 03:04 UTC)

<p>Hi there</p>
<p>Has anyone tried to do a DICOM export of the contours from Slicer3D ?</p>
<p>I encountered a problem that not all slices of the contours are exported. The contours were produced from TotalSegmentator.</p>
<p>Thank you.</p>
<p>Regards<br>
Lip Teck</p>

---

## Post #2 by @lassoan (2023-02-15 03:32 UTC)

<p>Do you need to export DICOM RT structure set, Segmentation Object, or synthetic CT? What DICOM software do you want to use to view or use the images?</p>

---

## Post #3 by @LipTeck_Chew (2023-02-15 03:44 UTC)

<p>I have anonimised CT imported then run Totalsegmentator. Now, I’d like to DICOM export the image and rtstruct together.</p>
<p>When I tried this, only twenty over slices of contours and image could be exported as a set instead of the whole set at about over 100 slices.</p>
<p>If we can’t do that in slicer3d, could we do that by command line?</p>
<p>Regards<br>
Lip Teck</p>

---

## Post #4 by @lassoan (2023-02-15 04:27 UTC)

<p>By “100 slices” do you really mean “100 slices” or “100 segments”?</p>
<p>TotalSegmentator provides voxel-based segmentation. Shapes can contain holes and canbe extremely complex RT structure set can only store simple geometries.</p>
<p>DICOM Segmentation Object is a more modern, more appropriate information object for storing voxel-based segmentations.</p>
<p>All features that are available in the GUI, you can do in the command line or using Python scripting, so that’s not a limitation. You just need to figure out what information you want to export and in what format?</p>
<p>What DICOM software do you want to use to view or analyze the exported segmentation?</p>
<p>What is the clinical problem you want to solve? (the Slicer community has experience in all clinical specialties and procedures, so if we know what you want to do then we can share what worked/not worked for us in the past)</p>

---

## Post #5 by @LipTeck_Chew (2023-02-15 06:45 UTC)

<p>Hi Lassoan,</p>
<p>Thanks for your quick reply.</p>
<p>I mean 100 slices, not 100 contour type.</p>
<p>We need the DICOM RTStucture set and DICOM Image set.</p>
<p>We intend to bring it into treatment planning system or contouring system.</p>
<p>We want to reduce manual contouring time. In the anon CT, the totalsegmentator worked well in getting the bladder and bowels contours in the whole CT image of 100 slices. However, when we try to use dicom export, we could only export twenty over slices of structures out. Could there be a bug in SlicerRT module’s Dicom?</p>

---

## Post #6 by @lassoan (2023-02-15 06:56 UTC)

<p>Exporting the bladder should be fine, the bowels may be a complex mesh that may not be feasible to store in RT structure set. It would be really time for RT treatment planning systems to stop using this obsolete and limited parallel contour set representation and use labelmap images. If you have the opportunity, request DICOM Segmentation Object support from your TPS representative.</p>
<p>If you find that the exported RT structure set is cropped then double-check the reference CT image that is used for the export. If you still experience issues then provide a data set and instructions that we can use to reproduce the problem (if possible, use a publicly available test data set).</p>

---

## Post #7 by @LipTeck_Chew (2023-02-21 09:17 UTC)

<p>Hi Lassoan,</p>
<p>A recent released of the SlicerRT in Feb-2023 seems to have fixed this issue. I have updated and tested it ok.</p>
<p>regards,<br>
LipTeck</p>

---
