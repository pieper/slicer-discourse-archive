---
topic_id: 18593
title: "Slicer Models Node Number"
date: 2021-07-09
url: https://discourse.slicer.org/t/18593
---

# Slicer models node number

**Topic ID**: 18593
**Date**: 2021-07-09
**URL**: https://discourse.slicer.org/t/slicer-models-node-number/18593

---

## Post #1 by @F.A (2021-07-09 00:25 UTC)

<p>Hi, I have been using 3D Slicer to create a FE model from CT images. I meshed the model and used “probe volume with model” module to get HU and coordinates of each node. I imported the probe’s output to Abaqus using Paraview and Solidworks. When I wanted to assign the material property in Abaqus, I realized that the number of nodes in imported model and the number of the nodes in Slicer are not the same. According to attached image, the difference is mostly related to the interior nodes of the model.<br>
Thanks in advance for your help.<br>
F</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a46dd240c255151419f8e9fe6f7c79748caad16c.jpeg" alt="DifferentElems" data-base62-sha1="nsBAXOnhDIqTZwzFMCSFHR2wtC4" width="514" height="411"></p>

---

## Post #2 by @lassoan (2021-07-09 05:59 UTC)

<p>Are you working with volumetric meshes (created by Segment Mesher) or surface meshes?</p>

---

## Post #3 by @F.A (2021-07-09 14:09 UTC)

<p>I’m working with volumetric meshes created by “segment mesher” module.</p>

---

## Post #4 by @lassoan (2021-07-09 14:46 UTC)

<p>Importers/exporters may decide to merge and/or reorder points. If you cannot prevent your importers/exporters from doing this then you can save point IDs in a point array or split the mesh and import them piece by piece.</p>

---
