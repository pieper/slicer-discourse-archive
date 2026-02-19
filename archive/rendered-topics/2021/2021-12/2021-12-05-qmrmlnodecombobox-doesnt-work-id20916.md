---
topic_id: 20916
title: "Qmrmlnodecombobox Doesnt Work"
date: 2021-12-05
url: https://discourse.slicer.org/t/20916
---

# qMRMLNodeComboBox doesn't work

**Topic ID**: 20916
**Date**: 2021-12-05
**URL**: https://discourse.slicer.org/t/qmrmlnodecombobox-doesnt-work/20916

---

## Post #1 by @476663616 (2021-12-05 11:53 UTC)

<p>Hello everyone, I’m trying to add a new qMRMLNodeComboBox in my extension. However it seems doesn’t work. Like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/aff558183c942954b51850f3197b7efbfb90cebb.png" alt="image" data-base62-sha1="p6BcGNdRiLSi9cgBsTbdB9kcfVN" width="533" height="119"><br>
In the .ui file,</p>
<pre><code class="lang-auto">&lt;widget class="qMRMLNodeComboBox" name="SeedsNodeSelector"&gt;
        &lt;property name="enabled"&gt;
         &lt;bool&gt;false&lt;/bool&gt;
        &lt;/property&gt;
        &lt;property name="toolTip"&gt;
         &lt;string&gt;Select the seed point to refine&lt;/string&gt;
        &lt;/property&gt;
        &lt;property name="nodeTypes"&gt;
         &lt;stringlist&gt;
          &lt;string&gt;vtkMRMLMarkupsFiducialNode&lt;/string&gt;
         &lt;/stringlist&gt;
        &lt;/property&gt;
        &lt;property name="showChildNodeTypes"&gt;
         &lt;bool&gt;false&lt;/bool&gt;
        &lt;/property&gt;
        &lt;property name="noneEnabled"&gt;
         &lt;bool&gt;true&lt;/bool&gt;
        &lt;/property&gt;
       &lt;/widget&gt;
</code></pre>
<p>When I set the property “enabled” as True, it got nothing in list.<br>
My code about it has been shown below:</p>
<pre><code class="lang-auto"> self.ui.SeedsNodeSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
self._parameterNode.SetNodeReferenceID("SeedPoints", self.ui.SeedsNodeSelector.currentNodeID)
self.ui.SeedsNodeSelector.setCurrentNode(self._parameterNode.GetNodeReference("SeedPoints"))
</code></pre>
<p>How to deal with it?<br>
Thanks for any help!</p>

---

## Post #2 by @RafaelPalomar (2021-12-05 12:02 UTC)

<p>Hello. Try setting the MRML Scene for your <code>qMRMLNodeComboBox</code> and see if it helps. In your code, it would be something like:</p>
<pre><code class="lang-auto">self.ui.SeedsNodeSelector.setMRMLScene(slicer.mrmlScene)
</code></pre>

---

## Post #3 by @476663616 (2021-12-06 07:26 UTC)

<p>Oh, yes, it works! Thank you very much!<br>
But I can’t understand it, because I have set them all before:</p>
<pre><code class="lang-auto">uiWidget = slicer.util.loadUI(self.resourcePath('UI/Unet_test.ui'))
self.layout.addWidget(uiWidget)
self.ui = slicer.util.childWidgetVariables(uiWidget)
uiWidget.setMRMLScene(slicer.mrmlScene)
</code></pre>
<p>Whatever, thanks for your help.</p>

---

## Post #4 by @cpinter (2021-12-07 09:47 UTC)

<p>If you look closely you see that you set it to the wrong object. It is important to be set to the MRML node combobox, instead you set it to the uiWidget object. For automatic propagation of the scene you can add mrmlSceneChanged-&gt;setMRMLScene signal/slot.</p>

---

## Post #5 by @476663616 (2021-12-07 11:21 UTC)

<p>Okay, I get it, thank you. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=10" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #6 by @zhutouzjq (2025-09-16 08:47 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="2" data-topic="20916">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p><code>self.ui.SeedsNodeSelector.setMRMLScene(slicer.mrmlScene)</code></p>
</blockquote>
</aside>
<p>magic, this problem has already troubled me for several days, it has been solved by only one line of code</p>

---
