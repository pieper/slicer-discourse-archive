---
topic_id: 3861
title: "Segmentation For Swine Brain Mri"
date: 2018-08-21
url: https://discourse.slicer.org/t/3861
---

# Segmentation for swine brain MRI

**Topic ID**: 3861
**Date**: 2018-08-21
**URL**: https://discourse.slicer.org/t/segmentation-for-swine-brain-mri/3861

---

## Post #1 by @uchen9 (2018-08-21 19:57 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1</p>
<p>Hello,<br>
I require a segmentation of part of a swine brain and I have an atlas to use; however the EMSegmenter with Atlas does not allow for the swine atlas to be selected as the “task”. I am very new to segmentation- is there another module I can use to segment a volume using my Atlas or is there some way to upload my atlas as the task?</p>

---

## Post #2 by @lassoan (2018-08-21 21:05 UTC)

<p>If you have a single pair of grayscale image + segmentation as atlas, then you can use image registration to warp the atlas to the new case:</p>
<ul>
<li>install Elastix extension</li>
<li>register grayscale volumes using “General registration (Elastix)” module (atlas grayscale volume is moving, new case grayscale volume is fixed volume; choose to save the computed transform)</li>
<li>apply the computed transform to the atlas segmentation to warp it to the new case</li>
</ul>

---

## Post #3 by @uchen9 (2018-08-22 15:19 UTC)

<p>Thank you, I will try this out. However, I also have another question- what is the best method/a good tutorial for segmenting the atlas in the first place? I have been trying to use the paint tool in Segment Editor but what I am painting is not showing on the atlas or creating an output volume.</p>

---

## Post #4 by @lassoan (2018-08-22 15:21 UTC)

<p>This is a good starting point for learning segmentation: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---
