---
topic_id: 11246
title: "Can Slicer Be Used To Segment Radially Orientated Dicom Imag"
date: 2020-04-22
url: https://discourse.slicer.org/t/11246
---

# Can slicer be used to segment radially orientated DICOM images?

**Topic ID**: 11246
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/can-slicer-be-used-to-segment-radially-orientated-dicom-images/11246

---

## Post #1 by @Jiang_Yao (2020-04-22 11:22 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.10.2 r28257<br>
Expected behavior:  I have a set of dicom images that are rotating radially with 10 degrees apart, totally 18 slices for left ventricle in the heart.<br>
Actual behavior: I imported the DICOM data in slicer, but instead of getting a volume of image, I got individual image. I can’t use it for segmentation. Is there a way to get around it?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-04-22 13:20 UTC)

<p>You can either reconstruct a volume from slices using SlicerIGSIO extension or place markup points in each slice and use “Markups to model” to reconstruct a surface.</p>
<p>To give you more specific instructions, we would need some more information. Is it a TEE image? What would you like to segment? Can you post a screenshot of how the image appears in Slicer? Can you upload a scan of a phantom (or anonymized) data set somewhere and post the link here?</p>

---
