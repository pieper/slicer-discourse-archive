# Access Color Node from Colors Widget (python)

**Topic ID**: 4752
**Date**: 2018-11-13
**URL**: https://discourse.slicer.org/t/access-color-node-from-colors-widget-python/4752

---

## Post #1 by @Valtiel (2018-11-13 21:55 UTC)

<p>Hi!</p>
<p>I managed to connect the colors widget via <code>slicer.modules.colors.widgetRepresentation</code>.<br>
Now I want to use the color node from the ColorTableComboBox, but I can’t access it.</p>
<p>Basically, my code would be:<br>
self.visualization_button.enabled = True<br>
displayNode = self.uncertainty_selector.currentNode().GetScalarVolumeDisplayNode()<br>
colormap = self.colormap_selector.ColorTableComboBox.getNode()<br>
displayNode.SetAndObserveColorNodeID(colormap)</p>
<p>However, python can’t find this combobox. How can I access the colorNode?<br>
Thanks in advance!</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.10.0</p>

---

## Post #2 by @lassoan (2018-11-14 05:53 UTC)

<p>Would you like to change the currently selected color node in the Colors module? Or you would like to add a color table or a color node selector into your own module GUI?</p>

---

## Post #3 by @Valtiel (2018-11-14 16:41 UTC)

<p>I want to apply the currenty selected color node in the Colors Module to a displayNode via <code>displayNode.SetAndBoserveColorNodeID(ColorNode)</code>, but I can’t access the selected colorNode.</p>
<p>EDIT:<br>
In the source code of qSlicerColorsModuleWidget.cxx, there is a pointer <code>d</code> that is used to access the <code>ColorTableComboBox</code> from <code>SlicerColorsModuleWidgetPrivate</code>, like in Line 370, for example:<br>
<code>d-&gt;ColorTableComboBox-&gt;currentNode()</code>. I want that exact node.</p>

---

## Post #4 by @lassoan (2018-11-15 01:05 UTC)

<p>In general, you are not supposed to access GUI of other modules but instead you can communicate with them using MRML and module logic classes.</p>
<p>For selecting a color node, you can put a node selector widget on your module GUI. Would that work for you?</p>

---

## Post #5 by @Valtiel (2018-11-15 09:05 UTC)

<p>I see, my bad.</p>
<p>I’ll try using the node selector widget, I guess that should work, too. Thank you!</p>

---

## Post #6 by @Valtiel (2018-11-15 10:10 UTC)

<p>I did it!<br>
I used the <code>slicer.qMRMLColorPickerWidget()</code> to select a premade color node and accessed it via <code>.currentColorNode().GetID()</code> to set it as the ColorNode for my DisplayNode. Thank you!</p>

---
