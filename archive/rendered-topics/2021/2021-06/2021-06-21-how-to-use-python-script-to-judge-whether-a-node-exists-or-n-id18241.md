# How to use Python script to judge whether a node exists or not

**Topic ID**: 18241
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/how-to-use-python-script-to-judge-whether-a-node-exists-or-not/18241

---

## Post #1 by @qiqi5210 (2021-06-21 07:10 UTC)

<p>segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
After creating a node, you don’t want to create a new node. How to judge whether a node has been created</p>

---

## Post #2 by @Juicy (2021-06-21 07:35 UTC)

<p>I don’t know exactly what you want to do but here is a snippet of code I used to check whether there are any segmentation nodes in the scene and if so, cycle through them all and turn their visibility off so that they are hidden. You may be able to use some part of it or something similar for what you are doing.</p>
<pre><code class="lang-auto">  # Hide all Segments
  noOfSegmentationNodes = slicer.mrmlScene.GetNumberOfNodesByClass('vtkMRMLSegmentationNode')
  if noOfSegmentationNodes &gt; 0:
    for i in range(0, noOfSegmentationNodes):
      currentSegment = slicer.mrmlScene.GetNthNodeByClass(i, 'vtkMRMLSegmentationNode')
      currentSegment.SetDisplayVisibility(0)
</code></pre>

---

## Post #3 by @lassoan (2021-06-21 13:30 UTC)

<aside class="quote no-group" data-username="qiqi5210" data-post="1" data-topic="18241">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qiqi5210/48/15920_2.png" class="avatar"> qiqi5210:</div>
<blockquote>
<p>How to judge whether a node has been created</p>
</blockquote>
</aside>
<p>If you develop a module: You would normally store the selected node as a node reference in a parameter node. If you create a new module using Extension Wizard module then the generated module already works like this. You can also look at many other Python modules in Slicer core and extensions.</p>
<p>If you develop a script: store the node in some variable. If you create the node in a function then return that variable from the function.</p>

---
