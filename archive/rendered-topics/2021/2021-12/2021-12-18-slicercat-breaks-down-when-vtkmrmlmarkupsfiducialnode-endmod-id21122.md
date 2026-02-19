---
topic_id: 21122
title: "Slicercat Breaks Down When Vtkmrmlmarkupsfiducialnode Endmod"
date: 2021-12-18
url: https://discourse.slicer.org/t/21122
---

# SlicerCAT breaks down when `vtkMRMLMarkupsFiducialNode::EndModify()` is called

**Topic ID**: 21122
**Date**: 2021-12-18
**URL**: https://discourse.slicer.org/t/slicercat-breaks-down-when-vtkmrmlmarkupsfiducialnode-endmodify-is-called/21122

---

## Post #1 by @keri (2021-12-18 03:10 UTC)

<p>Hi,</p>
<p>Via GUI interface I add control points to <code>vtkMRMLMarkupsFiducialNode</code> one by one.<br>
I’m able to add the first control point but when I’m trying to add second control point SlicerCAT falls down on the line <code>fiducialNode-&gt;EndModify(wasModified);</code></p>
<p>The code that I use is below and the output to console that I get will be a little bit lower:</p>
<pre><code class="lang-auto">  // fiducialNode has type `vtkMRMLMarkupsFiducialNode`
  int wasModified = fiducialNode-&gt;StartModify();
  std::cout &lt;&lt; "START MODIFY: " &lt;&lt; wasModified &lt;&lt; std::endl;

  int id = fiducialNode-&gt;AddFiducial(1,2,3,"my name");
  std::cout &lt;&lt; "fiducial id: " &lt;&lt; id &lt;&lt; std::endl;

  fiducialNode-&gt;SetNthControlPointDescription(
        id, "my description");
  std::cout &lt;&lt; "description is set" &lt;&lt; std::endl;

  fiducialNode-&gt;EndModify(wasModified);
  std::cout &lt;&lt; "END MODIFY" &lt;&lt; std::endl;  // when I add the second point to the `fiducialNode` this line is not shown and SlicerCAT breaks down
</code></pre>
<p>The output:</p>
<pre><code class="lang-auto">START MODIFY: 0
fiducial id: 0
description is set
END MODIFY
START MODIFY: 0
fiducial id: 1
description is set
</code></pre>
<p>I noticed that the the app falls because of line code <code>int wasModified = Superclass::EndModify(previousDisableModifiedEventState);</code> within <code>vtkMRMLMarkupsNode::EndModify(int previousDisableModifiedEventState)</code> function.</p>
<p>I don’t know yet how <code>StartModify()/EndModify()</code> works so I’m not sure whether the error is caused by my own code or native Slicer core. But if somebody have some ideas I would appreciate.</p>

---

## Post #2 by @jcfr (2021-12-18 03:43 UTC)

<p>To ensure your question can be answer, could you indicate which version of Slicer is associated with custom application ?</p>

---

## Post #3 by @keri (2021-12-18 09:23 UTC)

<p>Yes, the one under <code>c72d890515ccca70e4173dfcedd370e197c44ae9</code> git tag</p>

---

## Post #4 by @keri (2021-12-18 17:59 UTC)

<p>I just found the bug in my custom code.<br>
So this is not a Slicer issue.</p>

---
