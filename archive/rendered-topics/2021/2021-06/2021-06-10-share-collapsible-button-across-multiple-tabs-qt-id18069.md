---
topic_id: 18069
title: "Share Collapsible Button Across Multiple Tabs Qt"
date: 2021-06-10
url: https://discourse.slicer.org/t/18069
---

# Share Collapsible button across multiple tabs - Qt

**Topic ID**: 18069
**Date**: 2021-06-10
**URL**: https://discourse.slicer.org/t/share-collapsible-button-across-multiple-tabs-qt/18069

---

## Post #1 by @agporto (2021-06-10 21:47 UTC)

<p>I am updating one of SlicerMorph’s tools with several suggestions that were made by users. During that process, one question occured to me. Is it possible to have a single Collapsible button be shared across multiple tabs in the qt interface?<br>
Currently, we are creating a generic function that adds a button to each tab separately:</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/5c7f335faa21f32169e86b7de68799eecb05bc2d/ALPACA/ALPACA.py#L532" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/5c7f335faa21f32169e86b7de68799eecb05bc2d/ALPACA/ALPACA.py#L532" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/5c7f335faa21f32169e86b7de68799eecb05bc2d/ALPACA/ALPACA.py#L532</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="522" style="counter-reset: li-counter 521 ;">
          <li>    self.parameterDictionaryMulti["maxRANSAC"] = int(self.maxRANSACMulti.value)</li>
          <li>    self.parameterDictionaryMulti["maxRANSACValidation"] = int(self.maxRANSACValidationMulti.value)</li>
          <li>    self.parameterDictionaryMulti["ICPDistanceThreshold"] = self.ICPDistanceThresholdMulti.value</li>
          <li>    self.parameterDictionaryMulti["alpha"] = self.alphaMulti.value</li>
          <li>    self.parameterDictionaryMulti["beta"] = self.betaMulti.value</li>
          <li>    self.parameterDictionaryMulti["CPDIterations"] = int(self.CPDIterationsMulti.value)</li>
          <li>    self.parameterDictionaryMulti["CPDTolerence"] = self.CPDTolerenceMulti.value</li>
          <li>    </li>
          <li>
          </li>
<li>    </li>
          <li class="selected">def addAdvancedMenu(self, currentWidgetLayout):</li>
          <li>  #</li>
          <li>  # Advanced menu for single run</li>
          <li>  #</li>
          <li>  advancedCollapsibleButton = ctk.ctkCollapsibleButton()</li>
          <li>  advancedCollapsibleButton.text = "Advanced parameter settings"</li>
          <li>  advancedCollapsibleButton.collapsed = True</li>
          <li>  currentWidgetLayout.addRow(advancedCollapsibleButton)</li>
          <li>  advancedFormLayout = qt.QFormLayout(advancedCollapsibleButton)</li>
          <li>
          </li>
<li>  # Point density label</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But that creates a lot of extra code to make sure the shared parameters are updated in one tab when changed in another one. Any ideas?</p>

---

## Post #2 by @pieper (2021-06-10 22:04 UTC)

<p>What we typically do is associate a widget class with the scene, so that each instance automatically updates when the corresponding elements (e.g. a parameter node) of the scene change.  For example the subject hierarchy widgets or the views themselves can have multiple instances and each is responsible for updating the UI when the scene changes or updating the scene in response to UI events.  This also gives the option of having multiple instances visible at the same time, possibly with different local configurations.</p>

---

## Post #3 by @agporto (2021-06-11 04:00 UTC)

<p>Hi Steve,<br>
Something like this would definitely work. From the top of your head, can you think of any Slicer module that has that kind of layout? It would be great to have an example to help visualize it.<br>
No worries if there is no example that comes to mind.<br>
Thanks!</p>

---

## Post #4 by @lassoan (2021-06-11 17:19 UTC)

<p>The <code>scripted</code> module template works like this (updates itself from MRML nodes).</p>
<p>If you want to “share” a collapsible button between multiple tabs then it sounds like the collapsible button does not really belong to the tab control, but should be place outside of it (below it, or maybe on one side). This is all trivial if you use Qt Designer. Using this visual editor significantly cuts down the time in implementing and maintaining complex GUI.</p>

---

## Post #5 by @agporto (2021-06-11 17:26 UTC)

<p>I’ve never used the Qt Designer, but I will definitely check it out. It looks fairly straightforward. And thanks for the example, I see now how the parameter node can be created</p>

---
