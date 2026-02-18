# How to add folder in scene?

**Topic ID**: 29499
**Date**: 2023-05-17
**URL**: https://discourse.slicer.org/t/how-to-add-folder-in-scene/29499

---

## Post #1 by @dsa934 (2023-05-17 02:09 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/460e27508a41c729774dc75f727730127a628515.png" data-download-href="/uploads/short-url/9ZJKiMnbf2cJTXtgJRJkRckiytn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/460e27508a41c729774dc75f727730127a628515_2_690x293.png" alt="image" data-base62-sha1="9ZJKiMnbf2cJTXtgJRJkRckiytn" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/460e27508a41c729774dc75f727730127a628515_2_690x293.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/460e27508a41c729774dc75f727730127a628515_2_1035x439.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/460e27508a41c729774dc75f727730127a628515.png 2x" data-dominant-color="C3C6E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1089×463 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>how can i do this in python code ?</p>
<p>I want to know how to add a folder in the scene and add data to that folder.</p>
<p>Or can I add a folder that I already have locally to the slicer and set the contents of that folder to be added at the same time?</p>

---

## Post #2 by @muratmaga (2023-05-17 02:16 UTC)

<p>Right click in the data module and choose “Create folder” from the popup menu. Then you can drag any object loaded into the scene to this folder.</p>

---

## Post #3 by @dsa934 (2023-05-17 02:20 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="1" data-topic="29499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>how can i do this <strong>in python code ?</strong></p>
</blockquote>
</aside>
<p>There are two things I want to know.</p>
<ol>
<li>
<p>How to add a folder to a scene</p>
</li>
<li>
<p>How to make it belong to the folder added when loading data to 3D slicer</p>
</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21dcd6d26c516e5372ea79dccf21571da977b63d.png" alt="image" data-base62-sha1="4PyTW7Nino86ESffDiZMkQKiHjD" width="576" height="193"></p>
<p>I would like to know the code to create a folderdisplaynode and put mesh data into subcategories of that folder.</p>

---

## Post #4 by @muratmaga (2023-05-17 03:32 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide" class="inline-onebox">Developer Guide — 3D Slicer documentation</a> subject hierarchy section/script_repository.html#subject-hierarchy</p>

---

## Post #5 by @dsa934 (2023-05-17 04:24 UTC)

<pre><code class="lang-auto">(ref : vtkMRMLSubjectHierarchyNode Class Reference )

shNode = slicer.modules.subjecthierarchy.logic().GetSubjectHierarchyNode()

# folder create
folderNum = shNode.CreateFolderItem(3, "test")

temp = getNode('F')

shNode.CreateItem(folderNum, temp)
</code></pre>
<p>a -ha it’s simple , thx</p>

---

## Post #6 by @dsa934 (2023-05-17 07:51 UTC)

<pre><code class="lang-auto">shNode = slicer.modules.subjecthierarchy.logic().GetSubjectHierarchyNode()

# get current SceneID
SceneID = shNode.GetSceneItemID()

# folder create
folderNum = shNode.CreateFolderItem(SceneID, "test")

# dummy item
temp = getNode('F')

# add item to folder
shNode.CreateItem(folderNum, temp)
</code></pre>
<p>However, when I run the code that adds data to the folder like this, there is a phenomenon that the slicer turns off when there is a lot of data. Is there an optimization method?</p>

---

## Post #7 by @cpinter (2023-05-17 09:24 UTC)

<p>Your code seems to work. A few comments:</p>
<p><code>CreateItem</code> is not intended to use in this way, so there may be side-effects, not sure. Try <code>shNode.SetItemParent</code> instead.</p>
<p>FYI there is a simpler way to get the SH node:<br>
<code>shNode = slicer.mrmlScene.GetSubjectHierarchyNode()</code></p>
<aside class="quote no-group" data-username="dsa934" data-post="6" data-topic="29499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>However, when I run the code that adds data to the folder like this, there is a phenomenon that the slicer turns off when there is a lot of data. Is there an optimization method?</p>
</blockquote>
</aside>
<p>I don’t understand this. Please elaborate.</p>

---

## Post #8 by @dsa934 (2023-05-18 01:36 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a></p>
<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="29499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I don’t understand this. Please elaborate.</p>
</blockquote>
</aside>
<p>The code I want to implement is:</p>
<ol>
<li>
<p>Load all markups (fiducialNode, ClosedcurvedNode, etc) used in slicer.</p>
</li>
<li>
<p>Create a folder corresponding to each markups</p>
</li>
<li>
<p>Distribute markups data corresponding to each folder.</p>
</li>
</ol>
<pre><code class="lang-auto">#example tree
Scene
| 
|
| ㅡㅡㅡ FiducialNode(tentative named)
|        |___ node1
|        |___ node2
|
|
| ㅡㅡㅡ  ClosedCurvedNode
|
|
|ㅡㅡ etc

# Get hierarychyNode
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()

# Get Current SceneID
SceneID = shNode.GetSceneItemID()

# Create folder
folderNum = shNode.CreateFolderItem(SceneID, "test")

# Set dummy data
temp = getNode('F')

# add item to folder
shNode.CreateItem(folderNum, temp)

</code></pre>
<p>However, in the case of proceeding as above, if there is a lot of data to put in the folder, the slicer is turned off.</p>
<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="29499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><code>CreateItem</code> is not intended to use in this way, so there may be side-effects, not sure. Try <code>shNode.SetItemParent</code> instead.</p>
</blockquote>
</aside>
<p>I will refer to this method and try it.</p>
<p>edit :</p>
<pre><code class="lang-auto"># Get hierarychyNode
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()

