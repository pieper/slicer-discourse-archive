---
topic_id: 29268
title: "Dicom Image Orientation Incorrect When Imageorientationpatie"
date: 2023-05-03
url: https://discourse.slicer.org/t/29268
---

# Dicom image orientation incorrect when imageorientationpatient is -1 0 0 0 -1 0

**Topic ID**: 29268
**Date**: 2023-05-03
**URL**: https://discourse.slicer.org/t/dicom-image-orientation-incorrect-when-imageorientationpatient-is-1-0-0-0-1-0/29268

---

## Post #1 by @Megan (2023-05-03 14:26 UTC)

<p>At the minute, slicer appears to load the dicom pixel data in the incorrect orientation when the dicom field,  ‘imageorientationpatient’ is -1 0 0 0 -1 0. See screenshot below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f24bab1a3ae7ee5890686b291395cf92205d1466.png" alt="dicom_orientation_fail" data-base62-sha1="yzrFkl2UMGB3mSiDbkfeFALWIZg" width="582" height="433"></p>

---

## Post #2 by @pieper (2023-05-03 15:23 UTC)

<p>Not clear to me what you are referring too.  Please refer to this material and come back with more info why you think the loaded image is incorrect.</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @Megan (2023-05-03 15:32 UTC)

<p>According to slicer as seen in the image, the right hip is the left hip and vice versa.</p>

---

## Post #4 by @pieper (2023-05-03 15:39 UTC)

<p>it’s entirely possible there’s a special case that Slicer doesn’t handle, but it heavily tested so it’s more likely there’s something wrong with your data, but we’ll only know if you provide more details, and ideally a dataset that demonstrates the issues you are seeing.</p>

---
