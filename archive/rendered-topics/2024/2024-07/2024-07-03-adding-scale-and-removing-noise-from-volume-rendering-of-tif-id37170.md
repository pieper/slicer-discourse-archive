---
topic_id: 37170
title: "Adding Scale And Removing Noise From Volume Rendering Of Tif"
date: 2024-07-03
url: https://discourse.slicer.org/t/37170
---

# Adding scale and removing noise from volume rendering of TIFF stacks

**Topic ID**: 37170
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/adding-scale-and-removing-noise-from-volume-rendering-of-tiff-stacks/37170

---

## Post #1 by @mariorollo (2024-07-03 09:47 UTC)

<p>I am completely new to the platform and I have two questions about using it at the moment. I got a stack of a few thousand TIFFs resulting from micro CT scanning of an insect body and applied a volume rendering after importing the images from the SlicerMorph plugin. I would like to have a scale on the exportable file but the scale I add in the orthographic perspective mode is not correct. Would there be a way to fix it? Additionally, the rendering contains a lot of noise around the body (like sawdust). Is it possible to reduce or filter it in any way with any of the available plugins? Thank you.</p>

---

## Post #2 by @muratmaga (2024-07-03 17:11 UTC)

<p>If the scale is wrong, it means the data were imported with wrong image spacing settings. Please check that you enter the correct image spacing information (in millimeters) to the ImageStacks during the import phase.</p>

---

## Post #3 by @mariorollo (2024-07-04 08:01 UTC)

<p>Thanks a lot for the tips. I entered the information in the appropriate fields (5 μm voxel size, then 0.005 mm). However, the rendering became dusty (previously it was great even at medium resolution) and the shift slider with the chosen preset became slow, less responsive. My hardware is good, M1 Max 64 GB RAM. What could have happened?</p>

---

## Post #4 by @muratmaga (2024-07-05 03:05 UTC)

<p>What do you mean by dusty? Can you provide a screenshot.</p>
<p>Is any dimension of your full resolution data more than 2048 voxels? Apple silicon macs cannot render such datasets. You will need to resample.</p>

---

## Post #5 by @mariorollo (2024-07-12 08:45 UTC)

<p>I think I found the problem. I was using a preset associated with ultrasound rendering (US-Fetal. When I selected a preset associated with uCT (uCT-Skull or uCT-Bone-8bit), it worked.</p>

---
