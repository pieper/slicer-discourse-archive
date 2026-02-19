---
topic_id: 12866
title: "Dicom Import Single File Checkboxes"
date: 2020-08-05
url: https://discourse.slicer.org/t/12866
---

# DICOM import "single file" checkboxes

**Topic ID**: 12866
**Date**: 2020-08-05
**URL**: https://discourse.slicer.org/t/dicom-import-single-file-checkboxes/12866

---

## Post #1 by @briannawhitener (2020-08-05 16:55 UTC)

<p>when importing dicom files (in this case, from a disk from outside facility), each slice comes in as a separate file. I’ve found where to show options and uncheck each box for “single file” but this must be done on EVERY slice… is there a setting somewhere to change this so it defaults to being NOT checked? didn’t see anything in the settings area when i checked.<br>
thanks!</p>

---

## Post #2 by @lassoan (2020-08-05 17:03 UTC)

<p>We have not explicitly disabled the possibility of loading DICOM files via “Add data” yet, but DICOM files should be always imported and loaded using DICOM module. In recent Slicer Preview Releases DICOM import is very fast, you just need to switch to DICOM module and drag-and-drop the <em>folder</em> that contains your DICOM data and import typically completes within seconds. Then you can double-click on the patient/study/series that you want to load into the scene.</p>
<p>“Add data” has many issues and limitations: it can only load data from a single folder, it can only load images, images with variable spacing or tilted gantry acquisitions may be distorted, etc. When you load a DICOM series using “Add data” then you need to select only a single file (not all the files of the series, so you don’t need to uncheck many files), but you would need to know which single file belongs to which series.</p>

---
