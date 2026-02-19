---
topic_id: 1916
title: "Segmentation To Binary Label Map Through Python Console"
date: 2018-01-23
url: https://discourse.slicer.org/t/1916
---

# Segmentation to binary label map through python console

**Topic ID**: 1916
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/segmentation-to-binary-label-map-through-python-console/1916

---

## Post #1 by @mmtg (2018-01-23 21:09 UTC)

<p>Hello,</p>
<p>I have a lot of RTstructs that I need to convert to binary label maps. I tried using the scripts for exporting to label map in the repository here (<a href="https://www.slicer.org/wiki/Documentation/4.8/ScriptRepository#Export_labelmap_node_from_segmentation_node" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.8/ScriptRepository - Slicer Wiki</a>)</p>
<p>here is the code:</p>
<blockquote>
<p>seg = getNode(‘Segmentation’)<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)<br>
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelmapVolumeNode)</p>
</blockquote>
<p>That worked great except for the fact that the label map node is only the size of the label (if the image is like 512x512x100, the label map ended up being 7x7x3). I assume this is because the label map volume that is created isn’t created with the same image dimensions as the original image. I can do this manually using the segmentations module using export but I would rather do it programmatically. I tried following this example: <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.py#L97" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Utilities/Templates/Modules/ScriptedSegmentEditorEffect/SegmentEditorTemplateKeyLib/SegmentEditorEffect.py at main · Slicer/Slicer · GitHub</a></p>
<p>for creating a label map but I couldn’t get it to work.</p>
<p>Any help that can be provided would be great thanks</p>

---

## Post #2 by @cpinter (2018-01-23 21:22 UTC)

<aside class="quote no-group" data-username="mmtg" data-post="1" data-topic="1916">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b5e925/48.png" class="avatar"> mmtg:</div>
<blockquote>
<p>I have a lot of RTstructs that I need to convert to binary label maps</p>
</blockquote>
</aside>
<p>There is a tool just doing that: <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/_readme.txt" class="inline-onebox">SlicerRT/BatchProcessing/_readme.txt at master · SlicerRt/SlicerRT · GitHub</a></p>
<p>If you insist on using your own code you can call <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L169-L190">ExportVisibleSegmentsToLabelmapNode or a few others</a> that have an argument called referenceVolumeNode where you can specify the reference volume.</p>

---

## Post #3 by @mmtg (2018-01-23 21:32 UTC)

<p>Oh great, thanks. I think I figured out how to do what I was thinking but I can use this.</p>
<p>I just tried to use it in my command line (windows 10), it doesn’t seem to do anything. How are the files supposed to be? Currently they are all dicoms in their own folders (each RTstruct is in its own folder, same with the reference CT). I tried moving them all to the same folder and it didn’t work Here is how I called it:</p>
<p>“C:\Program Files\Slicer 4.8.0\Slicer.exe” --no-main-window --python-script “F:\c study\Python\<a href="http://BatchStructureSetConversion.py" rel="nofollow noopener">BatchStructureSetConversion.py</a>” --input-folder “F:/c study/R1/Ims” --output-folder “F:/contouring study/R1/testBatch”</p>
<p>where the input folder Ims has all the files.</p>
<p>EDIT: also it seems that running this script completely removed everything from my dicom directory?</p>

---

## Post #4 by @drusmanbashir (2018-02-01 15:06 UTC)

<p>Hi, have you tried using the following code to convert segmentation map to a labelmap using your reference volume to determine the dimensions of the labelmap?:</p>
<pre data-code-wrap="python"><code class="lang-python">seg = getNode('Segmentation')
reference = getNode ('InputVolume') # this will be the volume the segmentation was drawn on
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')

ids = vtk.vtkStringArray()
seg.GetDisplayNode().GetVisibleSegmentIDs(ids)
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg, ids, labelmapVolumeNode, reference)
</code></pre>

---

## Post #5 by @Celina_Amber_Gilmore (2024-08-15 19:02 UTC)

<p>Hi! I believe my code is exporting the labelmap volume node without the segmentation.  For reference here is the code I am running after I crop the volumes. The purpose of this code is to segment, threshold, convert to a label map and export and save.</p>
<pre data-code-wrap="python"><code class="lang-python">substack = "Name_set_X_######"
specimen = "Name_set_X_######"
substackLetter = "X"
v1 = "C3"
v2 = "C5"
v3 = "T1"
v4 = "T6"
v5 = "T13"
v6 = "L1"
v7 = "L3"
v8 = "L6"
vert = [v1, v2, v3, v4, v5, v6, v7, v8]
resolution = "30"

