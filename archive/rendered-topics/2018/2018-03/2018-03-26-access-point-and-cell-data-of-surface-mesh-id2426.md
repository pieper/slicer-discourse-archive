---
topic_id: 2426
title: "Access Point And Cell Data Of Surface Mesh"
date: 2018-03-26
url: https://discourse.slicer.org/t/2426
---

# Access point and cell data of surface mesh

**Topic ID**: 2426
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/access-point-and-cell-data-of-surface-mesh/2426

---

## Post #1 by @MGM (2018-03-26 14:59 UTC)

<p>Hello everyone,</p>
<p>I used vtkMarchingCubes to generate isosurface, from volume file.<br>
I need to extract data from this surface, which mean print point and index in separate files.</p>
<p>Which mean, without passing via a writer.</p>
<p>Some steps are mentioned in<a href="https://discourse.slicer.org/t/how-to-get-correct-mask-value-from-one-segment-from-segment-editor/1895/9">this post</a></p>
<p>Any suggestion!</p>
<p>Thank you</p>

---

## Post #2 by @mschumaker (2018-03-26 15:36 UTC)

<p>The point set within a model’s poly data is accessible. The output of the vtkMarchingCubes algorithm is a vtkPolyData. I’m doing something similar. Here is how I loop over the point indices and get the position of each point via Python script:</p>
<pre><code>modelNode = slicer.util.getNode(modelNodeID)
modelPolyData = modelNode.GetPolyData()
numPoints = modelPolyData.GetNumberOfPoints()
for ptId in range(numPoints):
    pointPos = [0,0,0]
    modelPolyData.GetPoint(ptId, pointPos)
</code></pre>
<p>GetPoint fills the three-element list with the position of the point corresponding to index ptId. You can then write these values to files.</p>

---

## Post #3 by @MGM (2018-03-26 15:45 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="2" data-topic="2426">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>modelNode</p>
</blockquote>
</aside>
<p>Thank you <a class="mention" href="/u/mschumaker">@mschumaker</a> for your fast reply.<br>
in fact, I already got the surface from MarchingCubes step, under vtk.</p>
<pre><code> vtkSmartPointer&lt;vtkMarchingCubes&gt; surface = vtkSmartPointer&lt;vtkMarchingCubes&gt;::New();
 surface-&gt;SetValue(0, isoValue);
</code></pre>
<p>I’m looking for a way to extract data from “surface”, with vtk method.</p>
<p>Do you have any idea ?</p>
<p>Thanks again</p>

---

## Post #4 by @mschumaker (2018-03-26 15:53 UTC)

<p>Oh, you’re working in C++. You can clean this up as necessary, but the next steps after that would be:</p>
<pre><code>surface-&gt;SetInputData(&lt;image data input&gt;)
surface-&gt;ReleaseDataFlagOn()
surface-&gt;Update()
vtkSmartPointer&lt;vtkPolyData&gt; modelPolyData = surface-&gt;GetOutput()
int numPoints = modelPolyData-&gt;GetNumberOfPoints()
double pointPos[3]
for (ptId=0; ptId&lt;numPoints; ptId++){
    modelPolyData-&gt;GetPoint(ptId, pointPos)
}
</code></pre>
<p>Here is the vtkPolyData class reference, which can give you other options for accessing the point data within the data structure (or cell data, if necessary).<br>
<a href="https://www.vtk.org/doc/nightly/html/classvtkPolyData" class="onebox" target="_blank" rel="nofollow noopener">https://www.vtk.org/doc/nightly/html/classvtkPolyData</a></p>

---

## Post #5 by @MGM (2018-03-27 09:11 UTC)

<p>Thank you a lot <a class="mention" href="/u/mschumaker">@mschumaker</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>just, I would like to take your advice :</p>
<p>I’m trying to find an IDE under Linux ( Ubuntu ), in order to work easily with vtk library, I mean which support gotoDefiniton functionality.</p>
<p>please, let me know your idea</p>
<p>Thanks again</p>

---

## Post #6 by @mschumaker (2018-03-27 14:29 UTC)

<p>You’re welcome.<br>
I don’t know much about IDEs for Linux, and I don’t know of one that has that functionality for VTK. All of my work with VTK in C++ was in Windows with Visual Studio.</p>
<p>Maybe other people here will have ideas?</p>

---

## Post #7 by @lassoan (2018-03-27 14:33 UTC)

<p>I think most of us uses PyCharm as Python IDE. But you can use Eclipse, LiClipse, Visual Studio. All can be connected to Slicer for interactive debugging. See more information here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools</a></p>

---

## Post #8 by @MGM (2018-03-27 14:53 UTC)

<p>Thank you <a class="mention" href="/u/mschumaker">@mschumaker</a><br>
I really appreciate your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>By the way, it’s work, now I can extract points and index <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #9 by @MGM (2018-03-27 15:29 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>the problem that I can’t find an IDE wich support vtk recursive sub-folder.<br>
I tried Visual studio code, Eclipse</p>

---

## Post #10 by @lassoan (2018-03-27 15:36 UTC)

<p>PyCharm works well for me, including documentation, auto-complete, etc. Of course only when the debugger is connected to Slicer, otherwise the IDE cannot figure out what type each variable is.</p>

---
