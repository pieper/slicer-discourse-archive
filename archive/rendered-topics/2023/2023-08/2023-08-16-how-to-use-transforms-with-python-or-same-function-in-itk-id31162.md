---
topic_id: 31162
title: "How To Use Transforms With Python Or Same Function In Itk"
date: 2023-08-16
url: https://discourse.slicer.org/t/31162
---

# How to use Transforms with python or same function in itk

**Topic ID**: 31162
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/how-to-use-transforms-with-python-or-same-function-in-itk/31162

---

## Post #1 by @Xinyue (2023-08-16 06:09 UTC)

<p>Hi,</p>
<p>I am working  on a image registration task, and currently, I try to split a deformation vector field into two dvfs so I could move the image two times.</p>
<p>dvf = dvf1+dvf2, dvf1 is a dvf which move all voxels in an image to same direction and same distance, which works like a “rigid registration”, to move the organ in the moving image to the same location as the fixed image. I used ITK resamplefilter to apply the dvfs, but it seems resamplefilter has some computational loss so the edge of the deformed image looks different as my expectation, I tried with 3dslicer GUI, and the result looks exactly what I want.</p>
<p>I am wondering if there is any documentation about Transforms module that I could read to learn more about Tranforms, and it would be great if there are any sample code to use Transforms model in python. After some reading, it seems like I cannot simply install Slicer as a package and import it in python, may I ask if this is still the case?</p>
<p>Thank you,<br>
Xinyue</p>

---
