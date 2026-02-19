---
topic_id: 38301
title: "How To Set Closed Surface Representation As Default Segmenta"
date: 2024-09-09
url: https://discourse.slicer.org/t/38301
---

# How to set Closed Surface representation as default segmentation for RTSTRUCT?

**Topic ID**: 38301
**Date**: 2024-09-09
**URL**: https://discourse.slicer.org/t/how-to-set-closed-surface-representation-as-default-segmentation-for-rtstruct/38301

---

## Post #1 by @achiravu (2024-09-09 20:32 UTC)

<p>I am using the SlicerRT extension to view RTSTRUCT contours in 3D Slicer, and I’m finding the Closed Surface representation to be more useful than Planar Contour. How do I set Closed Surface as the default representation when importing contours into Slicer?</p>
<p>Also, what are useful Python scripts for changing the default slice fill and 3D view opacities in the segmentations module?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2024-09-10 03:38 UTC)

<aside class="quote no-group" data-username="achiravu" data-post="1" data-topic="38301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f14d63/60.png" class="avatar"> achiravu:</div>
<blockquote>
<p>I’m finding the Closed Surface representation to be more useful than Planar Contour. How do I set Closed Surface as the default representation when importing contours into Slicer?</p>
</blockquote>
</aside>
<p>Closed surface representation is indeed useful for visualization, therefore it is automatically computed. You can change the source representation to closed surface by clicking on “Make source” button in Segmentations module, but it would just unnecessarily change the loaded data.</p>
<aside class="quote no-group" data-username="achiravu" data-post="1" data-topic="38301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f14d63/60.png" class="avatar"> achiravu:</div>
<blockquote>
<p>Also, what are useful Python scripts for changing the default slice fill and 3D view opacities in the segmentations module?</p>
</blockquote>
</aside>
<p>In theory, something like this should work:</p>
<pre data-code-wrap="python"><code class="lang-python">defaultSegmentationDisplayNode = slicer.vtkMRMLSegmentationDisplayNode()
defaultSegmentationDisplayNode.SetOpacity2DFill(0.1)
slicer.mrmlScene.AddDefaultNode(defaultSegmentationDisplayNode)
</code></pre>
<p>Unfortunately, SlicerRT’s DICOM importer does not use information in the default display node (it instantiates the display node directly instead of creating via the scene). Please submit a bug report to <a href="https://github.com/SlicerRt/SlicerRT" class="inline-onebox">GitHub - SlicerRt/SlicerRT: Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), structure comparison and morphology, isodose line/surface generation, etc.</a></p>
<p>Until it is fixed, you can add an observer to the scene so that you get notification when a new node is added and if a segmentation display node gets created then you can adjust its properties.</p>

---
