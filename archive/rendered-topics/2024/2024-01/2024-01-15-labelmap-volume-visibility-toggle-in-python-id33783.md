---
topic_id: 33783
title: "Labelmap Volume Visibility Toggle In Python"
date: 2024-01-15
url: https://discourse.slicer.org/t/33783
---

# Labelmap volume visibility toggle in Python

**Topic ID**: 33783
**Date**: 2024-01-15
**URL**: https://discourse.slicer.org/t/labelmap-volume-visibility-toggle-in-python/33783

---

## Post #1 by @Djennifer (2024-01-15 16:31 UTC)

<p>I’d like to be able to toggle a labelmap volume in the slicer viewer. I thought it would work the same like with a segmentation.<br>
<code>laNode = slicer.util.getNodesByClass("vtkMRMLLabelMapVolumeNode")[0] laNode.GetDisplayNode().SetVisibility(False)</code></p>
<p>However the display still shows the labelmap volume although laNode.GetDisplayNode().GetVisibility() does return 0. Am I doing something wrong here?</p>

---

## Post #2 by @pieper (2024-01-15 16:37 UTC)

<p>Volume layers work differently.  You can use this method instead:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers</a></p>

---
