---
topic_id: 20633
title: "How To Import Fiducial Points Into Segment Editor"
date: 2021-11-16
url: https://discourse.slicer.org/t/20633
---

# How to import Fiducial points into Segment Editor?

**Topic ID**: 20633
**Date**: 2021-11-16
**URL**: https://discourse.slicer.org/t/how-to-import-fiducial-points-into-segment-editor/20633

---

## Post #1 by @Karthik (2021-11-16 03:23 UTC)

<p>I have some fiducial points which I have placed using the fiducial selector in a module. If I go to Data, I can see the Markups there. I am now creating an effect in Segment Editor. How can I import the markups present in scene in to an Effect in Segment Editor?<br>
Some Segment Editor effects such as Surface Cut, Draw Tube and Engrave have option to place fiducial points, but these seem to be temporary as they are not visible outside of the Segment Editor.<br>
So, please suggest a way to get markups in scene into Segment Editor, and save Markups from Segment Editor to scene.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-11-16 06:29 UTC)

<p>You cannot use existing points in the Surface Cut and Draw Tube effects. It would not be hard to implement the possibility to import an existing markup, but this need has not come up often enough. You can submit a feature request to <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/issues" class="inline-onebox">Issues · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a> and if it gets many votes (add thumbs-up reaction to the first post there) then someone will implement it.</p>
<p>Until then, you can use “MarkupsToModel” extension to generate models of tubes or closed surfaces that you can drag-and-drop into a segmentation. This extension uses the same underlying classes as the two segment editor effects.</p>

---

## Post #3 by @Karthik (2021-11-16 07:25 UTC)

<p>If you give me a brief idea of how to implement it, I can get started. Do I have to make changes to qSlicerSegmentEditorAbstractEffect class?<br>
Just as Volume is available inside Segment Editor to select Master Volume, I would like to import markups.</p>

---

## Post #4 by @lassoan (2021-11-16 13:54 UTC)

<p>You can add a markups points selector and an Import button to both the Draw Tube and Surface Cut effects by modifying these files:</p>
<ul>
<li><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py" class="inline-onebox">SlicerSegmentEditorExtraEffects/SegmentEditorEffect.py at master · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a></li>
<li><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSurfaceCut/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py" class="inline-onebox">SlicerSegmentEditorExtraEffects/SegmentEditorEffect.py at master · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a></li>
</ul>
<p>If you add this feature and test it locally then submit a pull request and we’ll review and add it to the extension.</p>

---

## Post #5 by @Karthik (2021-11-17 04:02 UTC)

<p>Thank you for your guidance.<br>
So, from what I understand, I need to implement an Import Button which is able to get the markups that are stored in scene and make them available inside the Effect.<br>
Then, I need to implement a markups points selector which is a dropdown consisting of all the markups available (which have been imported using the import button). Using this, I will be able to import any markups fiducials from the ones available in scene.</p>
<p>Please help in understanding how to import markups from scene into our effect. I am aware of sitkUtils.PullVolumeFromSlicer to get the volume from scene into our script. But, does such a thing exist for markups?</p>
<p>Also, I have implemented some extensions in python. I am wondering whether I should have some of that code as an Effect inside Segment Editor. Is this a good idea? What are the circumstances where one would look to create an Extension vs an Effect?<br>
I understand that operations such as Thresholding or Smoothing might make good Effects but if I wanted to perform a series of operations such as thresholding, levelset segmentation, smoothing etc. one after the other, would it be better to implement it as a Module in an extension or as an Effect?</p>

---

## Post #6 by @lassoan (2021-11-17 06:02 UTC)

<aside class="quote no-group" data-username="Karthik" data-post="5" data-topic="20633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9fc348/48.png" class="avatar"> Karthik:</div>
<blockquote>
<p>Please help in understanding how to import markups from scene into our effect. I am aware of sitkUtils.PullVolumeFromSlicer to get the volume from scene into our script. But, does such a thing exist for markups?</p>
</blockquote>
</aside>
<p>sitkUtils.PullVolumeFromSlicer is for copying a SimpleITK image into a Slicer volume node. Copying data between Slicer nodes is much simpler. For example, you can call:</p>
<pre data-code-wrap="python"><code class="lang-python">self.segmentMarkupNode.CopyContent(fiducialNodeToImportFrom)
</code></pre>
<aside class="quote no-group" data-username="Karthik" data-post="5" data-topic="20633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9fc348/48.png" class="avatar"> Karthik:</div>
<blockquote>
<p>Also, I have implemented some extensions in python. I am wondering whether I should have some of that code as an Effect inside Segment Editor. Is this a good idea? What are the circumstances where one would look to create an Extension vs an Effect?</p>
</blockquote>
</aside>
<p>If you want to make any module available for others then you need to put them into an extension. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html">here</a>.</p>
<p>If you implement interactive segmentation tools then I would recommend to make them available as Segment Editor effects so that users can easily access it along with other interactive tools in the Segment Editor module. If you implement an automated segmentation workflow then it may make more sense to create a separate scripted module, with a simple GUI (input image and output segmentation node selectors and maybe a few more widgets to set some additional segmentation parameters).</p>

---
