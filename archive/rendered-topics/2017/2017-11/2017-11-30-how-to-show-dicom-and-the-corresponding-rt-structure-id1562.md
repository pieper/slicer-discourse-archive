---
topic_id: 1562
title: "How To Show Dicom And The Corresponding Rt Structure"
date: 2017-11-30
url: https://discourse.slicer.org/t/1562
---

# How to show DICOM and the corresponding RT STRUCTURE?

**Topic ID**: 1562
**Date**: 2017-11-30
**URL**: https://discourse.slicer.org/t/how-to-show-dicom-and-the-corresponding-rt-structure/1562

---

## Post #1 by @glhfgg1024 (2017-11-30 00:59 UTC)

<p>Hello everyone, I’m a newbie to Slicer.</p>
<p>I have one DICOM directory where many .dcm files are there and another DICOM RT STRUCTURE directory where one .dcm file is there. I want to load the two directories into Slicer and shown in 3-D view.</p>
<p>I have tried to set the Options into “Scalar Overlay”, but it didn’t work. How could I do next? Thanks a lot!</p>

---

## Post #2 by @lassoan (2017-11-30 04:16 UTC)

<p>Install SlicerRT extension, import the data into Slicer by drag-and-dropping the entire folder to the Slicer application window, and load it using DICOM module. RTSTRUCT will be loaded as segmentation and you can show that in 3D and slice views.</p>

---

## Post #4 by @lassoan (2017-12-03 06:14 UTC)

<p>A post was merged into an existing topic: <a href="/t/convert-dicom-rtstruct-format-to-nifti-format/1580">Convert DICOM-RTSTRUCT format to Nifti format</a></p>

---

## Post #5 by @Mgi (2020-12-02 12:54 UTC)

<p>Hello! I am using the 3D slicer 4.10.2, I followed this sequence but I can’t see the segmentation. Some ideas?</p>

---

## Post #6 by @lassoan (2020-12-03 03:55 UTC)

<p>You need to use latest Slicer stable or preview release and install SlicerRT extension.</p>

---

## Post #7 by @lassoan (2020-12-05 23:05 UTC)

<p>A post was split to a new topic: <a href="/t/longitudinalpetct-extension-fails-to-read-dicom-files/14902">LongitudinalPETCT extension fails to read DICOM files</a></p>

---
