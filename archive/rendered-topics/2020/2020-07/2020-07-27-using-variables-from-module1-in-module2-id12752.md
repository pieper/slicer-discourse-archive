---
topic_id: 12752
title: "Using Variables From Module1 In Module2"
date: 2020-07-27
url: https://discourse.slicer.org/t/12752
---

# Using variables from module1 in module2

**Topic ID**: 12752
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/using-variables-from-module1-in-module2/12752

---

## Post #1 by @rohan_n (2020-07-27 21:15 UTC)

<p>I have two modules, module1 and module2. I am asking the user to select a folder using qFileDialog in this part of module 1</p>
<p>class module1Logic(ScriptedLoadableModuleLogic):<br>
def run(self):<br>
exampath = qt.QFileDialog.getExistingDirectory(0,(“Select folder for DCE-MRI exam”))</p>
<p>Then in this part of module2</p>
<p>class module2Widget(ScriptedLoadableModuleWidget):<br>
def setup(self):</p>
<p>I want to be able to reuse that same exampath that they chose in module1 without making the user select the exampath from QFileDialog again.</p>
<p>What would be the syntax for doing this?</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @lassoan (2020-07-27 22:33 UTC)

<p>Modules should only interact through nodes in the MRML scene, i.e., you select parameter node of one module as input of the other module. If you don’t want to require users to select nodes then you can use singleton parameter node (then you can look it up based on singleton tag).</p>
<p>Note that it is the best to minimize usage of file paths in the scene, as you don’t want your processing code littered with file reader/writer code. Instead, load data into nodes once and then only work with data nodes and node references. If you need to import data from proprietary file formats then you can implement a custom file reader in Python.</p>

---

## Post #3 by @rohan_n (2020-07-28 22:43 UTC)

<p>Thanks, I ended up doing this in module1:</p>
<pre><code>exampath_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScriptedModuleNode","path node")
exampath_node.SetParameter("exampath",exampath)
</code></pre>
<p>And this in module2:</p>
<pre><code>exampath_node = slicer.util.getNode("path node")

self.exampath = exampath_node.GetParameter("exampath")</code></pre>

---

## Post #4 by @lassoan (2020-07-28 23:09 UTC)

<p>Thanks for sharing your solution. Referring to nodes by name is very fragile, because you can have many nodes in the scene by the same name. Instead, if you want to find a node in the scene by a string identifier then set that unique string in its singleton tag and retrieve it using <code>slicer.mrmlScene.GetSingletonNode()</code>. You can use something like “YourModuleName.SomeOtherString” as singleton tag to ensure that it is unique (each module names is unique).</p>

---
