---
topic_id: 26096
title: "Use Orient Scaler Volume In Python Interactor For Batch Proc"
date: 2022-11-06
url: https://discourse.slicer.org/t/26096
---

# Use orient scaler volume in python interactor for batch processing

**Topic ID**: 26096
**Date**: 2022-11-06
**URL**: https://discourse.slicer.org/t/use-orient-scaler-volume-in-python-interactor-for-batch-processing/26096

---

## Post #1 by @hourieh (2022-11-06 23:44 UTC)

<p>Operating system:windows<br>
Slicer version:5.0.3<br>
Expected behavior:i want to orient my .nii volumes to axial dicom volumes in python code but I can not find any example of that. please help me!<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2022-11-07 05:00 UTC)

<p>You can find <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format">example of how to export a volume to DICOM using Python in the script repository</a>.</p>

---

## Post #3 by @hourieh (2022-11-07 07:28 UTC)

<p>Thank you for your quick response.<br>
i used this code but it export my volume to saggital slices and I want axial slice…<br>
i wrote this for changing to axial but not working and I got the same result as before:</p>
<p>volumeNode = slicer.util.loadVolume(r"F:\arshad\payannameh\New folder (3)\MRI\ADNI_002_S_0413_MR_MPR__GradWarp__B1_Correction__N3_Br_20070821171714281_S22557_I69527.nii", {"name ": ‘alzheimerMRI’})</p>
<p>axialSliceToRas=vtk.vtkMatrix3x3()<br>
sliceNode = getNode(“ADNI_002_S_0413_MR_MPR__GradWarp__B1_Correction__N3_Br_20070821171714281_S22557_I69527”)<br>
red_logic = slicer.app.layoutManager().sliceWidget(“Red”).sliceLogic()<br>
red_cn = red_logic.GetSliceCompositeNode()<br>
red_logic.GetSliceCompositeNode().SetBackgroundVolumeID(sliceNode.GetID())</p>
<p>outputFolder = r"F:\arshad\payannameh\New folder (3)\axial\New folder"</p>
<p>slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)<br>
patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(), “test patient”)<br>
studyItemID = shNode.CreateStudyItem(patientItemID, “test study”)<br>
volumeShItemID = shNode.GetItemByDataNode(sliceNode)<br>
shNode.SetItemParent(volumeShItemID, studyItemID)</p>
<p>import DICOMScalarVolumePlugin<br>
exporter = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()<br>
exportables = exporter.examineForExport(volumeShItemID)<br>
for exp in exportables:<br>
exp.directory = outputFolder<br>
exp.setTag(‘PatientID’, “test patient”)<br>
exp.setTag(‘StudyID’, “test study”)</p>
<p>exporter.export(exportables)</p>
<p>In addition, can I use orient scaler volume module to achieve my goal?<br>
if yes how to use it in python interaction?</p>

---

## Post #4 by @hourieh (2022-11-07 12:49 UTC)

<p>I was able to find the solution with your help:</p>
<pre><code>volumeNode = slicer.util.loadVolume(inputdir)

slicer.util.selectModule('OrientScalarVolume')
orient_scalar = slicer.modules.orientscalarvolume


outputVolume = slicer.vtkMRMLScalarVolumeNode()
slicer.mrmlScene.AddNode(outputVolume)
outputVolume.CreateDefaultDisplayNodes()
outputVolume.SetName("output_orient")

parametersOrient = {}
parametersOrient["inputVolume1"] = volumeNode
parametersOrient["outputVolume"] = outputVolume
parametersOrient["orientation"] = 'Axial'

orientNode = None
orientNode = slicer.cli.runSync(orient_scalar, None, parametersOrient)        
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(), "test patient")
studyItemID = shNode.CreateStudyItem(patientItemID, "test study")
volumeShItemID = shNode.GetItemByDataNode(outputVolume)
shNode.SetItemParent(volumeShItemID, studyItemID)

import DICOMScalarVolumePlugin
exporter = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
exportables = exporter.examineForExport(volumeShItemID)
for exp in exportables:
    exp.directory = outputdir
    exp.setTag('PatientID', "test patient")
    exp.setTag('StudyID', "test study")

exporter.export(exportables)
</code></pre>

---
