---
topic_id: 15773
title: "Overlapping Segmentions Export To Nifti"
date: 2021-02-01
url: https://discourse.slicer.org/t/15773
---

# Overlapping Segmentions Export to NIFTI

**Topic ID**: 15773
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/overlapping-segmentions-export-to-nifti/15773

---

## Post #1 by @Pete (2021-02-01 14:09 UTC)

<p>Hi,</p>
<p>Apologies if this has been answered elsewhere, but my search can only find answers regarding NON-overlapping segmentations.</p>
<p>I have segmented a DICOM image and have 4 different segmentations. These all overlap.</p>
<p>I need to export as NIFTI (as that is the only filetype compatible with my colleagues Radiomics software). If I “export to file” as NIFTI some data is obviously lost due to the overlap. I have been able to compensate for this by hiding all layers but one, exporting to file, change to another layer, export to file and repeat for the 4 layers.</p>
<p>Is it possible to reduce the number of steps, i.e. export each segmentation to a separate NIFTI file rather than hiding/unhiding each one and manually saving?</p>
<p>Many thanks in advance,</p>
<p>Pete</p>

---

## Post #2 by @lassoan (2021-02-01 14:49 UTC)

<p>Nifti is a very rigid neuroimaging file format. There is no clean way of encoding 4D segmentations and metadata in it. On the other hand, nrrd is a simple, much more flexible, general-purpose file format that can store all the necessary metadata. Unless there is a very very strong community pressure to improve Nifti support (and preferably accompanied by improvement of the Nifti file format), we will probably not invest time into it.</p>
<p>Since .nrrd file readers are available in all development environments (and due to simplicity of the file format, parsers can be implemented with very small effort, if additional dependencies to existing nrrd readers are unacceptable), it should be no problem to add nrrd support to your colleagues radiomics software. What programming language that software is implemented in and what libraries it is using already?</p>
<p>You can of course write a Python script that saves each segment in a separate volume (it would probably take 3-4 lines of code). You can find all the code pieces that you need in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">Slicer script repository</a>.</p>

---

## Post #3 by @Pete (2021-02-05 01:29 UTC)

<p>Thanks for your helpful and explanatory answer. I believe it is custom software based off Matlab analysis.</p>
<p>Unfortunately I think the python scripting is probably beyond my skills but I will take a look.</p>

---

## Post #4 by @lassoan (2021-02-05 03:23 UTC)

<p>There are several nrrd file readers for Matlab. For example, you can try this one (used by SlicerMatlabBridge): <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">nrrdread.m</a></p>

---

## Post #5 by @Pete (2021-02-05 11:42 UTC)

<p>Thanks for that suggestion I will pass it on to my colleague.</p>
<p>I have had a go with the python code and have been partially successful but get a syntax error for final line:</p>
<pre><code>segmentationNode = getNode('Segmentation')
segmentNames = ["Single", "Multi"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode)
</code></pre>
<p>For clarity my segmentation is called “Segmentation” and it contains segments named “Single”, “Multi”. My ultimate goal is to export each segment as a separate nifti (nii.gz) as they do overlap.</p>
<p>Is anyone able to point to what I am doing wrong? Do I need to create a labelmapVolumeNode first?</p>
<p>Many thanks in advance,</p>
<p>Pete</p>

---

## Post #6 by @lassoan (2021-02-05 15:37 UTC)

<p>What was the error message?</p>

---

## Post #7 by @Pete (2021-02-05 15:40 UTC)

<p>This was all that was listed in the error console:</p>
<pre><code> File "&lt;console&gt;", line 4
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode)
         ^
SyntaxError: invalid syntax</code></pre>

---

## Post #8 by @lassoan (2021-02-05 15:47 UTC)

<p>This works for me with a recent Slicer Preview Release:</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
referenceVolumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
segmentNames = ["Segment_1", "Segment_2"]
for segmentName in segmentNames:
    segmentIds = vtk.vtkStringArray()
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode)
</code></pre>

---

## Post #9 by @Pete (2021-02-05 16:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="15773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">segmentationNode = getNode('Segmentation')
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
referenceVolumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
segmentNames = ["Segment_1", "Segment_2"]
for segmentName in segmentNames:
    segmentIds = vtk.vtkStringArray()
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode)
</code></pre>
</blockquote>
</aside>
<p>Many thanks, that does export to a new Labelmap, but it is still a combined one. I am trying to get it to export each segment (single and multi) to their own Labelmap so I can then export them easily as separate files. Sorry if I am being stupid.</p>

---

## Post #10 by @lassoan (2021-02-05 16:34 UTC)

<p>You need to add a line in the for loop after the <code>ExportSegmentsToLabelmapNode...</code> line to write to file, or use a method that writes selected segments to file directly using <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#ace576efb43c16ee0478bf077b3324cff"> ExportSegmentsBinaryLabelmapRepresentationToFiles</a> method.</p>

