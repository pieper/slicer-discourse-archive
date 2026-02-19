---
topic_id: 43722
title: "Roi Of 3 Stl Files"
date: 2025-07-15
url: https://discourse.slicer.org/t/43722
---

# ROI of 3 stl files

**Topic ID**: 43722
**Date**: 2025-07-15
**URL**: https://discourse.slicer.org/t/roi-of-3-stl-files/43722

---

## Post #1 by @PLET (2025-07-15 04:26 UTC)

<p>I have 3 .stl files of a forearm segment (muscle, skin, bone). I want to use 3D Slicer to crop a specific section, but I can only do it with one layer. I don’t know how to crop all three layers together at the same time. As a new user of 3D Slicer, do you have any suggestions for me?</p>

---

## Post #2 by @muratmaga (2025-07-15 05:09 UTC)

<p>I presume you are using the Dynamic Modeler to crop these STLs? If so, just change your input model to the next object and crop it again. Make sure to output to a new model, so that don’t overwrite the previous output.</p>

---

## Post #3 by @PLET (2025-07-15 10:59 UTC)

<p>Thank you for your response. I didn’t use the Dynamic Modeler; instead, I converted the STL files to segmentation and then used volume rendering to crop the volume. However, I was only able to crop each layer separately. Did I do something wrong? I also tried using the Dynamic Modeler as you suggested, but it didn’t work for me.</p>

---

## Post #4 by @muratmaga (2025-07-15 14:55 UTC)

<p>If you turned them into segmentation, then simply copy every segment into the same segmentation, and you should be able crop all three at once.</p>

---
