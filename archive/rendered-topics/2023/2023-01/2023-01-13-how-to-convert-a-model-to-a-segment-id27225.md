---
topic_id: 27225
title: "How To Convert A Model To A Segment"
date: 2023-01-13
url: https://discourse.slicer.org/t/27225
---

# How to convert a model to a segment?

**Topic ID**: 27225
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/how-to-convert-a-model-to-a-segment/27225

---

## Post #1 by @Caetox (2023-01-13 11:54 UTC)

<p>I want to convert a model to a segment.<br>
I tried using the CreateSegmentFromModelNode Function from the slicer.modules.segmentations.logic(). It returns a segment, but how can I then add it to a segmentation?</p>
<pre><code class="lang-auto">        modelNode = slicer.util.getNode('Model')
        segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode', 'CurveSegmentation')

        # Get the segmentation logic
        segmentationLogic = slicer.modules.segmentations.logic()

        # Convert the model to a segment
        segmentID = segmentationLogic.CreateSegmentFromModelNode(modelNode, segmentationNode)
</code></pre>

---
