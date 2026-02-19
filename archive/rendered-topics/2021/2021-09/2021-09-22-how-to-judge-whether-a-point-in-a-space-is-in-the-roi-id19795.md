---
topic_id: 19795
title: "How To Judge Whether A Point In A Space Is In The Roi"
date: 2021-09-22
url: https://discourse.slicer.org/t/19795
---

# How to judge whether a point in a space is in the ROI?

**Topic ID**: 19795
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/how-to-judge-whether-a-point-in-a-space-is-in-the-roi/19795

---

## Post #1 by @jumbojing (2021-09-22 00:09 UTC)

<p>How to judge whether a point in a space is in the ROI?</p>

---

## Post #2 by @jumbojing (2021-09-22 10:14 UTC)

<p>没人回…换一个方式吧.怎么得到ROI的bounds,就是说那6个顶点的坐标呢</p>
<blockquote>
<p>No reply… I change the qestion to … how to get the bounds of the ROI, that is to say the coordinates of the 6 vertices?..</p>
</blockquote>
<p>我想把ROI先转换成vtkcube, 再用<code>IsInsideSurface</code>这个方法去判断,可是没成功…哪位大神帮帮我</p>
<blockquote>
<p>I want to convert the ROI to vtkcube first, and then use the method <code>IsInsideSurface</code> in  <a href="https://vtk.org/doc/release/5.10/html/classvtkSelectEnclosedPoints.html" rel="noopener nofollow ugc">VTK: vtkSelectEnclosedPoints Class Reference</a>  to judge, but it didn’t work…Which god can help me?</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #3 by @jumbojing (2021-09-22 10:24 UTC)

<p>我试了一下<code>GetPolyData()</code>这个方法,得到了一条线段</p>
<blockquote>
<p>I tried the method <code>GetPolyData()</code> to annotation ROI and got a line segment…</p>
</blockquote>

---

## Post #4 by @pieper (2021-09-22 12:23 UTC)

<p>The annotations ROI stores center and corner point (radius) so you can check if the point is inside center +/- radius in each dimension.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#write-annotation-roi-to-json-file" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#write-annotation-roi-to-json-file</a></p>

---

## Post #5 by @lassoan (2021-09-22 17:02 UTC)

<p>If you use the new markups ROI node then you can get an implicit function that you can use to quickly query points (and also use in all VTK filters that take implicit functions as inputs). Example:</p>
<pre><code class="lang-python">roiNode = getNode('R')
point = [73,45,-1181]

planes = vtk.vtkPlanes()
roiNode.GetPlanes(planes)
isInside = planes.EvaluateFunction(point) &lt; 0
print(f"Point {point} is {'inside' if isInside else 'outside'}")
</code></pre>
<p>The sign of the implicit function returns distance from the ROI boundary. Negative value means that the point is inside.</p>

---

## Post #7 by @jumbojing (2021-09-22 21:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="19795">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">roiNode = getNode('R')
point = [73,45,-1181]

planes = vtk.vtkPlanes()
roiNode.GetPlanes(planes)
isInside = planes.EvaluateFunction(point) &lt; 0
print(f"Point {point} is {'inside' if isInside else 'outside'}")
</code></pre>
</blockquote>
</aside>
<p>This method is wonderful! Thank you God</p>

---
