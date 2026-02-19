---
topic_id: 28601
title: "Create Model From 360 Scan"
date: 2023-03-27
url: https://discourse.slicer.org/t/28601
---

# create model from 360 scan?

**Topic ID**: 28601
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/create-model-from-360-scan/28601

---

## Post #1 by @studyskin (2023-03-27 18:05 UTC)

<p>hi, i downloaded this scan from morphosource but it is taken in 360 not usual slices but was called a ct scan, i dont imagine there is but is there a way to turn this into a model? thank you</p>
<p><a href="https://drive.google.com/drive/folders/1_VRi_lN2o1xEYSDEFfouR-Bf6TiZrG_h?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1_VRi_lN2o1xEYSDEFfouR-Bf6TiZrG_h?usp=sharing</a></p>

---

## Post #2 by @lassoan (2023-03-27 18:16 UTC)

<p>You can use <a href="https://www.kitware.com/rtk-the-reconstruction-toolkit/">RTK</a> to reconstruct a Cartesian image from a set of projection images. There is no GUI for using RTK in Slicer, but if you need to do this kind of reconstructions frequently then you may consider adding a module for it.</p>

---

## Post #3 by @muratmaga (2023-03-27 18:45 UTC)

<p>This is not what’s usually posted on MorphoSource. You can contact MorphoSource and/or the data owner, and ask if they can provide the reconstructed slice data. They probably upload this by mistake.</p>

---

## Post #4 by @Jed (2023-03-28 08:04 UTC)

<p>I 3D printed my CT scans of my spine,</p>

---
