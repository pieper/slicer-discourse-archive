---
topic_id: 42603
title: "How To Add Shortcut To Delete Item In Subject Hierarchy"
date: 2025-04-17
url: https://discourse.slicer.org/t/42603
---

# How to add shortcut to delete item in subject hierarchy

**Topic ID**: 42603
**Date**: 2025-04-17
**URL**: https://discourse.slicer.org/t/how-to-add-shortcut-to-delete-item-in-subject-hierarchy/42603

---

## Post #1 by @josephtandio27 (2025-04-17 12:03 UTC)

<p>Hi, may I know how to add shortcut to delete highlighted item in subject hierarchy? Right now, I can only delete it by selecting the item, and then right-click delete.</p>

---

## Post #2 by @cpinter (2025-04-22 10:13 UTC)

<p>I think you’ll need to add a keyboard shortcut to the <code>DeleteAction</code> in <code>qMRMLSubjectHierarchyTreeView</code>.</p>

---

## Post #3 by @josephtandio27 (2025-04-22 10:39 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="42603">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>qMRMLSubjectHierarchyTreeView</p>
</blockquote>
</aside>
<p>Thanks. The code below works when I press ‘Del’ in the ‘Data’ modules.</p>
<pre><code class="lang-auto">def deleteSelectedSubjectHierarchyItem():
    dataWidget = slicer.modules.data.widgetRepresentation()
    shTreeView = slicer.util.findChild(dataWidget, name='SubjectHierarchyTreeView')
    shTreeView.deleteSelectedItems()

# Set up the shortcut
shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence("Del"))
shortcut.connect('activated()', deleteSelectedSubjectHierarchyItem)
</code></pre>

---

## Post #4 by @cpinter (2025-04-22 10:42 UTC)

<p>What may be problematic is that you added the shortcut on the main window, so even if you don’t see the SH tree but press the button, the node will be deleted, and you’ll have no idea. I’d try to put it in the Slicer code itself, in the tree view class. It is a very small change, could you give it a try?</p>

---

## Post #5 by @josephtandio27 (2025-04-22 11:59 UTC)

<p>Do you mean to write these code to the c++ ( <a href="https://github.com/Slicer/Slicer" rel="noopener nofollow ugc">Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>)? I am a beginner in 3D Slicer, so I do not know how to do it. May I ask for more details on how to implement this?</p>

---

## Post #6 by @cpinter (2025-04-22 12:59 UTC)

<p>It is not much more code than what you wrote, just add the shortcut for the tree view itself (<code>this</code>).</p>
<p>Update: here is the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html">contribution guide</a>. If you want your name to appear among the Slicer developers and you have some time and motivation, this could be a great exercise <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @matt1 (2026-01-01 19:50 UTC)

<p>Hi, any chance that his could become part of the standard 3D slicer, implemented in a stable way? This is a feature I have really been missing over the years using 3D slicer, so making it default would be a great upgrade.</p>
<p>It’s really cool that you can customize 3D slicer this much, but this seems like something everyone would want to have, and maybe having everyone spent time understanding how to integrate code into 3D slicer, maybe this would be a nice update to have by default.</p>

---
