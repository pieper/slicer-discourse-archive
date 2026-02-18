# Adjust Window Label and choice a LUT for a vtkMRMLScalarVolumeNode

**Topic ID**: 11154
**Date**: 2020-04-16
**URL**: https://discourse.slicer.org/t/adjust-window-label-and-choice-a-lut-for-a-vtkmrmlscalarvolumenode/11154

---

## Post #1 by @xlucox (2020-04-16 15:05 UTC)

<p>Hello everyone.</p>
<p>I’m trying to adjust the window label of a vtkMRMLScalarVolumeNode and to Apply it a Rainbow LUT.</p>
<p>I thought to use the object SetWindowLevelToVolumeProp() of the class volumerendering.logic(). The problem which I am facing is that this function takes as argument a vtkVolumeProperty and I don’t know how to get it from the vtkMRMLScalarVolumeNode.</p>
<p>I wonder also if it is possible to automatic adjust the window label.</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2020-04-17 04:42 UTC)

<p>You can <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#aa08cd24eaceabdc9159d33702517c909">set colormap</a> in the volume’s scalar volume display node.</p>
<p>The volume may also have a volume rendering display node, but that controls how 3D raycasting of the volume is performed and not related to what colormap is used for displaying the volume in slice views.</p>

---
