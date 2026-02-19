---
topic_id: 23267
title: "Unable To Export Segment With Exportsegmentsclosedsurfacerep"
date: 2022-05-03
url: https://discourse.slicer.org/t/23267
---

# Unable to export segment with ExportSegmentsClosedSurfaceRepresentationToFiles

**Topic ID**: 23267
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/unable-to-export-segment-with-exportsegmentsclosedsurfacerepresentationtofiles/23267

---

## Post #1 by @Xabierenko (2022-05-03 18:31 UTC)

<p>Hi,</p>
<p>I have been using the code snippet below to export large amounts of segmentations to .stl format.</p>
<pre><code class="lang-auto">segmentation = slicer.util.loadSegmentation(seg)
vol = slicer.util.loadVolume(mag)
    
volumeNode = slicer.util.getNode('*magnitude*')  # Get the volume node  
segNode = slicer.util.getNode('*Segment*')
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(out, segNode, None, "STL", False, 0.001, False)
    
slicer.mrmlScene.RemoveNode(volumeNode)
slicer.mrmlScene.RemoveNode(segmentation)
</code></pre>
<p>I don’t know why when I’m trying the same code to export a new dataset I’m getting the following error.</p>
<p><code>TypeError: ExportSegmentsClosedSurfaceRepresentationToFiles argument 2: method requires a vtkMRMLSegmentationNode, a vtkMRMLSegmentationStorageNode was provided.</code></p>
<p>Kind regards,<br>
Xabier</p>

---

## Post #2 by @cpinter (2022-05-03 18:33 UTC)

<aside class="quote no-group" data-username="Xabierenko" data-post="1" data-topic="23267">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xabierenko/48/6710_2.png" class="avatar"> Xabierenko:</div>
<blockquote>
<p><code>segNode = slicer.util.getNode('*Segment*')</code></p>
</blockquote>
</aside>
<p>It seems that this returns the wrong node (the segmentation storage node instead of the segmentation node itself). I suggest using a more robust way to get the node.</p>

---

## Post #3 by @Xabierenko (2022-05-03 18:38 UTC)

<p>Is there a way of getting the first segment following the order displayed in the GUI?</p>

---

## Post #4 by @wawa (2022-05-10 03:52 UTC)

<p>Here is my working code:</p>
<pre><code class="lang-auto">nii_pathname =  ...   
seg = slicer.util.loadSegmentation(nii_pathname)
segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(out, segmentationNode, None, "STL")
slicer.mrmlScene.RemoveNode(segmentationNode)
slicer.mrmlScene.RemoveNode(seg)
</code></pre>
<p>I don’t know why using the function “GetFirstNodeByClass” works, but it does meet the need.</p>

---

## Post #5 by @lassoan (2022-05-10 04:44 UTC)

<aside class="quote no-group" data-username="wawa" data-post="4" data-topic="23267">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/f05b48/48.png" class="avatar"> wawa:</div>
<blockquote>
<p>I don’t know why using the function “GetFirstNodeByClass” works, but it does meet the need.</p>
</blockquote>
</aside>
<p><code>slicer.util.getNode('*Segment*')</code> returns the first node in the scene that contains <code>Segment</code> in its name or ID (including all the hidden nodes). There can be many nodes like that in the scene: the segmentation node, the segmentation display node, and segmentation storage node. <code>getNode</code> helper function (especially when it is used with wildcards as input) is only recommended for quick testing and troubleshooting.</p>
<p>If you specify the kind of node you are looking for (<code>vtkMRMLSegmentationNode</code>) and you only have one node of that type in the scene then the result is always as you expect.</p>

---
