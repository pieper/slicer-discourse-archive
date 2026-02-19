---
topic_id: 1166
title: "Modification Of Models Color In A Vtkmrmlsequencenode"
date: 2017-10-03
url: https://discourse.slicer.org/t/1166
---

# Modification of model's color in a vtkMRMLSequenceNode

**Topic ID**: 1166
**Date**: 2017-10-03
**URL**: https://discourse.slicer.org/t/modification-of-models-color-in-a-vtkmrmlsequencenode/1166

---

## Post #1 by @laurapascal (2017-10-03 14:50 UTC)

<p>Hi everyone!</p>
<p>I am trying to create a python scripted module using <a href="https://github.com/SlicerRt/Sequences" rel="noopener nofollow ugc">Sequences</a> extension and I have an issue to modify the color of the models in a sequence: I would like to have different color for each model contained in the sequence created.<br>
Here are the two codes that I tried:</p>
<p><strong>First try:</strong> Change of the models’ colors before adding them to the sequence.</p>
<blockquote>
<p>sequence = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceNode())<br>
sequencebrowser = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceBrowserNode())<br>
model0 = slicer.util.loadModel(“path/to/model0.vtk”,True)[1]<br>
model1 = slicer.util.loadModel(“path/to/model1.vtk”,True)[1]<br>
displayNode0 = model0.GetDisplayNode()<br>
displayNode0.SetColor(1,0,0)<br>
displayNode1 = model1.GetDisplayNode()<br>
displayNode1.SetColor(1,1,0)<br>
sequence.SetDataNodeAtValue(model0, “0”)<br>
sequence.SetDataNodeAtValue(model1, “1”)<br>
sequencebrowser.AddSynchronizedSequenceNodeID(sequence.GetID())</p>
</blockquote>
<p> → The models in the sequence stay gray: that’s probably due to the copy of the models in the sequence which didn’t copy the display nodes of the models.</p>
<p><strong>Second try:</strong> Change of the models’ colors after adding them to the sequence.</p>
<blockquote>
<p>sequence = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceNode())<br>
sequencebrowser = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceBrowserNode())<br>
model0 = slicer.util.loadModel(“path/to/model0.vtk”,True)[1]<br>
model1 = slicer.util.loadModel(“path/to/model1.vtk”,True)[1]<br>
model00 = sequence.SetDataNodeAtValue(model0, “0”)<br>
model01 = sequence.SetDataNodeAtValue(model1, “1”)<br>
displayNode0 = slicer.mrmlScene.AddNode(slicer.vtkMRMLModelDisplayNode())<br>
displayNode0.SetColor(1, 0, 0)<br>
displayNode0.VisibilityOff()<br>
displayNode1 = slicer.mrmlScene.AddNode(slicer.vtkMRMLModelDisplayNode())<br>
displayNode1.SetColor(1, 1, 0)<br>
displayNode1.VisibilityOff()<br>
model00.SetAndObserveDisplayNodeID(displayNode0.GetID())<br>
model01.SetAndObserveDisplayNodeID(displayNode1.GetID())<br>
model00.HideFromEditorsOn()<br>
model01.HideFromEditorsOn()<br>
slicer.mrmlScene.AddNode(model00)<br>
slicer.mrmlScene.AddNode(model01)<br>
sequencebrowser.AddSynchronizedSequenceNodeID(sequence.GetID())</p>
</blockquote>
<p>I checked the existence of the display node in one of the model added to the sequence.</p>
<blockquote>
<p><strong>print sequence.GetDataNodeAtValue(“0”).GetDisplayNode()</strong><br>
vtkMRMLModelDisplayNode (0x1310b1600)<br>
ID: vtkMRMLModelDisplayNode6<br>
Debug: Off<br>
Modified Time: 877045<br>
Name: ModelDisplay_2<br>
Description: (none)<br>
SingletonTag: (none)<br>
HideFromEditors: 1<br>
Selectable: 1<br>
Selected: 0<br>
Indent:      0<br>
Color:             0x1310b1848<br>
SelectedColor:     0x1310b1878<br>
SelectedAmbient:   0.4<br>
SelectedSpecular:  0.5<br>
Opacity:           1<br>
Ambient:           0<br>
Diffuse:           1<br>
Specular:          0<br>
Power:             1<br>
Visibility:        1<br>
ScalarVisibility:  0<br>
VectorVisibility:  0<br>
TensorVisibility:  0<br>
InterpolateTexture:0<br>
ScalarRangeFlag:   2<br>
AutoScalarRange:   1<br>
BackfaceCulling:   1<br>
Clipping:          0<br>
SliceIntersectionVisibility: 0<br>
SliceIntersectionThickness: 1<br>
ScalarRange:       0, 1<br>
ColorNodeID: (none)<br>
ActiveScalarName: (none)</p>
</blockquote>
<blockquote>
<p><strong>print sequence.GetDataNodeAtValue(“0”).GetDisplayNode().GetColor()</strong><br>
(1.0, 0.0, 0.0)</p>
</blockquote>
<p> → Even if it seems that the display nodes exist, the models in the sequence also stay gray.</p>
<p>Do you have any idea of what is wrong? Any help will be appreciated! Thanks in advance!<br>
Laura</p>

