# Placing of models under a hiearchy

**Topic ID**: 8587
**Date**: 2019-09-27
**URL**: https://discourse.slicer.org/t/placing-of-models-under-a-hiearchy/8587

---

## Post #1 by @Amine (2019-09-27 08:52 UTC)

<p>Hi, i faced some problems while dealing with models that are under a hiearchy:</p>
<ol>
<li>How to get the absolute visibility of a model (since <code>model.GetDisplayVisibility()</code> will return 1 wether the hiearchy is set to visible or not),</li>
<li>How to get the parent hiearchy of a model node and the hiearchy’s visibility</li>
<li>How to move a model from a hiearchy to an other one<br>
Thanks for any inputs!</li>
</ol>

---

## Post #2 by @cpinter (2019-09-27 13:34 UTC)

<ol>
<li>You can get hierarchy visibility using this function: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLFolderDisplayNode.h#L90" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLFolderDisplayNode.h#L90</a>
</li>
<li>You can call GetItemParent to traverse parents, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy</a>
</li>
<li>SetItemParent, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_subject_hierarchy_item" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_subject_hierarchy_item</a>
</li>
</ol>

---

## Post #3 by @Amine (2019-09-27 22:05 UTC)

<p>Thanks a lot for your answer, all works fine,<br>
a note on a bug i found is when illogical parent changing is applied (for example here setting the child as parent of its parent) makes the current windows nightly crash instead of returning an error (even when try/except is used) :</p>
<pre><code>shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
sceneItemID = shNode.GetSceneItemID()
mainfolder_ID = shNode.CreateFolderItem(sceneItemID, "Main Folder")
subfolder_ID = shNode.CreateFolderItem(sceneItemID, "Sub Folder")
shNode.SetItemParent(subfolder_ID,mainfolder_ID) # regular hiearchy setting
try:
    shNode.SetItemParent(mainfolder_ID, subfolder_ID) ## Makes slicer crash instead of returning an error
except:
    pass</code></pre>

---

## Post #4 by @lassoan (2019-09-28 20:54 UTC)

<aside class="quote no-group" data-username="Amine" data-post="3" data-topic="8587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>when illogical parent changing is applied (for example here setting the child as parent of its parent) makes the current windows nightly crash instead of returning an error</p>
</blockquote>
</aside>
<p>Doing checks may have performance impact, so some of the missing checks may be intentional. Is there any way you could make the application crash other than setting child as parent?</p>

---

## Post #5 by @Amine (2019-09-28 23:49 UTC)

<p>No, that was the only way it happened in hierarchies,</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="8587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Doing checks may have performance impact</p>
</blockquote>
</aside>
<p>agreed but users may end up making their own checks (with more performance loss) to make the scripts safer if doing intricate re-organisations (try/except would be fine but it doesn’t prevent the crash in this case)</p>

---

## Post #6 by @lassoan (2019-10-02 00:57 UTC)

<p>OK. I’ve added a ticket to track this: <a href="https://issues.slicer.org/view.php?id=4713" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4713</a></p>

---

## Post #7 by @cpinter (2019-10-02 18:26 UTC)

<p>I <a href="https://github.com/Slicer/Slicer/commit/ff7b83fc542497092a3aa127d5e7c45c98e9208b">fixed</a> the issue. Tomorrow’s preview version should include the fix.</p>

---
