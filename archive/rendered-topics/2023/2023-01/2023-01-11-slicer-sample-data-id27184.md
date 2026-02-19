---
topic_id: 27184
title: "Slicer Sample Data"
date: 2023-01-11
url: https://discourse.slicer.org/t/27184
---

# Slicer sample data

**Topic ID**: 27184
**Date**: 2023-01-11
**URL**: https://discourse.slicer.org/t/slicer-sample-data/27184

---

## Post #1 by @firatoz (2023-01-11 07:19 UTC)

<p>I downloaded the CTP cardio sample data in Slicer and converted it from seq.nrrd format to DICOM format. The file works as 4d in seq.nrrd format but becomes 3d in DICOM format. How can I convert this file to 4d in DICOM format? I will be glad if you can help</p>

---

## Post #2 by @pieper (2023-01-11 17:26 UTC)

<p>That probably requires some research and coding to implement.  There would need to be tags added to distinguish the timepoints, but I don’t think anyone has done that.  What would you use the 4D dicom for?</p>

---

## Post #3 by @firatoz (2023-01-11 17:41 UTC)

<p>I want to perform cardiac perfusion CT in our hospital, but I need to trial with a sample image.  The software we evaluate the images only supports DICOM format.  Therefore I need DICOM format.</p>

---

## Post #4 by @pieper (2023-01-11 17:49 UTC)

<p>Probably every commercial system uses some specific tags to define the time series, like the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMImageSequencePlugin.py">logic implemented in Slicer</a>.  Unless I’m mistaken I don’t think anyone has done the this kind of export from Slicer, but it should be doable.  If you or others ended up doing this a lot, someone could add an export option specific to sequences.</p>

---
