---
topic_id: 10827
title: "Threshold Segmentation Tool"
date: 2020-03-25
url: https://discourse.slicer.org/t/10827
---

# Threshold segmentation tool

**Topic ID**: 10827
**Date**: 2020-03-25
**URL**: https://discourse.slicer.org/t/threshold-segmentation-tool/10827

---

## Post #1 by @gbolaga (2020-03-25 10:45 UTC)

<p>Hello,<br>
I am using the segmentation tool in order to segment calcium from other structures within png IVUS frames. I created a 3D model and I am able to use thresholding. The problem is that there are no measure units.</p>
<p>What type of units does Slicer use for thresholding?</p>
<p>Thanks in advance, i would like to know if they are HU or other type of units</p>

---

## Post #2 by @lassoan (2020-03-25 12:43 UTC)

<p>Most medical images have no standardized units. There are exceptions - CT voxel values are defined in Hounsfield unit, you can obtain standardized values from PET, and there are special quantitative MRI protocols. However, ultrasound image pixels typically do not represent any absolute physical quantity, since you typically free to adjust gain and dynamic range, and even set different values in different image regions.</p>
<p>To make ultrasound image intensity somewhat standardized, you would need to use the same imaging settings a cross all patients and/or apply generic image equalization methods (histogram equalization, etc. - available in ITK toolkit, via Simple Filters library). If you post your question to the <a href="https://discourse.itk.org">ITK forum</a> along with example screenshots and explain what you would like to achieve then you may get recommendations for specific filters to use.</p>

---
