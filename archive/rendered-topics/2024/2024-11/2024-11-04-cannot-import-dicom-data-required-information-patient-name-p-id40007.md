---
topic_id: 40007
title: "Cannot Import Dicom Data Required Information Patient Name P"
date: 2024-11-04
url: https://discourse.slicer.org/t/40007
---

# Cannot import DICOM data - Required information (patient name, patient ID, study instance UID) is missing from dataset

**Topic ID**: 40007
**Date**: 2024-11-04
**URL**: https://discourse.slicer.org/t/cannot-import-dicom-data-required-information-patient-name-patient-id-study-instance-uid-is-missing-from-dataset/40007

---

## Post #1 by @ggbrown (2024-11-04 01:05 UTC)

<p>I’m using the latest version 5.6.2. It gave message “import completed: added 0 patients, 0 studies, 0 series, 0 instances”.</p>
<p>When I clicked “Import DICOM files”, clicked into the directory having lots of .dcm files, it said “no items matches your search”, but I can see all those .dcm files in window file explorer.</p>
<p>The error log displayed:<br>
Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
Failed to insert file into database (required fields missing): C:/Users/xiebr/Documents/morphoDownloadCTdata/morphoCTdata/aotus19801/Aotus81/newAotus1342.dcm<br>
Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
Failed to insert file into database (required fields missing): C:/Users/xiebr/Documents/morphoDownloadCTdata/morphoCTdata/aotus19801/Aotus81/new_Aotus_198010000.dcm<br>
Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
Failed to insert file into database (required fields missing): C:/Users/xiebr/Documents/morphoDownloadCTdata/morphoCTdata/aotus19801/Aotus81/new_Aotus_198010001.dcm<br>
Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
Failed to insert file into database (required fields missing): C:/Users/xiebr/Documents/morphoDownloadCTdata/morphoCTdata/aotus19801/Aotus81/new_Aotus_198010002.dcm<br>
…</p>

---

## Post #2 by @ggbrown (2024-11-04 02:39 UTC)

<p>Edit: “When I clicked “Import DICOM files”, clicked into the directory having lots of .dcm files, it said “no items matches your search”, but I can see all those .dcm files in window file explorer.” – I understand that I need to load the directory, so I probably won’t see anything when clicking into the directory.</p>

---
