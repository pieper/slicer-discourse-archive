---
topic_id: 11582
title: "How To Block The User Selection Of A Node In A Qmrmlnodecomb"
date: 2020-05-16
url: https://discourse.slicer.org/t/11582
---

# How to block the user selection of a node in a qMRMLNodeComboBox?

**Topic ID**: 11582
**Date**: 2020-05-16
**URL**: https://discourse.slicer.org/t/how-to-block-the-user-selection-of-a-node-in-a-qmrmlnodecombobox/11582

---

## Post #1 by @xlucox (2020-05-16 22:38 UTC)

<p>Hello !!!</p>
<p>I’m trying to prevent the user to select a node in a qMRMLNodeComboBox. I think it should be an object within this class to block the selection of nodes.</p>
<p>I would appreciate if someone can help me.</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2020-05-17 02:34 UTC)

<p>You can filter what MRML nodes are displayed by calling <a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a056b54be78c6053b6fd21d51b2b1d045">addAtribute</a>. You can show/hide nodes that have certain attribute value.</p>

---

## Post #3 by @Alex_Vergara (2020-08-24 16:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="11582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can show/hide nodes that have certain attribute value.</p>
</blockquote>
</aside>
<p>Are there any example of this? I can’t manage to do this and I can’t find any use case that implements this.</p>

---

## Post #4 by @lassoan (2020-08-24 16:14 UTC)

<p>You need to set an attribute value on MRML nodes that you want to show. Nodes that do not have this attribute set or the value does not match will not show up in the node selector.</p>
<p>You can use tests in Slicer core as examples: <a href="https://github.com/Slicer/Slicer/search?q=addattribute&amp;unscoped_q=addattribute">https://github.com/Slicer/Slicer/search?q=addattribute&amp;unscoped_q=addattribute</a></p>
<p>Let us know if you have any suggestions how to improve <a href="http://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a056b54be78c6053b6fd21d51b2b1d045">documentation</a> to make this more clear.</p>

---

## Post #5 by @Alex_Vergara (2020-08-24 16:17 UTC)

<p>Ah, is an MRML attribute! I was using a shnode attribute. Now it works, thanks!</p>
<pre><code class="lang-auto">        self.Image2 = slicer.qMRMLNodeComboBox()
        self.Image2.nodeTypes = ["vtkMRMLScalarVolumeNode"]
        self.Image2.addAttribute("vtkMRMLScalarVolumeNode", "DICOM.Modality", "RTDOSE")
</code></pre>

---
