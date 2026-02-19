---
topic_id: 3504
title: "Improve Segmentation Paint And Erase Or Scissors Effects In"
date: 2018-07-17
url: https://discourse.slicer.org/t/3504
---

# Improve segmentation : "Paint" and "Erase" (or "Scissors") effects in Segment Editor or Sphere brush?

**Topic ID**: 3504
**Date**: 2018-07-17
**URL**: https://discourse.slicer.org/t/improve-segmentation-paint-and-erase-or-scissors-effects-in-segment-editor-or-sphere-brush/3504

---

## Post #1 by @Laura (2018-07-17 14:30 UTC)

<p>Good afternoon,</p>
<p>First of all, thanks a lot to the one that is going to read my message !<br>
I am currently an intern doing the segmentation of an organ on 3D Slicer (I am so new on 3D Slicer).<br>
However, I have some problems by improving this segmentation…</p>
<p>From scanner volume in dicom and after image treatments, I have a “vtkMRMLScalarVolumeNode” which represents my organ segmented in white with a grey background.<br>
I would like to add some pixels that have been erased by mistake to my segmentation and also erase some pixels that are in my segmentation by mistake…<br>
After trying different techniques, I think that “Segment editor” with “Paint” and “Erase” could do the job perfectly.</p>
<p>However, these two effects don’t have any “self().onApply()” function so I can’t set the result in my segmentation.<br>
I have tried so many different ways to do this but unfortunately nothing works…<br>
Currently, I have written that on my python script :</p>
<blockquote>
<p>segmentEditorWidget.setActiveEffectByName(“Paint”)<br>
effect = segmentEditorWidget.activeEffect()	<br>
effect.SetParameter(“Paint, sphere”, “1”) # Agir en 3D sur image<br>
segmentEditorWidget = None<br>
slicer.mrmlScene.RemoveNode(segmentEditorNode)<br>
segmentationNode.CreateClosedSurfaceRepresentation()</p>
</blockquote>
<p>However, I don’t succeed in :</p>
<ul>
<li>Open “Segment Editor” as a little window in the foreground with my module extension in the background<br>
(my code generates that the “Segment editor” window appears as fast as it disappears…)</li>
<li>“Paint” on my segmented organ</li>
<li>Save the paint pixels as if they become part of my segmented organ</li>
<li>Get my new segmentation upgraded</li>
</ul>
<p>As a consequence, I have the same problems with “Erase” and “Scissors” effects…<br>
I hope that I have been clear a little bit<br>
It would be so grateful if someone could help me !<br>
Thanks a lot in advance<br>
Laura</p>

---

## Post #2 by @lassoan (2018-07-17 21:09 UTC)

<aside class="quote no-group" data-username="Laura" data-post="1" data-topic="3504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>Open “Segment Editor” as a little window in the foreground with my module extension in the background</p>
</blockquote>
</aside>
<p>You can embed a segment editor widget directly into your module’s user interface.</p>
<aside class="quote no-group" data-username="Laura" data-post="1" data-topic="3504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a4c791/48.png" class="avatar"> Laura:</div>
<blockquote>
<p>“Paint” on my segmented organ</p>
</blockquote>
</aside>
<p>You can use the segment editor widget to paint (activate the effect then draw in any of the views).</p>
<p>If you want to paint/erase at a certain position using Python script, you can create a sphere-shaped segment as <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b#file-segmentgrowcutsimple-py-L16-L21">shown in this example</a>. Then use logical operators effect to add (paint) or subtract (erase) this segment from the segment that you would like to modify.</p>

---

## Post #3 by @Laura (2018-07-18 08:00 UTC)

