---
topic_id: 26747
title: "How To Create A Python Module In Slicer From A Python Script"
date: 2022-12-15
url: https://discourse.slicer.org/t/26747
---

# How to create a Python Module in slicer from a python script?

**Topic ID**: 26747
**Date**: 2022-12-15
**URL**: https://discourse.slicer.org/t/how-to-create-a-python-module-in-slicer-from-a-python-script/26747

---

## Post #1 by @bremsstrahlung (2022-12-15 15:08 UTC)

<p>I have a python script that i paste in the Python Interactive console to achieve whatever task that i wish to. How do i convert this code into a simple module where the user just clicks on the module and the code runs?</p>
<p>Edit: I’m adding the script i wish to convert to a module below:</p>
<pre><code class="lang-python">import SampleData
import numpy as np
import random

def segmentation():
	sampleDataLogic = SampleData.SampleDataLogic()
	masterVolumeNode = sampleDataLogic.downloadSample('MRHead')
	volumeNode = arrayFromVolume(getNode('MRHead'))
	p = np.shape(volumeNode)[0]
	q = np.shape(volumeNode)[1]
	r = np.shape(volumeNode)[2]
	volumeNode = getNode('MRHead')
	point_Ijk = [r,q,p]
	volumeIjkToRas = vtk.vtkMatrix4x4()
	volumeNode.GetIJKToRASMatrix(volumeIjkToRas)
	point_VolumeRas = [0, 0, 0, 1]
	volumeIjkToRas.MultiplyPoint(np.append(point_Ijk,1.0), point_VolumeRas)
	transformVolumeRasToRas = vtk.vtkGeneralTransform()
	slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(volumeNode.GetParentTransformNode(), None, transformVolumeRasToRas)
	point_Ras = transformVolumeRasToRas.TransformPoint(point_VolumeRas[0:3])
	pqr_ras = [ ]
	for i in point_Ras:
		if i&lt;0:
			pqr_ras.append(-1*i)
		else:
			pqr_ras.append(i)
	roiNode = slicer.mrmlScene.AddNode(slicer.vtkMRMLAnnotationROINode())
	roiNode.SetRadiusXYZ(pqr_ras[0], pqr_ras[1], pqr_ras[2]/2)
	roiNode.SetXYZ(0,0,pqr_ras[2]/4)
	cropVolumeLogic = slicer.modules.cropvolume.logic()
	cropVolumeParameterNode = slicer.vtkMRMLCropVolumeParametersNode()
	cropVolumeParameterNode.SetROINodeID(roiNode.GetID())
	cropVolumeParameterNode.SetInputVolumeNodeID(volumeNode.GetID())
	cropVolumeParameterNode.SetVoxelBased(True)
	cropVolumeLogic.Apply(cropVolumeParameterNode)
	croppedVolume = slicer.mrmlScene.GetNodeByID(cropVolumeParameterNode.GetOutputVolumeNodeID())
	masterVolumeNode = getNode('MRHead cropped')
	segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
	segmentationNode.CreateDefaultDisplayNodes()
	segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
	segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
	segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
	segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
	segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
	segmentEditorWidget.setSegmentationNode(segmentationNode)
	segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
	segmentName = "Skull"
	thresholdMin = 20
	thresholdMax = 279
	addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
	segmentEditorNode.SetSelectedSegmentID(addedSegmentID)
	segmentEditorWidget.setActiveEffectByName("Threshold")
	effect = segmentEditorWidget.activeEffect()
	effect.setParameter("MinimumThreshold",str(thresholdMin))
	effect.setParameter("MaximumThreshold",str(thresholdMax))
	effect.self().onApply()
	segmentEditorWidget.setActiveEffectByName("Islands")
	effect = segmentEditorWidget.activeEffect()
	effect.setParameter("MinimumSize","1000")
	effect.setParameter("Operation","KEEP_LARGEST_ISLAND")
	segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
	effect.self().onApply()
	segmentEditorWidget = None
	slicer.mrmlScene.RemoveNode(segmentEditorNode)
	getNode('Segmentation').CreateClosedSurfaceRepresentation()
	segmentationNode = getNode("Segmentation")
	labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
	slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)
	segmentationNode = getNode("Segmentation")
	# Export segments to models
	shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
	exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Skull")
	slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)
	segmentModels = vtk.vtkCollection()
	shNode.GetDataNodesInBranch(exportFolderItemId, segmentModels)
	# Get exported model of first segment
	modelNode = segmentModels.GetItemAsObject(0)

segmentation()
</code></pre>

---

## Post #2 by @jcfr (2022-12-15 16:27 UTC)

<p>Using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html#extension-wizard">Extension Wizard</a> module will allow you to create a skeleton where you could integrate the logic you implemented.</p>
<p>Since your module is completely written in python, you can create the skeleton using the Slicer downloaded from <a href="https://download.slicer.org">https://download.slicer.org</a> without having to “build” the program.</p>
<p>Looking at the following resources will also be helpful:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#create-an-extension">Developer Guide / Extensions / Create an extension</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">Tutorials for developers</a></li>
<li><a href="https://discourse.slicer.org/t/how-to-release-an-extension/26289" class="inline-onebox">How to release an extension</a></li>
</ul>

---
