---
topic_id: 37056
title: "How To Perfectly Align Two Stl Files From Segmentation For D"
date: 2024-06-26
url: https://discourse.slicer.org/t/37056
---

# How to Perfectly Align Two STL Files from Segmentation for Dual Extrusion 3D Printing ?

**Topic ID**: 37056
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/how-to-perfectly-align-two-stl-files-from-segmentation-for-dual-extrusion-3d-printing/37056

---

## Post #1 by @kiki98 (2024-06-26 20:36 UTC)

<p>Hello!</p>
<p>I segmented breast MRI images with 3D Slicer into two components: one including skin and fibroglandular tissues connected to the nipple, and the other consisting of the adipose tissue. I created the adipose component by subtracting the skin and gland tissue from the total breast. Thus, the two segmentations perfectly overlap to recreate the entire breast. I then exported these two segmentations as STL files to 3D print a breast phantom for my thesis project using a dual extruder 3D printer, which prints each component simultaneously using different filaments.</p>
<p>However, I’m having trouble aligning the two STL files perfectly. Is there a way to do this in 3D Slicer, or do you have any other method to suggest? All the slicer software I’ve tried so far only allows for manual movement of the STL files, and I can’t align them as precisely as in the original segmentation.</p>
<p>Thank you!</p>

---

## Post #2 by @Mark_Ryan (2024-06-29 21:42 UTC)

<p>Sounds like it needs to be done in whatever slicer you are using for printing. Normally can export each as STL and use the “center” command to localize them both on the plate.</p>

---
