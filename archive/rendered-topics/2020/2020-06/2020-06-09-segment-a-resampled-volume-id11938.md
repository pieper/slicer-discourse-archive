# Segment a resampled volume

**Topic ID**: 11938
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/segment-a-resampled-volume/11938

---

## Post #1 by @caioath (2020-06-09 00:42 UTC)

<p>Hi<br>
I’m trying to run a script to perform automated segmentations right after resampling the volume to an isotropic spacing.<br>
The output is the resampled volume, but the segmentation from the original volume, not the resampled. I tried to use time.sleep() and also thread.join() to overcome the issue, but with the former the segmentation gets the original volume and with the latter Slicer crashes.</p>
<p>Which direction would you point me?</p>
<p>Thanks</p>
<pre><code>[success, VolumeNode] = slicer.util.loadVolume(path, returnNode=True)
# Resample the volume to 0.25mm spacing
parameters = {"outputPixelSpacing":"0.25,0.25,0.25", "InputVolume":VolumeNode,"interpolationType":'bspline',"OutputVolume":VolumeNode}
slicer.cli.run(slicer.modules.resamplescalarvolume, None, parameters)

# Create segmentation node
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(VolumeNode)
</code></pre>
<p>Operating system: Ubuntu 20.04<br>
Slicer version: 4.11</p>

---

## Post #2 by @lassoan (2020-06-09 01:42 UTC)

<p>The code that you posted looks good, it is just incomplete, so I cannot tell you what is missing  (setting segmentation node in a segment editor widget, set master volume in the widget, etc.). We can help if you provide a complete example that reproduces the unexpected behavior.</p>

---

## Post #3 by @caioath (2020-06-09 19:04 UTC)

<p>Thanks for your feedback</p>
<p>The code is similar to the <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">extract skin example</a> you provide, just adding the resampling step since in my dataset the AIAA prediction performs better on volumes with isotropic spacing.<br>
However, when I run this code, the prediction is done on the volume with the original spacing, not the resampled. Then I tried to add a “pause” right after the resampling using Python time module (adding time.sleep() with a couple of seconds to wait the task being executed before it continues, as in the example below) without success and also thread module (thread.join()) but no success.</p>
<p>Thanks</p>
<p>Caio</p>
<pre><code>import time
[success, VolumeNode] = slicer.util.loadVolume(path, returnNode=True)
# Resample the volume to 0.25mm spacing
parameters = {"outputPixelSpacing":"0.25,0.25,0.25", "InputVolume":VolumeNode,"interpolationType":'linear',"OutputVolume":VolumeNode}
slicer.cli.run(slicer.modules.resamplescalarvolume, None, parameters)

time.sleep(3)

# Create segmentation node with segment
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(VolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("segment")
# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setVolumeNode(VolumeNode)
# NVIDIA auto segmentation
segmentEditorWidget.setActiveEffectByName("Nvidia AIAA")
effect = segmentEditorWidget.activeEffect()
serverUrl = "http://LINK/v1/models"
effect.self().ui.serverComboBox.currentText = serverUrl
effect.self().onClickFetchModels()
effect.self().ui.segmentationModelSelector.currentText = "model_name"
effect.self().onClickSegmentation()</code></pre>

---

## Post #4 by @lassoan (2020-06-10 00:52 UTC)

<aside class="quote no-group" data-username="caioath" data-post="3" data-topic="11938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caioath/48/9688_2.png" class="avatar"> caioath:</div>
<blockquote>
<p><code>segmentEditorWidget.setVolumeNode(VolumeNode)</code></p>
</blockquote>
</aside>
<p>I don’t think that the segment editor widget has <code>setVolumeNode</code> method. Probably you meant to call<code>setMasterVolumeNode</code> method instead. You should have seen an error message when you executed this code.</p>

---

## Post #5 by @caioath (2020-06-10 02:21 UTC)

<p>I’m sorry, it was a mistake when I copied the code to the message. Thanks for pointing it out.</p>
<p>Please notice that In the example below the labelmap generated has the original spacing, rather than the isotropic resampled volume.<br>
The segmentation happens before the resampling is completed, that’s what I would like to avoid.</p>
<p>Thanks for your precious time</p>
<pre><code># 1st : load a CT into the scene (e.g. download CT Chest from sample data)

masterVolumeNode = getNode('vtkMRMLScalarVolumeNode1')

=========================
#resample the volume

parameters = {"outputPixelSpacing":"1,1,1", "InputVolume":masterVolumeNode,"interpolationType":'bspline',"OutputVolume":masterVolumeNode}
slicer.cli.run(slicer.modules.resamplescalarvolume, None, parameters)

========================
# Create segmentation with bone segment
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
bone = segmentationNode.GetSegmentation().AddEmptySegment("bone")

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Set bone segment color 
segmentationNode.GetSegmentation().GetSegment(bone).SetColor(0.9,1,0.7)
segmentEditorWidget.setCurrentSegmentID(bone)

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","200")
effect.setParameter("MaximumThreshold","2000")
effect.self().onApply()

labelmap = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmap, masterVolumeNode)
==============</code></pre>

---

## Post #6 by @lassoan (2020-06-10 03:14 UTC)

<p>Now, I see what the issue is: you do resampling in a background processing thread, therefore you still use the original, non-resampled volume as input for the segmentation. You don’t even notice, because you use the same volume as both input and output of resampling. All you need to do is to change <code>slicer.cli.run</code> to <code>slicer.cli.runSync</code>. See all the examples on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting">this page</a>.</p>

---

## Post #7 by @caioath (2020-06-10 10:50 UTC)

<p>Great!<br>
Thank you again</p>

---
