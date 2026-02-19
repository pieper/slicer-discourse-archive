---
topic_id: 9305
title: "Recovering A Folder Item Id"
date: 2019-11-26
url: https://discourse.slicer.org/t/9305
---

# Recovering a folder item ID

**Topic ID**: 9305
**Date**: 2019-11-26
**URL**: https://discourse.slicer.org/t/recovering-a-folder-item-id/9305

---

## Post #1 by @giovform (2019-11-26 17:09 UTC)

<p>I am not being able to recover the ID of the parent directory of a node. I am using:</p>
<pre><code>subjectHierarchyNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
dirID = subjectHierarchyNode.CreateFolderItem(subjectHierarchyNode.GetSceneItemID(), 'test folder')  # this returns the value 10
</code></pre>
<p>Then I move a volume to the test folder, using the Data module, and execute:</p>
<pre><code>childID = subjectHierarchyNode.GetItemByDataNode(slicer.util.getNode('test node'))
subjectHierarchyNode.GetItemParent(subjectHierarchyNode.GetItemParent(childID))
</code></pre>
<p>But the result is 3 instead of ID 10 of the directory. What am I doing wrong? Thank you!</p>

---

## Post #2 by @lassoan (2019-11-26 18:11 UTC)

<aside class="quote no-group" data-username="giovform" data-post="1" data-topic="9305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>subjectHierarchyNode.GetItemParent(subjectHierarchyNode.GetItemParent(childID))</p>
</blockquote>
</aside>
<p>This returns parent’s parent id. If you need parent id then call <code>subjectHierarchyNode.GetItemParent(childID)</code>.</p>

---

## Post #3 by @giovform (2019-11-26 18:15 UTC)

<p>My bad, silly mistake.</p>

---
