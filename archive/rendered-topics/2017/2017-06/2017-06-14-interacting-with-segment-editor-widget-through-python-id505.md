---
topic_id: 505
title: "Interacting With Segment Editor Widget Through Python"
date: 2017-06-14
url: https://discourse.slicer.org/t/505
---

# Interacting with Segment Editor Widget through Python

**Topic ID**: 505
**Date**: 2017-06-14
**URL**: https://discourse.slicer.org/t/interacting-with-segment-editor-widget-through-python/505

---

## Post #1 by @kohle (2017-06-14 20:57 UTC)

<p>Hi I’m new to the slicer python api and was wondering if someone could point me in the right direction.<br>
I would like to use a the python api to create serveral segements through the “Logic operators” function of the segment editor widget.  I would like to create these segements from existing segments.</p>
<p>I managed to load an example extentsion for slicer in which I select the master volume and segmentation through python.</p>
<p>My main question is how I can find out about the different classes and functions that I want to use.<br>
For example:<br>
How do I change the “overwrite other segment” parameter ?<br>
I found the setActiveEffectByName funtction were can I find its parameters ?<br>
How do figure out what the SegmentID of each segment is?</p>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2017-06-15 02:02 UTC)

<p>API of SegmentEditor:<br>
<a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html" class="onebox" target="_blank">http://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html</a></p>
<p>Examples for using segmentations and segment editor from Python scripts: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations</a></p>
<p>Let us know if you have more questions.</p>

---

## Post #3 by @kohle (2017-06-15 10:00 UTC)

<p>Thanks for pointing me in the right direction.</p>
<p>I am not quite sure how to set the parameters of the effects.</p>
<pre><code>effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation", LOGICAL_INTERSECT)
</code></pre>
<p>Does not seem to be the right code.<br>
Also I don’t know how to change the name of new segments after creating them.</p>
<pre><code>inSegmentation.GetSegmentation().AddEmptySegment(segmentName = "test")
</code></pre>
<p>Does not work for me.<br>
Neither does changing the name after creating it with</p>
<pre><code>inSegmentation.GetSegmentation().GetNthSegment(1).SetName("test")
</code></pre>
<p>Can someone please point out my mistakes?</p>

---

## Post #4 by @kohle (2017-06-15 11:14 UTC)

<p>I manged to find a the problem with</p>
<pre><code>inSegmentation.GetSegmentation().AddEmptySegment(segmentName = "test")
</code></pre>
<p>it is meant to be</p>
<pre><code> inSegmentation.GetSegmentation().AddEmptySegment("test")
</code></pre>
<p>this changes name and ID of the segment.</p>

---

## Post #5 by @lassoan (2017-06-15 16:59 UTC)

<p>Also note there are convenience functions for creating segments directly from polydata or labelmap:<br>
<code>segmentationNode.AddSegmentFromClosedSurfaceRepresentation(...)</code> and<br>
<code>segmentationNode.AddSegmentFromBinaryLabelmapRepresentation(..)</code> in <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html">segmentation node</a>; or importing from existing model or labelmap nodes using <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html">segmetations module logic</a></p>

---

## Post #6 by @kohle (2017-06-16 11:29 UTC)

<p>Thanks for your help again.</p>
<p>I  would like to create new segmentations with the threshold tool and save them. I am not sure if using the widget is the best way to do it. How do you think I can achive this easiest?<br>
Where can I find the different parameters each editor effect accepts ? as this does not seem to work:</p>
<pre><code>effect.setParameter("Operation", LOGICAL_INTERSECT)</code></pre>

---

## Post #7 by @lassoan (2017-06-16 17:02 UTC)

<aside class="quote no-group" data-username="kohle" data-post="6" data-topic="505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/f04885/48.png" class="avatar"> kohle:</div>
<blockquote>
<p>as this does not seem to work</p>
</blockquote>
</aside>
<p>Do you get an error message? Please copy-paste it here.</p>

---

## Post #8 by @kohle (2017-06-17 21:00 UTC)

<p>Thanks again for your great support. I managed to set the parameters with</p>
<pre><code>effect.setParameter("Operation","INTERSECT")</code></pre>

---

## Post #9 by @lassoan (2017-08-09 21:20 UTC)

<p>A post was split to a new topic: <a href="/t/set-segmentation-master-volume-from-python/851">Set segmentation master volume from Python</a></p>

---

## Post #10 by @moselhy (2017-08-25 00:42 UTC)

<p>How do I get the segmenteditor widget from Python when I am in the SegmentEditorEffect class? I want to use the setActiveEffectByName method</p>

---

## Post #11 by @lassoan (2017-08-25 02:17 UTC)

<p>self.scriptedEffect.selectEffect(“Paint”)</p>

---
