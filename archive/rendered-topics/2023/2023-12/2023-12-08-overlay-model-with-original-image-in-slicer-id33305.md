# Overlay model with original image in slicer

**Topic ID**: 33305
**Date**: 2023-12-08
**URL**: https://discourse.slicer.org/t/overlay-model-with-original-image-in-slicer/33305

---

## Post #1 by @G_Tom (2023-12-08 21:02 UTC)

<p>Hi, I have the following MWE code in slicer. I want to show the 3D grid of the image along with the image. I use  the vtkExtractEdges and pass that to a vtkTubeFilter.<br>
When I visualize the result, the extracted grid is much smaller than the original image? What gives ? Please see image below.</p>
<p>Thanks</p>
<pre><code class="lang-auto">import os

nodeName = "MyNewVolume"
imageSize = [4, 6, 4]
voxelType=vtk.VTK_UNSIGNED_CHAR
imageOrigin = [0.0, 0.0, 0.0]
imageSpacing = [13.0, 13.0, 13.0]
imageDirections = [[1,0,0], [0,1,0], [0,0,1]]
fillVoxelValue = 500

# Create an empty image volume, filled with fillVoxelValue
imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.AllocateScalars(voxelType, 1)
imageData.GetPointData().GetScalars().Fill(fillVoxelValue)

extractEdges = vtk.vtkExtractEdges()
extractEdges.SetInputData(imageData) 

# Tube the edges
tubes = vtk.vtkTubeFilter()
tubes.SetInputConnection(extractEdges.GetOutputPort())
tubes.SetRadius(0.008)
tubes.SetNumberOfSides(32)

model = slicer.modules.models.logic().AddModel(tubes.GetOutputPort())

# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetIJKToRASDirections(imageDirections)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356dd9288804d522e1be01f22d625991a79eff7d.png" data-download-href="/uploads/short-url/7CEEAXGah3AabdapEc8pgb5HOYl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/356dd9288804d522e1be01f22d625991a79eff7d_2_689x397.png" alt="image" data-base62-sha1="7CEEAXGah3AabdapEc8pgb5HOYl" width="689" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/356dd9288804d522e1be01f22d625991a79eff7d_2_689x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/356dd9288804d522e1be01f22d625991a79eff7d_2_1033x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356dd9288804d522e1be01f22d625991a79eff7d.png 2x" data-dominant-color="898BB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1374×791 33.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-12-08 21:45 UTC)

<p>Looks like you need to apply the spacing to expand the result of the tube filter.  For example, you could get the IJKToRAS matrix from the volumeNode and use it for a linear transform you could apply to the model node.</p>

---

## Post #3 by @G_Tom (2023-12-13 17:46 UTC)

<p>HI Pieper,<br>
thanks for your answer. I just wondered why the scaling is not applied automatically. Is my VTK code having an issue ?</p>
<p>Thanks</p>
<p>GT</p>

---

## Post #4 by @pieper (2023-12-13 22:11 UTC)

<p>Yes, you need to take the image spacing into account when to map your tube from local space to world (patient) space.  The edges are being extracted from the image data which doesn’t include the ijkToRAS information which is only added at the MRML level.</p>

---
