---
topic_id: 1064
title: "A Single 3Dra Dicom Image"
date: 2017-09-16
url: https://discourse.slicer.org/t/1064
---

# A single 3DRA DICOM image

**Topic ID**: 1064
**Date**: 2017-09-16
**URL**: https://discourse.slicer.org/t/a-single-3dra-dicom-image/1064

---

## Post #1 by @hamedtopic (2017-09-16 00:35 UTC)

<p>Hi everybody,</p>
<p>One of my colleagues sent me a single 3DRA DICOM image.<br>
Is there anyway to extract an STL output of the aneurysm from this single image which is 3d itself?!</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-09-16 00:39 UTC)

<p>Yes, this is a very common task. You can segment the image using Segment Editor module then export the segmentation to a model node (that can be saved as STL). Use the latest nightly version of Slicer.</p>

---
