---
topic_id: 11823
title: "Maximum Intensity Projection"
date: 2020-06-02
url: https://discourse.slicer.org/t/11823
---

# Maximum Intensity Projection

**Topic ID**: 11823
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/maximum-intensity-projection/11823

---

## Post #1 by @ada (2020-06-02 07:31 UTC)

<p>Hello all,</p>
<p>I would like to create my own scripted module in Slicer3D.<br>
Is it possible to create a button and apply the “Maximum intensity projection” algorithm available in “Volume rendering” on 3D volume using Python (with the same opacity) ?<br>
Thank you for your help,<br>
Best</p>

---

## Post #2 by @lassoan (2020-06-02 19:46 UTC)

<p>All features of Slicer are available using Python scripting. Most parameters are stored in nodes of the MRML scene and you can find the relevant class by searching in full text of Slicer source code (search for some text that is shown on screen to find the corresponding widget class, then check which MRML nodes are modified there).</p>
<p>For example, you can choose a raycast technique using <a href="http://apidocs.slicer.org/master/classvtkMRMLViewNode.html#a8ed1dd0f05e9be1942d14405ac2322d8">vtkMRMLViewNode.SetRaycastTechnique</a>:</p>
<pre><code>viewNode = slicer.util.getNode('View1')
viewNode.SetRaycastTechnique(slicer.vtkMRMLViewNode.MaximumIntensityProjection)
</code></pre>
<p>You can find many examples of commonly needed code snippets in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---

## Post #3 by @ada (2020-06-03 13:48 UTC)

<p>It works well !<br>
Thank you so much.</p>

---
