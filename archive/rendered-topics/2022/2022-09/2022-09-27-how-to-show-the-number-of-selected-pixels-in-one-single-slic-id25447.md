---
topic_id: 25447
title: "How To Show The Number Of Selected Pixels In One Single Slic"
date: 2022-09-27
url: https://discourse.slicer.org/t/25447
---

# How to show the number of selected pixels in one single slice after apply the segmeation operation?

**Topic ID**: 25447
**Date**: 2022-09-27
**URL**: https://discourse.slicer.org/t/how-to-show-the-number-of-selected-pixels-in-one-single-slice-after-apply-the-segmeation-operation/25447

---

## Post #1 by @yiliberkeley (2022-09-27 14:26 UTC)

<p>Operating system: Windwons 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior: display the selected pixels in one single slice after segmentation operation<br>
Actual behavior: No data shows out.</p>
<p>Hi All,</p>
<p>I am a newbie in 3D slicer. I am currently learning how to process the sample DICOM data using the segmentation module. I wondered how I could get the number of selected pixels in each slice.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2022-09-28 04:16 UTC)

<p>You can get cross-section area of a segmentation for each slice using <code>Segment Cross-Section Area</code> in Sandbox extension, but I would recommend much more advanced modules for this, such as in <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">Segment Geometry</a> and <a href="https://github.com/vmtk/SlicerExtension-VMTK#the-vmtk-extension-for-3d-slicer">SlicerVMTK</a> extensions.</p>

---

## Post #3 by @muratmaga (2022-09-29 04:03 UTC)

<p><a class="mention" href="/u/yiliberkeley">@yiliberkeley</a><br>
Since you are a new user, please go ahead and switch to the latest stable, v5.0.3. The version you are using is over 1.5 years old, and no longer maintained. There are ton of bug fixed and new features that you will benefit.</p>

---

## Post #4 by @yiliberkeley (2022-10-03 13:34 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Great! Thank you so much for your reply. I will try these three modules for learning purposes.</p>

---

## Post #5 by @yiliberkeley (2022-10-03 13:37 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thanks for your suggestion. I will deploy the latest stable version of 3d Slicer on the workstation.</p>

---
