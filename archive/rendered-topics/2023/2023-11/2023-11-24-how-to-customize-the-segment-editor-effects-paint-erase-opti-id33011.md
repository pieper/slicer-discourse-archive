---
topic_id: 33011
title: "How To Customize The Segment Editor Effects Paint Erase Opti"
date: 2023-11-24
url: https://discourse.slicer.org/t/33011
---

# How to customize the Segment Editor effects - Paint/Erase options in Python?

**Topic ID**: 33011
**Date**: 2023-11-24
**URL**: https://discourse.slicer.org/t/how-to-customize-the-segment-editor-effects-paint-erase-options-in-python/33011

---

## Post #1 by @rajmadhan (2023-11-24 19:14 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.4.0<br>
Expected behavior:<br>
I would like to customize the Segment Editor options for the Paint/Erase effects in Python.</p>
<p>Desired functionality:</p>
<ol>
<li>Set a fixed brush diameter, say 5mm</li>
<li>Hide all the options exposed by the Paint/Erase effects.</li>
</ol>
<p>Functionality 1:<br>
Able to set a fixed size for the brush diameter using the below code:<br>
paintEffect = self.ui.embeddedSegmentEditorWidget.effectByName(“Paint”)<br>
paintEffect.setCommonParameter(“BrushDiameterIsRelative”, “0”)<br>
paintEffect.setCommonParameter(“BrushAbsoluteDiameter”, 5)                crosshairNode=slicer.mrmlScene.GetSingletonNode(‘default’,‘vtkMRMLCrosshairNode’)<br>
sliceNode = crosshairNode.GetCursorPositionXYZ([0,0,0])<br>
if sliceNode:<br>
sliceNode.Modified()</p>
<p>The code works, but not consistently. The change for “BrushDiameterIsRelative” works correctly all the time. The UI always displays brush diameter units in “mm”, but the diameter value is not 5 all the time. Sometimes it shows as 5, other times 25.</p>
<p>Functionality 2:<br>
I’m not able to hide the “Masking” options exposed by the Paint/Erase effects.<br>
Tried the below code, but is not working:<br>
self.ui.embeddedSegmentEditorWidget.MaskingGroupBox.hide()<br>
or<br>
self.ui.embeddedSegmentEditorWidget.MaskingGroupBox.setVisible(False)</p>
<p>Actual behavior:</p>

---
