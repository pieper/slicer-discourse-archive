---
topic_id: 36041
title: "3D Rendering Of Tomosynthesis"
date: 2024-05-10
url: https://discourse.slicer.org/t/36041
---

# 3D Rendering of Tomosynthesis

**Topic ID**: 36041
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/3d-rendering-of-tomosynthesis/36041

---

## Post #1 by @bazaria (2024-05-10 05:05 UTC)

<p>Hi,<br>
I’m a newbie in using 3D Slicer, so maybe I am missing something obvious.<br>
I am trying to view breast tomosynthesis images that I got from TCIA, and though I can see the image in different planes, I cannot get it to show the 3D image.<br>
Maybe I’m doing something wrong, or maybe tomo dicom files are somehow structured differently.<br>
Would appreciate any advice on how to make it work.</p>

---

## Post #2 by @pieper (2024-05-10 11:23 UTC)

<p>I’ve only seen a few of those, but I know they have a very specific DICOM encoding that is different from other images.  A specific dicom plugin may be required to handle them (i.e. a python script that maps them to Slicer’s concept of a volume).</p>

---
