# Python equivalent of C++ pass by reference

**Topic ID**: 15710
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/python-equivalent-of-c-pass-by-reference/15710

---

## Post #1 by @joachim (2021-01-28 10:10 UTC)

<p>Here is an example of a C++ function using pass by reference (non-const pointer arguments): <a href="http://apidocs.slicer.org/master/classvtkMRMLAnnotationROINode.html#a951f54fefa1e4e9e8a0f0ec7439e96f7" rel="noopener nofollow ugc">vtkMRMLAnnotationsROINode::GetXYZ(double[3] point)</a>.</p>
<p>How do I call this function in Python, i.e. pass an array as argument? With no arguments, <code>node.GetXYZ()</code> gives <em>TypeError: GetXYZ() takes exactly 1 argument (0 given)</em>.</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-01-28 13:22 UTC)

<p>Dear <a class="mention" href="/u/joachim">@joachim</a></p>
<p>you have to first create a list array. For example.</p>
<pre><code class="lang-python"># create annotation ROI MRML node 

roi = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")

# interact with it in the application.. move it around then to retrieve the center of the annotation ROI

point = [0., 0., 0.]
roi.GetXYZ(point)
</code></pre>
<p>HTH<br>
Andinet</p>

---

## Post #3 by @joachim (2021-01-30 14:50 UTC)

<p>Thank you, this was very helpful for me! It should be some tip for this on the wiki - how to emulate C++ calls through Python - because the <a href="http://apidocs.slicer.org/master/index.html" rel="noopener nofollow ugc">C++ API</a> is the only way I know how to do Python scripting.</p>

---

## Post #4 by @lassoan (2021-01-30 15:40 UTC)

<aside class="quote no-group" data-username="joachim" data-post="3" data-topic="15710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>It should be some tip for this on the wiki - how to emulate C++ calls through Python - because the <a href="http://apidocs.slicer.org/master/index.html">C++ API</a> is the only way I know how to do Python scripting</p>
</blockquote>
</aside>
<p>This page describes how to translate C++ API to Python: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation" class="inline-onebox">Slicer API — 3D Slicer documentation</a></p>
<p>Some additional useful tips: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html" class="inline-onebox">Python FAQ — 3D Slicer documentation</a></p>

---
