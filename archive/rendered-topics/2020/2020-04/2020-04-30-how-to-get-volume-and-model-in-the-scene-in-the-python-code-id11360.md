---
topic_id: 11360
title: "How To Get Volume And Model In The Scene In The Python Code"
date: 2020-04-30
url: https://discourse.slicer.org/t/11360
---

# How to get volume and model in the scene in the python code？

**Topic ID**: 11360
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/how-to-get-volume-and-model-in-the-scene-in-the-python-code/11360

---

## Post #1 by @Shicong (2020-04-30 06:22 UTC)

<p>I loaded a volume, in the scene and created a model. Below the data tree structure you can see the data shown in the figure. i want to get them in python code,The following:<br>
model = slicer.mrmlScene.GetNumberOfNodesByClass(“vtkMRMLModelHierarchyNode”)<br>
volume = slicer.mrmlScene.GetNumberOfNodesByClass(“vtkMRMLVolumeHeaderlessStorageNode”)<br>
Is it possible to do this, but I test seems to have some problems, can you solve it? Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a12faf57999da04bf278beb83609f4c1dfbf56bd.png" data-download-href="/uploads/short-url/mZV2j82aDRSauuIbx0rShzN0pPf.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a12faf57999da04bf278beb83609f4c1dfbf56bd.png" alt="图片" data-base62-sha1="mZV2j82aDRSauuIbx0rShzN0pPf" width="609" height="500" data-dominant-color="F1F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">614×504 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-04-30 21:05 UTC)

<p>If you put a subject hierarchy tree widget into your module, you can get the current selection by calling <a href="http://apidocs.slicer.org/master/classqMRMLSubjectHierarchyTreeView.html#a696587e7f872d3221151658252dd0920"> currentItem()</a>.</p>

---
