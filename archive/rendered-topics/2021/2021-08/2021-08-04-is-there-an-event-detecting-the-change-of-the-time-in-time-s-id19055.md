---
topic_id: 19055
title: "Is There An Event Detecting The Change Of The Time In Time S"
date: 2021-08-04
url: https://discourse.slicer.org/t/19055
---

# Is there an event detecting the change of the time in time sequence browser?

**Topic ID**: 19055
**Date**: 2021-08-04
**URL**: https://discourse.slicer.org/t/is-there-an-event-detecting-the-change-of-the-time-in-time-sequence-browser/19055

---

## Post #1 by @slicer (2021-08-04 12:38 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>Is there an event detecting the change of the time in time sequence browser? I want to build my own extension and how can I detect the real-time change of the time value for a sequence file in python?</p>
<p>Hope for your help.</p>

---

## Post #2 by @pieper (2021-08-04 14:47 UTC)

<p>You probably want something like this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py#L668">
  <header class="source">

      <a href="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py#L668" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py#L668" target="_blank" rel="noopener">pieper/SlicerAnimator/blob/master/Animator/Animator.py#L668</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="658" style="counter-reset: li-counter 657 ;">
          <li>    sequenceBrowserNodeID = animationNode.GetAttribute('Animator.sequenceBrowserNodeID')</li>
          <li>  sequenceBrowserNode = slicer.mrmlScene.GetNodeByID(sequenceBrowserNodeID)</li>
          <li>  sequenceNodeID = animationNode.GetAttribute('Animator.sequenceNodeID')</li>
          <li>  sequenceNode = slicer.mrmlScene.GetNodeByID(sequenceNodeID)</li>
          <li>  self.removeSequenceBrowserObserver()</li>
          <li>
          </li>
<li>  def onBrowserModified(caller, event):</li>
          <li>    index = sequenceBrowserNode.GetSelectedItemNumber()</li>
          <li>    scriptTime = float(sequenceNode.GetNthIndexValue(index))</li>
          <li>    self.logic.act(animationNode, scriptTime)</li>
          <li class="selected">  tag = sequenceBrowserNode.AddObserver(vtk.vtkCommand.ModifiedEvent, onBrowserModified)</li>
          <li>  self.sequenceBrowserObserverRecord = (sequenceBrowserNode, tag)</li>
          <li>
          </li>
<li>  self.animatorActionsGUI = AnimatorActionsGUI(animationNode, deleteCallback=self.onSelect)</li>
          <li>  self.actionsFormLayout.addRow(self.animatorActionsGUI.buildGUI())</li>
          <li>
          </li>
<li>self.actionsMenuButton.enabled = animationNode != None</li>
          <li>self.exportCollapsibleButton.enabled = animationNode != None</li>
          <li>self.sequencePlay.setMRMLSequenceBrowserNode(sequenceBrowserNode)</li>
          <li>self.sequenceSeek.setMRMLSequenceBrowserNode(sequenceBrowserNode)</li>
          <li>
      </li>
</ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
