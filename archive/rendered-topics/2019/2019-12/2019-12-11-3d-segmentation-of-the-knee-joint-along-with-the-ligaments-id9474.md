---
topic_id: 9474
title: "3D Segmentation Of The Knee Joint Along With The Ligaments"
date: 2019-12-11
url: https://discourse.slicer.org/t/9474
---

# 3d segmentation of the knee joint along with the ligaments

**Topic ID**: 9474
**Date**: 2019-12-11
**URL**: https://discourse.slicer.org/t/3d-segmentation-of-the-knee-joint-along-with-the-ligaments/9474

---

## Post #1 by @nash (2019-12-11 17:12 UTC)

<p>I’m trying to generate a 3D model of the knee along with the ligaments with the help of MRI Dicom images.</p>
<p>I have been trying to do it for sometime now and I have tried other platforms which haven’t yielded desired results.</p>
<p>I was wondering if there is someone doing similar work and how effective the latest version of Slicer can be used to generate as accurate image as possible.</p>

---

## Post #2 by @lassoan (2019-12-11 17:18 UTC)

<p>Several groups are using Slicer for knee segmentation on MRI and can produce beautiful results. See segmentation tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>. I would recommend using “Grow from seeds” effect if there is visible contrast between structures. For structures where you need to rely on your anatomical knowledge to draw contours (because their intensity is very similar), you can segment 1 out of every 10-20 slices and generate contours between them automatically using “Fill between slices” effect (this is particularly useful in the superior and inferior regions where there is not variation between neighbor slices).</p>

---
