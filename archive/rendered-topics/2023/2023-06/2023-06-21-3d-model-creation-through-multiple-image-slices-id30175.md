---
topic_id: 30175
title: "3D Model Creation Through Multiple Image Slices"
date: 2023-06-21
url: https://discourse.slicer.org/t/30175
---

# 3D model creation through multiple image slices

**Topic ID**: 30175
**Date**: 2023-06-21
**URL**: https://discourse.slicer.org/t/3d-model-creation-through-multiple-image-slices/30175

---

## Post #1 by @LavaBunny (2023-06-21 18:32 UTC)

<p>After trying multiple tools, I think this tool may work for my project. Is this software able to take a set of 2D images and create a 3D model by stacking the 2D images one on top of another?</p>
<p>Sorry if this question is super simple. Thanks in advance.</p>

---

## Post #2 by @muratmaga (2023-06-21 19:05 UTC)

<p>You need to import 2D images as a volume using the ImageStacks module of SlicerMorph extension, and then segment the structure you would like to build a model of from it.</p>
<p>This is the imagestacks tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" class="inline-onebox">Tutorials/ImageStacks at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>and please read the documentation about Segment Editor and Segmentation in Slicer at <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>

---

## Post #3 by @waltbobrowski (2023-06-22 15:45 UTC)

<p>You don’t specify your source images. If they are “optical slices” (aka confocal, MRI, etc) with a fixed subject and moving focal plane then alignment will not be an issue. If on the other hand they are something like individual “slices” (aka histopathology) then you may have problems with rotational and other distortion issues requiring improved alignment. In my case, a stack of 414 histopathology slide images required the use of TrackEM module within ImageJ to align the stack of microscopy images. It was very tedious requiring the use of pair-wise “landmarks” which allowed for more precise elasticity and proper alignment throughout all features. That stack of images, once properly aligned, can then be exported to a new folder of aligned images, and then that set of images can be brought into 3D Slicer using the SlicerMorph extension descibed.</p>
<p>If so, more info can be found here:<br>
<a href="http://stefischer.de/2019/06/01/aligning-an-image-stack-in-trackem2/#comments" rel="noopener nofollow ugc">Aligning an image stack in TrackEM2 – Electron microscopy / Image analysis / 3D reconstruction (stefischer.de)</a></p>

---
