---
topic_id: 14819
title: "Set Color Cut Offs For Volume"
date: 2020-11-30
url: https://discourse.slicer.org/t/14819
---

# Set color cut-offs for volume

**Topic ID**: 14819
**Date**: 2020-11-30
**URL**: https://discourse.slicer.org/t/set-color-cut-offs-for-volume/14819

---

## Post #1 by @Even (2020-11-30 18:38 UTC)

<p>Hi!</p>
<p>I have two volumes: One with a common MNI brain and one with specific scalar values. The goal is to overlay the volume with specific values on top of the MNI brain. Both volumes have the same dimensions. I want to change the colors of the volume with specific scalar values, so that different cut-offs have different colors, i.e. 0-20 red, 20-40 blue et cetera.</p>
<p>I have tried making a copy of a LUT in the Colors module, but the cut-offs I set for “X” do not at all correspond to the specific values in each voxel (F values in Data Probe in the lower left corner).</p>
<p>Is this possible, and if yes – how? I am medium tech savvy, so please describe in relative detail</p>
<p>Operating system: OSX 10.14.6<br>
Slicer version: 4.11.2020</p>

---

## Post #2 by @lassoan (2020-12-05 20:31 UTC)

<p>How this works now is that you need to specify colors in the range of 0-255 (any colors below or above this range are ignored). These colors will be mapped to the voxel values that are specified by the window/level properties of the volume display node.</p>
<p>This is how you can set up absolute intensity-&gt;RGB mapping for a volume now:</p>
<pre><code class="lang-auto">displayNode = volumeNode.GetDisplayNode()

colorTransferFunction = vtk.vtkDiscretizableColorTransferFunction()
offset = -displayNode.GetWindowLevelMin()
scale = 255.0/(displayNode.GetWindowLevelMax()-displayNode.GetWindowLevelMin())
for x, rgb in colors:
    colorTransferFunction.AddRGBPoint((x+offset)*scale, *rgb)

colorNode = slicer.vtkMRMLProceduralColorNode()
colorNode.SetAttribute("Category", "LungCT")
colorNode.SetType(slicer.vtkMRMLColorTableNode.User)
colorNode.SetHideFromEditors(False)
slicer.mrmlScene.AddNode(colorNode)
colorNode.SetAndObserveColorTransferFunction(colorTransferFunction)

displayNode.SetAndObserveColorNodeID(colorNode.GetID())
</code></pre>
<p>I agree that the current behavior of procedural color nodes is too complicated/misleading, therefore I’ve filed a <a href="https://github.com/Slicer/Slicer/issues/5336">bug report</a> to improve this.</p>

---
