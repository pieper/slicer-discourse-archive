---
topic_id: 26810
title: "Cannot Get Display Node Of Customized Markups In C"
date: 2022-12-19
url: https://discourse.slicer.org/t/26810
---

# Cannot get display node of customized markups in c++

**Topic ID**: 26810
**Date**: 2022-12-19
**URL**: https://discourse.slicer.org/t/cannot-get-display-node-of-customized-markups-in-c/26810

---

## Post #1 by @nnzzll (2022-12-19 02:37 UTC)

<p>I customized a node called <code>vtkMRMLDeformableROINode</code> which is derived from <code>vtkMRMLMarkupsNode</code>.<br>
I tried to get its display node and set some properties.</p>
<p>The code below written in python works fine without any problem:</p>
<pre><code class="lang-auto">roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDeformableROINode")
# setup Node ...
displayNode = roiNode.GetDisplayNode()
displayNode.SetDisplayableOnlyInView("vtkMRMLSliceNodeRed")
</code></pre>
<p>However, when I trying to do the same thing in C++:</p>
<pre><code class="lang-auto">auto displayNode = vtkMRMLMarkupsDisplayNode::SafeDownCast(roiNode-&gt;GetDisplayNode());
displayNode-&gt;SetDisplayableOnlyInView("vtkMRMLSliceNodeRed");
</code></pre>
<p>Segmentation fault occured  and by printing out the backtrace I found out that <code>roiNode-&gt;GetDisplayNode()</code> returned a <code>nullptr</code>.</p>
<p>Why does the C++ code performed different with python code? How can I fix it?</p>

---

## Post #2 by @nnzzll (2022-12-19 02:47 UTC)

<p>I figured out the reason.</p>
<p>In c++ version, I called <code>qSlicerApplication::application()-&gt;mrmlScene()-&gt;StartState(vtkMRMLScene::BatchProcessState)</code> before adding the new node. If I comment out this line, everything works just fine.</p>
<p>So can anyone gives an advice about how or when should I use the <strong>State</strong> feature?</p>

---

## Post #3 by @lassoan (2022-12-19 05:03 UTC)

<p>After you create a new displayable node programmatically it is your responsibility to add display node as well. The easiest way for creating the display node and associate it with the markup node is to call <code>CreateDefaultDisplayNodes()</code> method.</p>
<aside class="quote no-group" data-username="nnzzll" data-post="2" data-topic="26810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nnzzll/48/16350_2.png" class="avatar"> nnzzll:</div>
<blockquote>
<p>So can anyone gives an advice about how or when should I use the <strong>State</strong> feature?</p>
</blockquote>
</aside>
<p>Use it if you manipulate at least 10-20 nodes. Starting/ending batch processing state is quite costly (rebuilds scene models in all node selector GUI widgets, etc.), so it is only worth activating it if you save a lot of time by not ignoring scene updates during the batch process state.</p>

---
