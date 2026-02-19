---
topic_id: 36518
title: "Load Segmentation With Surfacenet Smoothing"
date: 2024-05-31
url: https://discourse.slicer.org/t/36518
---

# Load segmentation with surfacenet smoothing

**Topic ID**: 36518
**Date**: 2024-05-31
**URL**: https://discourse.slicer.org/t/load-segmentation-with-surfacenet-smoothing/36518

---

## Post #1 by @Djanbo (2024-05-31 10:01 UTC)

<p>Hi, i am new, can we load the segmentation surface net smoothed directly progamatically ? I think i have to modify the header of each .seg.nrrd file before loading? (If yes how we modify the particular key for that i think it’s <code>['Segmentation_ConversionParameters']</code><br>
The goal is to reduce the loading time of the sample, i mean when creating the closed surface representation.</p>
<p>Thanks in advance and have a good day !</p>

---

## Post #2 by @lassoan (2024-05-31 15:36 UTC)

<p>Slicer will use the binary labelmap to closed surface conversion algorithm that is specified in the conversion parameters in the .seg.nrrd file header. You can conveniently modify the header of a segmentation file using slicerio or pynrrd Python packages.</p>

---
