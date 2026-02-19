---
topic_id: 15203
title: "Exporting Segmentation To Another Software"
date: 2020-12-23
url: https://discourse.slicer.org/t/15203
---

# Exporting segmentation to another software

**Topic ID**: 15203
**Date**: 2020-12-23
**URL**: https://discourse.slicer.org/t/exporting-segmentation-to-another-software/15203

---

## Post #1 by @FatihSogukpinar (2020-12-23 20:33 UTC)

<p>Hi all,</p>
<p>I am exporting a segmentation (as .seg.nrrd) from Slicer to Matlab using nrrdread function provided by Slicer Matlab Bridge. I realized that, when I plug in the coordinates of the reference MRI (specified as source geometry) I sometimes cannot replicate the segments as they are in Slicer. It is as if they are somewhat shifted or segmented, etc. It is not like the whole segmentation is read wrong in Matlab, because most of the coordinates are correct.</p>
<p>I just want to be able to replicate in Matlab what I am seeing in Slicer, so that when I plug in the coordinates of the MRI image I get the segment at that particular location.<br>
Everything else seems consistent (sizes of the segmentation, names, etc.)</p>
<p>Any ideas ? I tried a bunch of things, eg., exporting the segmentation in different ways, labelmap,.nii, . But all have the same problem.</p>
<p>Thanks !</p>

---

## Post #2 by @lassoan (2020-12-23 20:51 UTC)

<p>Previously, Slicer cropped the segmentation to the minimum necessary size on save. Current Slicer versions save the segmentation with the same extent as the first master volume, so voxel coordinates should match.</p>

---

## Post #3 by @FatihSogukpinar (2020-12-23 20:54 UTC)

<p>Yes, I observed this behavior by comparing versions 4.10 and 4.11.</p>
<p>But I am sure that this problem is present . Because I am manually plugging in the coordinates and observing the results.</p>
<p>Any suggestions ? (I am using 4.11)</p>

---

## Post #4 by @FatihSogukpinar (2020-12-24 00:55 UTC)

<p>Can I ask a very simple question, to make sure that I don’t misunderstand the basic steps :<br>
While saving the segmentation:<br>
I just save the segmentation node (.seg.nrrd ) file.<br>
And then read it to matlab with nrrdread<br>
And then plug in the coordinates of the source geometry MRI image.<br>
Is there anything which sounds wrong to you ?</p>
<p>Thank you so much.</p>

---
