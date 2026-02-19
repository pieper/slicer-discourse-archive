---
topic_id: 14691
title: "Realign Ct Along The Femurs Centerline"
date: 2020-11-19
url: https://discourse.slicer.org/t/14691
---

# Realign CT along the femur's centerline

**Topic ID**: 14691
**Date**: 2020-11-19
**URL**: https://discourse.slicer.org/t/realign-ct-along-the-femurs-centerline/14691

---

## Post #1 by @BobbyZhang26 (2020-11-19 16:14 UTC)

<p>Hi, I have a sequence of CT scans of a patient’s femur. The original scans are aligned with conventional axial axis. I wish to realign the CT scan along the femur’s centerline which is a curve from condyles to the center of femur head. I do not know how to do it, please can you offer some advise ? Thanks!</p>

---

## Post #2 by @mau_igna_06 (2023-03-21 13:27 UTC)

<p>I think you could create a femur segmentation with the segment editor module. Then export a 3D model and then use vmtk extract centerline module from vmtk extension (maybe you’ll need also to smooth the curve you get to clean some noise)</p>

---
