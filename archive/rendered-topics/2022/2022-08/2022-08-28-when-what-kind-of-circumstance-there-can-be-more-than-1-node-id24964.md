---
topic_id: 24964
title: "When What Kind Of Circumstance There Can Be More Than 1 Node"
date: 2022-08-28
url: https://discourse.slicer.org/t/24964
---

# When (what kind of circumstance) there can be more than 1 NodeReference with the same ReferenceRole?

**Topic ID**: 24964
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/when-what-kind-of-circumstance-there-can-be-more-than-1-nodereference-with-the-same-referencerole/24964

---

## Post #1 by @sunshine (2022-08-28 17:17 UTC)

<p>Hi everyone,</p>
<p>I got confused when requiring a node using <code>ReferenceRole</code>.<br>
As far as I know about the scene file, one <code>NodeReferenceRole</code> seems to appear only once in a node description.</p>
<p>How can we add the 2nd <code>NodeReference</code> into a node using the same <code>ReferenceRole</code>?<br>
And when (at what kind of circumstance) should we call <code>node.GetNumberOfNodeReferences(refRole)</code>?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @sunshine (2022-08-28 19:33 UTC)

<p>not only <code>node.GetNumberOfNodeReferences(refRole)</code>,<br>
but also <code>node.GetNthNodeReference(refRole, n)</code>.</p>
<p>If we get<br>
<code>node.GetNumberOfNodeReferences(refRole) &gt; 1 == True</code>, what would we get by calling</p>
<pre><code class="lang-auto">node.GetNodeReference(refRole)
</code></pre>
<p>Do we get just one node, or a list of nodes?</p>

---

## Post #3 by @lassoan (2022-08-29 03:59 UTC)

<p>You can assign multiple nodes to the same reference role. For example, a model node node can have multiple display nodes, each using the “display” role.</p>
<p>Most commonly you can use convenience methods that get/set the first node for a role (such as <code>SetNodeReferenceID</code>, <code>GetNodeReference</code>). In case you may have multiple nodes for a role, you can use <code>GetNumberOfNodeReferences</code>/<code>GetNthNodeReference...</code>/<code>SetNthNodeReference...</code> methods.</p>

---
