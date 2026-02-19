---
topic_id: 11862
title: "Event When Volume Loading"
date: 2020-06-04
url: https://discourse.slicer.org/t/11862
---

# Event when volume loading

**Topic ID**: 11862
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/event-when-volume-loading/11862

---

## Post #1 by @ada (2020-06-04 15:20 UTC)

<p>Hi all,</p>
<p>I have create a box to select a volume to display :</p>
<pre><code>self.inputFrame = qt.QFrame(self.displayCollapsibleButton)
self.inputFrame.setLayout(qt.QHBoxLayout())
self.displayFormLayout.addWidget(self.inputFrame)
self.inputSelectorDisp = qt.QLabel("Displayed Volume: ", self.inputFrame)
self.inputFrame.layout().addWidget(self.inputSelectorDisp)
self.inputSelectorDisp = slicer.qMRMLNodeComboBox(self.inputFrame)
self.inputSelectorDisp.nodeTypes = (("vtkMRMLScalarVolumeNode"), "")
self.inputSelectorDisp.addEnabled = False
self.inputSelectorDisp.removeEnabled = False
self.inputSelectorDisp.setMRMLScene(slicer.mrmlScene)
self.inputFrame.layout().addWidget(self.inputSelectorDisp)
</code></pre>
<p>I would like to know if it is possible to update it every time a new volume is loaded ? (I mean automaticaly selecting the last loaded volume). Maybe with an event every time a new volume is loaded ?</p>
<p>Thank you for your help,<br>
Best</p>
<p>Thank you,<br>
Best</p>

---

## Post #2 by @pieper (2020-06-04 15:34 UTC)

<p>Hi - Have a look at this example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_volume_rendering_automatically_when_a_volume_is_loaded" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_volume_rendering_automatically_when_a_volume_is_loaded</a></p>

---
