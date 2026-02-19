---
topic_id: 25479
title: "Is There A Way To Perform Simple Mathematics On Voxel Values"
date: 2022-09-29
url: https://discourse.slicer.org/t/25479
---

# Is there a way to perform simple mathematics on voxel values and then generate an image based on them? 

**Topic ID**: 25479
**Date**: 2022-09-29
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-perform-simple-mathematics-on-voxel-values-and-then-generate-an-image-based-on-them/25479

---

## Post #1 by @Mmirzaa1 (2022-09-29 05:10 UTC)

<p>Hello everyone!<br>
I was having trouble performing a task at 3Dslicer. I wanted to do some simple mathematics on the voxel values on 3d slicer ( to be exact I wanted to subtract the In-phase voxel intensity values of an abdominal MR scan from an out of phase scan (same case and no need of registration) and then divide it by in phase voxel values multiplied by 2. I would like to generate a new set of images based on the obtained values ( to be concise : (Inphase-Outphase)/inphase X 2) ).<br>
FYI our aim is to see if it would be possible to generate a quantification heat map of the liver.<br>
Thank you very much for everything</p>

---

## Post #2 by @pieper (2022-09-29 12:27 UTC)

<p>It sounds like what you are trying to do can all be done efficiently by accessing the volumes as numpy arrays.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume</a></p>

---

## Post #3 by @Mmirzaa1 (2022-11-01 18:37 UTC)

<p>Thank you very much for the suggestion</p>

---

## Post #4 by @NikhilM (2024-01-24 02:41 UTC)

<p>Hi, I’m looking to do something quite similiar on 3d slicer but not having much luck getting the Python scripts working on my data set. Did you manage to figure it out? Thanks</p>

---
