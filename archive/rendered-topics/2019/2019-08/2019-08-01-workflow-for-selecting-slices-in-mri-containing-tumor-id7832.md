---
topic_id: 7832
title: "Workflow For Selecting Slices In Mri Containing Tumor"
date: 2019-08-01
url: https://discourse.slicer.org/t/7832
---

# Workflow for selecting slices in MRI containing tumor

**Topic ID**: 7832
**Date**: 2019-08-01
**URL**: https://discourse.slicer.org/t/workflow-for-selecting-slices-in-mri-containing-tumor/7832

---

## Post #1 by @bit2002 (2019-08-01 03:50 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.10</p>
<p>I’m a true imaging newbie here. I have roughly 260 patients with MRIs of brain tumors. I’m trying to obtain high quality jpeg files of 3 slices containing the largest amount of tumor. Since this is obviously, quite a bit of work. What is the most efficient way for me to do this?</p>
<p>My current worfklow is loading all the patients scans at once in the import DICOM. and then using the screencapture module to find the slice containing the largest section and use the screencapture to screenshot the 3 slices (1 above it and 1 below it too). Is there a more efficient way of doing this? Perhaps segment the tumor out from each one first and then use some built in functions to choose largest slice?</p>
<p>Any help would be appreciated! Thank you!</p>

---

## Post #2 by @rkikinis (2019-08-01 11:07 UTC)

<p>Hi,<br>
use the Four up layout to get three orthogonal views at once, use shift hover to position all three orthogonal views to your liking, use the scale factor option on the screen capture pop-up of Slicer to get to the resolution that you want. Change the screen capture file name to something that will let you keep track of your patients.<br>
Good luck<br>
Ron</p>

---
