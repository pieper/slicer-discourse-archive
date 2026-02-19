---
topic_id: 1854
title: "How To Get Same Voxel Values In Matlab As In Slicer"
date: 2018-01-15
url: https://discourse.slicer.org/t/1854
---

# How to get same voxel values in Matlab as in Slicer

**Topic ID**: 1854
**Date**: 2018-01-15
**URL**: https://discourse.slicer.org/t/how-to-get-same-voxel-values-in-matlab-as-in-slicer/1854

---

## Post #1 by @Kamil (2018-01-15 21:20 UTC)

<p>Thanks a lot. It works now. I should have read about it.</p>
<p>Just as I am writing here…somebody can me explain why the intensity in the slicer 3D is different than for example in Matlab? Where I can read about it? Thank!</p>

---

## Post #2 by @lassoan (2018-01-15 22:38 UTC)

<p>Voxel value depends on imaging modality. For example, in CT voxel values are in Hounsfield unit.</p>
<p>Have you tried Segment Editor? With that you won’t need things like manual model making.</p>
<p>Do you run your Matlab functions using MatlabBridge? If yes, then Slicer takes care of image scaling, such as converting to Hounsfield unit; and has many other advantages.</p>

---

## Post #3 by @Kamil (2018-01-16 08:28 UTC)

<p>I am writing a program which is apart from 3D slicer. Just I was wondering why it is difference. For example the gray level intensity in Matlab is between 0-32767 for the voxel while 3D slicer shows me -8604.1 to 24163. Does it actually connected to the RescaleIntercept value which seems to be the same as minimum value which shows 3D slicer -8.6041e+03?</p>

---

## Post #4 by @lassoan (2018-01-16 12:39 UTC)

<p>It seems that Matlab you get the stored value of the voxel, not the actual physical value. To compute the physical value, you need to apply linear scaling (defined by rescale intercept and slope fields) or modality LUT transformation. For display, you need to apply additional transformation (either linear scaling by window width/center, or arbitrary transformation defined by VOI LUT). Additional transforms may be defined by photometric interpretation or presentation LUT.</p>
<p>See exact specification in the <a href="http://www.dicomstandard.org/">DICOM standard</a>. Slicer can use GDCM or DCMTK libraries for image loading, which implement the intensity scaling. Some information about scaling can be found on <a href="http://gdcm.sourceforge.net/wiki/index.php/Modality_LUT">GDCM website</a>.</p>

---

## Post #5 by @Kamil (2018-01-16 12:51 UTC)

<p>Yes, I found something similar. Thanks!</p>
<p><a href="https://stackoverflow.com/questions/8756096/window-width-and-center-calculation-of-dicom-image/8765366#8765366" rel="nofollow noopener">Matlab</a></p>

---
