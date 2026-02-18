# Scissors segment, rectangle shape selection from a python script

**Topic ID**: 30757
**Date**: 2023-07-24
**URL**: https://discourse.slicer.org/t/scissors-segment-rectangle-shape-selection-from-a-python-script/30757

---

## Post #1 by @Honeee (2023-07-24 11:24 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.2.2</p>
<p>Hello, I’m a beginner on 3D Slicer and I’m struggling on a project.<br>
I aim to write a program in the application startup script .slicerrc.py which should enable me to import a .nrrd file and select the skull thanks to a tresholding and smoothing/closing segmentation. Now I would like to select only the higher part of the skull and dismiss the mandible. My idea is to create a rectangle, to select only the higher part of the skull and to erase outside of this zone and then to collect datas such as HU. I read posts about cylinder segmentations and Scissors segm but nothing about rectangle shape and its coordinates in space. Do not hesitate to tell me if it’s not clear or if you need explanations.<br>
Here is the code :</p>
<pre><code class="lang-auto">import slicer

# Path to the ctvol.nrrd file
file_path_nrrd = "my_file_path/ctvol.nrrd"

# Load the ctvol.nrrd file
volume_node = slicer.util.loadVolume(file_path_nrrd)

# Check if the loading was successful
if volume_node:
    # Create segmentation
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume_node)
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("Skull")

    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(volume_node)  # Change deprecated method

    #---THRESHOLDING---#
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold", "1500")
    effect.setParameter("MaximumThreshold", "4095")
    effect.onApply()

    #---SMOOTHING---#
    segmentEditorWidget.setActiveEffectByName("Smoothing")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("SmoothingMethod", "CLOSING")
    effect.setParameter("KernelSizeMm", 3)
    effect.onApply()

    #---SCISSORS---#
    # Set Scissors tool parameters (optional)
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("PaintThresholdMin", "1500")
    effect.setParameter("PaintThresholdMax", "4095")

    # Define the contour for Scissors segmentation
    # Define the contour in each plan using pixel coordinates (For each plans, I checked some coordinates which should be suitable to build the shape and select the part I need)

    points_axial = [[65, 25], [425, 25], [425, 440], [65, 440], [65, 25]]
    points_sagittal = [[35, 256], [35, 460], [256, 460], [256, 256], [35, 256]]
    points_coronal = [[90, 255], [425, 255], [425, 70], [90, 70], [90, 255]]

    # Apply the Scissors tool with the defined contour in each plan
    segmentEditorWidget.setActiveEffectByName("Scissors")
    scissors_effect = segmentEditorWidget.activeEffect()
    scissors_effect.setParameter("ContourAxial", points_axial)
    scissors_effect.setParameter("ContourSagittal", points_sagittal)
    scissors_effect.setParameter("ContourCoronal", points_coronal)
    scissors_effect.onApply()

    #---ERASE OUTSIDE---#
    # Set EraseOutside tool parameters (optional)
    erase_outside_effect = segmentEditorWidget.activeEffect()
    erase_outside_effect.setParameter("MinimumThreshold", "0")
    erase_outside_effect.setParameter("MaximumThreshold", "1499")

    # Apply the EraseOutside tool to remove the exterior of the region defined by the Scissors contour
    segmentEditorWidget.setActiveEffectByName("EraseOutside")
    erase_outside_effect.onApply()

    # Clean up
    slicer.mrmlScene.RemoveNode(segmentEditorNode)

    # Make segmentation results visible in 3D
    segmentationNode.CreateClosedSurfaceRepresentation()

    # Write to STL file in specified coordinate system (LPS)
    output_folder = "C:/Desktop/Segmentations/"
    output_file = "Segmentation_skull_LPS.stl"
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(output_folder, segmentationNode, None, "STL", output_file)

else:
    print("Unable to load the ctvol.nrrd file.")
</code></pre>
<p>With this script, I manage to open the the file, to perform the tresholding and smoothing.<br>
However, the scissors segmentation do not happen and I keep having errors such as : AttributeError: qSlicerSegmentEditorScriptedEffect has no attribute named ‘onApply’.</p>
<p>Thank you very much in advance.</p>

---

## Post #3 by @Jsyy (2024-08-08 01:55 UTC)

<p>i have the same questions, how can i use the scissors to create a contour in Slicer by python code,and how to set coordinates such as axial , sagittal and coronal ?</p>

---
