# Problem with MRI data classification

**Topic ID**: 6876
**Date**: 2019-05-22
**URL**: https://discourse.slicer.org/t/problem-with-mri-data-classification/6876

---

## Post #1 by @doc-xie (2019-05-22 01:04 UTC)

<p>Hi everyone,<br>
All of MRI data including T1,T2,FLAIR and DWI from GE scanner are saved into single folder by default. Is it possible to separate them apart and save them into different folders  with Slicer? Is there any other recommended software out of Slicer?<br>
Thanks,<br>
Xie</p>

---

## Post #2 by @lassoan (2019-05-22 02:48 UTC)

<p>You can reorganize folder(s) full of random DICOM files and put them in a new folder structure organized by patients, studies, series by using “DICOM Patcher” modules. Select input folder (top-level folder containing DICOM files, there can be subdirectories), output folder (it should be an empty folder), enable “Normalize file names” option (and only that), and click “Patch”.</p>

---

## Post #3 by @doc-xie (2019-05-22 09:05 UTC)

<p>Thanks,<br>
The problem was solved successfully.<br>
Xie</p>

---
