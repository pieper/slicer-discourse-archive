---
topic_id: 30281
title: "Problems Applying Autothresholdmethod"
date: 2023-06-28
url: https://discourse.slicer.org/t/30281
---

# Problems applying AutoThresholdMethod

**Topic ID**: 30281
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/problems-applying-autothresholdmethod/30281

---

## Post #1 by @Ikannuna (2023-06-28 14:11 UTC)

<p>Hello and good afternoon,</p>
<p>Iam new to 3D Slicer and using it in a project for university.</p>
<p>The goal is to segment DICOM bone scans automatically with python via the implemented AutoThresholdMethod’s Otsu, Iso Data, Maximum Entropy and so on and later on compare them.</p>
<p>Iam having big problems applying the AutoThresholdMethod via .setParameter.<br>
Using MaximumThreshold or MinimumThreshold works for my case.</p>
<p>Below is my code, iam thankful for any advice.</p>
<p>Greetings</p>
<pre><code class="lang-auto">
import os
import vtk
import DICOMLib.DICOMUtils as utils

utils.openDatabase('/Dicom')
utils.importDicom('/Dicom')

patients = slicer.dicomDatabase.patients()

utils.loadPatientByUID(patients[0])

scene = slicer.mrmlScene
segmentationNode = slicer.vtkMRMLSegmentationNode()
scene.AddNode(segmentationNode)
volumeNodes = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
volumeNode = volumeNodes[0] if volumeNodes else None
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
segmentId = segmentationNode.GetSegmentation().AddEmptySegment("OTSU")

segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(volumeNode)
segmentEditorWidget.setCurrentSegmentID(segmentId) 

segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()

# Here seems to be the main problem, chaning the AutoThresholdMethod to different methods 
# does not apply the Method, all generated stls stay the same

effect.setParameter("AutoThresholdMethod", "OTSU")
effect.setParameter("AutoThresholdMode", "SET_LOWER")

#uncommenting and applying the MaximumThreshold works as intended
#effect.setParameter("MaximumThreshold", "450")


effect.self().onApply()

modelNode = slicer.vtkMRMLModelNode()
modelNode.SetName("3DModel")
slicer.mrmlScene.AddNode(modelNode)

modelDisplayNode = slicer.vtkMRMLModelDisplayNode()
slicer.mrmlScene.AddNode(modelDisplayNode)

modelNode.SetAndObserveDisplayNodeID(modelDisplayNode.GetID())

segmentation = segmentationNode.GetSegmentation()
segmentation.CreateRepresentation("Closed surface")

output_path = os.path.join('/Datensatz_Ulna_CT-Scan')

segmentationLogic = slicer.modules.segmentations.logic()

segmentIds = vtk.vtkStringArray()
segmentIds.InsertNextValue(segmentId)

segmentationLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(output_path, segmentationNode, segmentIds, "STL")

slicer.util.exit()
</code></pre>

---

## Post #2 by @MarkHan0518 (2023-11-26 23:35 UTC)

<p>I am encountering the same issue. Any luck in solving the problem?</p>

---

## Post #3 by @lassoan (2023-11-27 05:11 UTC)

<p>It seems that updating of the threshold (by calling <code>onAutoThreshold</code>) was missed in the script.</p>
<p>However, I would not recommend to use these algorithms. The main reason I added these automatic thresholding methods to the Threshold tool was to allow people to see for themselves how useless these methods are. Global thresholding is a very limited, fragile, method, which very rarely makes sense:</p>
<ul>
<li>For CT images, voxel values are in HU, so it is better to hardcode a specific value. In other imaging modalities, global thresholding is usually not sufficient for meaningful segmentation and the chance that one of the automatic methods guess the optimal threshold value is quite low.</li>
<li>The automatic algorithms may provide completely different threshold values depending on cropping of the image or filling value of the unexposed image area (e.g., outside the cylinder-shaped reconstructed CT image).</li>
</ul>
<p>Instead of using global thresholding, I would recommend fully-automatic neural network based segmentation tools, such as TotalSegmentator, HD-BET, and many others. You can train your own segmentation model using MONAILabel extension.</p>

---
