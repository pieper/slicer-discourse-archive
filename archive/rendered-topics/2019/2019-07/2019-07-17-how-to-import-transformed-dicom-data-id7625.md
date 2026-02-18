# How to import transformed DICOM data

**Topic ID**: 7625
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/how-to-import-transformed-dicom-data/7625

---

## Post #1 by @Sachal (2019-07-17 12:34 UTC)

<p>Hi,<br>
I am new in using Slicer. I did AC-PC alignment of Brain DICOM, which was quite easy to do. After that I did harden transform and finally exported the DICOM. When I open this new AC-PC aligned DICOM in Slicer then it comes fine and perfectly aligned but when I open this same DICOM in some other software like Amira/Avizo, it is not aligned.<br>
Please suggest me where I am doing wrong?</p>

---

## Post #2 by @pieper (2019-07-17 12:59 UTC)

<p>Maybe Amira/Avizo is showing you the images in pixel space and ignoring the orientation.  You probably need to resample the images in slicer before exporting (e.g. with Resample Image (BRAINS)).</p>

---

## Post #3 by @Sachal (2019-07-17 13:08 UTC)

<p>If I do resample Image (BRAINS), what should be my “Reference Image” because after AC-PC alignment, I have only one DICOM dataset?</p>

---

## Post #4 by @Sachal (2019-07-17 14:56 UTC)

<p>Problem Solved:<br>
Use Resample Image (BRAINS) module<br>
Reference Image: Actual image before AC-PC alignment<br>
Pixel Type: Int<br>
Interpolation Mode: Lanczos</p>
<p>Thank you Pieper…</p>

---
