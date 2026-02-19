---
topic_id: 17628
title: "Could Not Load The Dicom Data As A Scalar Volume"
date: 2021-05-15
url: https://discourse.slicer.org/t/17628
---

# Could not load the dicom data as a Scalar Volume

**Topic ID**: 17628
**Date**: 2021-05-15
**URL**: https://discourse.slicer.org/t/could-not-load-the-dicom-data-as-a-scalar-volume/17628

---

## Post #1 by @Matteo_Falanga (2021-05-15 14:20 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: loading dicom data<br>
Actual behavior: not loading</p>
<p>Hello everyone, i’m actually trying to load Echo 3D dicom data but it appears:<br>
“Could not load 0001: Unnamed Series as a Scalar Volume”.<br>
When i go in details it says:<br>
“0001: Unnamed Series [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.<br>
Reference image in series does not contain geometry information. Please use caution”.</p>
<p>Can you help me? Thanks!</p>

---

## Post #2 by @lassoan (2021-05-16 00:37 UTC)

<p>Storage of 3D/4D ultrasound is not standardized, each device uses its own custom file format. <a href="https://github.com/SlicerHeart/SlicerHeart#importing-dicom-files">SlicerHeart extension</a> can load many of them but not all.</p>

---
