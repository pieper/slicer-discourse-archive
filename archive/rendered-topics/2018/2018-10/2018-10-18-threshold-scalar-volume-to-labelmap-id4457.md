---
topic_id: 4457
title: "Threshold Scalar Volume To Labelmap"
date: 2018-10-18
url: https://discourse.slicer.org/t/4457
---

# Threshold scalar volume to labelmap

**Topic ID**: 4457
**Date**: 2018-10-18
**URL**: https://discourse.slicer.org/t/threshold-scalar-volume-to-labelmap/4457

---

## Post #1 by @kayarre (2018-10-18 20:22 UTC)

<p>I  am trying to use the python interface to load a (float) scalar volume in the form of a signed distance field want to apply thresholdscalarvolume  to generate a label map with everything below 0.0. It doesn’t seem to be working in terms of creating the label map and running the cli interface.</p>
<p>here is a brief attempt with the code:</p>
<pre><code class="lang-auto">level_set = value['level_set']

[success, volumeNode] = slicer.util.loadVolume(level_set, returnNode=True)
volumeNode.SetName("case4" + "level_set")

tempLabel = slicer.vtkMRMLLabelMapVolumeNode() 
slicer.mrmlScene.AddNode(tempLabel) 
tempLabel.SetName("case4" + "thingy") 
temp_stuff = slicer.vtkSlicerVolumesLogic().CreateLabelVolumeFromVolume(slicer.mrmlScene, tempLabel, volumeNode)

# Compute the thresholded output volume using the Threshold Scalar Volume CLI module
cliParams = {'InputVolume': volumeNode.GetID(), 'OutputVolume': tempLabel.GetID(), 'ThresholdValue' : 0.0, 'ThresholdType' : 'Below', 'OutsideValue' : 1.0}
cliNode = slicer.cli.runSync(slicer.modules.thresholdscalarvolume, None, cliParams, wait_for_completion=True)
</code></pre>

---

## Post #2 by @lassoan (2018-10-18 20:52 UTC)

<p>You can do it much simpler way:</p>
<pre><code class="lang-auto">voxelArray = slicer.util.arrayFromVolume(volumeNode)
voxelArray[voxelArray &lt; thresholdValue] = 0
slicer.util.arrayFromVolumeModified(volumeNode)
</code></pre>
<p>Next steps depend on what you would like to do. Would you like to convert this to a segmentation node?</p>

---

## Post #3 by @kayarre (2018-10-18 21:23 UTC)

<p>I figured out two things. runSync forces the command to wait until completed whereas run immediately returns and has to be checked.</p>
<p>the second thing was checking cliNode.GetErrorText() is empty the problem is that I used lower case “below” rather than “Below”.</p>
<p>now the line executes but doesn’t show anything on the screen.</p>

---

## Post #4 by @kayarre (2018-10-18 21:24 UTC)

<p>That is much simpler. thank you.</p>
<p>yes that is it exactly, I saw the another post where there are commands to import the the label map to a segmentation mode, but hadn’t gotten that far yet.</p>

---

## Post #5 by @lassoan (2018-10-18 22:15 UTC)

<p>You can create a segmentation from thresholded input <code>volumeNode</code> like this:</p>
<pre><code class="lang-auto">volumeNode = ...
thresholdValue = 80

# Create temporary labelmap
labelVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.vtkSlicerVolumesLogic().CreateLabelVolumeFromVolume(slicer.mrmlScene, labelVolumeNode, volumeNode)

# Fill temporary labelmap by thresholding input volumeNode
voxelArray = slicer.util.arrayFromVolume(volumeNode)
labelVoxelArray = slicer.util.arrayFromVolume(labelVolumeNode)
labelVoxelArray[voxelArray &gt;= thresholdValue] = 100
labelVoxelArray[voxelArray &lt; thresholdValue] = 0
slicer.util.arrayFromVolumeModified(labelVolumeNode)

# Import labelmap to segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelVolumeNode, segmentationNode)
segmentationNode.CreateClosedSurfaceRepresentation()

# Delete temporary labelmap
slicer.mrmlScene.RemoveNode(labelVolumeNode)
</code></pre>

---

## Post #6 by @kayarre (2018-10-18 23:08 UTC)

<p>is it possible to set the master volume in the editor? can I do from the segmentationNode?</p>
<p>and also is it possible to select the slice views orientation button via as well?</p>

---

## Post #7 by @lassoan (2018-10-19 03:11 UTC)

<p>Yes, good point, you can easily create segments directly from a grayscale volume by choosing the volume as master volume and using Threshold effect. See full examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>