<p>Good morning,</p>
<p>Thanks a lot for your answer !<br>
However I still have some difficulties to implement…</p>
<p>On my python script I have written :</p>
<blockquote>
<pre><code>            segmentationNode = slicer.vtkMRMLSegmentationNode()
	    slicer.mrmlScene.AddNode(segmentationNode)
	    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
	    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolCor)
	    segmentationNode.SetName("SegmentationAffinee")	    
	    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("Foie")
	    
	    lm = slicer.app.layoutManager()
	    for sliceViewName in lm.sliceViewNames():
	      sliceWidget = lm.sliceWidget(sliceViewName)
	      view = lm.sliceWidget(sliceViewName).sliceView()
	      sliceNode = view.mrmlSliceNode()
	      sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
	      compositeNode = sliceLogic.GetSliceCompositeNode()
					## Setup background volume
	      compositeNode.SetBackgroundVolumeID(masterVolumeNode.GetID())
					## Setup foreground volume
	      compositeNode.SetForegroundVolumeID(inputVolCor.GetID())
					## Changer l'opacite
	      compositeNode.SetForegroundOpacity(0.7)
	    
	    editorWidget = slicer.modules.segmenteditor.createNewWidgetRepresentation()
	    editorWidget.setMRMLScene(slicer.app.mrmlScene())
	    editorWidget.show() 
	
	    segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
	    slicer.mrmlScene.AddNode(segmentEditorNode)
</code></pre>
</blockquote>
<p>So :</p>
<ul>
<li>I create my node ‘Foie’ which is used to paint</li>
<li>I am able to get a little window Segment Editor which appears</li>
<li>I use the effect “paint” in some areas of my image vtkMRMLScalarVolumeNode (with the “Edith in 3D views”)</li>
</ul>
<p>But then, I don’t know how to implement “put what is painted as white pixels in my vtkMRMLScalarVolumeNode” just to be able to create only one image which compiled my previous segmentation + my additionnal adjustements with paint (or erase, of course)</p>
<p>I have tried to export segments (that is to say my ‘Foie’ node) but after I don’t know how to put everything together…<br>
Moreover, I would love being able to do everything from my widget extension without going in the different modules on 3D Slicer manually…</p>
<p>Do you know how can I do that, what kind of code I have to add ?<br>
I just add that the areas that I want to paint (or erase) are not previously selected, I have to do that “visually” so it is different from one scanner to another</p>
<p>Thanks a lot in advance<br>
Laura</p>

---

## Post #4 by @Laura (2018-07-18 13:59 UTC)

<p>Good afternoon,</p>
<p>After this second day of only looking for the segment editor tool with “paint” and “erase”, I have maybe another idea that could be easier (I hope so because I despair to succeed in doing this improvement on my image…) :</p>
<ul>
<li>Create a sphere brush</li>
<li>Click with the sphere brush on my image vtkMRMLScalarVolumeNode</li>
<li>Get the voxels values that I have clicked on</li>
<li>Set these values to 255 so that they have the same value as the pixel of my organ segmented<br>
However I haven’t find how to do this even if I have read lot and lot of codes (such as PaintEffect.py and so on)</li>
</ul>
<p>Do you think this is a better idea to get my result ?<br>
Do you know some parts of code that I can use to do this ?<br>
Sorry if this is very easy to answer but it seems to me that I don’t see the end of this road…</p>
<p>Thanks a lot for your help<br>
Laura</p>

---

## Post #5 by @rkikinis (2018-07-18 14:24 UTC)

<p>Hi,</p>
<p>I often mouse over a target area and look at the voxel values displayed in the data probe area in the lower left of the slicer window, when I need to decide on values.</p>
<p>Ron</p>

---

## Post #6 by @Laura (2018-07-18 15:05 UTC)

<p>I agree with you it is possible to do that except that I want to set lots of pixels at a certain value for painting more than my organ segmented (because it misses some voxels after my image treatments) or for erasing some voxels.<br>
That’s why I think it is important to succeed in creating a “sphere brush” in order to get more than one voxel at a time<br>
This is to improve and get a perfect organ segmented (because after I measure distances, volumetric data…and everything is already done, I have just this part that I don’t manage to do)</p>
<p>Thanks a lot for your help !</p>

---
