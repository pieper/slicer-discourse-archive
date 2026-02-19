---
topic_id: 36364
title: "Python Segmentation Conversion Specifying Geometry For Binar"
date: 2024-05-24
url: https://discourse.slicer.org/t/36364
---

# Python segmentation conversion - specifying geometry for binary labelmap

**Topic ID**: 36364
**Date**: 2024-05-24
**URL**: https://discourse.slicer.org/t/python-segmentation-conversion-specifying-geometry-for-binary-labelmap/36364

---

## Post #1 by @LRAnti (2024-05-24 06:35 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.2.2</p>
<p>Hello! I’m trying to alter an existing python script which converts segmentations from an RT Struct dataset to binary labelmaps for export as stls. I’ve found that when I do this manually through the GUI, I get the best result when I use “Advanced Create” in Segmentations, choose the Planar Contour &gt; Closed Surface &gt; Binary Labelmap path, and click “Specify geometry” (it doesn’t matter whether I select the source geometry or not - as long as the spacing is set to 1mm on all axes).</p>
<p>I am trying to replicate this in my script but have had no luck primarily because I have no idea what I’m doing. The current script does this, but it gives me a large stl with a rough surface:</p>
<p>def convert_to_model():<br>
log_info(“Generate Binary Label Map”)<br>
segmentations = slicer.util.getNodesByClass(‘vtkMRMLSegmentationNode’)<br>
segmentations[0].CreateBinaryLabelmapRepresentation()<br>
segmentations[0].SetMasterRepresentationToBinaryLabelmap()</p>
<pre><code>seg = getNode('*RTSTRUCT*')
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()

slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(seg)

# export segmentation to a model
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Segments")

log_info("Export all segments to models")
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(seg, exportFolderItemId)
</code></pre>
<p>Would anyone be able to point me in the direction of what I might do to modify this to use the conversion path/parameters as described above? I’ve spent a long time going through documentation but I’m not quite sure what I’m looking for. I tried using this:</p>
<p>segmentationNode = getNode(“Segmentation”)<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)</p>
<p>but didn’t get the same result as I did from the UI.  Any help would be greatly appreciated!</p>

---

## Post #2 by @cpinter (2024-05-27 09:13 UTC)

<p>If you want to skip the direct Planar contour → Closed surface conversion path so that the Planar contour → Ribbon model → Binary labelmap path is used, you can do this:</p>
<pre><code class="lang-auto">factory = slicer.vtkSegmentationConverterFactory.GetInstance()
factory.DisableConverterRule('Planar contour', 'Closed surface')
</code></pre>

---

## Post #3 by @LRAnti (2024-05-27 09:21 UTC)

<p>Thank you! The main issue is that I can’t find a way to specify the reference image geometry when creating the binary label map. I have noticed that when I click “specify geometry”,  I don’t need to choose a segment, as long as it populates the reference image geometry with generic values like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c294492d8ebf85d344f0ca20f0e66320d740c2ac.png" data-download-href="/uploads/short-url/rLkktr5rY1eMYk9JgDr6SuX3exu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c294492d8ebf85d344f0ca20f0e66320d740c2ac.png" alt="image" data-base62-sha1="rLkktr5rY1eMYk9JgDr6SuX3exu" width="690" height="36" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1028×55 888 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
then the conversion works as expected. I haven’t been able to find a way to replicate this with my python script however. I tried making a dummy volume node, adding spacing values to this and setting reference geometry of the segment I’m trying to convert, but it still doesn’t work. Do you have any suggestions for this?</p>

---

## Post #4 by @cpinter (2024-05-27 11:17 UTC)

<p>This is how you can specify reference geometry from Python:</p>
<pre><code class="lang-auto">referenceGeometryMatrix = #TODO: Specify your direction matrix
extent = [0, 1, 0, 1, 0, 1]  # Arbitrary extent, the "effective extent" will be determined automatically
geometryString = slicer.vtkSegmentationConverter.SerializeImageGeometry(referenceGeometryMatrix, extent)
segmentationNode.GetSegmentation().SetConversionParameter(
  slicer.vtkSegmentationConverter.GetReferenceImageGeometryParameterName(), geometryString)
</code></pre>

---

## Post #5 by @LRAnti (2024-05-27 13:02 UTC)

<p>Thank you so much, I really appreciate the help! I tried using that but am still getting output that is different to what happens when clicking specify geometry on the UI:</p>
<p>This is what I used:<br>
extent = [0,1,0,1,0,1]<br>
matrix = vtk.vtkMatrix4x4()<br>
referenceGeometryMatrix = matrix.Identity()<br>
geometryString = slicer.vtkSegmentationConverter.SerializeImageGeometry(referenceGeometryMatrix, extent)<br>
segmentationNode = getNode(‘<em>RTSTRUCT</em>’)<br>
segmentationNode.GetSegmentation().SetConversionParameter(slicer.vtkSegmentationConverter.GetReferenceImageGeometryParameterName(), geometryString)<br>
segmentationNode.CreateBinaryLabelmapRepresentation()</p>
<p>the console output was:<br>
[VTK] CalculateOutputGeometry: No image geometry specified, default geometry is calculated (0.366345130101627;0;0;-83.49600219726562;0;0.366345130101627;0;355.9289855957031;0;0;0.366345130101627;-47.14999771118164;0;0;0;1;0;299;0;215;0;241;)</p>
<p>[VTK] CalculateOutputGeometry: No image geometry specified, default geometry is calculated (0.8751702253519644;0;0;-128.906005859375;0;0.8751702253519644;0;200.16799926757812;0;0;0.8751702253519644;-114.75;0;0;0;1;0;232;0;253;0;265;)</p>
<p>The resulting representation was still very stepped (it is smooth when specifying geometry with the button on the ui).  Do you have any suggestions?</p>

---

## Post #6 by @cpinter (2024-05-27 14:35 UTC)

<p>The problem is that you don’t actually set a geometry.</p>
<p>After the call</p>
<pre><code class="lang-auto">referenceGeometryMatrix = matrix.Identity()
</code></pre>
<p>referenceGeometryMatrix is <code>None</code>. I strongly suggest that you try to run these lines in the Python console and see the output. It is very easy but super important to see the content of the variables, and unfortunately the <code>Identity()</code> function has no return value.</p>
<p>Do you want to set an identity matrix? Then try</p>
<pre><code class="lang-auto">referenceGeometryMatrix = vtk.vtkMatrix4x4()
</code></pre>

---

## Post #7 by @LRAnti (2024-05-28 03:05 UTC)

<p>Oh right I see!</p>
<p>That worked perfectly to replicate setting the geometry from the UI (just using an identity matrix). Details for anyone experiencing the same problem:</p>
<p>extent = [0,1,0,1,0,1]<br>
referenceGeometryMatrix = vtk.vtkMatrix4x4()<br>
geometryString = slicer.vtkSegmentationConverter.SerializeImageGeometry(referenceGeometryMatrix, extent)<br>
segmentationNode.GetSegmentation().SetConversionParameter(slicer.vtkSegmentationConverter.GetReferenceImageGeometryParameterName(), geometryString)<br>
segmentationNode.CreateBinaryLabelmapRepresentation()</p>
<p>Thank you SO much for your help, I have been battling this for quite some time!</p>

---
