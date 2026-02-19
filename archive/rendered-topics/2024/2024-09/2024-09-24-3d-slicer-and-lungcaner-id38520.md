---
topic_id: 38520
title: "3D Slicer And Lungcaner"
date: 2024-09-24
url: https://discourse.slicer.org/t/38520
---

# 3D Slicer and lungcaner

**Topic ID**: 38520
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/3d-slicer-and-lungcaner/38520

---

## Post #1 by @Chris3D (2024-09-24 15:24 UTC)

<p>Hello everyone,</p>
<p>i am new to 3d Slicer and am very excited after i am digging deeper into it.</p>
<p>And i have a question if there is already an extension for the following purpose:</p>
<p>I have often the problem, when i get new CT dvds from a radiologist that the images are hard to read for someone who is not a doctor. Especially when the findings are done from different doctors with different focus. Therefore the comparison of the NSCLC of a close person  are pretty hard.</p>
<p>But as i am good with computers my idea was:<br>
Is there a way (one or more extension to 3d Slicer) that can do the following</p>
<p>Analyse the CT data from Thorax and make proposal / highlights for nsclc cancer spots like round focus in the lung or metastasis at the  carina etc. as i have a big struggle to identify those spots and therefore have a problem with seeding etc there. i want to create a way to automatize this so that over time i can compare the volumetric differences in different CTs ( Add DICOM DATA, check the data for cancer suspicious spots, create segments, show segments with info like volume etc)</p>
<p>i found the lung ct extention for e.g. and i saw that there is a way to integrate ai  tools for the image classification etc. but i am at the very beginning of my research.</p>
<p>if there is already such a set of tool it would be great, if not i want to see if the way to a solution for this problem is possible.</p>
<p>thanks</p>
<p>chris</p>

---

## Post #2 by @Matteboo (2024-09-30 13:54 UTC)

<p>Totalsemgentator has a task that allows you to segment the blood vessel and cancer in the liver. However, the “cancer” segmentation often needs refinement, it could be a place to start.<br>
The issue is that you would need a lot of segmented data to train your model.</p>

---
