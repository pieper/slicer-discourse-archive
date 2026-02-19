---
topic_id: 35898
title: "What Underlying Concepts Are Being Used Going From Segmentat"
date: 2024-05-03
url: https://discourse.slicer.org/t/35898
---

# What underlying concepts are being used going from segmentation to .STL

**Topic ID**: 35898
**Date**: 2024-05-03
**URL**: https://discourse.slicer.org/t/what-underlying-concepts-are-being-used-going-from-segmentation-to-stl/35898

---

## Post #1 by @koenterheegde (2024-05-03 18:29 UTC)

<p>I’m currently developing a program which has some of the same features as Slicer. Eventually, I get a .STL file and extract the centerline from it. However, when I apply this to my own generated .STL files, it doesn’t work compared to the ones being made in Slicer. It made me think that the segmentations/models are actually volumetric meshes instead of surface meshes, but I’m not sure whether I’m correct. And how does Slicer generate these volumetric meshes (if they are) from segmentations?<br>
Cheers.</p>

---

## Post #2 by @muratmaga (2024-05-03 18:55 UTC)

<p>please read this document for answers to your questions:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">Image Segmentation — 3D Slicer documentation</a></p>

---
