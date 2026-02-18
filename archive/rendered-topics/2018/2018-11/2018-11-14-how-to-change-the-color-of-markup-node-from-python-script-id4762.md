# How to change the color of markup node from python script?

**Topic ID**: 4762
**Date**: 2018-11-14
**URL**: https://discourse.slicer.org/t/how-to-change-the-color-of-markup-node-from-python-script/4762

---

## Post #1 by @brhoom (2018-11-14 16:55 UTC)

<p>Operating system: Ubuntu<br>
Slicer version: 4.10<br>
Expected behavior: Color changed<br>
Actual behavior: does not</p>
<p>Hi,</p>
<p>I am trying to change the color and the text scale of a markup node. the text scale works but the color does not. Here is the code:</p>
<pre><code>     mNode = getNode('myMarkUpNode')
     mDisplayNode=slicer.vtkMRMLMarkupsDisplayNode()
     slicer.mrmlScene.AddNode(mDisplayNode)
     mNode.SetAndObserveDisplayNodeID(mDisplayNode.GetID())
     mDisplayNode.SetTextScale(1)
     mDisplayNode.SetColor(0,1,0)
</code></pre>
<p>How can I fix this?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2018-11-14 17:29 UTC)

<p>No need to create a new display node, just use the current one. By default, markups are selected, so you may want to change color of the selected markups, too.</p>
<pre><code class="lang-auto">mDisplayNode = getNode('myMarkUpNode').GetDisplayNode()
mDisplayNode.SetTextScale(1)
mDisplayNode.SetColor(0,1,0)
mDisplayNode.SetSelectedColor(0,1,0)
</code></pre>

---

## Post #3 by @brhoom (2018-11-14 17:52 UTC)

<p>Thanks a lot for the quick reply and the valuable information. It seems SetColor does nothing. I only used SetSelectedColor and it works:</p>
<pre><code>getNode('myMarkUpNode').GetDisplayNode()().SetSelectedColor(0,1,0)</code></pre>

---

## Post #4 by @lassoan (2018-11-14 17:54 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="3" data-topic="4762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>It seems SetColor does nothing</p>
</blockquote>
</aside>
<p><code>SetColor</code> changes color of non-selected markups. Uncheck the checkbox next to the markup’s name in Markups module and you’ll then see how non-selected color is used.</p>

---
