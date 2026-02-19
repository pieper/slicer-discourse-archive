---
topic_id: 16032
title: "Query On Exporting Annotation"
date: 2021-02-17
url: https://discourse.slicer.org/t/16032
---

# Query on exporting annotation

**Topic ID**: 16032
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/query-on-exporting-annotation/16032

---

## Post #1 by @Akash (2021-02-17 11:34 UTC)

<p>Operating system: Windows10<br>
Slicer version:4.11.20200930<br>
Expected behavior: NA<br>
Actual behavior:NA</p>
<p>I would like to export the annotation co ordinates in a JSON/CSV/XML format containing the filename, label and co ordinate points. Please guide me on how to do it. I am new to this tool so kindly excuse.</p>

---

## Post #2 by @lassoan (2021-02-17 11:43 UTC)

<p>Markups are already saved in json or csv format in recent Slicer versions.</p>
<p>What filename would you like to see in the file?</p>

---

## Post #3 by @Akash (2021-02-17 11:48 UTC)

<p>Thanks for your response sir. Suppose I open a DICOM series say 1.dcm, 2.dcm and 3.dcm. And I annotate a ROI in 2.dcm. Then in the saved file I would like to have this filename as 2.dcm. By doing so when I annotate images in bulk say 50 or 100 DICOM files then I will know the corresponding images and csvs.</p>

---

## Post #4 by @lassoan (2021-02-17 11:55 UTC)

<p>Do you annotate the images to generate training data for object detection, localization, or segmentation? What kind of annotations do you use?</p>
<p>Do you work with 2D or 3D images? A single 3D volume is usually made up of many DICOM files, so your annotation can spread over multiple files and/or may be between defined between two files.</p>

---

## Post #5 by @Akash (2021-02-17 12:03 UTC)

<p>I am annotating 2D DICOM files for object detection training.</p>

---

## Post #6 by @lassoan (2021-02-18 19:25 UTC)

<p>How do you open the DICOM files? Do you use <a href="https://github.com/JoostJM/SlicerCaseIterator">CaseIterator extension</a>, load the images one by one, or do they show up as a sequence of images or as a 3D image stack?</p>

---

## Post #7 by @Akash (2021-02-20 06:14 UTC)

<p>I am not directly using DICOM for training purpose. I convert them to PNG and feed to my network. Also currently I am using only 2D DICOM images and not 3D.</p>

---
