# DICOM metadata transfer

**Topic ID**: 35207
**Date**: 2024-04-01
**URL**: https://discourse.slicer.org/t/dicom-metadata-transfer/35207

---

## Post #1 by @Bahram_Zargar (2024-04-01 19:36 UTC)

<p>Hi Slicer team!<br>
I wish to export the Dicom mri as a new file after segmenting it, however the new series of DICOMs lacks many of the original DICOm files’ tags. Is it possible to move the metadata from one series of the Dicom mri to another?<br>
Thank you!</p>

---

## Post #2 by @lassoan (2024-04-01 19:41 UTC)

<p>We only transfer metadata that is needed for making derived images show up at the same patient/study. Why would you need to copy more fields to the processed MRI image? What is your overall clinical goal?</p>

---

## Post #3 by @Bahram_Zargar (2024-04-01 20:06 UTC)

<p>The goal is the have the new dicom series with applied masking, which has all the tags of the original one, except updating the AccessionNumber, StudyDescription, and SOPInstanceUID. I do have a python script to do updating of those specific tags, however the slices are missing lots of information from the original dicom series.</p>

---

## Post #4 by @lassoan (2024-04-01 21:05 UTC)

<p>If you alter the image content then there is not a lot that you are allowed to copy from the original image. But anyway, if you want to set some additional tags then probably the easiest is to let the current exporter to create the output files and then modify them using pydicom or dcmtk. You can add a custom plugin that performs this patching as part of the DICOM export process; or in your module you can perform the export and then patch the generated files.</p>

---
