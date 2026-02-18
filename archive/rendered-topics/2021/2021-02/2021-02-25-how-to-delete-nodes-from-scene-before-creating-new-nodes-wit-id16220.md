# How to delete nodes from scene before creating new nodes with the same name?

**Topic ID**: 16220
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/how-to-delete-nodes-from-scene-before-creating-new-nodes-with-the-same-name/16220

---

## Post #1 by @akshay_pillai (2021-02-25 18:31 UTC)

<p>Operating system:Windows 11<br>
Slicer version:4.11.20200930</p>
<p>How do I remove some specific nodes with a specific name before creating new nodes of the same type? For example: if I have a node in my scene that starts with “XYZ…” then how do I programmatically remove this pre-existing node starting with XYZ . I’m trying to do this in python.</p>

---

## Post #2 by @Alex_Vergara (2021-02-25 18:37 UTC)

<p>I have lots of examples in my code on how to achieve this. Just watch <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/Dosimetry4D/Logic/Dosimetry4DLogic.py#L465" class="inline-onebox" rel="noopener nofollow ugc">Dosimetry4D/Logic/Dosimetry4DLogic.py · develop · OpenDose / SlicerOpenDose3D · GitLab</a></p>

---

## Post #3 by @lassoan (2021-02-25 18:39 UTC)

<p>In general, you should not rely on node <em>name</em> to identify nodes, because node name is not guaranteed to be unique. You can use node ID instead, which is unique. You can also specify a node to be singleton, so that when you add a new instance of that node then it overwrites the previous instance in the scene instead of adding a new one. If you describe your workflow then we can recommend suitable approaches.</p>

---

## Post #4 by @akshay_pillai (2021-02-25 19:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="16220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ibe your workflow then we c</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> i’m just trying to edit the endoscopy module so when I click create path button I only have the current paths and the previous ones get removed.</p>

---

## Post #5 by @akshay_pillai (2021-02-25 19:11 UTC)

<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> Thanks, I’ll take a look at this.</p>

---

## Post #6 by @lassoan (2021-02-25 19:11 UTC)

<p>This is fixed in recent Slicer Preview Releases. Endoscopy module no longer creates new node each time you create a path, but it updates the node that is selected as “Output path”.</p>

---

## Post #7 by @akshay_pillai (2021-02-25 19:13 UTC)

<p>ok, I’ll check that out.</p>

---
