---
topic_id: 18485
title: "Help With Binary Labelmaps Of Reformatted Dicom"
date: 2021-07-02
url: https://discourse.slicer.org/t/18485
---

# Help with binary labelmaps of reformatted DICOM 

**Topic ID**: 18485
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/help-with-binary-labelmaps-of-reformatted-dicom/18485

---

## Post #1 by @DaZo (2021-07-02 15:15 UTC)

<p>Operating system: Win 10 Home<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi everyone!<br>
I have the following issue: I want to create a 2D segmentation on a single slice of reformatted CT DICOM images and export it to a binary labelmap. However, after saving the labelmap and opening it, it displays the segmentation with a “staircase” effect and not as a single 2D ROI.</p>
<p>Detailed approach:<br>
After loading the DICOM files, I use the “rotate to volume plane” function on the DICOM series, because otherwise the “level tracing” segmentation is displayed on more than one slice.<br>
After creating the segmentation (which looks fine when using the rotate to volume plane function) I export the visible segmentation to a binary labemap and save it as NifTI (nii.gz). However, after opening the labelmap file, the volume is displayed with a staircase effect (see attached screenshot) and not on a single slice, as the original segmentation. What am I doing wrong?</p>
<p>Thanks for the help!!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11c3510cb8176b7e92a9b11837d4a8abdfeed116.jpeg" alt="nifti labelmap" data-base62-sha1="2x8A0UTIsHSNDwJO133P8N4uQeO" width="642" height="472"></p>

---

## Post #2 by @lassoan (2021-07-08 17:29 UTC)

<p>This is the expected behavior - see detailed explanation <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html?highlight=oblique#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments">here</a>. Let us know if you have any remaining questions.</p>

---
