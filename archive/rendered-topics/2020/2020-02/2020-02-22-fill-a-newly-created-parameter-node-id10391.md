---
topic_id: 10391
title: "Fill A Newly Created Parameter Node"
date: 2020-02-22
url: https://discourse.slicer.org/t/10391
---

# Fill a newly created parameter node

**Topic ID**: 10391
**Date**: 2020-02-22
**URL**: https://discourse.slicer.org/t/fill-a-newly-created-parameter-node/10391

---

## Post #1 by @Juicy (2020-02-22 02:31 UTC)

<p>I have some confusion regarding the creation of a new parameter node for a scripted module.</p>
<p>I have seen in other modules that you can over-ride the base class createParameterNode method in the logic class so that you can add default parameters which are added to the parameter node when it is first created. This works well for when the module is first opened and the getParameterNode function is run. However, when I create a new parameter node from the parameter node combo box at the top of the GUI then the new parameter node is created completely blank. The issue here is I get errors when running the updateGUIFromParameterNode. For example the following line (which is used in a for loop):</p>
<p><code>self.valueEditWidgets[parameterName].setValue(float(self.parameterNode.GetParameter(parameterName)))</code></p>
<p>gives an error because a blank string cannot be converted to a float.</p>
<p>Is there some sort of standard practice to address this? Perhaps  something in the SetParameterNode function which updates all the parameters based on the current state of the GUI when the parameter node was created using the combo box?</p>
<p>I was just asking as I don’t want to reinvent the wheel if someone else already has an elegant solution to this problem?</p>
<p>Thanks again,</p>

---

## Post #2 by @lassoan (2020-02-22 03:09 UTC)

<p>You need to initialize the parameter node with default values when the parameter node gets selected in the node selector:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/daecb6e24e83c02e990871b4db80e01c0e77d68a/Utilities/Templates/Modules/ScriptedDesigner/TemplateKey.py#L95" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/daecb6e24e83c02e990871b4db80e01c0e77d68a/Utilities/Templates/Modules/ScriptedDesigner/TemplateKey.py#L95" target="_blank">Slicer/Slicer/blob/daecb6e24e83c02e990871b4db80e01c0e77d68a/Utilities/Templates/Modules/ScriptedDesigner/TemplateKey.py#L95</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="85" style="counter-reset: li-counter 84 ;">
<li>  """</li>
<li>  self.removeObservers()</li>
<li>
</li>
<li>def setParameterNode(self, inputParameterNode):</li>
<li>  """</li>
<li>  Adds observers to the selected parameter node. Observation is needed because when the</li>
<li>  parameter node is changed then the GUI must be updated immediately.</li>
<li>  """</li>
<li>
</li>
<li>  if inputParameterNode:</li>
<li class="selected">    self.logic.setDefaultParameters(inputParameterNode)</li>
<li>  wasBlocked = self.ui.parameterNodeSelector.blockSignals(True)</li>
<li>  self.ui.parameterNodeSelector.setCurrentNode(inputParameterNode)</li>
<li>  self.ui.parameterNodeSelector.blockSignals(wasBlocked)</li>
<li>  if inputParameterNode == self._parameterNode:</li>
<li>    return</li>
<li>  if self._parameterNode is not None:</li>
<li>    self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)</li>
<li>  if inputParameterNode is not None:</li>
<li>    self.addObserver(inputParameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)</li>
<li>  self._parameterNode = inputParameterNode</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Juicy (2020-02-22 10:16 UTC)

<p>Thank you, this worked well.</p>

---
