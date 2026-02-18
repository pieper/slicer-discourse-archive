# Volume Rendering ROI SetAndObserveROINodeID problem

**Topic ID**: 9608
**Date**: 2019-12-24
**URL**: https://discourse.slicer.org/t/volume-rendering-roi-setandobserveroinodeid-problem/9608

---

## Post #1 by @apparrilla (2019-12-24 15:58 UTC)

<p>Merry Christmas everyone.</p>
<p>I´ve made a function to init VR with a previously made ROI.<br>
I want to have full interaction with Slicer VR module for advance use if i need it.</p>
<p>It looks like:</p>
<blockquote>
<p>def InitVRDisplayNode(self):<br>
volumeRenderingWidgetRep = slicer.modules.volumerendering.widgetRepresentation()<br>
volumeRenderingWidgetRep.setMRMLVolumeNode(InputVolumeNode())<br>
bonepreset = slicer.modules.volumerendering.logic().GetPresetByName(‘CT-AAA’)<br>
volumeRenderingNode = slicer.mrmlScene.GetFirstNodeByName(‘VolumeRendering’)<br>
volumeRenderingNode.GetVolumePropertyNode().Copy(bonepreset)<br>
volumeRenderingNode.SetCroppingEnabled(1)<br>
volumeRenderingNode.SetAndObserveROINodeID(RoiNode.GetID())<br>
volumeRenderingNode.SetVisibility(1)</p>
</blockquote>
<p>At this point, VR is visible but ROI changes do not crop VR and Slicer VR module do not interact with visible VR image.</p>

---

## Post #2 by @lassoan (2020-01-15 02:29 UTC)

<p>Does everything work well if you create the ROI node on the GUI?<br>
Try with both latest stable and latest preview release.</p>

---
