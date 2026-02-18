# Saving to one dicom file, not in image sequence

**Topic ID**: 9803
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/saving-to-one-dicom-file-not-in-image-sequence/9803

---

## Post #1 by @Niels (2020-01-14 08:28 UTC)

<p>Sometimes I obtain dicom scans containing multiple slices in one dcm large file instead of multiple image files. Can slicer also export a volume to a single dcm file? I searched the forum on this but I cannot get a clear answer to this question.</p>

---

## Post #2 by @pieper (2020-01-14 14:50 UTC)

<p>Hi -</p>
<p>Are you referring to <a href="https://www.dicomstandard.org/wp-content/uploads/2018/10/Day1_S9-Solomon-Multiframe.pdf">multiframe</a> instances?  The latest preview builds should be able to read and display them, but we don’t have a way to generate them right now.  We do have work in progress for converters, and once those exist we should add the export functionality.  No particular timeline, but if you have a particular need any contributions would be welcome.</p>

---

## Post #3 by @Niels (2020-01-24 09:24 UTC)

<p>Hi Steve,<br>
Thanks for the referring link, this was indeed the file format I meant. Reading them works fine, for saving I found a work around by saving them to a different file format that does packs all slices together.</p>

---
