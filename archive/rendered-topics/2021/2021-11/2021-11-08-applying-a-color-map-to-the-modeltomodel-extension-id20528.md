---
topic_id: 20528
title: "Applying A Color Map To The Modeltomodel Extension"
date: 2021-11-08
url: https://discourse.slicer.org/t/20528
---

# Applying a Color Map to the ModeltoModel extension

**Topic ID**: 20528
**Date**: 2021-11-08
**URL**: https://discourse.slicer.org/t/applying-a-color-map-to-the-modeltomodel-extension/20528

---

## Post #1 by @MathiasBrucker (2021-11-08 14:59 UTC)

<p>Ater applying the ModeltoModel distance exentsion on my two segments. I get the bone colored in the RedBlueGreen LUT. I know color red is close and blue is bigger distance but since there is no color scale bar shown there is no way to find out which color represents which distance and the vtkMRMLModelNode doesn’t have a LUT linked to it either.</p>
<p>Since we want to map the distance of two bones we need the specific distance to each color.<br>
Is there any way to create a color scale bar and link it to the vtkModelNode?</p>

---

## Post #2 by @MathiasBrucker (2021-11-08 14:59 UTC)

<p>Operating system: WIN10-x64<br>
Slicer version: 4.11.202…<br>
Expected behavior: After applying the ModeltoModel-distance the bone is colored with the RedGreenBlue LUT but in the vtkMRMLModelNode there is no LUT linked and you cannot display the scale of the colors → I know red is close and Blue is far aways but I don’t know the exact values</p>
<p>Actual behavior: After finishing the ModelToModelDistance there should be a color scale bar with the distance in mm and the colors for the distance the colors represent.</p>

---

## Post #3 by @MathiasBrucker (2021-11-09 09:22 UTC)

<p>I did it, used the “vtkMRMLProceduralColorNode”. Was able to set all the colors for different values and display it in the Slicer with the vtkScalarBarWidget</p>

---
