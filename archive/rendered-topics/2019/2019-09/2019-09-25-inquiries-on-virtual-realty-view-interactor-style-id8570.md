---
topic_id: 8570
title: "Inquiries On Virtual Realty View Interactor Style"
date: 2019-09-25
url: https://discourse.slicer.org/t/8570
---

# Inquiries on Virtual Realty View Interactor Style

**Topic ID**: 8570
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/inquiries-on-virtual-realty-view-interactor-style/8570

---

## Post #1 by @Netta_Z (2019-09-25 20:04 UTC)

<p>Hi,<br>
I was trying to configure my own controller interactions for Windows Mixed Reality when I came across vtkVitualRealityViewInteractorstyle (<a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/MRML/vtkVirtualRealityViewInteractorStyle.cxx" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/VirtualReality/MRML/vtkVirtualRealityViewInteractorStyle.cxx</a>). However I couldn’t seem to access some of the methods (eg. MapInputToAction() couldn’t be used). I used slicer.vtkVirtualRealityViewInteractorStyle() in slicer to try and access those functionalities. What can I do to call methods within this class? Or is there another way to configure virtual reality controllers?<br>
Running on Nightly 4.11.0!<br>
Thank you.</p>

---

## Post #2 by @lassoan (2019-10-02 02:36 UTC)

<aside class="quote no-group" data-username="Netta_Z" data-post="1" data-topic="8570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/netta_z/48/4697_2.png" class="avatar"> Netta_Z:</div>
<blockquote>
<p>However I couldn’t seem to access some of the methods (eg. MapInputToAction() couldn’t be used</p>
</blockquote>
</aside>
<p>Are you trying to access these from Python or C++?</p>
<p>You can configure lots of quite complex interactions by setting up a scene (and optionally further customizing by Python code snippets). You can enable/disable which models can be picked, you can group multiple models under one transform and then they are moving together, you can enable exposing of controller poses as transform nodes and you can use that to move/orient slices (using Volume reslice driver module in SlicerIGT extension), you can observe the transforms and compute derived transforms, etc.</p>
<p>Interaction with markups is still a work in progress. If you are familiar with VTK programming in C++ then we would very welcome your contribution.</p>

---
