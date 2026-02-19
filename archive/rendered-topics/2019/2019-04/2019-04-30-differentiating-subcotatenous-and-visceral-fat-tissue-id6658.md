---
topic_id: 6658
title: "Differentiating Subcotatenous And Visceral Fat Tissue"
date: 2019-04-30
url: https://discourse.slicer.org/t/6658
---

# Differentiating Subcotatenous and Visceral Fat Tissue

**Topic ID**: 6658
**Date**: 2019-04-30
**URL**: https://discourse.slicer.org/t/differentiating-subcotatenous-and-visceral-fat-tissue/6658

---

## Post #1 by @dyasat (2019-04-30 17:00 UTC)

<p>Hello Everyone!<br>
I am trying to differentiate and measure the volumes of subcotaneous(SC) and visceral fat (V) from 3T T2 MRI images of mice, which are the white areas on this MRI image:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd8954ef9dd7328b44c49da8270956876cf30ef2.png" alt="image" data-base62-sha1="tkg720GSxc6ScG8OTQsdd1gWibM" width="137" height="295"><br>
FYI: SC is differentiated from V by its location: if it is inside Peritoneum (the membrane that surrounds the abdominal cavity-can be seen on the MRI image with the arrow on the image below):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d7079fb996e40c784dc1f63594e596573c682f1.png" alt="image" data-base62-sha1="dkBnQ8F5mm1xbSNCmNNDdWDgklr" width="137" height="295"><br>
it is V, and if its outside, its SC.<br>
I normally use Editor-&gt;ThresholdEffect to select all adipose tissue, then erase V to get the SC for each slice-and vice versa to get V. This takes a lot of time considering I have tons of images to analyze, so I was wondering if there is a method to split my selection, or if there is anyway I can write a Python code that would recognise Peritoneum and do the analyzing.<br>
Thank you!</p>

---

## Post #2 by @lassoan (2019-05-01 12:44 UTC)

<p>You can probably make the segmentation dramatically faster by using “Grow from seeds effect”. You can specify an intensity range that only contains adipose tissue, then paint seeds with two different segments in subcutaneous and visceral regions. The process is similar to how you can separate between bone and contrast agent (both appear with same image intensity) in vascular CT images, so you can follow <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/" rel="nofollow noopener">this segmentation recipe</a>.</p>
<p>To fully automate the process: If the images are sufficiently similar then you may be able to automate seed placement by registering an average patient image to the current image and apply the transform to the seeds defined on the average patient. After this, it may be enough to just review and adjust the seeds.</p>

---
