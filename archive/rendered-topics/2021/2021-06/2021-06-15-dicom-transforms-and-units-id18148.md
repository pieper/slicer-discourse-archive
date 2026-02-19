---
topic_id: 18148
title: "Dicom Transforms And Units"
date: 2021-06-15
url: https://discourse.slicer.org/t/18148
---

# DICOM transforms and units

**Topic ID**: 18148
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/dicom-transforms-and-units/18148

---

## Post #1 by @Kaya_Zelazny (2021-06-15 17:23 UTC)

<p>Hello -</p>
<p>I’m new to 3D slicer, and trying to use the transforms module to extract cross-sections of a bone from a DICOM image stack. The original CT was not in the correct orientation for the bone I am looking at, so I segmented the bone out, oriented it correctly to calculate a linear transform (translation and rotation, no scaling), and then applied that transform to the DICOM images. However, now that I am taking measurements (areas of closed curves) on the transformed images, I’m getting unexpectedly large values. Is it possible that the transform or some other part of this procedure has changed the units somehow?</p>

---

## Post #2 by @lassoan (2021-06-15 19:07 UTC)

<p>Translations/rotations should not affect size measurements. Do you see different results if you measure on the original CT?</p>
<p>If the CT image is acquired by a clinical system then the size scale should be good. However, pre-clinical/industrial/research systems often don’t implement the DICOM standard correctly and scale may be incorrect as a result. The image may get corrupted due to incorrect anonymization, too. Can you share the data set? (make sure it contains no patient information)</p>

---
