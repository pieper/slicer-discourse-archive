---
topic_id: 28342
title: "How To Programmatically Add Control Points In Slicer From A"
date: 2023-03-13
url: https://discourse.slicer.org/t/28342
---

# How to programmatically add control points in slicer from a numpy array

**Topic ID**: 28342
**Date**: 2023-03-13
**URL**: https://discourse.slicer.org/t/how-to-programmatically-add-control-points-in-slicer-from-a-numpy-array/28342

---

## Post #1 by @mukund_shah (2023-03-13 12:55 UTC)

<p>In slicer documentation following example</p>
<pre><code class="lang-auto">curveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
slicer.util.updateMarkupsControlPointsFromArray(curveNode, pointPositions)
</code></pre>
<p>where pointPositions is a numpy array but this gives a open markup curve ,what I want to do is just add markup points so I did this</p>
<pre><code class="lang-auto">markup_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsNode")
slicer.util.updateMarkupsControlPointsFromArray(markup_node, pointPositions)
</code></pre>
<p>But this is not adding any points as markup points</p>

---

## Post #2 by @lassoan (2023-03-13 14:04 UTC)

<aside class="quote no-group" data-username="mukund_shah" data-post="1" data-topic="28342">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mukund_shah/48/18282_2.png" class="avatar"> mukund_shah:</div>
<blockquote>
<p><code>markup_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsNode")</code></p>
</blockquote>
</aside>
<p><code>vtkMRMLMarkupsNode</code> is an abstract base class. You cannot instantiate it, but only a concrete child class. See the list of child classes in the <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html">inheritance diagram</a>.</p>

---

## Post #3 by @mukund_shah (2023-03-13 16:39 UTC)

<p>Thanks ,solution to this problem is to use <strong>vtkMRMLMarkupsFiducialNode</strong> class</p>

---

## Post #4 by @mukund_shah (2023-03-13 17:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> i am now able to put  markup points programmatically but since the number of points I am displaying is too large I have to rename them manually from eg <strong>Markuppoint_1</strong> to 1 for better visibility,is there a way to show the points without their names?</p>

---

## Post #5 by @ebrahim (2023-03-13 18:05 UTC)

<p><a class="mention" href="/u/mukund_shah">@mukund_shah</a> I haven’t found a way to turn off the label completely with fiducials but you can set the text scale to zero with <code>markup_node.GetDisplayNode().SetTextScale(0)</code>. Example:</p>
<pre><code class="lang-py">import numpy as np
markup_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
slicer.util.updateMarkupsControlPointsFromArray(markup_node, np.random.rand(10,3))
markup_node.GetDisplayNode().SetTextScale(0)
</code></pre>

---

## Post #6 by @smrolfe (2023-03-13 18:27 UTC)

<aside class="quote no-group" data-username="ebrahim" data-post="5" data-topic="28342">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>I haven’t found a way to turn off the label completely with fiducials</p>
</blockquote>
</aside>
<p>This can be done using:<br>
<code>markup_node.GetDisplayNode().SetPointLabelsVisibility(False)</code></p>

---
