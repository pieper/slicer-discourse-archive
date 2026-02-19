---
topic_id: 32460
title: "Accuracy Evaluation"
date: 2023-10-29
url: https://discourse.slicer.org/t/32460
---

# Accuracy evaluation

**Topic ID**: 32460
**Date**: 2023-10-29
**URL**: https://discourse.slicer.org/t/accuracy-evaluation/32460

---

## Post #1 by @Caterina (2023-10-29 18:53 UTC)

<p>Dear support,<br>
I would like to know if there is a way to evaluate the accuracy of segmentation. I mean that I need a quantitative measure of how accurate the segmentation is.<br>
Thanks</p>

---

## Post #2 by @pieper (2023-10-29 19:25 UTC)

<p>That entirely depends on what you are trying to measure and what kind of images you use to do the measurements.  As a general rule, you would make a ground truth measurement of something like a phantom and compare it to what you can measure from images.</p>

---

## Post #3 by @Caterina (2023-10-29 19:50 UTC)

<p>Thanks for reply. In case of CT or rm dicom images and of anatomical regions segmentation, which is the best way to evaluate how accurate the segmentation is compared to real organs?</p>

---

## Post #4 by @vet0282 (2023-10-29 20:09 UTC)

<p>We have done some work on the accuracy of segmentation and 3D-printed<br>
replicas of bones.</p>
<p>Tow most common ways are</p>
<ol>
<li>To directly measure geometry and compare distances between multiple<br>
points or landmarks.</li>
<li>To compare a segmented model derived from CT with a 3D surface scan of<br>
the model. So, this can be done in cadavers or dry bones.</li>
</ol>

---

## Post #5 by @Caterina (2023-10-31 12:55 UTC)

<p>Thanks for reply. Can you please share with me the the work on the accuracy of segmentation and 3D-printed replicas of bones?<br>
Thanks</p>

---
