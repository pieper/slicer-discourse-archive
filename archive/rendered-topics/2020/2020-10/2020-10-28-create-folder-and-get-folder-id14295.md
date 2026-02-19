---
topic_id: 14295
title: "Create Folder And Get Folder"
date: 2020-10-28
url: https://discourse.slicer.org/t/14295
---

# Create Folder and Get Folder

**Topic ID**: 14295
**Date**: 2020-10-28
**URL**: https://discourse.slicer.org/t/create-folder-and-get-folder/14295

---

## Post #1 by @Christos_Tzerefos (2020-10-28 23:45 UTC)

<p>Hello to all,</p>
<p>during a part of my code, I create a folder with the following code to export a certain model I create.</p>
<blockquote>
<p>shNode = slicer.mrmlScene.GetSubjectHierarchyNode()<br>
sceneItemID = shNode.GetSceneItemID()<br>
exportFolderItemId = shNode.<strong>CreateFolderItem(sceneItemID , “Models”)</strong></p>
</blockquote>
<p>How can I check if this certain folder exists later in my code and use it to export another model?</p>

---

## Post #2 by @lassoan (2020-10-28 23:50 UTC)

<p>You can find many subject hierarchy <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy">examples in the script repository</a> and full documentation <a href="http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html">here</a>.</p>

---
