# Update model node color once the node is selected

**Topic ID**: 12704
**Date**: 2020-07-23
**URL**: https://discourse.slicer.org/t/update-model-node-color-once-the-node-is-selected/12704

---

## Post #1 by @szhang (2020-07-23 04:01 UTC)

<p>Hello, I would like to learn in a scripted module, how to update the model color display once the model is selected in the slicer.qMRMLNodeComboBox() type of drop-down menu.<br>
For example, is it about to update this line? or something else?</p>
<blockquote>
<p>self.parent.connect(‘mrmlSceneChanged(vtkMRMLScene*)’,                        self.someModelNodeSelector, ‘setMRMLScene(vtkMRMLScene*)’)</p>
</blockquote>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2020-07-23 13:42 UTC)

<p>Setting MRML scene in the node combobox is necessary, so leave this line as is. Instead connect a method to the <code>currentNodeChanged</code> signal and in that method change the model’s color using <code>modelNode.GetDisplayNode().SetColor(r,g,b)</code>.</p>

---

## Post #3 by @szhang (2020-07-23 15:42 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a><br>
A follow-up question, to avoid all nodes turned to same highlight color, how should I return the previous selection to its original color upon every new selection in qMRMLNodeComboBox?</p>

---

## Post #4 by @lassoan (2020-07-23 15:45 UTC)

<p>Yes, you should save the previously selected node and its color and restore it when a new model is selected.</p>

---

## Post #5 by @szhang (2020-07-24 05:57 UTC)

<p>Agree, I am not sure how to store the “previously selected node”, could you please provide some examples? Thanks a lot!</p>

---

## Post #6 by @lassoan (2020-07-24 06:06 UTC)

<p>You store the node that you have just changed and its original color in member variables. Next time you change a new node, these member variables contain the previously selected node and its color.</p>

---

## Post #7 by @szhang (2020-08-06 21:25 UTC)

<p>I see, but I am afraid I still have trouble in implementing this, currently it is like this in the Widget main body setup</p>
<blockquote>
<p>changedNodeColor = self.abcModelsNodeSelector.currentNode().GetDisplayNode().GetColor()<br>
changedNode = self.abcModelsNodeSelector.currentNode()<br>
self.abcModelsNodeSelector.connect(“currentNodeChanged(vtkMRMLNode*)”,self.onUpdateColor(changedNode,changedNodeColor))</p>
</blockquote>
<p>and then the class definition is like this</p>
<blockquote>
<p>def onUpdateColor(self,rNode,rNodeColor):<br>
rNode.CreateDefaultDisplayNodes()<br>
rNode.GetDisplayNode().SetColor(rNodeColor)<br>
self.abcModelsNodeSelector.currentNode().GetDisplayNode().SetColor(0,1,0)</p>
</blockquote>
<p>It did not generate error until I selected a new node, with the message of</p>
<blockquote>
<p>TypeError: ‘NoneType’ object is not callable</p>
</blockquote>
<p>Could you please kindly advise? Thanks a lot!</p>

---

## Post #8 by @lassoan (2020-08-07 03:09 UTC)

<p>You need to save the previous node and color to member variables (self.previousModelNode, self.previousModelColor).</p>

---

## Post #9 by @szhang (2020-08-07 13:37 UTC)

<p>I see, I just changed the code to</p>
<blockquote>
<p>self.changedNodeColor = self.abcModelsNodeSelector.currentNode().GetDisplayNode().GetColor()<br>
self.changedNode = self.abcModelsNodeSelector.currentNode()<br>
self.abcModelsNodeSelector.connect(“currentNodeChanged(vtkMRMLNode*)”, self.onUpdateColor(self.changedNode,self.changedNodeColor))</p>
</blockquote>
<p>and keep the class definition the same, but the same error message appears</p>
<blockquote>
<p>TypeError: ‘NoneType’ object is not callable</p>
</blockquote>
<p>Am I missing something? Thank you again!</p>

---

## Post #10 by @szhang (2020-08-07 20:02 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I suppose it is related to some syntax in Qt Signals and Slots which I am trying to read upon, but I am not sure why self.changedNode will become empty once “currentNodechanged” happens, could you please help a bit further? Thank you!</p>

---

## Post #11 by @lassoan (2020-08-08 01:38 UTC)

<p>In Python, the callback funcrion is specified by only its name (no argument list). Look at examples in the programming tutorials to see the correct syntax of <code>connect</code>.</p>

---

## Post #12 by @szhang (2020-08-08 02:49 UTC)

<p>Oh right, there is no need to put member variables as arguments, thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> , it worked!<br>
Here’s how the definition looks like for restoring the previous node, to wrap up this thread of discussion.</p>
<blockquote>
<p>def onUpdateColor(self)<br>
self.changedNode.CreateDefaultDisplayNodes()<br>
self.changedNode.GetDisplayNode().SetColor(self.changedNodeColor)<br>
self.changedNode = self.abcModelsNodeSelector.currentNode()<br>
self.changedNodeColor = self.abcModelsNodeSelector.currentNode().GetDisplayNode().GetColor()<br>
self.abcModelsNodeSelector.currentNode().GetDisplayNode().SetColor(1,0,0)</p>
</blockquote>

---