# Get Current SceneID
SceneID = shNode.GetSceneItemID()

# Create folder
folderNum = shNode.CreateFolderItem(SceneID, "test")

# Set dummy data
temp = getNode('F')

# Get the item ID of the node
nodeItemID = shNode.GetItemByDataNode(node)

# Set the parent of the node item to the folder item
shNode.SetItemParent(nodeItemID, folderItemID)
</code></pre>
<p>I understand what you mean.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/341d326b5d0954365b0e5c9a4dc712a60e22c05e.png" alt="image" data-base62-sha1="7r1nISfSUxQoCZUGeUFgkJpVyb4" width="562" height="116"></p>
<p>Last question. What is this problem caused by?</p>

---

## Post #9 by @cpinter (2023-05-22 08:29 UTC)

<blockquote>
<ol start="3">
<li>Distribute markups data corresponding to each folder.</li>
</ol>
</blockquote>
<p>Having data nodes under other nodes is possible in SH, but it is not something I’d consider default behavior. If you only have folders as parents of nodes, does it work?</p>
<aside class="quote no-group" data-username="dsa934" data-post="8" data-topic="29499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>if there is a lot of data to put in the folder, the slicer is turned off.</p>
</blockquote>
</aside>
<p>I assume this means it crashes. If you can reproduce this with only using sample or synthetic data, please upload a scene and/or provide instructions and we’ll try to fix the crash.</p>
<aside class="quote no-group" data-username="dsa934" data-post="8" data-topic="29499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Last question. What is this problem caused by?</p>
</blockquote>
</aside>
<p>Unfortunately subject hierarchy is still not bullet-proof. Sticking to the “normal” behavior it tends to work fine, but some errors do pop up. If you have cases that are not that normal (see above), probably mode. This particular warning does not indicate serious issues. If you know how to debug in C++, it would be great if you could find the cause for these.</p>

---

## Post #10 by @cpinter (2023-05-22 09:31 UTC)

<p><a class="mention" href="/u/dsa934">@dsa934</a> I’m glad the last comment was helpful enough to set it as solution, but maybe it would help others seeing this topic later if you told us what exactly helped. Was it using folder items? Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #11 by @dsa934 (2023-05-22 10:26 UTC)

<p>I mischecked the solution checkbox.</p>
<p>I understood that slicer creates a tree structure automatically when you designate a parent as a viewnode after creating some data.</p>

---

## Post #12 by @cpinter (2023-05-22 10:41 UTC)

<p>It’s better to use folders (or patient and study items which behave similarly) when you need a hierarchy.</p>

---

## Post #14 by @Victor_Wayne (2025-08-07 10:10 UTC)

<p>How to hide folders from the Data module subject Hierarchy? not to remove them, hide them.</p>

---

## Post #15 by @cpinter (2025-08-07 10:41 UTC)

<p>The folders have a special folder display node, but it is only created when you show/hide it in the Data module (you’ll notice because the color item will appear in its row). In theory you can create it programmatically, but as I see that function is not python wrapped. This is the code:</p>
<pre><code class="lang-auto">pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
folderPlugin = pluginHandlerSingleton.pluginByName('Folder')
folderPlugin.createDisplayNodeForItem(folderItemID)
</code></pre>
<p>If you need to create the display node programmatically, there are two ways:</p>
<ol>
<li>Do in Python what this <code>createDisplayNodeForItem</code> function does</li>
<li>Fix Python wrapping of the function</li>
</ol>

---

## Post #16 by @Victor_Wayne (2025-08-07 11:59 UTC)

<p>I have to admit that I don’t quite get what you are saying.</p>
<p>Here’s what I want to do.</p>
<p>I inspected the Data module and found out that it is using qMRMLSubjectHierarchyTreeView widget for showing the nodes in a tree view. I wanted to customize the Data module by creating my own custom widget. So I created a widget, with a combo box that selects from the list plans. The plans contains lines. I want to show the lines like a list and with all the added functionality of hide/show `eye` button, transformation tracking, color picking, and their IDs like how the Data module shows it. So I created one instance of qMRMLSubjectHierarchyTreeView, and set it like this.</p>
<pre data-code-wrap="python"><code class="lang-python">self.lineDetailView = qMRMLSubjectHierarchyTreeView()
self.lineDetailView.setMRMLScene(slicer.mrmlScene)
</code></pre>
<p>The problem is that it shows all the nodes and folders. I just want to show the line that corresponds to the selected plan. I thought I could do the following</p>
<pre data-code-wrap="python"><code class="lang-python">self.lineDetailView.nodeTypes = ['vtkMRMLMarkupsLineNode']
</code></pre>
<p>but this shows the folders with the lines. even if it didn’t show the folders, I don’t know how to delete the other line nodes that doesn’t belong to the current selected plan.</p>
<p>Any help will be appreciated. Thank you for replying to me.</p>

---

## Post #17 by @cpinter (2025-08-07 12:26 UTC)

<p>OK, it turns out you want to hide them from the tree view, and not their contents from the views. This is why explaining a problem in more than a single line helps preventing misunderstandings <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I thought this was a very simple question related to the original topic, but it’s quite different. Please open a new topic with your question if you cannot find the solution among the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L87-L106">filtering options of the tree view</a>, which is quite comprehensive.</p>

---
