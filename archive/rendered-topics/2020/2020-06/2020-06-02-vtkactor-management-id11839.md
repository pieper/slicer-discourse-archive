---
topic_id: 11839
title: "Vtkactor Management"
date: 2020-06-02
url: https://discourse.slicer.org/t/11839
---

# vtkActor management

**Topic ID**: 11839
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/vtkactor-management/11839

---

## Post #1 by @Eloi_gbrt (2020-06-02 21:35 UTC)

<p>Hi everybody,<br>
I’m trying to create a python module which permits to display an image and different other features for a VR project purpose. To achieve this goal i decided to code functions creating the vtkActor(s) that would be added in the Slicer Renderer. I reached the renderer using those lines :</p>
<p>lm = slicer.app.layoutManager()<br>
renderer = lm.threeDWidget(0).threeDView().renderWindow().GetRenderers().GetFirstRenderer()</p>
<p>My issue is that i would want the user to be able to add or remove the different volume rendered that match with the vtkActors(s) i mentionned. So i used checkboxes and adding the actors works fine and render what i wanted but i cannot update any of them or remove them. I would like to know if it is possible to get the different actors from the renderer precisely or if there is another method to track what i add in order to be able to manage it at will.</p>

---

## Post #2 by @lassoan (2020-06-02 21:54 UTC)

<p>If you insert objects into the scene as model nodes (<code>slicer.modules.models.logic().AddModel(somVtkPolyDataObject)</code>) then you can <a href="https://github.com/KitwareMedical/SlicerVirtualReality#transform-objects">grab and move them using VR controllers</a>.</p>

---

## Post #3 by @Eloi_gbrt (2020-06-02 22:10 UTC)

<p>To be honest i don’t really have to use VR for now. I just want to display everything correctly and to be able to have control over it with the UI. Can I remove or update this model with a simple function too ?<br>
I didn’t find a RemoveModel() function.</p>

---

## Post #4 by @lassoan (2020-06-02 22:27 UTC)

<p>You can remove the node by using <code>slicer.mrmlScene.RemoveNode</code> method. You can move around a model if you apply a transform to it and show the transform interactor in Transforms module / Display / Interaction.</p>

---

## Post #5 by @Eloi_gbrt (2020-06-02 22:36 UTC)

<p>Ok, thank you, i’ll try it.</p>

---
