---
topic_id: 14314
title: "Convert Dcm Images To Dicom Case"
date: 2020-10-29
url: https://discourse.slicer.org/t/14314
---

# Convert .dcm images to DICOM case

**Topic ID**: 14314
**Date**: 2020-10-29
**URL**: https://discourse.slicer.org/t/convert-dcm-images-to-dicom-case/14314

---

## Post #1 by @OLIVIA_GENOVA (2020-10-29 20:51 UTC)

<p>Operating system: iOS<br>
Slicer version: 4.10.2<br>
Expected behavior: Open DICOM 3D image<br>
Actual behavior: 0 patients found…</p>
<p>Hello,</p>
<p>I’m a student and I need to do the segmentation and mesh of an aorta with a disease. We have been sent the images of a patient with that disease, but in a .jpg format.<br>
I have converted those images into .dcm, and I have been trying to import the file with those images into 3D Slicer as a DICOM file, but it says ‘0 patients found’.<br>
I’ve been trying all the different methods and solutions proposed in this page and others, but nothing works.<br>
I can send you the file.zip with the .dcm images!</p>
<p>Thank you,<br>
Olivia</p>

---

## Post #2 by @lassoan (2020-10-30 04:32 UTC)

<p>If you just need to create a segmentation and mesh then you don’t need to convert to DICOM, just import the jpeg images and segment the volume.</p>
<p>JPG images of course are not well suited for the job, as they are just 8-bit images, therefore the segmented surfaces may be more noisy than using the original 16-bit images, you may also have compression artifacts, and you may not know the exact image spacing values. The aorta on contrasted CTs are very well visible, so overall JPEG images might provide sufficient quality, but in the long term, try to get the proper DICOM images instead (write a DICOM CD/DVD instead of download the JPEG stack from the PACS web viewer).</p>

---
