---
topic_id: 18494
title: "Enable Markup Plane Visibility Programmatically"
date: 2021-07-02
url: https://discourse.slicer.org/t/18494
---

# Enable markup plane visibility programmatically

**Topic ID**: 18494
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/enable-markup-plane-visibility-programmatically/18494

---

## Post #1 by @tpereira (2021-07-02 20:18 UTC)

<p>So I created a markups plane using the code and now I was to make the interaction handles visible. I know you can just select the box in the markups menu but I am trying to automate as much of the process as possible so it can be used by others at my company who have never used slicer. I have spent some time searching but have not found anything on this subject.</p>
<p>This is the code I used to make the plane:<br>
P = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsPlaneNode”)<br>
P.SetOrigin([0,0,0])<br>
P.SetNormal([1,0,0])<br>
P.SetAxes([100,0,0],[0,100,0],[0,0,100])</p>

---

## Post #2 by @smrolfe (2021-07-03 21:44 UTC)

<p>The interaction handles are a property of the display node, so you can use:</p>
<pre><code class="lang-auto">P.GetDisplayNode().SetHandlesInteractive(True)
</code></pre>

---

## Post #3 by @tpereira (2021-07-06 17:42 UTC)

<p>Thanks so much worked perfectly!</p>

---
