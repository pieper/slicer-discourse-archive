---
topic_id: 9300
title: "Dicom Export Of Segments Did Not Work Irrespective Of Platfo"
date: 2019-11-25
url: https://discourse.slicer.org/t/9300
---

# Dicom export of segments did not work (irrespective of platform since 4.10)

**Topic ID**: 9300
**Date**: 2019-11-25
**URL**: https://discourse.slicer.org/t/dicom-export-of-segments-did-not-work-irrespective-of-platform-since-4-10/9300

---

## Post #1 by @malbert (2019-11-25 19:46 UTC)

<p>Operating system: OSX (Mojave) and Windows 10 (French version)<br>
Slicer version: 4.10 and 4.11<br>
Expected behavior: Save the segment with the image as indicated in “Create files from CT volumes and segmentation” under dicom. (video tutorial)<br>
Actual behavior: Save only the image and not the segmentation. The export dicom window did not show the RT type (only scalar volume are shown unlike what was shown in the explanatory video). The behavior is easily reproducible with built in exemples.</p>

---

## Post #2 by @lassoan (2019-11-25 19:56 UTC)

<p>Segmentation export as RTSTRUCT should work well. Make sure SlicerRT extension is installed and select the entire study you would like to export (not just the CT image). If you still experience problems then reproduce it with any of the Slicer sample data sets, save the scene as an .mrb file and post here a download link so that we can investigate.</p>

---

## Post #3 by @malbert (2019-11-26 07:04 UTC)

<p>Thanks. works like a charm indeed. May I suggest to be more explicit in the video about the mandatory download of the RT extension.<br>
Sincerely</p>

---

## Post #4 by @lassoan (2019-11-26 16:00 UTC)

<p>Thanks for the suggestion, I’ve added a comment about this here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>

---
