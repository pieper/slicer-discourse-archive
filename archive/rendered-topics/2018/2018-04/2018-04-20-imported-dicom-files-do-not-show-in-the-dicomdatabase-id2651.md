---
topic_id: 2651
title: "Imported Dicom Files Do Not Show In The Dicomdatabase"
date: 2018-04-20
url: https://discourse.slicer.org/t/2651
---

# Imported dicom files do not show in the dicomDatabase

**Topic ID**: 2651
**Date**: 2018-04-20
**URL**: https://discourse.slicer.org/t/imported-dicom-files-do-not-show-in-the-dicomdatabase/2651

---

## Post #1 by @EricWilson (2018-04-20 21:52 UTC)

<p>I am attempting to take a series of dicom files, import them to slicer, then iterate over them to get the first file to use for data. currently, I have an issue where the import method I am using will get the data in the files properly and will display the volume in the 3 views, but If the dicomDatabase does not already have the patient, no patient will display there. the functions for iteration over the data also return no patient data. if the patient is already in the database from being imported manually, everything will work as expected.</p>
<p>this is the method i am currently using:</p>
<p>path = ‘PATH_TO_DIR’<br>
ctk.ctkDICOMIndexer().addDirectory(slicer.dicomDatabase, path)<br>
db = slicer.dicomDatabase<br>
for patient in db.patients():<br>
for study in db.studiesForPatient(patient):<br>
for series in db.seriesForStudy(study):<br>
files = db.filesForSeries(series)</p>
<p>I’ve been looking through the source for the DICOM and DICOMLib scripts, but most things I have found related to the database are only done through the widget rather than the logic.</p>
<p>What is the best way to do this, and trigger the update on the dicomDatabase with the new directory?</p>

---

## Post #2 by @lassoan (2018-04-21 05:11 UTC)

<p>You can import DICOM files to the database by using <code>DICOMUtils.LoadDICOMFilesToDatabase</code>. You can use this automated test as an example: <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py">https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py</a></p>

---
