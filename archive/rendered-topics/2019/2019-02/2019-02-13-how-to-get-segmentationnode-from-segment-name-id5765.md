---
topic_id: 5765
title: "How To Get Segmentationnode From Segment Name"
date: 2019-02-13
url: https://discourse.slicer.org/t/5765
---

# How to get segmentationNode from segment name

**Topic ID**: 5765
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/how-to-get-segmentationnode-from-segment-name/5765

---

## Post #1 by @angkr (2019-02-13 19:44 UTC)

<p>I was wondering how to get the segmentationNode from segment name.</p>
<p>With version 4.5.0, I was using the subject hierarchy function:<br>
modelLogic = slicer.vtkSlicerSegmentationsModuleLogic()<br>
segmentSH = slicer.util.getNode(segmentName)<br>
segmentationNode=modelLogic.GetSegmentationNodeForSegmentSubjectHierarchyNode(segmentSH)</p>
<p>But with version 4.10.1, subject hierarchy doesn’t seem to exist anymore?</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2019-02-13 20:28 UTC)

<p>Subject hierarchy has been completely reimplemented since that version. This specific operation is not obvious in the new system, but here is how you can do it:</p>
<pre><code>itemName = 'What you are looking for'
shn = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
sc = shn.GetSceneItemID()
items = vtk.vtkIdList()
shn.GetItemChildren(sc, items, True)
for i in xrange(items.GetNumberOfIds()):
  name = shn.GetItemName(items.GetId(i))
  if name == itemName:
    foundItem = items.GetId(i)
    break
parentItem = shn.GetItemParent(foundItem)
parentNode = shn.GetItemDataNode(parentItem)</code></pre>

---

## Post #3 by @angkr (2019-02-13 22:10 UTC)

<p>Thanks!</p>
<p>But it doesn’t seem to work for if there is more than one segmentation.</p>
<p>What I want to do is : from segments (DICOM RTstruct), with the slicerRT extension, I do bool. operation  -intersection/expansion - of segments in new segmentation and I want to get the segmentation node for all the segments (original and newly created in new segmentation) based on their segment name.</p>
<p>For example:<br>
‘structure1’ -&gt; vtkMRMLSegmentationNode1<br>
‘Expanded_5_5_5_structure1’  -&gt; vtkMRMLSegmentationNode2</p>
<p>Hope it’s clear &amp; possible !</p>

---

## Post #4 by @cpinter (2019-02-13 22:24 UTC)

<p>The script works for any scene content as long as <code>itemName</code> is unique, or the first result is a segment.</p>

---
