# How to remove the SubjectHierarchyNode (e.g. folder)and its items?

**Topic ID**: 21070
**Date**: 2021-12-15
**URL**: https://discourse.slicer.org/t/how-to-remove-the-subjecthierarchynode-e-g-folder-and-its-items/21070

---

## Post #1 by @jumbojing (2021-12-15 05:58 UTC)

<h1><a name="p-71218-how-to-remove-the-subjecthierarchynode-eg-folderand-its-items-1" class="anchor" href="#p-71218-how-to-remove-the-subjecthierarchynode-eg-folderand-its-items-1" aria-label="Heading link"></a>How to remove the SubjectHierarchyNode (e.g. folder)and its items?</h1>
<p>可能是Subject Hierarchy太大了吧, 进行到一个数量就会崩掉, 所以我想分阶段, 把前面那个节段的nodes放到一个folder, 保存后删除再进行下个节段的操作, 我已经把它们装进了一个folder, 该怎么删掉这个folder呢?</p>
<blockquote>
<p>It may be that the Subject Hierarchy is too large, and it will crash when it reaches a certain large amount, so I want to put the nodes of the previous section into a folder in stages, save it and delete it before proceeding to the next section. I have  a folder including  the nodes of the previous section, how can I delete this folder and its items?</p>
</blockquote>

---

## Post #2 by @Alex_Vergara (2021-12-15 08:17 UTC)

<pre><code class="lang-auto">def deleteFolder(folderID, removeDataNode=True, recursive=True):
    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    shNode.RemoveItem(folderID, removeDataNode, recursive)
</code></pre>

---

## Post #3 by @cpinter (2021-12-15 11:22 UTC)

<p>I’d modernize the above snippet by:</p>
<p><code>shNode = slicer.mrmlScene.GetSubjectHierarchyNode()</code></p>
<p>Also I don’t really see the use of a function for this two-liner (that could be one), but it’s a matter of taste.</p>

---

## Post #4 by @jumbojing (2021-12-15 13:13 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="21070">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>shNode = slicer.mrmlScene.GetSubjectHierarchyNode()</p>
</blockquote>
</aside>
<p>*<strong>folderID</strong>? How to get it? Why don’t use folderName?</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a><br>
<a class="mention" href="/u/alex_vergara">@Alex_Vergara</a></p>

---

## Post #5 by @cpinter (2021-12-15 13:27 UTC)

<p>Learn about Subject Hierarchy here<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy</a></p>

---

## Post #6 by @jumbojing (2021-12-15 13:30 UTC)

<pre><code class="lang-auto">def deleteFolder(folderName, removeDataNode=True, recursive=True):
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    sceneItemID = shNode.GetSceneItemID()
    folderID = shNode.GetItemChildWithName(sceneItemID,folderName)
    shNode.RemoveItem(folderID, removeDataNode, recursive)
</code></pre>
<p>This is my code…</p>

---

## Post #7 by @jumbojing (2021-12-15 13:36 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="21070">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><strong>two-line</strong></p>
</blockquote>
</aside>
<p><strong>tow-line</strong>?what’s mean?</p>

---

## Post #8 by @jumbojing (2021-12-15 14:01 UTC)

<pre><code class="lang-auto">NNs=[]
nodes = slicer.util.getNodes("*")
for key in nodes.keys():
  if key != "12: Unnamed Series":
    modNode = slicer.util.getNode(key)
    if isinstance(modNode, slicer.vtkMRMLTransformableNode):
      NNs.append(modNode)
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
newParentFolderItem = shNode.CreateFolderItem(shNode.GetSceneItemID(), "folder")
for node in NNs:
  nodeItem = shNode.GetItemByDataNode(node)
  shNode.SetItemParent(nodeItem, newParentFolderItem)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14426bfab6793bf5a43874d29c5c80b3c681da4e.png" data-download-href="/uploads/short-url/2TdRa1CZSdgPtSDUra6g0xYSlkO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14426bfab6793bf5a43874d29c5c80b3c681da4e_2_495x500.png" alt="image" data-base62-sha1="2TdRa1CZSdgPtSDUra6g0xYSlkO" width="495" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14426bfab6793bf5a43874d29c5c80b3c681da4e_2_495x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14426bfab6793bf5a43874d29c5c80b3c681da4e_2_742x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14426bfab6793bf5a43874d29c5c80b3c681da4e_2_990x1000.png 2x" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×1000 71.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>这貌似是另一个问题, 如图和code, 有一些重名的nodes没包括到folder里面,怎么整呀?<a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<blockquote>
<p>This seems to be another problem. As shown in the figure and code, some nodes with the same name are not included in the folder. How to fix it?<br>
<a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>@cpinter@Alex_Vergara</p>
</blockquote>

---