for v in vert:
	cr_ca_count = 0
	while cr_ca_count &lt;=1:
		#when cr_ca_count = 0, analyze CRANIAL side of v; when cr_ca_count = 1, analyze CAUDAL side
		cr_ca = "CRANIAL"
		if cr_ca_count == 1:
			cr_ca = "CAUDAL"

		#segment all vertebrae in vert
		crop = getNode(specimen + "_" + v + "_" + cr_ca + "_" + resolution)

		# Compute bone threshold value automatically
		import vtkITK
		thresholdCalculator = vtkITK.vtkITKImageThresholdCalculator()
		thresholdCalculator.SetInputData(crop.GetImageData())
		thresholdCalculator.SetMethodToOtsu()
		thresholdCalculator.Update()
		boneThresholdValue = thresholdCalculator.GetThreshold()
		volumeScalarRange = crop.GetImageData().GetScalarRange()
		logging.info("Volume minimum = {0}, maximum = {1}, bone threshold = {2}".format(volumeScalarRange[0], volumeScalarRange[1], boneThresholdValue))
		slicer.app.processEvents()

		# Create segmentation
		slicer.app.processEvents()
		segmentationNode = slicer.vtkMRMLSegmentationNode()
		slicer.mrmlScene.AddNode(segmentationNode)
		segmentationNode.SetName(specimen + "_" + v + "_" + cr_ca + "_" + resolution + "_Segmentation")
		segmentationNode.CreateDefaultDisplayNodes() # only needed for display
		segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(crop)

		# Create segment editor to get access to effects
		slicer.app.processEvents()
		segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
		segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

		segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
		slicer.mrmlScene.AddNode(segmentEditorNode)
		segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
		segmentEditorWidget.setSegmentationNode(segmentationNode)
		segmentEditorWidget.setSourceVolumeNode(crop)

		# Create bone segment by thresholding
		slicer.app.processEvents()
		boneSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("bone")
		segmentEditorNode.SetSelectedSegmentID(boneSegmentID)
		segmentEditorWidget.setActiveEffectByName("Threshold")
		effect = segmentEditorWidget.activeEffect()
		effect.setParameter("MinimumThreshold",str(boneThresholdValue))
		effect.setParameter("MaximumThreshold",str(volumeScalarRange[1]))
		effect.self().onApply()

		# Make segmentation results nicely visible in 3D
		segmentationDisplayNode = segmentationNode.GetDisplayNode()

		# Export segmentation to binary labelmap
		labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
		ids = vtk.vtkStringArray()
		slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, ids, labelmapVolumeNode, croppedCT)
		slicer.util.saveNode(labelmapVolumeNode, "c:/OMAC_internal_label_maps/Mus_set_" + substackLetter + "/" + specimen + "/" + specimen + "_" + v + "_" + cr_ca + "_" + resolution + ".nrrd")

		# Clean up
		slicer.mrmlScene.RemoveNode(segmentEditorNode)
		segmentEditorWidget = None

		cr_ca_count += 1
</code></pre>
<p>Thank you for your help!</p>

---

## Post #6 by @lassoan (2024-08-19 20:31 UTC)

<p><a class="mention" href="/u/celina_amber_gilmore">@Celina_Amber_Gilmore</a> do you have any questions or you have shared your code to help others with a working example?</p>

---

## Post #7 by @Celina_Amber_Gilmore (2024-08-21 18:26 UTC)

<p>Hi, Can you take a look at the export process of my code? When I export, all of the NRRD files have ‘space directions’ that are the same number for each file. However,’ space origin’ values are different for each NRRD file. These files are being analyzed in BoneJ and when I run the NRRD files, their values are identical. This is problematic because every volume that is cropped is a bone segment so it is suspicious as to why they would have the same value. So I am trying to trace back the error and I am trying to figure out if the code is not saving the volume, segment, and ID correctly. When I “manually” (R-click, export binary labelmap) the segment, the space direction values were the same as the code. So, I am trying to figure out what ‘space direction’ means exactly, because in the NRRD files that were running fine, their space direction values were not identical. The protocol has not changed when running those segments. I am asking for help to confirm that the code to export the segmentation as a binary labelmap is correct.</p>

---
