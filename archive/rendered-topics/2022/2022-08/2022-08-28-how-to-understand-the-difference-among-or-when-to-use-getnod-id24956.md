---
topic_id: 24956
title: "How To Understand The Difference Among Or When To Use Getnod"
date: 2022-08-28
url: https://discourse.slicer.org/t/24956
---

# How to understand the difference among (or when to use) getNode byName(), byRenferenceRole(), byID()?

**Topic ID**: 24956
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/how-to-understand-the-difference-among-or-when-to-use-getnode-byname-byrenferencerole-byid/24956

---

## Post #1 by @sunshine (2022-08-28 01:30 UTC)

<p>Hi everyone,</p>
<p>I am trying to write my first extension module, however, really confused by the various methods to get a node:</p>
<pre><code class="lang-auto">self._parameterNode.GetNodeReference('InputVolume')
slicer.mrmlScene.GetNodeByID()
slicer.util.getNode('F')
</code></pre>
<p>I can understand that we try to avoid using <code>slicer.util.getNode() </code> because there could be variables with the same node name.</p>
<p>I am confused that when should I call <code>self._parameterNode.SetNodeReferenceID()</code> and when should I save the node ID, e.g., <code>self.InputVolume_ID = node_InputVolume.GetID()</code>?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @lassoan (2022-08-28 11:05 UTC)

<p>You need to use node references if you want to store connection between nodes persistently, in a scene file. This is because when a scene is loaded the application automatically modifies a loaded node’s ID if that ID is already used in the scene.</p>

---

## Post #3 by @sunshine (2022-08-28 16:05 UTC)

<p>Thank you so much, Andras!</p>
<p>I kind of understand what is a node reference now. But still, I miss something:</p>
<p>When there is a scene change, if we can always do an update, is there a difference<br>
between   updating the ID:                          <code>self.InputVolume_ID = node_InputVolume.GetID()</code><br>
and           updating the node reference:     <code>self._parameterNode.SetNodeReferenceID('InputVolume', node_InputVolume.GetID())</code><br>
?</p>

---

## Post #4 by @lassoan (2022-08-28 18:52 UTC)

<p>I would recommend to avoid node ID as a member variable as it would be too fragile. For example, if the user closes the scene and loads another scene then your module may find some completely unrelated node by that ID. You can make your module observe scene close and clear out the obsolete node ID, but there are several similar potential issues and node references take care of them.</p>
<p>Using node IDs are fine within method calls, as the user cannot close a scene or add/remove nodes while a method is running.</p>

---

## Post #5 by @sunshine (2022-08-28 19:28 UTC)

<p>Thank you so much, Andreas! I will try to void using nodeID.</p>

---
