---
topic_id: 24074
title: "Report A Bug In Function Dicomutils Loadpatientbypatientid P"
date: 2022-06-28
url: https://discourse.slicer.org/t/24074
---

# Report a bug in function " DICOMUtils.loadPatientByPatientID(patientID); "

**Topic ID**: 24074
**Date**: 2022-06-28
**URL**: https://discourse.slicer.org/t/report-a-bug-in-function-dicomutils-loadpatientbypatientid-patientid/24074

---

## Post #1 by @zhang_ming (2022-06-28 07:55 UTC)

<p>DICOMUtils.loadPatientByPatientID(patientID);   If the patientID use long string  like : 2b89691a0744504491ef91d711d94918, it will failed. because I found the entry in sql database. but the 3d slicer python terminal report error : Patient not found by PatientID 2b89691a0744504491ef91d711d94918</p>

---

## Post #2 by @pieper (2022-06-28 12:29 UTC)

<p>PatientID is not unique in dicom, so slicer assigns an arbitrary one.</p>

---
