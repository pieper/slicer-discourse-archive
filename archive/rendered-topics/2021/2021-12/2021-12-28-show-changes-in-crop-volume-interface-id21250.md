# Show changes in Crop Volume interface

**Topic ID**: 21250
**Date**: 2021-12-28
**URL**: https://discourse.slicer.org/t/show-changes-in-crop-volume-interface/21250

---

## Post #1 by @bserrano (2021-12-28 12:29 UTC)

<p>Hi all,</p>
<p>I am writing my own code to crop a volume. What I have is:</p>
<pre><code class="lang-python">#Input volume
slicer.util.selectModule('CropVolume')
cropVolumeNode = slicer.vtkMRMLCropVolumeParametersNode()
cropVolumeNode.SetScene(slicer.mrmlScene)
cropVolumeNode.SetInputVolumeNodeID(volumeNode.GetID())

# specify desired roi's dimensions in voxels
radiusIJK = [400, 400, 200]

# assign roi node to a variable
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
cropVolumeNode.SetROINodeID(roiNode.GetID())
roiNode.Initialize(slicer.mrmlScene)

slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeNode)

# get the size of the volume voxels
spacing = volumeNode.GetSpacing()
# convert the number of pixels to measurements in mm
radiusRAS = [(radiusIJK[0]*spacing[0])/2, (radiusIJK[1]*spacing[1])/2, (radiusIJK[2]*spacing[2])/2]
# change the size of the ROI
roiNode.SetRadiusXYZ(radiusRAS)

#Manually put ROI in the desired place 
</code></pre>
<p>I cannot see changes in the interface of Crop Volume module. For example, if I change the input volume, in the interface I always see the same. How can I reflect those changes in the interface?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2021-12-30 05:17 UTC)

<p>If you want to see the changes that you make in the new parameter set node that you created then choose that node as “Parameter set” in the Crop Volume module GUI.</p>

---

## Post #3 by @bserrano (2021-12-30 09:49 UTC)

<p>This was what I needed.<br>
I write the line of code in case so anyone may find it useful<br>
slicer.modules.cropvolume.widgetRepresentation().setParametersNode(cropVolumeNode)</p>

---
