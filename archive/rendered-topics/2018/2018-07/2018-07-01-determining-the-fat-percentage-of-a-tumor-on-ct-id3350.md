---
topic_id: 3350
title: "Determining The Fat Percentage Of A Tumor On Ct"
date: 2018-07-01
url: https://discourse.slicer.org/t/3350
---

# Determining the fat percentage of a tumor on CT? 

**Topic ID**: 3350
**Date**: 2018-07-01
**URL**: https://discourse.slicer.org/t/determining-the-fat-percentage-of-a-tumor-on-ct/3350

---

## Post #1 by @SMR (2018-07-01 12:15 UTC)

<p>I’m basically trying to quantity the fat percentage of tumors on CT, any suggestions on how to do this in 3D slicer would be very much appreciated.</p>

---

## Post #2 by @lassoan (2018-07-01 13:22 UTC)

<p>This kind of analysis is usually done by segmenting regions that you would like to quantify (tumor and fat), using Segment Editor module, then compute volumes using Segment Statistics module.</p>
<p>You may need to do some experimentation to find a good way of segmenting structures. These should help:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></li>
<li><a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></li>
</ul>

---
