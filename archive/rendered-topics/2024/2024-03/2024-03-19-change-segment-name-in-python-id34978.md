---
topic_id: 34978
title: "Change Segment Name In Python"
date: 2024-03-19
url: https://discourse.slicer.org/t/34978
---

# Change segment name in python

**Topic ID**: 34978
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/change-segment-name-in-python/34978

---

## Post #1 by @rkraaijveld (2024-03-19 15:40 UTC)

<p>Hi!</p>
<p>I’m making a module where I go through the connected components in the image (by clicking previous/next) and give them a label according to the button a user has pressed. For example, the user goes through the segmentations and assigns the correct organ to the segmentation by clicking on one of the three buttons: Liver, Brain or Other.</p>
<p>I want to now change the name of the segmentation according to the button that they have pressed. How do I get the segment ID that the segment editor is currently on?</p>
<p>I know you can get an ID or name of a segment like this:<br>
segment =  self.segmentation_node.GetSegment(segment_ID)</p>
<p>but I don’t know the ID/name. I just want to get the ID of the current segment that is selected in the segment editor.</p>
<p>Any advice will be appreciated! Thanks!</p>

---

## Post #2 by @mikebind (2024-03-19 16:46 UTC)

<p>The currently selected segment is a property of the segment editor node, rather than the segmentation itself.  Conceptually, the segmentation node holds the segmentation itself, while a segment editor node modifies the segmentation in a segmentation node.  With this separation, it would be possible for a segmentation to be being modified by two independent segment editors, for example.  So, what you need is the segment editor node that the user is selecting the current segment with.  Then, you can get the segment ID of the currently selected segment and change its name with something like</p>
<pre><code class="lang-auto">newSegmentName = 'Liver'
currentSegmentID = mySegmentEditorNode.GetSelectedSegmentID()
segmentationNode = mySegmentEditorNode.GetSegmentationNode()
currentSegment = segmentationNode.GetSegmentation().GetSegment(currentSegmentID)
currentSegment.SetName(newSegmentName)
</code></pre>

---

## Post #3 by @rkraaijveld (2024-03-19 16:53 UTC)

<p>Thanks for helping me out!</p>
<p>At the moment I have this:</p>
<pre><code class="lang-auto">segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
currentSegmentID = segmentEditorNode.GetSelectedSegmentID()
segmentationNode = segmentEditorNode.GetSegmentationNode()
currentSegment = segmentationNode.GetSegmentation().GetSegment(currentSegmentID)
</code></pre>
<p>But I get this error:</p>
<pre><code class="lang-auto">File "C:/Users/.../CheckSeg.py", line 306, in confirm_label_clicked
    currentSegment = segmentationNode.GetSegmentation().GetSegment(currentSegmentID)
AttributeError: 'NoneType' object has no attribute 'GetSegmentation'
</code></pre>
<p>What am I doing wrong?</p>

---

## Post #4 by @mikebind (2024-03-19 20:57 UTC)

<p>You have created a new segment editor node, which has not been associated with a segmentation yet. Instead, what you want to do is access the segment editor node which is associated with the Slicer GUI.  You can do this via</p>
<pre><code class="lang-auto">segmentEditorNode = slicer.modules.SegmentEditorWidget.editor.mrmlSegmentEditorNode()
</code></pre>
<p>I also learned while investigating this that as an alternative path, you can get the current segment ID and segmentation node directly from the segment editor widget via:</p>
<pre><code class="lang-auto">currentSegmentID = slicer.modules.SegmentEditorWidget.editor.currentSegmentID() 
segmentationNode = slicer.modules.SegmentEditorWidget.editor.segmentationNode()
</code></pre>
<p>Either way should work equivalently.</p>

---

## Post #5 by @rkraaijveld (2024-03-20 10:58 UTC)

<p>Thanks!! This worked for me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @cpinter (2024-10-24 08:30 UTC)

<p>A post was split to a new topic: <a href="/t/error-when-changing-segment-name-from-python/39831">Error when changing segment name from Python</a></p>

---
