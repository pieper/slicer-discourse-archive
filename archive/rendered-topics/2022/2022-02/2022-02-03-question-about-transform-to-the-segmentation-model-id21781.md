---
topic_id: 21781
title: "Question About Transform To The Segmentation Model"
date: 2022-02-03
url: https://discourse.slicer.org/t/21781
---

# Question about transform to the segmentation model

**Topic ID**: 21781
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/question-about-transform-to-the-segmentation-model/21781

---

## Post #1 by @user5 (2022-02-03 16:24 UTC)

<p>I would like to use python script to move the segmentation model which is imported by a STL model.</p>
<p>I try to use these code to finish it.</p>
<blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-a-transformation-matrix-from-a-numpy-array" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
</blockquote>
<blockquote>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#example-of-moving-a-volume-along-a-trajectory-using-a-transform" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
</blockquote>
<p>I combine them together, but it is not work.</p>
<pre><code class="lang-auto"># Create a 4x4 transformation matrix as numpy array
transformNode = ...
transformMatrixNP = np.array(
  [[0.92979,-0.26946,-0.25075,52.64097],
  [0.03835, 0.74845, -0.66209, -46.12696],
  [0.36608, 0.60599, 0.70623, -0.48185],
  [0, 0, 0, 1]])

# Update matrix in transform node
transformNode.SetAndObserveMatrixTransformToParent(slicer.util.vtkMatrixFromArray(transformMatrixNP)
slicer.mrmlScene.AddNode(transformNode)
rcm_1.SetAndObserveTransformNodeID(transformNode.GetID())
</code></pre>
<p>I would like to know the problem of my code and how to improve it.<br>
Is it have any other way to do the automatic transform on segmentation model?</p>

---

## Post #2 by @mikebind (2022-02-03 21:32 UTC)

<p>The 2nd line of your code is not functional python code.  The <code>...</code> needs to be replaced with wherever you are getting the transform node from.  Simplest is to create it. Assuming your model node is named <code>rcm_1</code>, the following code should work.</p>
<pre><code class="lang-auto">import numpy as np # need to import numpy before np.array will work
transformNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', 'myNewTransformNode')
transformMatrixNP = np.array(
  [[0.92979,-0.26946,-0.25075,52.64097],
  [0.03835, 0.74845, -0.66209, -46.12696],
  [0.36608, 0.60599, 0.70623, -0.48185],
  [0, 0, 0, 1]])
# Change transformation matrix in the transform node
transformNode.SetAndObserveMatrixTransformToParent(slicer.util.vtkMatrixFromArray(transformMatrixNP))
# Apply transformation to the model in rcm_1
rcm_1.SetAndObserveTransformNodeID(transformNode.GetID())
</code></pre>
<p>You mentioned that your segmentation is an imported STL model and this code will work for that.  Note that in Slicer, not just models, but also segmentations, images, and markups can all have transforms applied.</p>
<p>Hopefully this code helps you get started.</p>

---

## Post #3 by @user5 (2022-02-04 15:02 UTC)

<p>It works well <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:">.<br>
Thanks you so much.</p>

---
