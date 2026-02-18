# Reload the slice view automatically after reorientation

**Topic ID**: 25410
**Date**: 2022-09-23
**URL**: https://discourse.slicer.org/t/reload-the-slice-view-automatically-after-reorientation/25410

---

## Post #1 by @AMK (2022-09-23 09:38 UTC)

<p>Hi,</p>
<p>I have written script which takes the volume as an input and then based on the transform reorients the volume.</p>
<pre><code>def onReorientVolumeButton(self):
    volumeNode  = self.ui.inputSelector.currentNode()

    # Create a new ROI that will be fit to volumeNode
    roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")

    cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
    cropVolumeParameters.SetInputVolumeNodeID(volumeNode.GetID())
    cropVolumeParameters.SetROINodeID(roiNode.GetID())
    #slicer.modules.cropvolume.logic().SnapROIToVoxelGrid(cropVolumeParameters)  # optional (rotates the ROI to match the volume axis directions)
    slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeParameters)
    slicer.mrmlScene.RemoveNode(cropVolumeParameters)


    # Get the first volume in the scene
  #  volumeNode = slicer.util.getNode("vtkMRMLScalarVolumeNode1")
    # Create a new ROI
#    roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
    # Make new parameter node in order to use the crop volume module programmatically
    crop_module = slicer.vtkMRMLCropVolumeParametersNode()
    # Add parameter node to the scene
    slicer.mrmlScene.AddNode(crop_module)
    # Set the volume as the input volume in the crop volume module
    crop_module.SetInputVolumeNodeID(volumeNode.GetID())
    # Set output volume as the same volume to overwrite original volume (only needed if you actually want to crop the volume)
    crop_module.SetOutputVolumeNodeID(volumeNode.GetID())
    # Set the input ROI
    crop_module.SetROINodeID(roiNode.GetID())

    crop_module.SetInterpolationMode(1)
    crop_module.SetIsotropicResampling(1)
 #   crop_module.SetVoxelBased(1)

    # Use the Fit ROI to Volume function of the crop volume module
    slicer.modules.cropvolume.logic().Apply(crop_module)
</code></pre>
<p>Everything works fine. Except that I have to first uncheck the visibility of the volume and then recheck it to actually reorient the volume. Is there any way that I can automatically accomplish this functionality?</p>
<p>Thanks</p>

---
