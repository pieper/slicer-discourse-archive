---
topic_id: 7187
title: "Change Data Transform Hierarchy Nodes"
date: 2019-06-16
url: https://discourse.slicer.org/t/7187
---

# Change data-transform hierarchy nodes

**Topic ID**: 7187
**Date**: 2019-06-16
**URL**: https://discourse.slicer.org/t/change-data-transform-hierarchy-nodes/7187

---

## Post #1 by @zapaishchykova (2019-06-16 18:42 UTC)

<p>Hi there!<br>
I’m trying to find how can I with python change transform hierarchy of the scene, and all I was able to find is only how to change subject hierarchy:<br>
sceneItemID = shn.GetSceneItemID()<br>
shn = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)<br>
subjectItemID = shn.GetItemChildWithName(sceneItemID, ‘volume3-TrackerToProbe’)<br>
subjectItemID2 = shn.GetItemChildWithName(sceneItemID, ‘NeedleModel_1’)<br>
shn.SetItemParent(subjectItemID,subjectItemID2)</p>
<p>Can someone please guide me how to change transform hierarchy nodes? Many thanks!</p>

---

## Post #2 by @cpinter (2019-06-17 13:44 UTC)

<p>Subject hierarchy is for organizing your data, but it has no effect in terms of transforms. Here’s how you can apply the transform:</p>
<pre><code>transformNode = slicer.util.getNode(‘volume3-TrackerToProbe’)
needleModelNode = slicer.util.getNode(‘NeedleModel_1’)
needleModelNode.SetAndObserveTransformNodeID(transformNode.GetID())</code></pre>

---

## Post #3 by @zapaishchykova (2019-06-17 14:15 UTC)

<p>Thank you so much, that worked!</p>

---
