---
topic_id: 329
title: "Api For Surface Models Model Maker For Python Access"
date: 2017-05-16
url: https://discourse.slicer.org/t/329
---

# API for Surface Models -> Model Maker for Python Access?

**Topic ID**: 329
**Date**: 2017-05-16
**URL**: https://discourse.slicer.org/t/api-for-surface-models-model-maker-for-python-access/329

---

## Post #1 by @jks1995 (2017-05-16 19:31 UTC)

<p>Does the surface models module have an api that will allow you to access its features via python?</p>

---

## Post #2 by @lassoan (2017-05-16 19:32 UTC)

<p>Yes, all features of all modules are accessible from Python. What would you like to achieve?</p>

---

## Post #3 by @jks1995 (2017-05-18 14:31 UTC)

<p>I would like to be able to render a 3D view in a slicelete and then display the model in a 3D view. I have a label map I would like to provide as input.</p>

---

## Post #4 by @lassoan (2017-05-18 20:45 UTC)

<p>The simplest way of showing segmentation in 2D and 3D is to convert your labelmap node to a segmentation node:</p>
<pre><code>seg=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(getNode('label'), seg)
seg.CreateClosedSurfaceRepresentation()
</code></pre>
<p>After this conversion you can delete your original labelmap node.</p>

---
