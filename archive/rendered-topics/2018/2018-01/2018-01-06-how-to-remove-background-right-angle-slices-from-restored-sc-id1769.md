---
topic_id: 1769
title: "How To Remove Background Right Angle Slices From Restored Sc"
date: 2018-01-06
url: https://discourse.slicer.org/t/1769
---

# How to remove background right-angle slices from restored Scene Views of models from SPL Brain Atlas

**Topic ID**: 1769
**Date**: 2018-01-06
**URL**: https://discourse.slicer.org/t/how-to-remove-background-right-angle-slices-from-restored-scene-views-of-models-from-spl-brain-atlas/1769

---

## Post #1 by @aNonprofessional (2018-01-06 01:20 UTC)

<p>Note: my usage of Slicer is non-typical, just toward trying to learn brain anatomy.</p>
<p>Operating system: Windows 8.1 win-amd64 Intel Core i7<br>
Slicer version: 4.8.0 r26489<br>
Expected behavior: restored SPL scene view minus <strong>background</strong> slices<br>
Actual behavior: 3-D models show with background right-angle slices</p>
<p>When I ‘restore’ a Scene View from the SPL Brain Atlas, it presents the selected set of structures with a <strong>background</strong> of 2 right-angle slices, which can get in the way of viewing the 3-D structures from different angles, and also seem to slow down the user rotation of the model.</p>
<p>How can I remove those 2 right-angle slice backgrounds from the view, without removing them from the scene that SPL included in their atlas, and then save that modified view for later viewing?</p>

---

## Post #2 by @pieper (2018-01-06 15:24 UTC)

<p>I think you are referring to the visibility of the slices in 3D.  Use the ‘eye’ icon in the slice controller.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Slice_Viewers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Slice_Viewers</a></p>
<p>Also you should try some of the general tutorials to get familiar with things:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#General_Introduction" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#General_Introduction</a></p>
<p>(Note that saving and restoring scene files with scene views has had some bugs but what you describe should work).</p>

---

## Post #3 by @aNonprofessional (2018-01-06 21:24 UTC)

<p>Thank you Steve, your first reference does indeed work to remove the background 90 degree slices from the restored Scene View that is provided within the SPL Brain Atlas.</p>
<p>However, there is still a lag in rotating the 3D view of the restored provided Scene View of a selected structure that is not present when rotating the 3D view of the base brain itself from the SPL atlas.  I suspect I’ll have to create my own Scene Views from the base brain.</p>
<p>And I’ll re-look at some of the tutorials, thanks.</p>

---
