---
topic_id: 4800
title: "Create A New Axial Dicom Series 8Bit Rgb With All The Segmen"
date: 2018-11-19
url: https://discourse.slicer.org/t/4800
---

# Create a new axial dicom series (8bit RGB) with all the segmentations (or labelmaps) displayed in the Red Slices burned in

**Topic ID**: 4800
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/create-a-new-axial-dicom-series-8bit-rgb-with-all-the-segmentations-or-labelmaps-displayed-in-the-red-slices-burned-in/4800

---

## Post #1 by @Michele_Bailo (2018-11-19 13:07 UTC)

<p>Hi there,<br>
I need to create a new axial dicom series (8bit RGB) with all the segmentations (or labelmaps) displayed in the Red Slices “burned in” in a single layer.<br>
I need it to be able to send to the local PACS a single volumetric exam with all the ROIs burned in as a part of the dicom series (tumor, fiber tracking, region activated with functional MRI).<br>
I’m able to do that with Osirix (with the function "Export to dicom files as displayed in 8-bit RGB with ROIs) but I’m not able to do that with Slicer.<br>
I only found the function to export it as a series of png images/videos or DICOM RT files (which unfortunately cannot be displayed in normal DICOM viewer)</p>
<p>thank you very much for your help</p>
<p>Mic</p>
<p>Operating system: Mac<br>
Slicer version: 4.10.0</p>

---

## Post #2 by @pieper (2018-11-19 14:24 UTC)

<p>Hi <a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> -</p>
<p>There’s no GUI that does that exactly, but with the ScreenCapture module you can get a series of png files and then use img2dcm to make secondary capture images (on a mac you can get dcmtk via homebrew).</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/ScreenCapture" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Modules/ScreenCapture</a></p>
<p><a href="https://support.dcmtk.org/docs/img2dcm.html" class="onebox" target="_blank">https://support.dcmtk.org/docs/img2dcm.html</a></p>

---