---

## Post #11 by @Pete (2021-02-05 21:17 UTC)

<p>Great, that was a big help. I have it exporting to file using ExportSegmentsBinaryLabelmapRepresentationToFiles as you suggested. It always saves the file as Segmentation.nii.gz. Is there a way to specify the file name, so I can run the script more than once to export individual segments as their segment name or ID? Meaning it won’t overwrite itself</p>
<pre><code>extension = "nii.gz"
useCompression = "true"
destinationFolder = "/Users/pete/Public/Test"
segmentationNode = getNode('Segmentation')
segmentNames = ["Mask"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(destinationFolder, segmentationNode, segmentIds, extension, useCompression)</code></pre>

---

## Post #12 by @lassoan (2021-02-06 01:44 UTC)

<p>Filename is the same as the segmentation node name, so if you want to change the filename then you can temporarily rename the segmentation node.</p>

---

## Post #13 by @Pete (2021-02-06 10:14 UTC)

<p>Great idea, working perfectly now. Thanks so much for your extensive help. In case anyone else wants to do something similar, here is my final code:</p>
<pre><code># ***** THE FINAL SCRIPT *****

# Required to have 3 segments - "Mask", "Single", "Multi"

# Save Image data as Image Data.nii.gz

node = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
file_path = "/Users/pete/OneDrive/ImageData.nii.gz"
properties = {'useCompression': 1}; #use compression
slicer.util.saveNode(node, file_path, properties)

# Get segmentation called "Segmentation" and rename to "Single"

segmentationNode = getNode('Segmentation')
segmentationNode.GetName()
segmentationNode.SetName('Single')

# get segment "Single" and export to Single.nii.gz

extension = "nii.gz"
useCompression = "true"
destinationFolder = "/Users/pete/OneDrive"
segmentationNode = getNode('Single')
segmentNames = ["Single"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(destinationFolder, segmentationNode, segmentIds, extension, useCompression)

# Get segmentation called "Single" and rename to "Multi"

segmentationNode = getNode('Single')
segmentationNode.GetName()
segmentationNode.SetName('Multi')

# get segment "Multi" and export to Multi.nii.gz

segmentationNode = getNode('Multi')
segmentNames = ["Multi"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(destinationFolder, segmentationNode, segmentIds, extension, useCompression)

# Get segmentation called "Multi" and rename to "Mask"

segmentationNode = getNode('Multi')
segmentationNode.GetName()
segmentationNode.SetName('Mask')

# get segment "Mask" and export to Mask.nii.gz

segmentationNode = getNode('Mask')
segmentNames = ["Mask"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
    slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(destinationFolder, segmentationNode, segmentIds, extension, useCompression)

# Get segmentation called "Mask" and rename to "Segmentation"

segmentationNode = getNode('Mask')
segmentationNode.GetName()
segmentationNode.SetName('Segmentation')
segmentationNode.GetName()</code></pre>

---

## Post #14 by @rbumm (2023-01-02 18:14 UTC)

<p>Thanks Pete,</p>
<p>fed that into ChatGPT and maybe it is interesting what the bot said:</p>
<p>ChatGPT:</p>
<p>I removed the unnecessary lines of code where the segmentation node<br>
is re-assigned to a new node with the same name and made some other<br>
minor changes to improve the readability of the script.<br>
Let me know if you have any questions!</p>
<pre><code class="lang-auto"># ***** THE FINAL SCRIPT *****

# Required to have 3 segments - "Mask", "Single", "Multi"

# Save Image data as Image Data.nii.gz

node = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
file_path = "/Users/pete/OneDrive/ImageData.nii.gz"
properties = {'useCompression': 1} # use compression
slicer.util.saveNode(node, file_path, properties)

# Get segmentation called "Segmentation"

segmentationNode = getNode('Segmentation')

# Rename segmentation to "Single"
segmentationNode.SetName('Single')

# get segment "Single" and export to Single.nii.gz

extension = "nii.gz"
useCompression = "true"
destinationFolder = "/Users/pete/OneDrive"
segmentNames = ["Single"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(destinationFolder, segmentationNode, segmentIds, extension, useCompression)

# Rename segmentation to "Multi"
segmentationNode.SetName('Multi')

# get segment "Multi" and export to Multi.nii.gz

segmentNames = ["Multi"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(destinationFolder, segmentationNode, segmentIds, extension, useCompression)

# Rename segmentation to "Mask"
segmentationNode.SetName('Mask')

# get segment "Mask" and export to Mask.nii.gz

segmentNames = ["Mask"]
segmentIds = vtk.vtkStringArray()
for segmentName in segmentNames:
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentIds.InsertNextValue(segmentId)
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsBinaryLabelmapRepresentationToFiles(destinationFolder, segmentationNode, segmentIds, extension, useCompression)

# Rename segmentation to "Segmentation"
segmentationNode.SetName('Segmentation')

</code></pre>

---
