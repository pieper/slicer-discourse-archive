# Using observer tags

**Topic ID**: 14041
**Date**: 2020-10-14
**URL**: https://discourse.slicer.org/t/using-observer-tags/14041

---

## Post #1 by @mms25 (2020-10-14 19:40 UTC)

<p>Hi there,<br>
I am creating a module that will continually calculate the angle between two planes as one is moved. I followed the tutorial on the wiki to add an observer to the transform which is getting moved and it works great but I am having trouble removing the observer. My code to remove the observer doesn’t seem to work as after I run it the angle is still continually calculated. I have copied my code below:</p>
<pre><code class="lang-python">  def onSelect(self):
    self.applyButton.enabled = self.plannedTransformSelector.currentNode() and self.actualTransformSelector.currentNode()
    self.clearButton.enabled = self.actualTransformSelector.currentNode()

  def onApplyButton(self):
    logic = CalculateActualFibulaCutsLogic()
    logic.Results(self.plannedTransformSelector.currentNode(), self.actualTransformSelector.currentNode())
    self.angleDif.text = str(logic.angle)
    self.actualTransformNode = self.actualTransformSelector.currentNode()
    self.sawobserverTag = self.actualTransformNode.AddObserver(vtk.vtkCommand.ModifiedEvent, self.onTransformUpdated)

  def onTransformUpdated(self, caller = None, event = None):
    self.onApplyButton()

  def continuousDisplay(self):
    self.logic.Result(self.plannedTransformSelector.currentNode(), self.actualTransformSelector.currentNode())
    print(self.logic.angle)
    self.angleDif.text = str(self.logic.angle)

  def onClearButton(self):
    if self.sawobserverTag:
      print("removing...")
      self.actualTransformNode.RemoveObserver(self.sawobserverTag)
      self.actualTransformNode = None
      self.sawobserverTag = None
    self.angleDif.text = "0"
</code></pre>
<p>Any chance you can help me out?<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-10-15 02:54 UTC)

<p>The problem is that you did not add any check that would prevent adding multiple observers. Before you add a new observation, usually you remove previous observation (because it might have been added for a different node). You also need to remove the observation on Cleanup. See these examples (the syntax is slightly different syntax, as VTKObservationMixin is used, so you don’t need to store observation tags):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L208-L212" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L208-L212" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L208-L212</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="208" style="counter-reset: li-counter 207 ;">
<li>if self._parameterNode is not None:</li>
<li>  self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)</li>
<li>self._parameterNode = inputParameterNode</li>
<li>if self._parameterNode is not None:</li>
<li>  self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L146-L150" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L146-L150" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Utilities/Templates/Modules/Scripted/TemplateKey.py#L146-L150</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="146" style="counter-reset: li-counter 145 ;">
<li>def cleanup(self):</li>
<li>  """</li>
<li>  Called when the application closes and the module widget is destroyed.</li>
<li>  """</li>
<li>  self.removeObservers()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mms25 (2020-10-15 23:05 UTC)

<p>Thanks for the quick reply. I am still struggling to get this to work. I have updated the code to this:</p>
<pre><code class="lang-python">  def cleanup(self):
    self.removeObservers()
 
 def onApplyButton(self):
    logic = CalculateActualFibulaCutsLogic()
    logic.Results(self.plannedTransformSelector.currentNode(), self.actualTransformSelector.currentNode())
    self.angleDif.text = str(logic.angle)
    self.disDif.text = str(logic.dis)
    self.actualTransformNode = self.actualTransformSelector.currentNode()
    if self.actualTransformNode is not None:
      self.removeObserver(self.actualTransformNode,vtk.vtkCommand.ModifiedEvent, self.onTransformUpdated)
    if self.actualTransformNode is not None:
      self.addObserver(self.actualTransformNode,vtk.vtkCommand.ModifiedEvent, self.onTransformUpdated)
 
 def onClearButton(self):
    if self.actualTransformNode is not None:
      print("removing...")
      self.removeObserver(self.actualTransformNode,vtk.vtkCommand.ModifiedEvent, self.onTransformUpdated)
      self.actualTransformNode = None
    self.angleDif.text = "0"
    self.disDif.text = "0"
</code></pre>
<p>but when I try to run it, I get this error:<br>
AttributeError: CalculateActualFibulaCutsWidget instance has no attribute ‘removeObservers’</p>
<p>I have tried importing VTKObservationMixin but it doesn’t seem to solve the problem.</p>

---

## Post #4 by @lassoan (2020-10-15 23:34 UTC)

<aside class="quote no-group" data-username="mms25" data-post="3" data-topic="14041">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mms25/48/8447_2.png" class="avatar"> mms25:</div>
<blockquote>
<p>AttributeError: CalculateActualFibulaCutsWidget instance has no attribute ‘removeObservers’</p>
</blockquote>
</aside>
<p>You can create a new skeleton for your module using the Extension Wizard in latest Slicer Stable Release. It has the observation mixin preconfigured.</p>
<p>If you send a link to your repository then we can have a look at your source code and give advice. These incomplete code snippets give a very vague idea of what might happen in your code.</p>

---

## Post #5 by @mms25 (2020-10-20 21:59 UTC)

<p>Thanks, I really appreciate the help. That worked perfectly.</p>

---
