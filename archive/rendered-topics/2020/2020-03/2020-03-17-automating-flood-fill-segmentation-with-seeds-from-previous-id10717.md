# Automating "Flood Fill" segmentation with seeds from previous marker locations

**Topic ID**: 10717
**Date**: 2020-03-17
**URL**: https://discourse.slicer.org/t/automating-flood-fill-segmentation-with-seeds-from-previous-marker-locations/10717

---

## Post #1 by @jdp (2020-03-17 13:49 UTC)

<p>Sorry if this is a basic question but I’m currently trying to automate a segmentation tool for my project needs. I basically want to segment a preprocessed image volume in which I previously collected fiducial marker locations. To segment, I want to use the “flood filling” - which I can do manually. However, I want to automate the segmentation process. Is there a way for me seed the “flood filling” with a control point that I previously collected with a marker and then turn off ‘flood filling’ - using python scripting and not manually clicking as my code below requires? This is what I have so far from online resources - I think I would need to add something between the “flood filling” and “none” active effect by name settings. Any advice would be appreciated:</p>
<p>masterVolumeNode = slicer.util.getNode(‘Preproccessed Image’)</p>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.show()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
slicer.mrmlScene.AddNode(segmentEditorNode)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)</p>
<p>segmentationNode = slicer.vtkMRMLSegmentationNode()<br>
segmentationNode.GetSegmentation().AddEmptySegment(“skin”)<br>
slicer.mrmlScene.AddNode(segmentationNode)<br>
segmentationNode.CreateDefaultDisplayNodes()<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</p>
<p>segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</p>
<p>segmentEditorWidget.setActiveEffectByName(‘Flood filling’)<br>
segmentEditorWidget.setActiveEffectByName(‘None’)</p>

---

## Post #2 by @lassoan (2020-03-18 03:02 UTC)

<p>I’ve split out the logic that performs the actual processing in Flood Fill effect into a new method: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/4fda27c827e2ddfe334a5e4069ebb5e2950f65b4/SegmentEditorFloodFilling/SegmentEditorFloodFillingLib/SegmentEditorEffect.py#L142">floodFillFromPoint</a>.</p>
<p>You can call this method (after you activated the effect) like this:</p>
<pre><code class="lang-python">floodFillEffect=slicer.modules.segmenteditor.widgetRepresentation().self().editor.activeEffect().self()
floodFillEffect.floodFillFromPoint([130,65,28])
</code></pre>
<p>The coordinates are IJK voxel coordinates of the master volume. You can find <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates">here</a> how to get IJK coordinates from RAS coordinates (such as physical position of a markups fiducial point).</p>

---

## Post #3 by @jdp (2020-03-18 06:14 UTC)

<p>Thank you very much for building that method for me, Iassoan!</p>
<p>For those who are interested I have provided my rough, sample code that I was able to pull together from online resources. One needs to make sure the new function that Lassoan created is added to the segmentation editor module - I did this manually. The following code takes an image volume and fiducial marker node called “Right Vertebral Artery” and flood fills, i.e., segments, the image based on the marker’s first control point. The code then converts the segmentation to a surface mesh model.</p>
<pre><code class="lang-python">masterVolumeNode = slicer.util.getNode('Preproccessed Image')

segmentEditorWidget = slicer.qMRMLSegmentEditorWidget() 
segmentEditorWidget.show() 
segmentEditorWidget.setMRMLScene(slicer.mrmlScene) 
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode() 
slicer.mrmlScene.AddNode(segmentEditorNode) 
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode) 


segmentationNode = slicer.vtkMRMLSegmentationNode() 
segmentationNode.GetSegmentation().AddEmptySegment("skin")
slicer.mrmlScene.AddNode(segmentationNode) 
segmentationNode.CreateDefaultDisplayNodes() 
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode) 


segmentEditorWidget.setSegmentationNode(segmentationNode) 
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode) 


segmentEditorWidget.setActiveEffectByName('Flood filling')

R0 = slicer.util.getNode('Right Vertebral Artery').GetNthControlPointPositionVector(0)[0]
R1 = slicer.util.getNode('Right Vertebral Artery').GetNthControlPointPositionVector(0)[1]
R2 = slicer.util.getNode('Right Vertebral Artery').GetNthControlPointPositionVector(0)[2]

# Get point coordinate in RAS
point_Ras = [R0, R1, R2, 1]
markupsNode.GetNthFiducialWorldCoordinates(markupsIndex, point_Ras)

# If volume node is transformed, apply that transform to get volume's RAS coordinates
transformRasToVolumeRas = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transformRasToVolumeRas)
point_VolumeRas = transformRasToVolumeRas.TransformPoint(point_Ras[0:3])

# Get voxel coordinates from physical coordinates
volumeRasToIjk = vtk.vtkMatrix4x4()
masterVolumeNode.GetRASToIJKMatrix(volumeRasToIjk)
point_Ijk = [0, 0, 0, 1]
volumeRasToIjk.MultiplyPoint(numpy.append(point_VolumeRas,1.0), point_Ijk)
point_Ijk = [ int(round(c)) for c in point_Ijk[0:3] ]

# Print output
print(point_Ijk)

a = segmentEditorWidget.activeEffect().self()
a.floodFillFromPoint(point_Ijk)

segmentEditorWidget.setActiveEffectByName('None')


segmentationNode = getNode("Segmentation")
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Segments")
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)
</code></pre>

---
