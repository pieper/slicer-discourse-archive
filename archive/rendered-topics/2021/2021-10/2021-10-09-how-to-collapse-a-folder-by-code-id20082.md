# How to collapse a folder by code?

**Topic ID**: 20082
**Date**: 2021-10-09
**URL**: https://discourse.slicer.org/t/how-to-collapse-a-folder-by-code/20082

---

## Post #1 by @apparrilla (2021-10-09 11:00 UTC)

<p>Hi everyone!!<br>
Order all new nodes maked by a process is wonderfull !!!.. Every thing in a human comprensive tree of elements… But I don´t find the way to collapse by code all made folders… Is it possible?</p>
<p>Thanks in advance!!!</p>

---

## Post #2 by @lassoan (2021-10-10 12:51 UTC)

<p>You can use <a href="http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html#aff3cba573e67923da6f60d5300263e5a">SetItemExpanded method</a> of the subject hierarchy node.</p>

---

## Post #3 by @apparrilla (2021-10-10 13:42 UTC)

<p>It also works for collapsing segmentations on Data Tree. Some code to copy/paste:</p>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

sceneItemID = shNode.GetSceneItemID()
folderID = shNode.GetItemChildWithName(sceneItemID,"folder_name")
shNode.SetItemExpanded(folderID , False)

SegmentationNode = slicer.mrmlScene.GetFirstNodeByName("segmentationNode_name")
segmentationNodeID = shNode.GetItemByDataNode(SegmentationNode)
shNode.SetItemExpanded(segmentationNodeID , False)
</code></pre>
<p>Wonderfull!</p>
<p>Thanks a lot!</p>

---

## Post #4 by @apparrilla (2021-10-17 18:43 UTC)

<p>A bit more complex but in the same line…<br>
Is it possible to reorder items position in the tree? I mean, to put simillar folders one over the other, not following the creation orden…</p>
<p>Thanks in advance!!</p>

---

## Post #5 by @lassoan (2021-10-17 20:26 UTC)

<p>You can reorder items using the <a href="http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html#a9b23e40db6c1988e8de1a033e8fcaf72">MoveItem</a> method.</p>

---

## Post #6 by @apparrilla (2021-11-03 00:23 UTC)

<p>I have some problem with MoveItem.<br>
I´ve check both itemIDs and they are right but they don´t move with the function. There is no error message either… I´ve aldo tried to invert items order, but anything happends.<br>
I don´t know what i´m doing wrong.</p>
<p>Thanks</p>

---

## Post #7 by @lassoan (2021-11-03 03:30 UTC)

<p>C++ methods cannot log error on the console, so check out the application log for errors or warnings. If there are no messages or you cannot figure out what goes wrong then share your scene (save as .mrb file, upload some, and copy the link here) and the script that does not work as you expect.</p>

---

## Post #8 by @apparrilla (2021-11-03 17:31 UTC)

<p>There is no error message in slicer log either.</p>
<p>I´ve made a simple example scene with an empty segmentation and 2 folders:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687498f15a7b446891a0a526c75262bd9c2de594.png" data-download-href="/uploads/short-url/eU3sSr3mapqZBoPcehFEEwHPL36.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/687498f15a7b446891a0a526c75262bd9c2de594_2_517x92.png" alt="image" data-base62-sha1="eU3sSr3mapqZBoPcehFEEwHPL36" width="517" height="92" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/687498f15a7b446891a0a526c75262bd9c2de594_2_517x92.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/687498f15a7b446891a0a526c75262bd9c2de594_2_775x138.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/687498f15a7b446891a0a526c75262bd9c2de594_2_1034x184.png 2x" data-dominant-color="252525"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1204×215 7.44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
sceneItemID = shNode.GetSceneItemID()
folderItemID = shNode.GetItemChildWithName(sceneItemID,'NewFolder')
otherFolderItemID = shNode.GetItemChildWithName(sceneItemID,'OtherFolder')
segmentationItemID = shNode.GetItemChildWithName(sceneItemID,'Segmentation')
</code></pre>
<p>I tried:</p>
<pre><code class="lang-auto">shNode.MoveItem(otherFolderItemID,segmentationItemID)
shNode.MoveItem(folderItemID,segmentationItemID)
</code></pre>
<p>Both send me a “True” but there is no change in Subject Hierarchy order of items…</p>
<p>I´m sure I´m doing something wrong but I can´t find it out.</p>
<p>Thanks and sorry…</p>

---

