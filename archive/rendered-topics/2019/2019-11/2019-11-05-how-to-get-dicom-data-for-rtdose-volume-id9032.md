---
topic_id: 9032
title: "How To Get Dicom Data For Rtdose Volume"
date: 2019-11-05
url: https://discourse.slicer.org/t/9032
---

# How to get dicom data for RTDose volume

**Topic ID**: 9032
**Date**: 2019-11-05
**URL**: https://discourse.slicer.org/t/how-to-get-dicom-data-for-rtdose-volume/9032

---

## Post #1 by @dominicrushforth (2019-11-05 15:07 UTC)

<p>I have some code that saves images as RTDose files using the DicomRtImportExportPlugin.</p>
<p>When these files are reloaded I want to be able to read the dicom tags but the imported volume does not have the attribute DICOM.instanceUIDs, which I would normally use to get the dicom data using slicer.dicomDatabase.fileForInstance(instUids[0]).</p>
<p>The reloaded volume only has the attribute DicomRtImport.DoseVolume:1 and I have been unable to find a way to use this to help.</p>
<p>Is there any way to get dicom tag information for a file that has been saved and reopened in this way?</p>

---

## Post #2 by @lassoan (2019-11-05 15:36 UTC)

<p>You can get DICOM UIDs from the subject hierarchy as shown in this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_an_item_in_the_Subject_Hierachy_tree.3F_For_example.2C_get_the_content_time_tag_of_a_structure_set:">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_an_item_in_the_Subject_Hierachy_tree.3F_For_example.2C_get_the_content_time_tag_of_a_structure_set:</a></p>

---

## Post #3 by @dominicrushforth (2019-11-18 17:02 UTC)

<p>Thanks, worked perfectly.</p>

---
