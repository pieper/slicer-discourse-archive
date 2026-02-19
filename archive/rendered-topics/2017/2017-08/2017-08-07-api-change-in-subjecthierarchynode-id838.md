---
topic_id: 838
title: "Api Change In Subjecthierarchynode"
date: 2017-08-07
url: https://discourse.slicer.org/t/838
---

# API change in SubjectHierarchyNode?

**Topic ID**: 838
**Date**: 2017-08-07
**URL**: https://discourse.slicer.org/t/api-change-in-subjecthierarchynode/838

---

## Post #1 by @jonieva (2017-08-07 23:27 UTC)

<p>I’m getting an error when trying to access the HierarchyNode corresponding to the MRLMScene node.<br>
I’m doing:</p>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
</code></pre>
<p>which was working fine.</p>
<p>Was there any change in the API?</p>
<p>This is happening even in the 4.6.2 stable Release, which is weird because I tested my module long ago and it was working fine.</p>
<p>Is it possible that there is any old cached setting that can make trouble?<br>
In any case, what would be the correct way to access this node now?</p>
<p>Thank you.</p>
<p>Jorge</p>

---

## Post #2 by @lassoan (2017-08-07 23:47 UTC)

<p>SubjectHierarchy was reworked a couple of months ago to make it much more efficient (so users do not need to explicitly enable it anymore). I would suggest to use a recent nightly build.</p>
<p>If you enter this into the Python console then a folder should appear in the Subject Hierarchy tab of the Data module:</p>
<pre><code>shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
shNode.CreateFolderItem(shNode.GetSceneItemID(),"MyFirstFolder")</code></pre>

---

## Post #3 by @cpinter (2017-08-08 00:21 UTC)

<p>I did a complete overhaul of SlicerCIP to SH 2.0 right when I integrated the new SH to Slicer, see <a href="https://github.com/cpinter/SlicerCIP/commits/subject-hierarchy-20">branch</a>. This might help.</p>

---

## Post #4 by @cpinter (2017-08-08 00:23 UTC)

<p>Also <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_subject_hierarchy_item">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_subject_hierarchy_item</a></p>

---

## Post #5 by @fedorov (2017-08-08 01:46 UTC)

<aside class="quote no-group" data-username="jonieva" data-post="1" data-topic="838">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/91b2a8/48.png" class="avatar"> jonieva:</div>
<blockquote>
<p>This is happening even in the 4.6.2 stable Release</p>
</blockquote>
</aside>
<p>We ran into this issue while trying to use CIP extension in 4.6.2 stable build, which was released in Nov 2016.</p>

---

## Post #6 by @jonieva (2017-08-08 13:35 UTC)

<p>Thanks for your answers.<br>
<a class="mention" href="/u/cpinter">@cpinter</a> I’m sorry I thought that SH 2.0 had been integrated into the Slicer 4.6.2 release. Let’s hope there’s a new release soon!</p>

---

## Post #7 by @jumbojing (2021-12-15 03:55 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="838">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>branch</p>
</blockquote>
</aside>
<p>How to remove the SubjectHierarchyNode (e.g. folder)and its items?</p>

---
