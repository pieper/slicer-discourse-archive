# Update Values at Widget

**Topic ID**: 8279
**Date**: 2019-09-03
**URL**: https://discourse.slicer.org/t/update-values-at-widget/8279

---

## Post #1 by @siaeleni (2019-09-03 16:11 UTC)

<p>Hello,</p>
<p>I want to clarify and underand how to set values from Logic to the GUI.<br>
So, I have a python module and I have Widget class where I define all my controls, for example:</p>
<blockquote>
<p>class Widget(ScriptedLoadableModuleWidget):</p>
<p>self.textBox = qt.QLineEdit()</p>
</blockquote>
<p>But I want from the Logic class to update the self.textBox text with the value.</p>
<blockquote>
<p>class Logic(ScriptedLoadableModuleLogic):<br>
value = 8</p>
</blockquote>
<p>What is the right way to do that?</p>

---

## Post #2 by @lassoan (2019-09-03 17:09 UTC)

<p>You should never update the GUI from the logic. The logic should not require, should not even know about that there is a GUI or not. Instead, the logic can update MRML nodes and since the GUI shows the current state of the MRML nodes, changes will automatically appear on the GUI. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">these tutorials</a> for details.</p>

---
