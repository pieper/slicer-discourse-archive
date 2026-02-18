# Slicer Scripted Module not calling updateParameterNodeFromGUI when UI is updated

**Topic ID**: 20122
**Date**: 2021-10-12
**URL**: https://discourse.slicer.org/t/slicer-scripted-module-not-calling-updateparameternodefromgui-when-ui-is-updated/20122

---

## Post #1 by @tsims (2021-10-12 20:28 UTC)

<p>Hi everyone,</p>
<p>I am working on python module for slicer and am running into a weird issue where my <code>updateParameterNodeFromGUI</code> function is not being called when I interacted with the UI. Is there a signal I may have broken somewhere in the module?</p>
<p>Any help on figuring out what is going on here would be greatly appreciated.<br>
Thanks!</p>

---

## Post #2 by @ungi (2021-10-12 22:04 UTC)

<p>Can you see an error message in the Python interactor? Are you sure the signal and the slot functions are connected in the setup function of the widget class?</p>

---

## Post #3 by @mikebind (2021-10-12 22:06 UTC)

<p>You need to connect each GUI element with the callback to updateParameterNodeFromGUI with lines like:</p>
<pre><code class="lang-auto">self.ui.myNodeSelectionWidget.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
</code></pre>
<p>or</p>
<pre><code class="lang-auto">self.ui.myCheckBox.connect("toggled(bool)", self.updateParameterNodeFromGUI) 
</code></pre>
<p>in the setup() function of the widget class</p>

---

## Post #4 by @tsims (2021-10-19 19:38 UTC)

<p>I can’t believe I overlooked something so obvious haha. This was the solution I forgot to add in my connections.</p>
<p>Thanks!</p>

---
