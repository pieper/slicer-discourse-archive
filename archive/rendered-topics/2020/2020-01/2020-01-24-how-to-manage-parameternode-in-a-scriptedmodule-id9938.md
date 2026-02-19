---
topic_id: 9938
title: "How To Manage Parameternode In A Scriptedmodule"
date: 2020-01-24
url: https://discourse.slicer.org/t/9938
---

# How to manage parameterNode in a ScriptedModule

**Topic ID**: 9938
**Date**: 2020-01-24
**URL**: https://discourse.slicer.org/t/how-to-manage-parameternode-in-a-scriptedmodule/9938

---

## Post #1 by @apparrilla (2020-01-24 19:55 UTC)

<p>Hi everyone,<br>
I´m trying to save my nodes in a parameter Node to manage them all over the module but I have problems no iniciate it.</p>
<blockquote>
<p>def setup(self):<br>
ScriptedLoadableModuleWidget.setup(self)<br>
self.parameterNode = None<br>
logic = MyModuleLogic()<br>
self.parameterNode = logic.getParameterNode()</p>
</blockquote>
<p>Everytime I try to use it, I get this error:</p>
<p>‘MRMLCorePython.vtkMRMLScriptedModuleNode’ object is not callable</p>

---

## Post #2 by @lassoan (2020-01-24 23:27 UTC)

<p>I don’t see anything wrong in this code or that could lead to the error message that you described. See more information and examples for using parameter nodes in scripted modules in this post: <a href="https://discourse.slicer.org/t/how-to-save-slicer-scene-with-both-slicer-data-and-with-self-variables-within-custom-widget/9830" class="inline-onebox">How to save slicer scene with both slicer data and with "self.variables" within custom widget</a></p>

---
