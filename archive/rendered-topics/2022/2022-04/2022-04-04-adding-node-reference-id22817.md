---
topic_id: 22817
title: "Adding Node Reference"
date: 2022-04-04
url: https://discourse.slicer.org/t/22817
---

# Adding node reference

**Topic ID**: 22817
**Date**: 2022-04-04
**URL**: https://discourse.slicer.org/t/adding-node-reference/22817

---

## Post #1 by @keri (2022-04-04 14:57 UTC)

<p>Hi,</p>
<p>I’m trying to understand how can I use <code>SetAndObserveNodeReferenceID()</code>.</p>
<p>For example I have a model node and a markups node.<br>
The markups node is some kind of a “child” node of a model and and it is going to be located under a model node within subject hierarchy module.</p>
<p>I would like to keep relative position (relative to the model node) of markups node to be constant.<br>
Thus whenever model/markups node gets transformed I need to apply the same transform to the markups/model node.</p>
<p>I understand that I can use <code>SetAndObserveNodeReferenceID("MyRole", "markups node Id")</code> but I dont understand where to process the events?<br>
I have some experience of working with vtk observers and vtk callback command and I guess there should be some method/function that I need to implement…</p>

---

## Post #2 by @mau_igna_06 (2022-04-05 08:45 UTC)

<p>You could try to investigste this usecase:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/BafflePlanner/BafflePlanner.py">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/BafflePlanner/BafflePlanner.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/BafflePlanner/BafflePlanner.py" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/BafflePlanner/BafflePlanner.py</a></h4>


      <pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin
import logging

#
# BafflePlanner
#

class BafflePlanner(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Baffle Planner"
    self.parent.categories = ["Cardiac"]
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerHeart/SlicerHeart/blob/42b75a6184b31d785eaef61ff695f4de99834356/BafflePlanner/BafflePlanner.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Source:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/search?l=Python&amp;q=SetAndObserveNodeReferenceID&amp;type=Code">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/search?l=Python&amp;q=SetAndObserveNodeReferenceID&amp;type=Code" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://github.githubassets.com/images/modules/open_graph/github-logo.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://github.com/search?l=Python&amp;q=SetAndObserveNodeReferenceID&amp;type=Code" target="_blank" rel="noopener">Build software better, together</a></h3>

  <p>GitHub is where people build software. More than 73 million people use GitHub to discover, fork, and contribute to over 200 million projects.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would interested in knowing how did you solve it at the end.</p>
<p>Thank you</p>

---

## Post #3 by @keri (2022-04-05 13:08 UTC)

<p>Thank you for the example,</p>
<p>For now I decided to postpone this and use <code>AddNodeReferenceID</code> without observing any events.</p>
<p>Probably later I will try to refer to the problem once again.</p>

---

## Post #4 by @lassoan (2022-04-07 12:38 UTC)

<p>Moving nodes together is very easy, just set the same parent transform to all of them. If you want to have a fixed relative transform between them then add the relative transform as a transform node, use the commom transform node as parent, and set this transform node as parent for the second model node.</p>
<p><code>SomeNode.SetAndOvserveNodeReferenceID(otherNode)</code> will notify the <code>SomeNode</code> if  <code>otherNode</code> is modified. No other classes will be notified. If you want to observe changes in <code>otherNode</code> outside of <code>SomeNode</code> then you can add an observer directly using <code>AddObserver</code>.</p>

---
