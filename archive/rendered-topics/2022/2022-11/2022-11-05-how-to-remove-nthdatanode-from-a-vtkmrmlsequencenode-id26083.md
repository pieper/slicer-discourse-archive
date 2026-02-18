# How to remove NthDataNode from a vtkMRMLSequenceNode?

**Topic ID**: 26083
**Date**: 2022-11-05
**URL**: https://discourse.slicer.org/t/how-to-remove-nthdatanode-from-a-vtkmrmlsequencenode/26083

---

## Post #1 by @sunshine (2022-11-05 16:09 UTC)

<p>Hi everyone,</p>
<p>I am working on the scripted module development, trying to edit the <code>vtkMRMLSequenceNode</code>.<br>
However, did not find any functions like <code>RemoveNthDataNode()</code>.</p>
<p>How could I remove the NthDataNode?</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @lassoan (2022-11-06 04:17 UTC)

<p>You can use this method:</p>
<pre><code>sequenceNode-&gt;RemoveDataNodeAtValue(sequenceNode-&gt;GetNthIndexValue(n));
</code></pre>

---

## Post #3 by @sunshine (2022-11-06 15:14 UTC)

<p>Thank you so much, Andras!</p>

---
