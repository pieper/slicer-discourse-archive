---
topic_id: 7410
title: "Changing Label Images"
date: 2019-07-04
url: https://discourse.slicer.org/t/7410
---

# Changing label images

**Topic ID**: 7410
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/changing-label-images/7410

---

## Post #1 by @pouyahoseini (2019-07-04 12:38 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Hi.I have some images with mistake label.for example sagital image that have coronal label.how i can the change this labels to correct form?</p>

---

## Post #2 by @lassoan (2019-07-04 17:30 UTC)

<p>Load the labelmap, convert to segmentation in Data module (right-click the labelmap volume and choose to convert to segmentation), and use Segment Editor to fix the segmentation. When you finished your corrections, you may convert the segmentation to labelmap volume using Data module (right-click on segmentation node and choose to export to labelmap).</p>

---
