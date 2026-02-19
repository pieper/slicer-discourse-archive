---
topic_id: 11338
title: "How To Get A Volume And A Model Object From In The Scene Man"
date: 2020-04-29
url: https://discourse.slicer.org/t/11338
---

# How to get a volume and a model object from in the scene management node?

**Topic ID**: 11338
**Date**: 2020-04-29
**URL**: https://discourse.slicer.org/t/how-to-get-a-volume-and-a-model-object-from-in-the-scene-management-node/11338

---

## Post #1 by @Shicong (2020-04-29 02:54 UTC)

<p>This is the case, I loaded a volume and exported a model object, if only one, how to get these two objects in the scene management node! how is implemented in python code?Thanks!</p>

---

## Post #2 by @lassoan (2020-05-01 15:52 UTC)

<p>You can get first instance of a certain MRML node class by calling <code>slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLVolumeNode")</code>. However, you should not need this. If input comes from user then you ask the user to make a selection on the GUI. If you process data then you can always set/get the input and output nodes, so you don’t need blind lookup either.</p>

---
