---
topic_id: 15581
title: "How To Make The Segmentation"
date: 2021-01-18
url: https://discourse.slicer.org/t/15581
---

# How to make the segmentation

**Topic ID**: 15581
**Date**: 2021-01-18
**URL**: https://discourse.slicer.org/t/how-to-make-the-segmentation/15581

---

## Post #1 by @Aleja_Ichina (2021-01-18 17:42 UTC)

<p>Hi, I have a question.<br>
How can I make the segmentation of my images? Has PyRadiomics this function?<br>
I don’t have idea please help me</p>

---

## Post #2 by @lassoan (2021-01-18 17:43 UTC)

<p>This page should help: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#basic-concepts" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>

---

## Post #3 by @Aleja_Ichina (2021-01-18 18:11 UTC)

<p>Thank you.</p>
<p>I have another question. Could you help me?<br>
Do I need to make the segmentation before apply pyradiomics? and this segmentation is the mask or what is the mask?</p>

---

## Post #4 by @JoostJM (2021-03-09 12:41 UTC)

<p>The segmentation is indeed the mask in PyRadiomics, and yes it is required. It tells PyRadiomics what the region of interest in your image is. Otherwise the texture would reflect the entire image and any signal would most likely be lost in the noise.</p>

---
