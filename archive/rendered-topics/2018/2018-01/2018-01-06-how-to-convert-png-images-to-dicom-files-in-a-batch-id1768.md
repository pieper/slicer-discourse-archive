---
topic_id: 1768
title: "How To Convert Png Images To Dicom Files In A Batch"
date: 2018-01-06
url: https://discourse.slicer.org/t/1768
---

# How to convert .png images to DICOM files in a batch

**Topic ID**: 1768
**Date**: 2018-01-06
**URL**: https://discourse.slicer.org/t/how-to-convert-png-images-to-dicom-files-in-a-batch/1768

---

## Post #1 by @timeanddoctor (2018-01-06 00:38 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
I have a CTA with png format. Can we convert png images to DICOM files in a batch?<br>
Thanks</p>

---

## Post #2 by @lassoan (2018-01-06 06:33 UTC)

<p>You can certainly do this with Slicer, but this should not be needed. Can you tell a bit more about your workflow?</p>
<p>Normally you don’t get medical images in png format. In png files you don’t have any metadata and if your CT images have only 8 bits per pixel (256 gray levels) then they may be unusable for clinical purposes.</p>
<p>Where these png files come from?</p>

---

## Post #3 by @timeanddoctor (2018-01-06 06:54 UTC)

<p>Thank you very much!<br>
I agree with you DICOM is the best format choise. But I got some pictures from my friend who are not a doctor, and I need convert these png files to DICOMs and then analysis. So can you give a tutorial to deal with it.<br>
Thanks!</p>

---

## Post #4 by @timeanddoctor (2018-01-06 07:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>get medical images in png format. In png files you don’t have any metadata and if your CT images have only 8 bits per pixel (256 gray levels) then they may be unusable for clinical purposes.</p>
<p>Where these png files come from</p>
</blockquote>
</aside>
<p>My friend photographed a group of sliced tissue cells through an electron microscope and hope me could hep rebuild a 3D picture.</p>

---

## Post #5 by @lassoan (2018-01-06 15:11 UTC)

<p>OK, when the images are not from a DICOM-capable device then importing from png makes sense.</p>
<p>I don’t think Slicer can easily export color images to DICOM. If you convert to grayscale using “Vector to scalar volume” module then you can export the volume to DICOM. Or, you can probably do it with pydicom and some Python scripting.</p>
<p>Instead of exporting, you may try perform all visualization and analysis in Slicer. Or, if you need limited 3D analysis then you may use ImageJ or other microscopy-oriented software.</p>

---
