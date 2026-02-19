---
topic_id: 31614
title: "Combining Different Files Of Dicom Images Into One File To D"
date: 2023-09-08
url: https://discourse.slicer.org/t/31614
---

# Combining different files of DICOM images into one file to do a segmentation

**Topic ID**: 31614
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/combining-different-files-of-dicom-images-into-one-file-to-do-a-segmentation/31614

---

## Post #1 by @darsh (2023-09-08 05:06 UTC)

<p>OS: Windows 10<br>
Slicer Version: 5.4.0</p>
<p>Hi y’all!</p>
<p>I’m trying to start a segmentation of the pulmonary arteries using MR images. I was able to load my dcm files into Slicer, but I can’t segment them since the files are separated into 9 different series. Each series is only giving me one or two images in one view, which isn’t enough to create a segmentation. Is there a way to combine all the different series into 1 nrrd so I can create 1 volume from 1 segmentation?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-09-08 13:29 UTC)

<p>It seems that the heuristics that determines how to group frames determined that splitting the series into multiple pieces was the most preferable interpretation. However, you can choose a different interpretation by enabling the “Advanced” option in the DICOM module and check the checkbox of the one you prefer. If you are not sure which one to choose, you can select all of them and then see which one works the best for you.</p>

---
