---
topic_id: 5304
title: "Relationship Between Segmenteditorwidget And Segmenteditorno"
date: 2019-01-07
url: https://discourse.slicer.org/t/5304
---

# Relationship between SegmentEditorWidget and SegmentEditorNode?

**Topic ID**: 5304
**Date**: 2019-01-07
**URL**: https://discourse.slicer.org/t/relationship-between-segmenteditorwidget-and-segmenteditornode/5304

---

## Post #1 by @mikebind (2019-01-07 21:26 UTC)

<p>I am working on a set of custom extensions, and I have been able to muddle through to get several things working, but I am now running into problems and having trouble debugging.  I think my problem may be related to not understanding the relationship between a segmentEditorWidget and a segmentEditorNode.  For example, in my code I create a segmentEditorWidget and a segmentEditorNode, add them to the mrmlScene, and try to link them together:</p>
<pre><code>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(newSegmentationNode) # This doesn't seem to link the widget to the new segmentation node, it still seems to link to an older, pre-existing segmentation node

segmentEditorWidget.setMRMLScene(slicer.mrmlScene) 
# Not sure if I should do this:
segmentEditorWidget.setMasterVolumeNode(volumeNode)
# or this:
segmentEditorNode.SetAndObserveMasterVolumeNode(volumeNode)

segmentEditorNode.SetAndObserveSegmentationNode(newSegmentationNode) # this line does seem to successfully link to the new segmentation node
</code></pre>
<p>I’m not sure how to properly understand the relationship between the widget and the node.  If I change something in one of them, when is that reflected in the other, and when is it not?  For my purposes, I want to start from an existing segmentation, make a copy of it, and then make several modifications to the new, copied segmentation.  Can I get by without using a widget at all, since I never need to interact with it graphically?  If so, how can I do the equivalent of segmentEditorWidget.setActiveEffectByName() and effect = segmentEditorWidget.activeEffect()?  I am aware of the documentation at <a href="http://apidocs.slicer.org" rel="nofollow noopener">apidocs.slicer.org</a> and find it helpful sometimes, but it never contains anything like a readable explanation of the logical structure of things, just a few word notes (if I am lucky!).</p>
<p>For example, at <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html</a>, I see that there is a function SetActiveEffectName(), but it isn’t clear to me whether that function means I am assigning a name to an active effect or selecting a name.  It allows me to use any string as an argument, even one which does not correspond to any of the set of possible active effects, which makes me worried that I am not selecting an effect but rather creating a name for an effect, but it could easily be that there just isn’t any error checking to make sure that the effect name I supply actually corresponds to an effect.  I don’t see anything in the documentation which would help me figure out which of those is happening. I am a relatively novice python programmer and worse than novice C++ programmer, so when things get down to the C++ code, looking at the source code is only sometimes helpful and is entirely lacking in nuance for me.</p>
<p>Is there any reference which outlines the basic programming design for slicer and/or vtk?  I mean something which might say something like “display nodes hold parameters related to the 2D and 3D display of segmentations.  For a given segmentation node, it’s display node can be accessed through segmentationNode.GetDisplayNode()” or simple explanations like that.   Thanks for any help you can provide.</p>

---

## Post #2 by @lassoan (2019-01-08 04:03 UTC)

<p><em>slicer.qMRMLSegmentEditorWidget</em> is a GUI widget. <em>slicer.vtkMRMLSegmentEditorNode</em> is a MRML node.</p>
<p><a href="https://github.com/PerkLab/PerkLabBootcamp/raw/master/Doc/day3_2_SlicerProgramming.pptx">These slides</a> should answer your questions.</p>
<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="5304">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>there is a function SetActiveEffectName(), but it isn’t clear to me whether that function means I am assigning a name to an active effect or selecting a name</p>
</blockquote>
</aside>
<p>It activates an effect.</p>
<p>There are many examples (short code snippets and full segmentation workflows) available in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>Feel free to ask if you cannot find the answer to any of your questions.</p>

---

## Post #3 by @mikebind (2019-01-08 21:18 UTC)

<p>Thanks, those slides are very helpful and will help organize my thinking about how to properly structure and use modules.</p>

---

## Post #4 by @pieper (2019-01-09 00:54 UTC)

<p>Agreed.  Why don’t we link them directly from here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a></p>

---

## Post #5 by @lassoan (2019-01-09 01:07 UTC)

<p>It was already added to nightly version, but now I’ve added it to 4.10, too.</p>

---
