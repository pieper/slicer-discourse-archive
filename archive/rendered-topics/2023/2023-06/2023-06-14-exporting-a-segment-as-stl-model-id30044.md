---
topic_id: 30044
title: "Exporting A Segment As Stl Model"
date: 2023-06-14
url: https://discourse.slicer.org/t/30044
---

# Exporting a segment as .stl model

**Topic ID**: 30044
**Date**: 2023-06-14
**URL**: https://discourse.slicer.org/t/exporting-a-segment-as-stl-model/30044

---

## Post #1 by @S_Arbabi (2023-06-14 21:30 UTC)

<p>I would like to export a segment of a segmentation node to a .stl 3d model file.<br>
I’m wondering how can I do it in python? I could create the volume like this, but then in saving it didn’t work the way I expected.</p>
<p>segmentationNode = getNode(“segmentationNode”)<br>
<span class="hashtag-raw">#I</span>’m not sure if I can also get a specific segment (and not the whole segmentation node) only for exporting as model?<br>
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()<br>
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), “Segments”)<br>
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)</p>
<p>but then how can I save the model? I tried:<br>
slicer.util.saveNode(slicer.util.getNode(“Segments”), r"./seg.stl")<br>
<span class="hashtag-raw">#with</span> error: “slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘Segments’”</p>
<p>thanks in advance</p>

---

## Post #2 by @lassoan (2023-06-16 14:16 UTC)

<p>This topic should help:</p>
<aside class="quote" data-post="2" data-topic="25111">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/export-volume-or-segment-to-stl-file-with-python/25111/2">Export volume (or segment?) to stl file with python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi, segmentation nodes cannot be saved as STL directly. You need to first export the segmentation to model node: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-nodes-from-segmentation-node" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> 
Then, model nodes can be saved as STL files.
  </blockquote>
</aside>


---

## Post #3 by @S_Arbabi (2023-06-16 20:28 UTC)

<p>Thanks. Also a very good code example:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://python.hotexamples.com/examples/vtk/-/vtkStringArray/python-vtkstringarray-function-examples.html">
  <header class="source">
      <img src="https://python.hotexamples.com/images/python/favicon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://python.hotexamples.com/examples/vtk/-/vtkStringArray/python-vtkstringarray-function-examples.html" target="_blank" rel="noopener nofollow ugc">python.hotexamples.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://python.hotexamples.com/examples/vtk/-/vtkStringArray/python-vtkstringarray-function-examples.html" target="_blank" rel="noopener nofollow ugc">Python vtkStringArray Examples, vtk.vtkStringArray Python Examples - HotExamples</a></h3>

  <p>Python vtkStringArray - 60 examples found. These are the top rated real world Python examples of vtk.vtkStringArray extracted from open source projects. You can rate examples to help us improve the quality of examples.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
