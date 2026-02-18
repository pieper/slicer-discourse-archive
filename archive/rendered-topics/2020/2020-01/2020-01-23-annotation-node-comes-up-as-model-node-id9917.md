# Annotation Node comes up as Model Node

**Topic ID**: 9917
**Date**: 2020-01-23
**URL**: https://discourse.slicer.org/t/annotation-node-comes-up-as-model-node/9917

---

## Post #1 by @Juicy (2020-01-23 05:46 UTC)

<p>Hi all,</p>
<p>I was trying to make some code to pick the last model node which was created in the scene. This is what I tried:</p>
<pre><code>noOfModelNodes = slicer.mrmlScene.GetNumberOfNodesByClass('vtkMRMLModelNode')
lastModel = slicer.mrmlScene.GetNthNodeByClass(noOfModelNodes - 1, 'vtkMRMLModelNode')
</code></pre>
<p>this code works fine for any other node type but for models it has errors. I decided to try and investigate. So I opened up a blank slicer instance and typed in the first line of code above. The noOfModelNodes is equal to 3 which is fine as there seem to be some model nodes present from startup in the node list (seen in the data module).</p>
<p>I then placed a ruler in the scene and ran the first line of code again and noticed that now noOfModelNodes = 4. Why is the ruler node coming up as a vtkMRMLModelNode?</p>
<p>To double check I put in the code:</p>
<pre><code>model = slicer.mrmlScene.GetNthNodeByClass(3, 'vtkMRMLModelNode')
model.GetClassName()
</code></pre>
<p>which gave me ‘vtkMRMLAnnotationRulerNode’. My question is why does slicer think that the ruler node is a model node? ROI nodes seem to be included as model nodes as well. I have tried this on 4.10.2 and the latest nightly build and the behavior is the same.</p>
<p>Also if anyone has any better suggestions of how to get the most recent model node in the scene then I would be keen to hear</p>

---

## Post #2 by @pieper (2020-01-23 10:05 UTC)

<p>Hi -</p>
<p>An annotation is a special type of model (see <a href="https://apidocs.slicer.org/v4.10/classvtkMRMLAnnotationNode.html">this diagram</a>).  You can just iterate until you get to a node that is a model node (check the class name).</p>

---

## Post #3 by @Juicy (2020-01-23 19:36 UTC)

<p>Thanks a lot for the clarification Steve. This was confusing me. I have updated my code and the following worked for me:</p>
<pre><code># get most recent model
noOfModelNodes = slicer.mrmlScene.GetNumberOfNodesByClass('vtkMRMLModelNode')
for i in range(0, noOfModelNodes):
  currentModel = slicer.mrmlScene.GetNthNodeByClass(i, 'vtkMRMLModelNode')
  if currentModel.GetClassName() == 'vtkMRMLModelNode':
    mostRecentModel = currentModel</code></pre>

---