---

## Post #2 by @lassoan (2017-10-03 14:53 UTC)

<p>If you want to make the display properties change in time, too, then you have to create a sequence node for the Model Display node (the same way as you create a sequence node for the Model node).</p>

---

## Post #3 by @laurapascal (2017-10-03 20:21 UTC)

<p>Thank you for your response!<br>
As you suggested, I tried with the following code to create a second sequence node containing the model display nodes corresponding to the model nodes, unfortunately, it still doesn’t work. Am I still doing something wrong?</p>
<pre><code class="lang-python">model0 = slicer.util.loadModel("path/to/model0.vtk",True)[1]
model1 = slicer.util.loadModel("/path/to/model1.vtk",True)[1]
model0.GetDisplayNode().VisibilityOff()
model0.GetDisplayNode().SetColor(1, 0, 0)
model1.GetDisplayNode().VisibilityOff()
model1.GetDisplayNode().SetColor(1, 1, 0)

sequence = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceNode())
sequence.SetDataNodeAtValue(model0, "0")
sequence.SetDataNodeAtValue(model1, "1")
 
displayNodeSequence = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceNode())
displayNodeSequence.SetDataNodeAtValue(model0.GetDisplayNode(), "0")
displayNodeSequence.SetDataNodeAtValue(model1.GetDisplayNode(), "1")

sequencebrowser = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceBrowserNode())
sequencebrowser.AddSynchronizedSequenceNodeID(displayNodeSequence.GetID())
sequencebrowser.AddSynchronizedSequenceNodeID(sequence.GetID())
</code></pre>

---

## Post #4 by @jcfr (2017-10-03 20:24 UTC)

<p><a class="mention" href="/u/laurapascal">@laurapascal</a> As a side note, to cite code you can simply enclose it with back-ticks. I updated your last response accordingly.</p>

---

## Post #5 by @lassoan (2017-10-03 21:08 UTC)

<p>You got it almost right. What you missed is replacing the default display node of the model proxy node by the temporally changing display node:</p>
<pre><code># Create model node sequence

modelSequence = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode")

model = slicer.util.loadModel("path/to/file1",True)[1]
modelSequence.SetDataNodeAtValue(model, "0")
slicer.mrmlScene.RemoveNode(model.GetDisplayNode())
slicer.mrmlScene.RemoveNode(model)

model = slicer.util.loadModel("path/to/file2",True)[1]
modelSequence.SetDataNodeAtValue(model, "1")
slicer.mrmlScene.RemoveNode(model.GetDisplayNode())
slicer.mrmlScene.RemoveNode(model)

# Create display node sequence

displayNodeSequence = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode")
displayNodeSequence.SetHideFromEditors(0)

modelDisplay = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelDisplayNode")

modelDisplay.SetColor(1, 0, 0)
displayNodeSequence.SetDataNodeAtValue(modelDisplay, "0")

modelDisplay.SetColor(0, 1, 0)
displayNodeSequence.SetDataNodeAtValue(modelDisplay, "1")

slicer.mrmlScene.RemoveNode(modelDisplay)

# Create sequence browser node

sequencebrowser = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceBrowserNode())

sequencebrowser.AddSynchronizedSequenceNodeID(modelSequence.GetID())
sequencebrowser.AddSynchronizedSequenceNodeID(displayNodeSequence.GetID())

# Replace default display node that is created automatically
# by the display proxy node
modelProxyNode = sequencebrowser.GetProxyNode(modelSequence)
modelDisplayProxyNode = sequencebrowser.GetProxyNode(displayNodeSequence)
slicer.mrmlScene.RemoveNode(modelProxyNode.GetDisplayNode())
modelProxyNode.SetAndObserveDisplayNodeID(modelDisplayProxyNode.GetID())</code></pre>

---

## Post #6 by @jcfr (2017-10-03 21:46 UTC)

<p>I will update methods like <code>slicer.utils.loadModel</code> to pass <code>kwargs</code> as <code>properties</code> to <code>loadNodeFromFile</code>, that way we should be able to simplify:</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="5" data-topic="1166">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>model = slicer.util.loadModel(“path/to/file1”,True)[1]<br>
modelSequence.SetDataNodeAtValue(model, “0”)<br>
slicer.mrmlScene.RemoveNode(model.GetDisplayNode())<br>
slicer.mrmlScene.RemoveNode(model)</p>
</blockquote>
</aside>
<p>into</p>
<pre><code class="lang-auto">model = slicer.util.loadModel("path/to/file1",returnNode=True, show=False)[1]
modelSequence.SetDataNodeAtValue(model, "0")
slicer.mrmlScene.RemoveNode(model)
</code></pre>

---

## Post #7 by @laurapascal (2017-10-05 15:50 UTC)

<p>Thank you for your help: it works perfectly!</p>

---
