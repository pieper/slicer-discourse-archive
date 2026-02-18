# Removing folders

**Topic ID**: 30195
**Date**: 2023-06-23
**URL**: https://discourse.slicer.org/t/removing-folders/30195

---

## Post #1 by @Patrick_Li (2023-06-23 14:01 UTC)

<p>I’ve been able to remove nodes with the RemoveNode() function, but I can’t find any corresponding function for non-Node objects, such as folders. Is there a function to remove folders, or a similar method?</p>

---

## Post #2 by @rbumm (2023-06-25 10:04 UTC)

<p>It turns out that if you convert folders to “subject”</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecbf7e43c7b2021e722cc2a389ce3d5c9321fa8d.png" alt="image" data-base62-sha1="xMmXepn50pFuXy9i852R3wdG4YR" width="423" height="214"></p>
<p>you can delete them with</p>
<pre><code class="lang-auto"># Get the MRML scene
scene = slicer.mrmlScene

# Get the folder node you want to remove. Replace 'FolderName' with your folder's name.
folderNode = scene.GetFirstNodeByName('MyFolder')

# If the node exists, then remove it
if folderNode:
     scene.RemoveNode(folderNode)
else: 
     print("Folder 'MyFolder' not found")


````</code></pre>

---

## Post #3 by @rbumm (2023-06-25 10:37 UTC)

<p>The preferred way seems to be:</p>
<pre><code class="lang-auto">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "MyNewFolder")

# do something with the folder
# later ...

shNode.RemoveItem(exportFolderItemId)
</code></pre>

---
