---
topic_id: 4088
title: "How To Convert To Stl From Nii"
date: 2018-09-12
url: https://discourse.slicer.org/t/4088
---

# How to convert to .stl from .nii

**Topic ID**: 4088
**Date**: 2018-09-12
**URL**: https://discourse.slicer.org/t/how-to-convert-to-stl-from-nii/4088

---

## Post #1 by @xwang2 (2018-09-12 17:11 UTC)

<p>Hi everyone,</p>
<p>I want to convert this .nii file directly into .stl file which can be used by Netgen, how can I do it without any segmentation in 3DSlicer? Because this file .nii was already a segmentation from itksnap.</p>
<p>The link of this file .nii:<br>
<a href="https://drive.google.com/open?id=1IQ7_5ha_MisHcfpndhLi_KlV33S1k0pp" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1IQ7_5ha_MisHcfpndhLi_KlV33S1k0pp</a></p>
<p>Thank you.</p>
<p>Xiaoyu.</p>

---

## Post #2 by @pieper (2018-09-17 14:27 UTC)

<p>Yes, this file can easily be converted to stl.  In the Add Data dialog, show the options and select the LabelMap.  Then in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations">Segmentations</a> module, create a segmentation and then use the Import option at the bottom to import the labelmap as a segmentation.  Then click the Create button next to Close Surface representation.  Then you can use the Export section to save as STL…</p>

---

## Post #3 by @lassoan (2018-09-17 19:30 UTC)

<p>Note that you can save a few steps (and have a few useful additional options) if you use “Export to files” section (instead of clicking on Create button, exporting to model, and using scene Save).</p>
<p>The example file contains an invalid coordinate system (determinant of voxel-&gt;physical transform is negative, i.e., left-handed coordinate system), therefore the generated STL file will be turned inside out. If that is a problem for you, either fix orientation of the input volume or reverse the model using Surface toolbox module’s auto-orient normals feature.</p>

---

## Post #4 by @lassoan (2018-09-17 22:56 UTC)

<p>3 posts were split to a new topic: <a href="/t/how-to-handle-images-defined-in-left-handed-coordinate-system/4133">How to handle images defined in left-handed coordinate system</a></p>

---
