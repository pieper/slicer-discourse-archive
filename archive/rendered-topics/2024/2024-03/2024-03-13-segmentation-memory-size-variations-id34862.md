---
topic_id: 34862
title: "Segmentation Memory Size Variations"
date: 2024-03-13
url: https://discourse.slicer.org/t/34862
---

# Segmentation memory size variations

**Topic ID**: 34862
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/segmentation-memory-size-variations/34862

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-03-13 12:15 UTC)

<p>Hi to everyone. Today we’re concerned with segmentation memory sizes.<br>
We are using two different approaches to the same problem: linear (input driven) and non-linear (event/button driven).</p>
<p>The main steps of the process can be summarized as:</p>
<p>· Loading the CT image and resampling it programatically. We’ll call the resampled volume ‘resliced’ from here onwards.</p>
<p>· Create a Segmentation node and set the ‘Source Volume’ as ‘resliced’.</p>
<p>· From a labelmap, we generate segments in this segmentation.</p>
<p>· For the linear case, the segments occupy ~300 MB whereas for the event-driven case the segments occupy ~2 GB.</p>
<p>We have also observed for the linear scenario that re-selecting the ‘resliced’ volume as ‘source geometry’ with the ‘Specify Geometry’ button in the SegmentEditor extension, the segments increase their memory size from ~300 MB to ~2GB.</p>
<p>For additional detail:</p>
<ul>
<li>
<p>In both cases we use the same functions to generate both the segmentation and the segments.</p>
</li>
<li>
<p>In the event-driven approach, the volumeNode is being stored as a global parameter, and functions are being called from classes, which control the button logic to launch each event.</p>
</li>
</ul>
<p>So, to summarize, we have a couple questions:</p>
<ul>
<li>
<p>Is it possible that our non-linear approach has a negative effect on RAM usage?</p>
</li>
<li>
<p>Can this effect be associated with the use of global variables to store the reference to the VolumeNode?</p>
</li>
<li>
<p>Why resetting the source geometry by hand increases the memory needed to store segments?</p>
</li>
</ul>
<p>Thank you all in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2024-03-13 16:34 UTC)

<p>These mechanisms should explain all the variations in memory size that you described:</p>
<ul>
<li>Segmentation geometry is determined from the source volume you select first.</li>
<li>If you then select a source volume that has a different geometry than the segmentation then an internal temporary volume is created that stores the source volume resampled to the segmentation’s geometry.</li>
<li>If you import a segment into a segmentation then it is not resampled until it is necessary (to allow copying segments between segmentations without data loss and heavy computation). When you edit any of the segments then it may trigger resampling of all segments.</li>
</ul>

---

## Post #3 by @SANTIAGO_PENDON_MING (2024-03-14 08:21 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>  for a quick an enlightening answer. We have noticed all this behaviours but we were not sure about their origin. Now it’s clear. But one question remains:</p>
<p>The code using <code>input('text')</code> to stop the script, calls the functions in exactly the same way the code driven with buttons. Both codes uses the line:</p>
<pre><code class="lang-auto">segmentEditorWidget.setSourceVolumeNode(volumeNode)
</code></pre>
<p>, all the times we need to automatically create and modify segments. Calling this line could affect to memory size segment if we uses it every time we create a new segment in the same segmentation? In that case, why this could affect in button process and not in input process?</p>
<p>The following code is the start of the segmentation process:</p>
<pre><code class="lang-auto">    # 1. Create the empty segmentation in slicer
    
    if (slicer.mrmlScene.GetNodesByClassByName('vtkMRMLSegmentationNode', segmentation_name).GetNumberOfItems() &gt; 0):
        # Segmentation node exists
        segmentationNode = slicer.mrmlScene.GetNodesByClassByName('vtkMRMLSegmentationNode', segmentation_name).GetItemAsObject(0)
    else:
        segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", segmentation_name)
            
    
    segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(volumeNode)

    segmentPrefix = f'{patientID}'
    segmentId = segmentationNode.GetSegmentation().AddEmptySegment(segmentPrefix)
    
    # Use random color
    red = random.random()
    green = random.random()
    blue = random.random()
    segmentationNode.GetSegmentation().GetSegment(segmentId).SetColor(red,green,blue)
    segmentationNode.GetSegmentation().SetConversionParameter("Smoothing factor","0.0")
       

    # Get segment as numpy array
    segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
</code></pre>
<p>Thanks for your helpful responses <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"> .</p>

---
