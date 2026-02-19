---
topic_id: 7213
title: "What Is Different Hu And Voxel Value"
date: 2019-06-18
url: https://discourse.slicer.org/t/7213
---

# What is different HU and voxel value

**Topic ID**: 7213
**Date**: 2019-06-18
**URL**: https://discourse.slicer.org/t/what-is-different-hu-and-voxel-value/7213

---

## Post #1 by @kscript (2019-06-18 02:36 UTC)

<p>HI.</p>
<p><strong>1.</strong> I open dicom file’s header using 3D Slicer. i can get LargestImagePixelValue and smallestImagePixelValue.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bd9f5d5363cd879e9c3c319b08c8be6d2e98325.png" alt="image" data-base62-sha1="3YnRUceG9MWoTQnULq0K8yZDwON" width="689" height="33"></p>
<p><strong>2.</strong> And I check Volumes’ Histogram using 3D Slicer. and I check HU(HounsField Unit) Range.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d1027dbce7c16cbabd3d3a063e65aba98ff054d.png" alt="image" data-base62-sha1="aZJntwgdxmVzRjizCs0yl81ICjH" width="570" height="192"></p>
<p>but Two results are different.<br>
pixel value range(first works result) is 0~4095. but HU(HounsField Unit) Range(Second works result) is -1410~3505</p>
<p>So I’m curious. Why Results are different.<br>
Can i convert HU to pixel value??</p>

---

## Post #2 by @lassoan (2019-06-18 03:17 UTC)

<p>Rescale slope and intercept values are used to compute displayed values (in HU) from raw pixel values.</p>

---
