---
topic_id: 23990
title: "Easy Way To Get Number Of Vertices From Segmentation In Pyth"
date: 2022-06-21
url: https://discourse.slicer.org/t/23990
---

# Easy way to get number of vertices from segmentation in python

**Topic ID**: 23990
**Date**: 2022-06-21
**URL**: https://discourse.slicer.org/t/easy-way-to-get-number-of-vertices-from-segmentation-in-python/23990

---

## Post #1 by @ChaoticBrainPerson (2022-06-21 15:43 UTC)

<p>Hey everyone.</p>
<p>I am would like to get the number of vertices of a model via Python, but I also need this model as a segment, not a modelNode.</p>
<p>I found a way to get this on the GUI via models → information → number of points and for modelNodes as len(slicer.util.arrayFromModelPoints(modelNode) but these both do not work with SegmentationNodes.</p>
<p>is there an easy way to do this?</p>
<p>Thanks in advance <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2022-06-21 15:47 UTC)

<p>You can export segments to models by right-clicking on the segmentation in Data module. You can also access the vtkPolyData object of a segment with a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-representation-of-a-segment">few Python commands</a> and get the number of points from there.</p>
<p>Usually the segmentation’s closed surface representation is generated on-the-fly from the labelmap representation, so the number of points in it should not matter. Why do you need this information?</p>

---

## Post #3 by @ChaoticBrainPerson (2022-06-22 08:40 UTC)

<p>I am working on a KI project, where I need all of my models to have the same size (otherwise it’s doing weird things). currently I’m doing this with MeshLab (here I can set a target face number, instead of target reduction number), but I want to reduce the number of dependencies as much as possible.<br>
I might get away with doing this all in modelNodes instead of segmentations, but if there were a way to get basically the number of faces without a conversion to modelNodes first, that’d be great.</p>

---

## Post #4 by @lassoan (2022-06-22 11:25 UTC)

<p>Number of faces does not matter, correspondence does. Because if <em>n</em>-th cell in one mesh does not correspond to <em>n</em>-th cell in the other mesh (e.g., they are not at the same anatomical location) then the two meshes are completely unrelated, even if two meshes have the same number of faces.</p>
<p>Decimation and all kinds of mesh reduction methods can change the number of faces but does not provide correspondence between meshes. What you need is spatial registration of models - warp one model to be aligned to the other, which results in not just the same number of faces but all points and faces corresponding to each other in the two meshes. Most commonly used model registration methods in Slicer are described <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#model-registration">here</a>.</p>

---
