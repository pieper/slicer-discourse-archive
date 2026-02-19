---
topic_id: 14605
title: "Set Up Different Scene For Slicer"
date: 2020-11-14
url: https://discourse.slicer.org/t/14605
---

# Set up different scene for Slicer

**Topic ID**: 14605
**Date**: 2020-11-14
**URL**: https://discourse.slicer.org/t/set-up-different-scene-for-slicer/14605

---

## Post #1 by @mau_igna_06 (2020-11-14 20:34 UTC)

<p>Hi. I want to create a new scene and set it up as principal scene that is because I want to populate a combobox with a list of models (the default scene has some models that I don’t want on the combobox)<br>
This code creates a scene:</p>
<pre><code class="lang-auto">self.myscene = slicer.vtkMRMLScene()
</code></pre>
<p>but I don’t know how to select it, something like this:</p>
<pre><code class="lang-auto">slicer.utils.setMRMLScene(self.myscene)
</code></pre>
<p>Now load the list of models to myscene:</p>
<pre><code class="lang-auto">for mypath in listOfModelPaths:
    #add model to myscene
    newModel = slicer.modules.models.logic().AddModel(mypath)
</code></pre>
<p>Here I create and populate the combobox</p>
<pre><code class="lang-auto">self.inputComboBox = slicer.qMRMLNodeComboBox()
self.inputComboBox.nodeTypes = ['vtkMRMLModelNode']
self.inputComboBox.setMRMLScene(self.myscene)
self.__layout.addWidget(self.inputComboBox)
</code></pre>

---

## Post #2 by @mau_igna_06 (2020-11-16 22:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Could you help with this?</p>

---

## Post #3 by @lassoan (2020-11-16 23:15 UTC)

<p>There is just one scene that the application knows about. You can create a new scene object but it will not contain any of your nodes (a node can only be in one scene).</p>
<p>If you want to show only certain models then you can add a custom attribute to your nodes and use that for filtering - see <a href="http://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a056b54be78c6053b6fd21d51b2b1d045">http://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a056b54be78c6053b6fd21d51b2b1d045</a></p>

---

## Post #4 by @mau_igna_06 (2020-11-16 23:22 UTC)

<p>Yes Andras. Thank you for the help. I had found that function in the documentation but I didn’t understand how to use it with vtkMRMLModelNode. I don’t know with what to replace “Category” and “Discrete”. I would like to show only some models I select. For example: show only models that start with “MyModelType1” and “MyModelType2”<br>
So in this list:<br>
MyModelType1D is shown<br>
MyModelType1G is shown<br>
MyModelType2H is shown<br>
MyModelType2J is shown<br>
MyModelType3R isn’t shown<br>
MyModelType3Y isn’t shown</p>

---

## Post #5 by @lassoan (2020-11-17 00:13 UTC)

<p>You can choose any text as attribute name and you can filter for value or presence of that attribute. For example:</p>
<pre><code class="lang-python">someNode.SetAttribute('MySpecialNodeCategory', '1')
comboBox.addAttribute('vtkMRMLModelNode', 'MySpecialNodeCategory', '1')
</code></pre>

---
