---
topic_id: 2510
title: "Vtkobjexporter Model Down Quality"
date: 2018-04-04
url: https://discourse.slicer.org/t/2510
---

# vtkObjExporter- model down quality

**Topic ID**: 2510
**Date**: 2018-04-04
**URL**: https://discourse.slicer.org/t/vtkobjexporter-model-down-quality/2510

---

## Post #1 by @anandmulay3 (2018-04-04 07:48 UTC)

<p>I’m getting so down quality obj file,</p>
<ul>
<li>when i try to get it using vtkObjexporter i get this output, …<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08fd82e1e3d58bf60a2ec3a766a6b9a97282cb01.png" alt="Capture2" data-base62-sha1="1hwXPXUgR2N0K93bIOfm43Se71n" width="362" height="215"></li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6848d82d04059674d635fd64d2e255c7ab0df8c.png" alt="Capture1" data-base62-sha1="skawZDHRzAr8aJoZFQY8dyUmOAY" width="416" height="248"></p>
<ul>
<li>And same model when i export it using segmentation exporter in slicer UI in latest slicer 4.9</li>
</ul>
<p>am i missing any parameter??</p>

---

## Post #2 by @lassoan (2018-04-04 18:35 UTC)

<p>There should be no extra smoothing. Are you sure that the software that you use to view the exported file does not apply smoothing? How the model looks in ParaView?</p>
<p>How do you use vtkOBJExporter? What do you do exactly: what buttons you click / what code do you execute?</p>
<p>It would help a lot if you could go back to your post and edit it so that it is clear where sentences start and end, and which picture belongs to which sentence. Right now, it is not clear if you want to get the top or the bottom image.</p>

---

## Post #3 by @anandmulay3 (2018-04-05 06:46 UTC)

<p>ohh sorry for bad arrangement of images in post<br>
I’m using windows MR viewer of windows 10 and 3D paint which comes default in windows 10.<br>
I;m using same code which you have given for exporting stl file of segmentation, stl works perfect but i’m getting this weird output for obj.</p>
<p>Code:</p>
<p>/Segmentation<br>
masterVolumeNode = getNode(‘Sft’)</p>
<p>/ Create segmentation<br>
segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)<br>
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(“skin”)</p>
<p>/ Create segment editor to get access to effects<br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</p>
<p>/ Thresholding<br>
segmentEditorWidget.setActiveEffectByName(“Threshold”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“MinimumThreshold”,“300”)<br>
effect.setParameter(“MaximumThreshold”,“5695”)<br>
effect.self().onApply()</p>
<p>/ Smoothing<br>
segmentEditorWidget.setActiveEffectByName(“Smoothing”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“SmoothingMethod”, “MEDIAN”)<br>
effect.setParameter(“KernelSizeMm”, 3)<br>
effect.self().onApply()</p>
<p>/ Clean up<br>
segmentEditorWidget = None<br>
slicer.mrmlScene.RemoveNode(segmentEditorNode)<br>
/ Make segmentation results visible in 3D<br>
segmentationNode.CreateClosedSurfaceRepresentation()</p>
<p>/ Make sure surface mesh cells are consistently oriented<br>
surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)<br>
normals = vtk.vtkPolyDataNormals()<br>
normals.AutoOrientNormalsOn()<br>
normals.ConsistencyOn()<br>
normals.SetInputData(surfaceMesh)<br>
normals.Update()<br>
surfaceMesh = normals.GetOutput()</p>
<p>/Write to OBJ file<br>
lm = slicer.app.layoutManager()<br>
tdv = lm.threeDWidget(0).threeDView()<br>
rw = tdv.renderWindow()<br>
Move renderer temporarily into another renderWindow<br>
It will make the application crash, but it allows the scene export to complete successfully.<br>
rw2 = vtk.vtkRenderWindow()<br>
rw2.AddRenderer(rw.GetRenderers().GetFirstRenderer())<br>
o = vtk.vtkOBJExporter()<br>
o.SetFilePrefix(‘c:/Anand Work/test’)<br>
o.SetRenderWindow(rw2)<br>
o.Write()</p>
<p>and yes , in slicer 3d view it looks perfect</p>

---

## Post #4 by @lassoan (2018-04-06 00:31 UTC)

<p>In recent nightly builds, export to file feature is built in - <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428/2">Save segmentation directly to STL or OBJ files</a>. I would recommend to use that.</p>

---

## Post #5 by @anandmulay3 (2018-04-06 08:18 UTC)

<p>Thanks , latest segmentation export works fine <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
