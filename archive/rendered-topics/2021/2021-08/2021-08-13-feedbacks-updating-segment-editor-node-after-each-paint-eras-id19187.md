# Feedbacks / Updating segment editor node after each paint/erase effect

**Topic ID**: 19187
**Date**: 2021-08-13
**URL**: https://discourse.slicer.org/t/feedbacks-updating-segment-editor-node-after-each-paint-erase-effect/19187

---

## Post #1 by @Raj_Kumar_Ranabhat (2021-08-13 14:07 UTC)

<p>Hi andras, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Are there any way to check programmatically using python whether erase/paint has been done?</p>
<p>In our project, we are using erase effect to erase the portion of the segmentation node.<br>
First, we set volume, segmentation, and segment for segment editor widget,  and when our resection tool is on then we set to erase effect.</p>
<p>We want update/feedback in each bite of segmentation. But this is not happening.<br>
a small portion of code is given below.</p>
<p>def turnONOrOFF(self, seg):<br>
if self.turnToolSelector.currentText == ‘On’:<br>
if self.resectToolTypeSelector.currentText == ‘Sphere Brush’:<br>
seg.GetSegmentation().SetConversionParameter(‘Smoothing factor’, ‘0.0’)<br>
self.segmentEditorWidget.setActiveEffectByName(“Erase”)<br>
effect = self.segmentEditorWidget.activeEffect()<br>
effect.setCommonParameter(“EditIn3DViews”, “1”)<br>
effect.setCommonParameter(“BrushSphere”, “1”)<br>
effect.setCommonParameter(“BrushAbsoluteDiameter”, 60)<br>
print(self.segmentEditorNode)<br>
else:<br>
self.segmentEditorWidget.setActiveEffectByName(“Scissors”)<br>
effect = self.segmentEditorWidget.activeEffect()<br>
effect.setParameter(‘Shape’, ‘Rectangle’)<br>
else:<br>
self.segmentEditorWidget.setActiveEffectByName(“None”)<br>
seg1 = slicer.mrmlScene.GetNodesByName(“Spine”).GetItemAsObject(0)<br>
seg2 = slicer.mrmlScene.GetNodesByName(‘All Segments’).GetItemAsObject(0)<br>
seg1.GetSegmentation().CreateRepresentation(‘Closed surface’, True)<br>
seg2.GetSegmentation().CreateRepresentation(‘Closed surface’, True)<br>
seg1.Modified()<br>
seg2.Modified()</p>
<p>I have printed segmentEditorNode to see the attributes. I would like to see these attributes in every bite during erase effect.</p>
<p>What are possible options ?</p>
<p>Thank you !!</p>

---

## Post #2 by @lassoan (2021-08-13 19:54 UTC)

<p>You can add an observer to various modified events of the segmentation node. It notifies you not just about paint/erase but about all editing operations.</p>

---

## Post #3 by @Raj_Kumar_Ranabhat (2021-08-17 02:02 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> . It is really helpful.</p>

---
