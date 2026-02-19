---
topic_id: 2957
title: "Viewing Image Data Eg Slice Number Sequence Parameters"
date: 2018-05-29
url: https://discourse.slicer.org/t/2957
---

# Viewing image data eg: slice number,sequence parameters

**Topic ID**: 2957
**Date**: 2018-05-29
**URL**: https://discourse.slicer.org/t/viewing-image-data-eg-slice-number-sequence-parameters/2957

---

## Post #1 by @Ash_Alarfaj (2018-05-29 12:50 UTC)

<p>Hi<br>
I don’t know if I can see slice number and other MRI image parameters on the viewer ?<br>
thanks</p>

---

## Post #2 by @lassoan (2018-05-29 13:33 UTC)

<p>Data probe window in the lower-right corner shows anatomical coordinates in millimeters (left/right, anterior/posterior, inferior/superior) and voxel coordinates (0-based slice index along image each image axis).</p>
<p>DICOM slice number is 1-based and most often slices are axially oriented, so usually you can get the DICOM slice number by adding 1 to the third voxel coordinate.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b789d9768cd8035a14032544ef5ac32cf7d52677.png" alt="image" data-base62-sha1="qbEIwNmUpgjV2BCu5IBGb2k1ySz" width="580" height="253"></p>

---

## Post #3 by @Ash_Alarfaj (2018-06-08 11:50 UTC)

<p>Hi thank you I got it, I have to move the mouse with scroll to get the slice number and yes it start from zero</p>

---
