---
topic_id: 12726
title: "Having Trouble Understanding Model Types"
date: 2020-07-24
url: https://discourse.slicer.org/t/12726
---

# Having trouble understanding model types

**Topic ID**: 12726
**Date**: 2020-07-24
**URL**: https://discourse.slicer.org/t/having-trouble-understanding-model-types/12726

---

## Post #1 by @Ugi_Mikla (2020-07-24 22:43 UTC)

<p>Hi there!<br>
I’m new at this software- Trying to learn to segment and create models for dental research purpose.<br>
I will really appreciate if someone could help me understand the difference between the surface model and the solid model.<br>
I understand that modelling with slicer reaches de surface one, am i right?<br>
What is it that i CANT do with a surface model, that i can with a SOLID one?</p>

---

## Post #2 by @lassoan (2020-07-24 23:08 UTC)

<p>Would you like to know the difference between surface meshes / volumetric meshes (stored in model node)? Or between model nodes / segmentation nodes / labelmap volume nodes?</p>
<p>What would you like to achieve?</p>

---

## Post #3 by @Ugi_Mikla (2020-07-24 23:33 UTC)

<p>okey, maybe I’d go with surface and volumetric meshes issue. I am trying to generate 3d models of bone and segmented teeth. I want to export them and have the possibility to print them. Also, I dont know if I cant analyze (particularly measure volume and surface area) of my models being surface. I have been reading buy I am a mess here. Thank you</p>

---

## Post #4 by @lassoan (2020-07-25 00:21 UTC)

<p>You typically need volumetric meshes for finite-element analysis (e.g., mechanical modeling). For everything else, such as 3D printing and surface and volume measurements, you only need a surface mesh, because you are only interested in the boundary surface of the object.</p>

---
