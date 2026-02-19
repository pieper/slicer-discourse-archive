---
topic_id: 24932
title: "Createdefaultvolumerenderingnodes Always Return None"
date: 2022-08-26
url: https://discourse.slicer.org/t/24932
---

# CreateDefaultVolumeRenderingNodes always return None

**Topic ID**: 24932
**Date**: 2022-08-26
**URL**: https://discourse.slicer.org/t/createdefaultvolumerenderingnodes-always-return-none/24932

---

## Post #1 by @ada (2022-08-26 07:07 UTC)

<p>Hello community!</p>
<p>I was using a custom script to display 3D dicom stacks but since I updated 3DSlicer version (from 4.11.0 to 5.0.3) my script is not working anymore.<br>
I am no more able to get the ROI node from a volume using the ‘CreateDefaultVolumeRenderingNodes’ function (always return None) as show below :<br>
On 4.11.0 version :<br>
ID: vtkMRMLGPURayCastVolumeRenderingDisplayNode1<br>
ClassName: vtkMRMLGPURayCastVolumeRenderingDisplayNode<br>
Name: VolumeRendering<br>
[…]<br>
Node references:<br>
roi [ROINodeID]: vtkMRMLAnnotationROINode1<br>
shaderProperty [shaderPropertyNodeId]: (none)<br>
volumeProperty [volumePropertyNodeID]: vtkMRMLVolumePropertyNode1</p>
<p>On 5.0.3 version :<br>
ID: vtkMRMLGPURayCastVolumeRenderingDisplayNode1<br>
ClassName: vtkMRMLGPURayCastVolumeRenderingDisplayNode<br>
[ …]<br>
Node references:<br>
roi [ROINodeID]: (none)<br>
shaderProperty [shaderPropertyNodeId]: (none)<br>
volumeProperty [volumePropertyNodeID]: vtkMRMLVolumePropertyNode1</p>
<p>Do you know can I get back the roi Node ID ?<br>
Are there lots of incompatibilities between consecutives 3DSlicer software versions ?<br>
Thank you so much for your help</p>

---

## Post #2 by @lassoan (2022-08-27 22:49 UTC)

<p><code>CreateDefaultVolumeRenderingNodes</code> unnecessarily polluted the scene with ROI node even though the user did not need cropping. In Slicer-5.x we fixed the issue by not creating the ROI nodes automatically, but you can <code>CreateROINode</code> if you need an ROI node.</p>

---
