---
topic_id: 35355
title: "Automatize Model Generation From Segmentation"
date: 2024-04-08
url: https://discourse.slicer.org/t/35355
---

# Automatize model generation from segmentation

**Topic ID**: 35355
**Date**: 2024-04-08
**URL**: https://discourse.slicer.org/t/automatize-model-generation-from-segmentation/35355

---

## Post #1 by @MrMarkus (2024-04-08 15:33 UTC)

<p>Hi,</p>
<p>I would like to automatically generate 3D-models from segmented 3D-data. The<br>
segmented data is stored as *.nrrd, and the segmentation was performed with<br>
an external program.</p>
<p>The idea is to store the segmented data in a folder and use “slicerpipelines” to<br>
automatize the task. But I am not exactly sure how to set up the pipeline.</p>
<p>The following steps need to be covered:</p>
<ul>
<li>load the data as “segmentation”</li>
<li>select only segment1 and segment2</li>
<li>keep largest element of segment1, keep largest element of segment2</li>
<li>generate model of segment1 and of segment2</li>
<li>store model_segment1 and model_segment2 → file names should be derived from<br>
the loaded segmentation-data</li>
</ul>
<p>Any hint / tutorial how to set-up the “SlicerPipeline” for this workflow?</p>
<p>Thanks!</p>
<p>Any help is greatly appreciated!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2024-04-08 18:02 UTC)

<p>I am not sure if all of this is possible through SlicerPipelines, but it is definitely possible via python scripting. See the script repository, specifically segmentations section for examples.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations</a></p>

---

## Post #3 by @MrMarkus (2024-04-09 11:16 UTC)

<p>Thanks for the hint!</p>
<p>Looks promising.</p>
<p>Best,<br>
Markus</p>

---

## Post #4 by @Matteboo (2024-04-09 11:33 UTC)

<p>There’s a functiun that should be very useful for you in the  <a href="https://github.com/naterex23/SlicerAblationPlanner/blob/main/AblationPlanner/AblationPlanner.py" rel="noopener nofollow ugc">ablation planner module</a> line 793</p>
<pre><code class="lang-auto">convertSegmentToModel(segmentNode, folderName="Folder")
</code></pre>

---

## Post #5 by @MrMarkus (2024-04-24 07:48 UTC)

<p>Hi,</p>
<p>once again thanks for the link.</p>
<p>I tried to find &amp; use the code snippets which looked promising to me.<br>
And it worked out, starting from the segmentation models were generated and<br>
also filtered using the “Islands” - Operation.</p>
<p>An nice example of how to apply the filter-effects is given here:</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d">
  <header class="source">

      <a href="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d</a></h4>

  <h5>FillHolesInSegments.py</h5>
  <pre><code class="Python">segmentationNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
# set value to the size of the larges cracks in the segment surfaces
maximumHoleSizeMm = 2.0

############
masterVolumeNode = segmentationNode.GetNodeReference(segmentationNode.GetReferenceImageGeometryReferenceRole())

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging):</code></pre>
   This file has been truncated. <a href="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>BUT. While testing I found out that the model generation /  exporting is<br>
introducing a “transformation” / or change of the coordinate system.</p>
<p> → in comparison to the position of the segmentation is the position of the<br>
model now changed.</p>
<p>Any idea how this is caused and how it could be solved?</p>
<p>I am using:</p>
<p>Export model to Blender, including color by scalar</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-to-blender-including-color-by-scalar" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-to-blender-including-color-by-scalar</a></p>
<p>Maybe there is a better way how to export “Segment” → “Model” ?</p>
<p>Thanks!<br>
Best,<br>
Markus</p>

---

## Post #6 by @MrMarkus (2024-04-29 16:20 UTC)

<p>Hi again,</p>
<p>meanwhile I discoverd similar topics, e.g.</p>
<aside class="quote quote-modified" data-post="1" data-topic="25111">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mike_flanigan/48/14586_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/export-volume-or-segment-to-stl-file-with-python/25111">Export volume (or segment?) to stl file with python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi there, 
Currently I’ve been working on automating a work flow in python that goes like the following: 

Load CT scans (as .tiffs)
Create a segmentation and threshold to identify air in the scans
Automate a mouse click in a known location and use the “Remove selected island” feature
Apply the “Keep largest island” feature
Calculate and report statistics

I’d like to add a 6th step that saves the final resulting volume as an STL file so users could easily open up a visual artifact at a later da…
  </blockquote>
</aside>

<p>and an example how to export the Model to disk:</p>
<p><a href="https://github.com/SlicerMorph/Scripts#2-run-an-image-processing-pipeline-on-a-folder-of-volumes" rel="noopener nofollow ugc">https://github.com/SlicerMorph/Scripts#2-run-an-image-processing-pipeline-on-a-folder-of-volumes</a></p>
<p>One question remains on how is the order in setting up the segmentEditorWidget.<br>
Not sure if the code is “fine” like it is applied, because after all files in the folder<br>
are processed the “KEEP_LARGEST_ISLAND” filter is still “active” → the mouse pointer has this typical “icon”…</p>
<pre><code class="lang-auto"># Load CurrentSegmentation
    CurrentSegmentation = os.path.join(ProjectFolder, FilesInFolder[sampleIndex])
    slicer.util.loadSegmentation(CurrentSegmentation)
    segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
    
    sampleID = segmentationNode.GetName()
    
    # storage of the segment volume 
    volumeSegment[sampleIndex][0] = sampleID 
    
    # masterVolume for segmentation
    masterVolumeNode = segmentationNode.GetNodeReference(segmentationNode.GetReferenceImageGeometryReferenceRole())
    
    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    
    # To show segment editor widget (useful for debugging):
    # segmentEditorWidget.show()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
    slicer.mrmlScene.AddNode(segmentEditorNode)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    
    # actual segmentation
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(masterVolumeNode)
    
    # Visible segments will be processed
    inputSegmentIDs = vtk.vtkStringArray()
    segmentationNode.GetDisplayNode().GetVisibleSegmentIDs(inputSegmentIDs)
    
    segmentationNode.GetDisplayNode().SetSegmentVisibility(inputSegmentIDs.GetValue(2), False)
    
    # apply filter: Keep_Largest_Island / get rid of "particles"
    for index in range(inputSegmentIDs.GetNumberOfValues()-1):
        segmentID = inputSegmentIDs.GetValue(index)
        segmentEditorWidget.setCurrentSegmentID(segmentID)
        
        # Remove islands in inverted segment (these are the holes inside the segment)
        segmentEditorWidget.setActiveEffectByName("Islands")
        effect = segmentEditorWidget.activeEffect()
        effect.setParameter("Operation", "KEEP_LARGEST_ISLAND")
        effect.self().onApply()

    # prepare: Export segment -&gt; to model
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), sampleID)
    slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)
itemList=[]
    shNode.GetItemChildren(exportFolderItemId,itemList)
    if itemList is []:
      print("Error: no model node exported for ", volumeNode.GetName())
      continue
    
    # export skull = Segment_1
    modelNode = shNode.GetItemDataNode(itemList[0])
    # Decimate the model 80%
    slicer.modules.SurfaceToolboxWidget.logic.decimate(modelNode, modelNode, 0.8)
    slicer.util.saveNode(modelNode, plyFilePathSkull)

  # Delete temporary segment editor
    slicer.mrmlScene.RemoveNode(segmentEditorNode)
    del segmentEditorWidget

  slicer.mrmlScene.Clear(0)  # EMPTY scene
</code></pre>
<p>Maybe one could comment on the lines above.</p>
<p>THANKS!</p>
<p>Best,<br>
Markus</p>

---
