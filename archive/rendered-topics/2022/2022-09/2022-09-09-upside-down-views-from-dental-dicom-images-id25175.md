---
topic_id: 25175
title: "Upside Down Views From Dental Dicom Images"
date: 2022-09-09
url: https://discourse.slicer.org/t/25175
---

# Upside down views from Dental Dicom images

**Topic ID**: 25175
**Date**: 2022-09-09
**URL**: https://discourse.slicer.org/t/upside-down-views-from-dental-dicom-images/25175

---

## Post #1 by @Senn (2022-09-09 11:29 UTC)

<p>Hi Community,</p>
<p>I am having problems when loading up Dental DICOM images as the Sagittal and Coronal views are being loaded upside down. This does not occur when I open these DICOM images on other platforms.<br>
Has anyone else experienced this problem or know how to address it?</p>
<p>Thank you</p>
<p>Senn</p>

---

## Post #2 by @lassoan (2022-09-09 11:33 UTC)

<p>You need to load DICOM images using DICOM module.</p>
<p>If you use “Add data” then ITK reader is used, which may not load all images correctly. <a href="https://github.com/Slicer/Slicer/issues/5726">We plan to remove this option</a> but has not happened yet.</p>

---

## Post #3 by @Senn (2022-09-09 12:00 UTC)

<p>Hi Andras</p>
<p>Thank you for your reply and solution. It has solved all the problems.<br>
Thanks so much</p>
<p>Kindest Regards</p>
<p>Senn</p>

---
