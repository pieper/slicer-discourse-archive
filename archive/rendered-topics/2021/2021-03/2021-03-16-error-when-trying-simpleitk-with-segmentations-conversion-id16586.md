---
topic_id: 16586
title: "Error When Trying Simpleitk With Segmentations Conversion"
date: 2021-03-16
url: https://discourse.slicer.org/t/16586
---

# Error when trying SimpleITK with Segmentations / conversion

**Topic ID**: 16586
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/error-when-trying-simpleitk-with-segmentations-conversion/16586

---

## Post #1 by @yannick_s (2021-03-16 22:28 UTC)

<p>Dear all,</p>
<p>I would like to use SimpleITK with Segmentations. For this, I tried the approaches described by <a class="mention" href="/u/lassoan">@lassoan</a> here: <a href="https://discourse.slicer.org/t/segmentation-using-simpleitk/13232/2" class="inline-onebox">Segmentation Using SimpleITK - #2 by lassoan</a></p>
<p>My <code>inputSeg</code> stems from a <code>vtkMRMLSegmentationNode</code> I get from a <code>qMRMLNodeComboBox</code>.</p>
<p>I first tried:</p>
<pre><code>    labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')

    segs = vtk.vtkStringArray()
    inputSeg.GetDisplayNode().GetVisibleSegmentIDs(segs)

    slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(inputSeg, segs, labelmapVolumeNode)

    segimg = sitkUtils.PullVolumeFromSlicer(labelmapVolumeNode)
</code></pre>
<p>This gives the error:<br>
RuntimeError: Exception thrown in SimpleITK ReadImage: /tmp/SimpleITK/Code/IO/src/sitkImageReaderBase.cxx:318:<br>
sitk::ERROR: Logic error!</p>
<p>Trying <code>sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(labelmapVolumeNode.GetName()))</code> gives the same error.</p>
<p>I then tried to get to the label map representation from the segmentation:</p>
<pre><code>img = vtkSegmentationCore.vtkOrientedImageData()
segimg2 = inputSeg.GetBinaryLabelmapRepresentation(segs.GetValue(3), img)
</code></pre>
<p>But this results in a <code>segimimg2</code> with <code>NoneType</code> that I cannot further process.</p>
<p>I do not need the label maps to be accessible through e.g. the Data module and use it only internally. That’s why I would prefer something like getting the label map without adding a node.</p>
<p>I am new to handling segmentations and need to use SimpleITK functions. Any help to get there highly appreciated!</p>

---

## Post #2 by @yannick_s (2021-03-18 15:51 UTC)

<p>I am switching to a scripted CLI, looks more straightforward to use my existing code based on SimpleITK</p>

---