---

## Post #8 by @kayarre (2018-10-22 18:24 UTC)

<p>Thanks,<br>
what I am doing is a little more complicated. I am pre segmenting with vmtk and want to edit that segmentation with slicer.</p>
<p>I used the command segmentEditorWidget.setMasterVolumeNode(volumeNode) to set the master volume but it didn’t change the gui view like it did when changed the name of the segmentation.</p>
<p>also whats the command to do the alignment? I wish I had a better way to figure out how buttons are linked to the commands to be used in as script.</p>

---

## Post #9 by @lassoan (2018-10-22 18:44 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="8" data-topic="4457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>I used the command segmentEditorWidget.setMasterVolumeNode(volumeNode) to set the master volume but it didn’t change the gui view like it did when changed the name of the segmentation.</p>
</blockquote>
</aside>
<p>You can change view by using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util"><code>slicer.util.setSliceViewerLayers</code> method</a>.</p>
<aside class="quote no-group" data-username="kayarre" data-post="8" data-topic="4457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>also whats the command to do the alignment?</p>
</blockquote>
</aside>
<p>I’m not sure what alignment you are referring to.</p>
<aside class="quote no-group" data-username="kayarre" data-post="8" data-topic="4457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>I wish I had a better way to figure out how buttons are linked to the commands to be used in as script.</p>
</blockquote>
</aside>
<p>When I need to find how GUI actions mapped to code, the most direct way is to download Slicer source code and search in full text of all files. Most cases GUI strings are defined in Qt .ui files. In the .ui file you can find widget’s name that shows that string. Once you have the widget name, search full text of Slicer source code for widget name and you’ll find code that runs when the widget is manipulated.</p>
<p>You might find <a href="http://apidocs.slicer.org/master/index.html">Slicer API documentation</a> and you can always ask on this forum.</p>

---

## Post #10 by @kayarre (2018-10-22 19:30 UTC)

<p>Whats the python command to do the alignment of the image volume and segmentation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2a53960f19e430a9f885137a5fdde5cc98fd7ea.jpeg" data-download-href="/uploads/short-url/ncPl9V4rWC9kIAVtHHibW1AzUx4.jpeg?dl=1" title="figure" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2a53960f19e430a9f885137a5fdde5cc98fd7ea_2_690x153.jpeg" alt="figure" data-base62-sha1="ncPl9V4rWC9kIAVtHHibW1AzUx4" width="690" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2a53960f19e430a9f885137a5fdde5cc98fd7ea_2_690x153.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2a53960f19e430a9f885137a5fdde5cc98fd7ea.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2a53960f19e430a9f885137a5fdde5cc98fd7ea.jpeg 2x" data-dominant-color="F2F3F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure</span><span class="informations">839×187 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>found it: segmentEditorWidget.rotateSliceViewsToSegmentation()</p>

---

## Post #11 by @kayarre (2018-10-22 21:09 UTC)

<p>when I try to execute the following I get an error:</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
</code></pre>
<p>segmentEditorWidget.setMRMLScene(slicer.mrmlScene) gives an error:</p>
<pre><code class="lang-auto">Python console user input: segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
void qMRMLSegmentEditorWidget::onSegmentSelectionChanged(const QItemSelection&amp;, const QItemSelection&amp;) : Invalid segment editor parameter set node
void qMRMLSegmentEditorWidget::onSegmentationNodeChanged(vtkMRMLNode*) : Invalid segment editor parameter set node
void qMRMLSegmentEditorWidget::onSegmentSelectionChanged(const QItemSelection&amp;, const QItemSelection&amp;) : Invalid segment editor parameter set node
void qMRMLSegmentEditorWidget::onSegmentationNodeChanged(vtkMRMLNode*) : Invalid segment editor parameter set node
void qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(vtkMRMLNode*) : Invalid segment editor parameter set node
void qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(vtkMRMLNode*) : Invalid segment editor parameter set node
void qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(vtkMRMLNode*) : Invalid segment editor parameter set node
virtual void qMRMLSegmentEditorWidget::updateWidgetFromMRML() : Invalid segment editor parameter set node

</code></pre>

---

## Post #12 by @lassoan (2018-10-22 23:01 UTC)

<p>These errors are logged because the widget attempts to update itself but segment editor parameter node is not set yet (using <code>setMRMLSegmentEditorNode</code>). You can ignore these errors and we’ll update the widget to not log these errors.</p>

---

## Post #13 by @lassoan (2021-06-04 13:34 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-get-intensity-range-of-a-volume/17949">How to get intensity range of a volume?</a></p>

---
