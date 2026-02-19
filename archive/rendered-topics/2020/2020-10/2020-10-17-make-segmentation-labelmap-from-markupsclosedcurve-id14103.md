---
topic_id: 14103
title: "Make Segmentation Labelmap From Markupsclosedcurve"
date: 2020-10-17
url: https://discourse.slicer.org/t/14103
---

# make segmentation labelmap from markupsclosedcurve

**Topic ID**: 14103
**Date**: 2020-10-17
**URL**: https://discourse.slicer.org/t/make-segmentation-labelmap-from-markupsclosedcurve/14103

---

## Post #1 by @doebow (2020-10-17 18:33 UTC)

<p>slicer version: 4.11.10</p>
<p>I’m trying to make a binary label mask from a closed curve markup. Here is my code</p>
<p>curves=slicer.util.getNodesByClass(“vtkMRMLMarkupsClosedCurveNode”)<br>
areaMm2 = slicer.modules.markups.logic().GetClosedCurveSurfaceArea(curves[0], crossSectionSurface)<br>
modelNode = slicer.modules.models.logic().AddModel(crossSectionSurface)</p>
<p>inputModel=getNode(“Model_1”)<br>
referenceVolumeNode=getNode(“1: No series description_1”)<br>
seg = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’)<br>
seg.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)<br>
slicer.modules.segmentations.logic().ImportModelToSegmentationNode(inputModel, seg)<br>
seg.CreateBinaryLabelmapRepresentation()</p>
<p>outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg, outputLabelmapVolumeNode, referenceVolumeNode)<br>
outputLabelmapVolumeArray = (slicer.util.arrayFromVolume(outputLabelmapVolumeNode) * 100).astype(‘int8’)</p>
<p>Here is what I get<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfb6636ae92c64684df9ed7a26d735d2e6d19ebe.jpeg" data-download-href="/uploads/short-url/vV3eWYjNxHxo4ydXoqZEjNQje58.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb6636ae92c64684df9ed7a26d735d2e6d19ebe_2_690x365.jpeg" alt="image" data-base62-sha1="vV3eWYjNxHxo4ydXoqZEjNQje58" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb6636ae92c64684df9ed7a26d735d2e6d19ebe_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb6636ae92c64684df9ed7a26d735d2e6d19ebe_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb6636ae92c64684df9ed7a26d735d2e6d19ebe_2_1380x730.jpeg 2x" data-dominant-color="A3A4A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1921×1018 331 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can only see the segmentation in 3D view however I couldn’t see it in other view and also the lablemap is empty.<br>
I think it is because the segmentation is closed surface representation not binary labelmap representation. Nevertheless I couldn’t get binary labelmap representation though this code seg.CreateBinaryLabelmapRepresentation()<br>
How can I fix it?</p>

---
