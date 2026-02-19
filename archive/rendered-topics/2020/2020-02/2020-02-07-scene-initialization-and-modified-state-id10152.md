---
topic_id: 10152
title: "Scene Initialization And Modified State"
date: 2020-02-07
url: https://discourse.slicer.org/t/10152
---

# Scene initialization and modified state

**Topic ID**: 10152
**Date**: 2020-02-07
**URL**: https://discourse.slicer.org/t/scene-initialization-and-modified-state/10152

---

## Post #1 by @rprueckl (2020-02-07 07:12 UTC)

<p>In my application, at startup or after a scene change, I do some initialization tasks for some of my modules. After this is finished, the scene of course is always marked as modified and when I try to close the application, it asks me whether I want to save the scene. For the user, however, the scene is empty and untouched. Is there a way to reset the modified state of all the nodes in the scene (including storage nodes) without actually saving the scene?</p>

---

## Post #2 by @timeanddoctor (2020-02-07 09:34 UTC)

<p>You can close the scence(shortcut:ctrl+w) in the “file” of the manu but not close the slicer app .</p>

---

## Post #3 by @lassoan (2020-02-07 14:10 UTC)

<p>You can iterate through all storage nodes and call <code>storageNode.GetStoredTime().Modified()</code> to indicate that changes has been already stored, so there is no need to save the node. I don’t think <code>StoredTime</code> attribute of <code>vtkMRMLScene</code> is exposed publicly, so you may need to call <code>Commit</code> method to write the scene to some dummy file (if it does not work then we can add a method to allow marking the scene object as “stored”).</p>

---

## Post #4 by @rprueckl (2020-02-07 21:50 UTC)

<p>Thanks for the hint. I managed to achieve what I need in this way:</p>
<pre><code class="lang-auto">// create default storage nodes for all storables
std::vector&lt;vtkMRMLNode*&gt; storableNodes;
mrmlScene-&gt;GetNodesByClass("vtkMRMLStorableNode", storableNodes);
for (auto&amp;&amp; storableNode : storableNodes)
{
  vtkMRMLStorableNode::SafeDownCast(storableNode)-&gt;AddDefaultStorageNode();
}

// set the stored time of all storage nodes to now
std::vector&lt;vtkMRMLNode*&gt; storageNodes;
qSlicerApplication::application()-&gt;mrmlScene()-&gt;GetNodesByClass("vtkMRMLStorageNode", storageNodes);
for (auto&amp;&amp; storageNode : storageNodes)
{
  vtkMRMLStorageNode::SafeDownCast(storageNode)-&gt;GetStoredTimePtr()-&gt;Modified();
}

// set stored time of scene to now
mrmlScene-&gt;GetStoredTimePtr()-&gt;Modified();
</code></pre>
<p>In my fork, I added:</p>
<pre><code class="lang-auto">//------------------------------------------------------------------------------
vtkTimeStamp vtkMRMLStorageNode::GetStoredTime()
{
  return *this-&gt;StoredTime;
}

//------------------------------------------------------------------------------
// Added method that returns pointer to StoredTime
vtkTimeStamp* vtkMRMLStorageNode::GetStoredTimePtr()
{
  return this-&gt;StoredTime;
}
</code></pre>
<p>and</p>
<pre><code class="lang-auto">//-----------------------------------------------------------------------------
vtkTimeStamp* vtkMRMLScene::GetStoredTimePtr()
{
  return &amp;this-&gt;StoredTime;
}
</code></pre>

---

## Post #5 by @lassoan (2020-02-08 01:10 UTC)

<p>Thanks for sharing. FYI, in custom applications we usually override the entire save dialog.</p>

---

## Post #6 by @rprueckl (2020-02-09 12:54 UTC)

<p>Thank you, yes, I alredy did this, however I still use</p>
<pre><code class="lang-auto">if (scene-&gt;GetStorableNodesModifiedSinceRead() || scene-&gt;GetModifiedSinceRead())
</code></pre>
<p>for determining whether there were changes to the scene.</p>

---
