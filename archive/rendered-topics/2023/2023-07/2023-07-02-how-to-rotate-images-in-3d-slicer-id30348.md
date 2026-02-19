---
topic_id: 30348
title: "How To Rotate Images In 3D Slicer"
date: 2023-07-02
url: https://discourse.slicer.org/t/30348
---

# How to rotate images in 3D slicer?

**Topic ID**: 30348
**Date**: 2023-07-02
**URL**: https://discourse.slicer.org/t/how-to-rotate-images-in-3d-slicer/30348

---

## Post #1 by @Mahrukh (2023-07-02 11:22 UTC)

<p>Hello,<br>
How can i rotate images in 3D slicer?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @muratmaga (2023-07-03 14:58 UTC)

<p>Do you mean the slice views? You can use the transforms module <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="inline-onebox">Transforms — 3D Slicer documentation</a></p>
<p>Otherwise you simply spin the object in 3D viewer.</p>

---

## Post #3 by @lassoan (2023-07-03 16:22 UTC)

<p>If the image was not acquired correctly (the imaging technician set wrong patient position) then indeed the transform module can be used to fix this - as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested above.</p>
<p>If you only want to flip/rotate images in slice views (not change the image orientation in physical space) then you can use the Reformat module’s LR/PA/IS sliders. Probably you want to use +/-90deg or +/-180deg rotation.</p>

---
