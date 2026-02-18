# Create a segmentation from a contour file using python

**Topic ID**: 29167
**Date**: 2023-04-27
**URL**: https://discourse.slicer.org/t/create-a-segmentation-from-a-contour-file-using-python/29167

---

## Post #1 by @RonJones (2023-04-27 06:34 UTC)

<p>We have a standard workflow that uses a LabelMap file which is then converted to a Segment node.</p>
<p>Is it possible to convert a LabelMapVolume to a Segmentation using the python API?</p>

---

## Post #2 by @RonJones (2023-05-01 06:43 UTC)

<p>For reference this is the solution I worked out.</p>
<pre><code class="lang-auto">    labelMapNode = slicer.util.getNodesByClass('vtkMRMLLabelMapVolumeNode')[0]
    segNode = slicer.util.getNodesByClass('vtkMRMLSegmentationNode')[0]
    logic = slicer.util.getModuleLogic('Segmentations')
    logic.ImportLabelmapToSegmentationNodeWithTerminology(contourImageNode, segNode, "")
</code></pre>

---
