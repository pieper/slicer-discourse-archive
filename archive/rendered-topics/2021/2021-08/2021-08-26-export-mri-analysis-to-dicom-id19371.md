---
topic_id: 19371
title: "Export Mri Analysis To Dicom"
date: 2021-08-26
url: https://discourse.slicer.org/t/19371
---

# Export MRI analysis to DICOM

**Topic ID**: 19371
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/export-mri-analysis-to-dicom/19371

---

## Post #1 by @SogolSadeghi (2021-08-26 15:21 UTC)

<p>Operating system:windows, x64<br>
Slicer version:latest stable version<br>
Expected behavior: export MRI analysis map in colorful images<br>
Actual behavior: export MRI analysis map in gray scale<br>
Hi slicer,</p>
<p>using slicer, I converted JPEG MRI color maps  to dicom. I supposed to use these images in treatment planning system so  I need dicom format of color maps but the problem is when I export the images, the color maps change to gray scale . how can I export <strong>colourful</strong> MRI maps in dicom format.</p>

---

## Post #2 by @lassoan (2021-08-27 02:00 UTC)

<p>I don’t think you can export color images from Slicer. It would not be hard to implement it, but since color images are typically used for screenshots (secondary capture), which are not suitable for further analysis (most software cannot segment it, cannot quantify it, cannot visualize using volume rendering), there is no strong motivation to spend time with this.</p>
<p>Surgical plans are most often exported as segmentation objects or masked volumes (volume where some segmented regions are set to constant intensity value, which can be easily segmented in the treatment planning or surgical navigation software).</p>
<p>What software do you plan to import the color images into?<br>
How do you envision that software will use color images?</p>

---

## Post #3 by @SogolSadeghi (2021-08-27 11:41 UTC)

<p>Hi, thanks for the reply,<br>
I see, the software I want to import the color images into is Eclipse v.13.0 (Varian Medical System Inc, Palo Alto, CA, USA).</p>

---

## Post #4 by @lassoan (2021-08-27 22:19 UTC)

<p>Eclipse surely will ignore any colorful secondary captures that you export from any software, so you don’t need that.</p>
<p>However, Eclipse can probably import DICOM RT structure sets that you export from Slicer using SlicerRT extensiom.</p>
<p>If Eclipse can only import CTs, then you can use Mask volume effect in Segment Editor to create a fake CT that contains uniform intensity areas for segments. This CT will be trivial to segment in Eclipse.</p>

---
