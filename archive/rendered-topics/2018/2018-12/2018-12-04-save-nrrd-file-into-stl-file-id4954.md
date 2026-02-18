# Save .nrrd file into STL file

**Topic ID**: 4954
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/save-nrrd-file-into-stl-file/4954

---

## Post #1 by @M_pavi (2018-12-04 18:44 UTC)

<p>Can we save full .nrrd file to STL file without doing any segmentation ?</p>

---

## Post #2 by @cpinter (2018-12-04 18:59 UTC)

<p>If your nrrd is binary (i.e. contains a segmentation) then you can load it as a labelmap (click Show Options in the load window and check LabelMap option). Then go to Data module, right-click the labelmap, select Convert labelmap to segmentation node. Then go to the Segmentations module, select the segmentation, go to the very bottom to the Export to files section, then select your options and click Export.</p>

---

## Post #3 by @S_Arbabi (2022-02-24 15:18 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>,<br>
Can I also write the segmentation node as stl from python code?</p>

---

## Post #4 by @cpinter (2022-02-25 09:38 UTC)

<p>Yes, using one of these functions:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L161-L169">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L161-L169" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L161-L169" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L161-L169</a></h4>



    <pre class="onebox">      <code class="lang-h">
        <ol class="start lines" start="161" style="counter-reset: li-counter 160 ;">
            <li>/// Export visible segments into a folder, a model node from each segment</li>
            <li>/// \param segmentationNode Segmentation node from which the the segments are exported</li>
            <li>/// \param folderItemId Subject hierarchy folder item ID to export the segments to</li>
            <li>static bool ExportVisibleSegmentsToModels(vtkMRMLSegmentationNode* segmentationNode, vtkIdType folderItemId);</li>
            <li>
            <li>/// Export all segments into a folder, a model node from each segment</li>
            <li>/// \param segmentationNode Segmentation node from which the the segments are exported</li>
            <li>/// \param folderItemId Subject hierarchy folder item ID to export the segments to</li>
            <li>static bool ExportAllSegmentsToModels(vtkMRMLSegmentationNode* segmentationNode, vtkIdType folderItemId);</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @S_Arbabi (2022-03-03 09:05 UTC)

<p>I tried to export an nrrd segmentation to an stl file using ExportAllSegmentsToModels function. I searched for similar examples and here is how I tried to do it, but it still doesn’t work, any ideas?</p>
<pre><code class="lang-auto">    #loading DICOM image and its nrrd segmentation
    imgNode = DiskSimulator.load_image(dicomPath, "dicom file")
    nrrdNode = slicer.util.loadSegmentation(nrrdPath)

    #creating labelmap from segmentation
    segmentationNode = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(segmentationNode)
    segmentationNode.CreateDefaultDisplayNodes()
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(imgNode)
    segmentationNode.GetSegmentation().AddSegment(nrrdNode.GetSegmentation().GetSegment("Segment_1"), "bone1")
    segmentationLblmap = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "segmentations")
    slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, segmentationLblmap,  imgNode)         
    
    #preparing to run the function ExportAllSegmentsToModels
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "E:\\segmentations\\bone1.stl")
    slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)
</code></pre>

---

## Post #6 by @cpinter (2022-03-03 09:08 UTC)

<p>This segmentation export function does not mean export to files. It means export to model nodes. After executing your code you should find the models in the folder item you created in Subject hierarchy (Data module). Then you can save the models to files from there.</p>

---