## Post #9 by @lassoan (2021-11-09 04:16 UTC)

<p>I was able to reproduce this update issue. A workaround is to force an update by temporarily switching to scene import state:</p>
<pre><code class="lang-python">slicer.mrmlScene.StartState(slicer.vtkMRMLScene.ImportState)
slicer.mrmlScene.EndState(slicer.vtkMRMLScene.ImportState)
</code></pre>
<p>I’ve filed a bug report here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6006">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6006" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6006" target="_blank" rel="noopener">SubjectHierachy MoveItem method has no visible effect</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-09" data-time="04:14:59" data-timezone="UTC">04:14AM - 09 Nov 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">vtkMRMLSubjectHierarchyNode::MoveItem method has no immediate visible effect.

<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
See more details here: https://discourse.slicer.org/t/how-to-collapse-a-folder-by-code/20082/8

## Steps to reproduce

Create scene like this:

![image](https://user-images.githubusercontent.com/307929/140860773-e960c719-4711-4e38-9efb-da151c4dd180.png)

Run this code snipped:

```python
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
sceneItemID = shNode.GetSceneItemID()
segmentationItemID = shNode.GetItemChildWithName(sceneItemID,'Segmentation')
folderItemID = shNode.GetItemChildWithName(sceneItemID,'NewFolder')
folder1ItemID = shNode.GetItemChildWithName(sceneItemID,'NewFolder_1')
shNode.MoveItem(folder1ItemID,segmentationItemID)
```

Nothing changes in the subject hierarchy tree in Data module.

## Expected behavior

NewFolder_1 should appear above Segmentation.

## Environment
- Slicer version: Slicer-4.13.0-2021-11-08
- Operating system: Windows 10

## Workaround

Force subject hierarchy tree rebuild by temporarily switching to scene import mode:

```python
slicer.mrmlScene.StartState(slicer.vtkMRMLScene.ImportState)
slicer.mrmlScene.EndState(slicer.vtkMRMLScene.ImportState)
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @apparrilla (2021-12-09 22:03 UTC)

<p>Any solution in the next future?</p>

---

## Post #11 by @Luca (2022-03-11 11:48 UTC)

<p>Hi!</p>
<p>I reached this post because I want to create a folder, put many nodes inside it, and then collapse it using a pyhton script run by prompt with --python-script.</p>
<p>I’m using the code below (from this discussion) to collapse it</p>
<aside class="quote no-group" data-username="apparrilla" data-post="3" data-topic="20082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

sceneItemID = shNode.GetSceneItemID()
folderID = shNode.GetItemChildWithName(sceneItemID,"folder_name")
shNode.SetItemExpanded(folderID , False)
</code></pre>
</blockquote>
</aside>
<p>but it doesn’t do anything. However when the script ended, if I type the same code in the python interactor it works. Could it be a problem related to the way I use the script? Otherwise, am I missing any lines?</p>
<p>Thanks in advance!!</p>

---

## Post #12 by @ebrahim (2022-03-11 14:09 UTC)

<p>Hmm maybe it will work if you connect your code to the <code>slicer.util.mainWindow().initialWindowShown</code> signal? I don’t know if the <code>--python-script</code> option already waits for this signal to execute your script. Or maybe you could connect to a <code>qt.QTimer.singleShot</code> with 0 or very small timeout in order to allow other events to process that might be expanding the folder at startup.</p>
<p>I recently ran into a situation where I wanted my script to make some changes to widgets at startup, but it had to happen after everything was sufficiently loaded that it wouldn’t revert my change. Here are the two lines that ended up working for my project:</p>
<ul>
<li><a href="https://github.com/KitwareMedical/lungair-desktop-application/blob/1cf6deb7d6cce0f63944aefdd463ea6053211428/Modules/Scripted/Home/Home.py#L138" class="inline-onebox" rel="noopener nofollow ugc">lungair-desktop-application/Home.py at 1cf6deb7d6cce0f63944aefdd463ea6053211428 · KitwareMedical/lungair-desktop-application · GitHub</a></li>
<li><a href="https://github.com/KitwareMedical/lungair-desktop-application/blob/1cf6deb7d6cce0f63944aefdd463ea6053211428/Modules/Scripted/Home/Home.py#L152" class="inline-onebox" rel="noopener nofollow ugc">lungair-desktop-application/Home.py at 1cf6deb7d6cce0f63944aefdd463ea6053211428 · KitwareMedical/lungair-desktop-application · GitHub</a></li>
</ul>

---

## Post #13 by @Arenhart (2023-01-13 19:41 UTC)

<p>I’ve been using .SetItemExpanded() and it works both in script and in the console, except for the Scene folder.<br>
I tested the following code, both in a script and directly in the Python console:</p>
<pre><code class="lang-auto">folder_tree = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
scene_id = folder_tree.GetSceneItemID()
folder_tree.SetItemExpanded(scene_id, True)
</code></pre>
<p>Runing the code,<code> folder_tree.GetItemExpanded(scene_id)</code> will return True, but no change will occur in the data widget, the Scene folder will remain collapsed. Using a children folder ID instead of scene_id will work, imediatelly expanding or collapsing the correct folder.</p>
<p>I have also tried qt.QTimer.singleShot(0, lambda : folder_tree.SetItemExpanded(scene_id, True)) following Ebrahim’s comment.</p>
<p>Is there any solution for this situation?</p>

---

## Post #14 by @cpinter (2023-01-16 10:59 UTC)

<p>The problem is that the scene does not have an item (thus it is not a folder either), so the SH model does not know about the collapsed state of the scene.</p>
<p>My only idea at the moment is trying <code>shTreeView.expandToDepth(0)</code>. Or a higher number, depending on what you want. If you need to conserve the expanded states of specific items then it may require some extra work.</p>
<p>Update: Maybe we could make <code>qMRMLSubjectHierarchyModel::subjectHierarchySceneIndex</code> callable from Python (<code>Q_INVOKABLE</code>) and call <code>shTreeView.expand(sceneItemModelIndex)</code>.</p>

---

## Post #15 by @Arenhart (2023-01-16 11:30 UTC)

<p>Unfortunatelly, we do need to conserve the expanded states. We even removed the multiple <code>shTreeView.expandToDepth(4)</code> in the code to avoid losing them. It is much better now, since after manually expanding the Scene, our folder pattern is displayed, so it is just a minor inconvenience currently, but on I believe we must fix. EDIT: I tried to programatically expand and collapsed the scene folder in the official 5.3 Slicer too, with the same results.</p>
<p>Ok, so I haven’t worked much with the Slicer source code, but what I understood is that we should include a function like QModelIndex qMRMLSortFilterSubjectHierarchyProxyModel::subjectHierarchySceneIndex()const in <code>qMRMLSubjectHierarchyModel</code> and then use it in the Python console with a new <code>shTreeView.expand(sceneItemModelIndex)</code> function.</p>
<p>I have two questions:<br>
One: Won’t the subjectHierarchySceneIndex be the same as folder_tree.GetSceneItemID()<br>
Second: shTreeView.expand(sceneItemModelIndex) should be different from SetExpanded ?</p>

---

## Post #16 by @cpinter (2023-01-17 12:48 UTC)

<aside class="quote no-group" data-username="Arenhart" data-post="15" data-topic="20082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arenhart/48/15650_2.png" class="avatar"> Arenhart:</div>
<blockquote>
<p>Won’t the subjectHierarchySceneIndex be the same as folder_tree.GetSceneItemID()</p>
</blockquote>
</aside>
<p>No. One is an SH ID, the other a Qt Model Index</p>
<aside class="quote no-group" data-username="Arenhart" data-post="15" data-topic="20082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arenhart/48/15650_2.png" class="avatar"> Arenhart:</div>
<blockquote>
<p>shTreeView.expand(sceneItemModelIndex) should be different from SetExpanded</p>
</blockquote>
</aside>
<p>These are two different things, yes. One sets it by SH ID (that the scene doesn’t have), the other by QModelIndex (that the scene has). Hence the whole thing I suggested</p>

---

## Post #17 by @Arenhart (2023-01-26 18:12 UTC)

<p>I found a workaround, if anyone else faces the same problem. Using the qMRMLSubjectHierarchyTreeView instance instead of vtkMRMLSubjectHierarchyNode to expand the folder worked, using the same scene Item ID.</p>
<p>This is the code I used:</p>
<pre><code class="lang-auto">        folder_tree = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
        scene_id = folder_tree.GetSceneItemID()
        dataWidget = slicer.modules.data.widgetRepresentation()
        shTreeView = slicer.util.findChild(dataWidget, name="SubjectHierarchyTreeView")
        shTreeView.expandItem(scene_id)
</code></pre>
<p>Can also be used to collapse the folder with shTreeView.collapseItem(scene_id)</p>

---
