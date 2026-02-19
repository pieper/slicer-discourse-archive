---
topic_id: 13921
title: "Manipulate Model Visibility"
date: 2020-10-07
url: https://discourse.slicer.org/t/13921
---

# Manipulate model visibility

**Topic ID**: 13921
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/manipulate-model-visibility/13921

---

## Post #1 by @aldoSanchez (2020-10-07 14:44 UTC)

<p>I want to manipulate the module created from the segmentation.<br>
what i did was to export the segmentation to modules<br>
and now I want to manipulate the colors and the visibility of the modules.<br>
here’s the code:</p>
<pre><code class="lang-python">#export segmentation
segmentationNode=getNode(‘Segmentation’)
modelHierarchyNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelHierarchyNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToModelHierarchy(segmentationNode, modelHierarchyNode)
</code></pre>

---

## Post #2 by @aldoSanchez (2020-10-07 16:43 UTC)

<p>I found out the following way to manipulate the model:</p>
<pre><code class="lang-python">vtkLWM=getNode('Left-Cerebral-White-Matter')
vtkLWM.SetDisplayVisibility(False)
</code></pre>

---
