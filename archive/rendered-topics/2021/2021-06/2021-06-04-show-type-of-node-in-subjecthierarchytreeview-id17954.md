# Show type of Node in SubjectHierarchyTreeView

**Topic ID**: 17954
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/show-type-of-node-in-subjecthierarchytreeview/17954

---

## Post #1 by @ond12 (2021-06-04 15:24 UTC)

<p>Hello,<br>
I Would like to show only ““vtkMRMLMarkupsFiducialNode”” in my SubjectHierarchyTreeView widget.<br>
I manage to hide the majority of node types thanks to this snipet <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<pre><code class="lang-auto">self.shFiducialTreeView = slicer.qMRMLSubjectHierarchyTreeView()
self.shFiducialTreeView.nodeTypes = ["vtkMRMLMarkupsFiducialNode"]
self.shFiducialTreeView.setShowRootItem(False)
self.shFiducialTreeView.setMRMLScene(slicer.mrmlScene)
</code></pre>
<p>But as you can some folder Nodes are still showing :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a185af9cbff9e3294ae4a421745380834ef7bb3f.png" alt="image" data-base62-sha1="n2TicLVe0parfSC4S1S6YgboI2z" width="627" height="349"></p>
<p>Do you have a solution for this issue ? what am i doing wrong ?</p>
<p>Thanks a lot</p>

---

## Post #2 by @lassoan (2021-06-04 23:21 UTC)

<p>Folders are shown by default (even if they are empty), because otherwise you could not create new folders and drag-and-drop nodes into them. In recent Slicer Preview Releases you can control visibility of empty folders.</p>

---

## Post #3 by @cpinter (2021-06-07 10:15 UTC)

<p>For that you need to do the following:</p>
<pre><code class="lang-auto">proxyModel = self.shFiducialTreeView.sortFilterProxyModel()
proxyModel.showEmptyHierarchyItems = False
</code></pre>

---

## Post #4 by @ond12 (2021-06-08 07:37 UTC)

<p>Hello  tanks for this python code</p>
<p>unfortunatly i have an error<br>
<code>AttributeError: 'showEmptyHierarchyItems' does not exist on qMRMLSortFilterSubjectHierarchyProxyModel and creating new attributes on C++ objects is not allowed</code></p>
<p>My version is 4.11 what should i do ?</p>

---

## Post #5 by @cpinter (2021-06-08 12:23 UTC)

<aside class="quote no-group" data-username="ond12" data-post="4" data-topic="17954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ond12/48/8706_2.png" class="avatar"> ond12:</div>
<blockquote>
<p>what should i do ?</p>
</blockquote>
</aside>
<p>Install the latest preview version.</p>

---
