---
topic_id: 10377
title: "Qradiobuttons And Parameter Nodes"
date: 2020-02-21
url: https://discourse.slicer.org/t/10377
---

# qRadioButtons and parameter nodes

**Topic ID**: 10377
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/qradiobuttons-and-parameter-nodes/10377

---

## Post #1 by @Juicy (2020-02-21 09:23 UTC)

<p>Hi all,</p>
<p>I am having a lot of trouble trying to save and recall the state of a pair of radio buttons (which I have put in a scripted module GUI) from a parameter node.</p>
<p>I have got all my qMRMLNodeComboBox and qSpinBoxes all saving and updating fine but I am having terrible trouble with the qRadioButtons.</p>
<p>Can anyone think of any scripted modules which save and recall the state of radio buttons from a parameter node which I can look at for ideas? I have sifted through quite a few on github but cant find any which use both a parameter node for saving the GUI state and have radio buttons.</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2020-02-21 15:02 UTC)

<p>See how radio buttons are managed in this Mask Volume effect: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorMaskVolume/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorMaskVolume/SegmentEditorMaskVolumeLib/SegmentEditorEffect.py</a></p>

---

## Post #3 by @Saima (2020-12-17 06:53 UTC)

<p>Hi Andras,<br>
I am not understanding this error.</p>
<p>File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/ElectricaConductivity/FuzzyClassification/FuzzyClassification.py”, line 136, in updateGUIFromParameterNode<br>
self.ui.nClass.value = int(self._parameterNode.GetParameter(“nnClass”))<br>
AttributeError: ‘setvalue’ does not exist on QSpinBox and creating new attributes on C++ objects is not allowed</p>
<p>I am trying to create a qspinbox and enabling pathlineedits depending on the qspin value</p>
<p>regards,<br>
Siama Safdar</p>

---

## Post #4 by @lassoan (2020-12-17 07:13 UTC)

<p>The code that is in the .py file is not the same that is being executed: the referenced line contains <code>self.ui.nClass.value</code>, while you are executing <code>self.ui.nClass.setvalue</code>. Restart Slicer to ensure that all previous versions of the module are unloaded.</p>
<p><code>setvalue</code> is indeed incorrect, there is no such method of QSpinBox. You need to fix spelling and write <code>self.ui.nClass.setValue(...)</code> or use the <code>value</code> property (<code>self.ui.nClass.value = ...</code>).</p>

---
