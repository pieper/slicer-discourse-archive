---
topic_id: 13866
title: "How To Access Child Node"
date: 2020-10-05
url: https://discourse.slicer.org/t/13866
---

# How to access child node

**Topic ID**: 13866
**Date**: 2020-10-05
**URL**: https://discourse.slicer.org/t/how-to-access-child-node/13866

---

## Post #1 by @aldoSanchez (2020-10-05 14:31 UTC)

<p>how can i access child node by code.<br>
for example :<br>
the Segmentation node<br>
has child nodes:<br>
Left-Cerebral-White-Matter<br>
Left-Cerebral-Cortex<br>
…</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-10-07 11:55 UTC)

<p>Hello <a class="mention" href="/u/aldosanchez">@aldoSanchez</a></p>
<aside class="quote no-group" data-username="aldoSanchez" data-post="1" data-topic="13866" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5f9b8f/48.png" class="avatar"> aldoSanchez:</div>
<blockquote>
<p>how can i access child node by code.<br>
for example :<br>
the Segmentation node<br>
has child nodes:<br>
Left-Cerebral-White-Matter<br>
Left-Cerebral-Cortex<br>
…</p>
</blockquote>
</aside>
<p>There are python snippets that you can use to do this in the Script repository</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_subject_hierarchy_item" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_subject_hierarchy_item</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Traverse_children_of_a_subject_hierarchy_item" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Traverse_children_of_a_subject_hierarchy_item</a></p>
<p>If you need to manipulate segments in the segmentation container, you can do something like the following</p>
<pre><code> segmentNames = ["Prostate", "Urethra"]
 segmentIds = vtk.vtkStringArray()
 for segmentName in segmentNames:
     segmentId = 
        segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
        segmentIds.InsertNextValue(segmentId)
 
 slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, referenceVolumeNode)
</code></pre>
<p>-Andinet</p>

---

## Post #3 by @cpinter (2020-10-07 12:18 UTC)

<p>Please note that in the case of segmentations, the segments are not actual nodes, but part of the segmentation node. So instead of using subject hierarchy functions for getting the children, you need to access the segments within the segmentations as <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a> suggests.</p>

---

## Post #4 by @aldoSanchez (2020-10-07 14:22 UTC)

<p>what i did was to export the segmentation to modules<br>
and now I want to manipulate the colors and the visibility of the modules.</p>

---
