---
topic_id: 33640
title: "Save Model As Stl In Ras"
date: 2024-01-05
url: https://discourse.slicer.org/t/33640
---

# Save model as stl in RAS

**Topic ID**: 33640
**Date**: 2024-01-05
**URL**: https://discourse.slicer.org/t/save-model-as-stl-in-ras/33640

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-01-05 11:43 UTC)

<p>Hi, at this time I’m trying to export the model node as RAS stl. Diving into documentation I saw that stl are saved as LPS by default, but it wont work for me…</p>
<p>Now I’m doing a quite simple process:</p>
<pre><code class="lang-auto">'Export segments to Models:'
    
    segmentationNode = slicer.util.getNode(segmentationName)
    segmentIDs = segmentationNode.GetSegmentation().GetSegmentIDs()
    segmentNames = [segmentationNode.GetSegmentation().GetSegment(segmentID).GetName() for segmentID in segmentIDs]
    'Create a folder to export models inside.'
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Segments")
    slicer.modules.segmentations.logic().ExportSegmentsToModels(segmentationNode,segmentIDs, exportFolderItemId)type or paste code here


    modelNode = slicer.util.getNode(segmentName)
    stlPath = os.path.join(saveResults_path,segmentName)
    slicer.util.saveNode(modelNode, stlPath+'.stl')
</code></pre>

---

## Post #3 by @mikebind (2024-01-05 21:42 UTC)

<p>You can control the coordinate system for a saved model by using the SetCoordinateSystem() method on the model storage node: <a href="https://apidocs.slicer.org/v5.0/classvtkMRMLModelStorageNode.html#a6fcf7b8b2f8281c171064b8020998c52" class="inline-onebox">Slicer: vtkMRMLModelStorageNode Class Reference</a></p>
<p>I think this should work:</p>
<pre><code class="lang-auto">modelStorageNode = modelNode.GetStorageNode()
modelStorageNode.SetCoordinateSystem(slicer.vtkMRMLStorageNode.CoordinateSystemRAS)
stlPath = os.path.join(saveResults_path,segmentName)
slicer.util.saveNode(modelNode, stlPath+'.stl')
</code></pre>

---
