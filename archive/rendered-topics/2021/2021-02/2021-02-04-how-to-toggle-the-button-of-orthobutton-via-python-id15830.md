---
topic_id: 15830
title: "How To Toggle The Button Of Orthobutton Via Python"
date: 2021-02-04
url: https://discourse.slicer.org/t/15830
---

# How to toggle the button of "orthobutton" via python

**Topic ID**: 15830
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/how-to-toggle-the-button-of-orthobutton-via-python/15830

---

## Post #1 by @aiden.zhu (2021-02-04 07:18 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.0-2019-06-23 r28335<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi all,<br>
What’s the sub-function to control the orthobutton to toggle here?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/862db834ff60eea85a7659fbaccb4666c768b08c.png" alt="image" data-base62-sha1="j8ZVX9oWchozryBX0lffiiNu7eI" width="414" height="211"><br>
Thanks a lot.<br>
Aiden</p>

---

## Post #2 by @jcfr (2021-02-04 07:27 UTC)

<p>To update the rendering mode associated with the first 3D viewer:</p>
<pre><code class="lang-python">viewNode = slicer.util.getNode('vtkMRMLViewNode1')

# Switch to orthographic
viewNode.SetRenderMode(slicer.vtkMRMLViewNode.Orthographic)

# Switch to perspective
viewNode.SetRenderMode(slicer.vtkMRMLViewNode.Perspective)
</code></pre>

---

## Post #3 by @aiden.zhu (2021-02-04 07:30 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="15830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><code>viewNode.SetRenderMode(slicer.vtkMRMLViewNode.Perspective)</code></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a>  Really appreciate your quick answer!  Thanks you very much!</p>

---
