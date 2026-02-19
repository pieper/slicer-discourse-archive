---
topic_id: 21264
title: "Upload Of Multi Frame Dicom Images"
date: 2021-12-29
url: https://discourse.slicer.org/t/21264
---

# upload of multi-frame Dicom images

**Topic ID**: 21264
**Date**: 2021-12-29
**URL**: https://discourse.slicer.org/t/upload-of-multi-frame-dicom-images/21264

---

## Post #1 by @sebastianvoigt (2021-12-29 16:54 UTC)

<p>Operating system:Windows<br>
Slicer version: 4.11.2021<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi there,</p>
<p>I am uploading Dicom files. However, I get the following report: 1: Unnamed Series [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution. Is it possible to use this series ? Thank you for your reply!</p>

---

## Post #2 by @lassoan (2021-12-29 17:00 UTC)

<p>Yes, you can use it, but if you want to do physical size measurements then first verify that the image spacing is correct. For example, you can measure an object of known size with markups module and verify that displayed size matches the actual size.</p>

---
