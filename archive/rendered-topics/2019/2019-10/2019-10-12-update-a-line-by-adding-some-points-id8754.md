---
topic_id: 8754
title: "Update A Line By Adding Some Points"
date: 2019-10-12
url: https://discourse.slicer.org/t/8754
---

# Update a line by adding some points

**Topic ID**: 8754
**Date**: 2019-10-12
**URL**: https://discourse.slicer.org/t/update-a-line-by-adding-some-points/8754

---

## Post #1 by @danial (2019-10-12 13:20 UTC)

<p>Hello,</p>
<p>I want to enlarge a line by adding the points in each iteration, i did it like this :</p>
<pre><code>    vtkSmartPointer&lt;vtkPoints&gt; points = realTimeInsertion-&gt;getPoints();
    vtkSmartPointer&lt;vtkPolyData&gt; poly = vtkSmartPointer&lt;vtkPolyData&gt;::New();
    poly-&gt;SetPoints(points);

    vtkIdType nbPoints = points-&gt;GetNumberOfPoints();

    if(nbPoints &gt; 1)
    {
        vtkSmartPointer&lt;vtkPolyLine&gt; polyLine = vtkSmartPointer&lt;vtkPolyLine&gt;::New();
        polyLine-&gt;GetPointIds()-&gt;SetNumberOfIds(nbPoints);
        for(int i=0; i&lt;nbPoints; i++)
            polyLine-&gt;GetPointIds()-&gt;SetId(i,i);
        vtkSmartPointer&lt;vtkCellArray&gt; cells = vtkSmartPointer&lt;vtkCellArray&gt;::New();
        cells-&gt;InsertNextCell(polyLine);
        poly-&gt;SetLines(cells);
    }

    vtkMRMLModelNode::SafeDownCast(realTimeTrajectory)-&gt;SetAndObservePolyData(poly);
    realTimeTrajectory-&gt;Modified();
</code></pre>
<p>But i got this error :</p>
<blockquote>
<p>error: [/RealTimeAblation/Slicer/Slicer-SuperBuild/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer] exit abnormally - Report the problem.</p>
<p>16:48:17: /RealTimeAblation/Slicer/Slicer-SuperBuild/Slicer-build/Slicer exited with code 1</p>
</blockquote>
<p>How can i replace the vtkPolyData of this node ?</p>
<p>I have also another question, how can i delete a vtkMRMLModelNode ?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2019-10-12 14:14 UTC)

<p>If you are not comfortable performing such low-level polydata manipulation then you can use higher-level VTK classes (such as vtkLineSource) to generate polydata instead.</p>
<p>To display polylines in Slicer, I would recommend to use markup curve nodes (available in recent Slicer Preview releases).</p>

---

## Post #3 by @danial (2019-10-12 15:08 UTC)

<p>Can you give me a simple example of markup curve nodes in c++, please ?<br>
And i want to know how can i remove a MRML Model Node in my codes, can you give a simple example for removing nodes ?</p>
<p>Thank you so much.</p>

---

## Post #4 by @lassoan (2019-10-12 16:02 UTC)

<aside class="quote no-group" data-username="danial" data-post="3" data-topic="8754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/danial/48/4888_2.png" class="avatar"> danial:</div>
<blockquote>
<p>Can you give me a simple example of markup curve nodes in c++, please ?</p>
</blockquote>
</aside>
<p>See these tests: <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Markups/Testing/Cxx" class="inline-onebox">Slicer/Modules/Loadable/Markups/Testing/Cxx at main · Slicer/Slicer · GitHub</a></p>
<aside class="quote no-group" data-username="danial" data-post="3" data-topic="8754">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/danial/48/4888_2.png" class="avatar"> danial:</div>
<blockquote>
<p>how can i remove a MRML Model Node</p>
</blockquote>
</aside>
<p>You can remove nodes by calling <a href="https://apidocs.slicer.org/master/classvtkMRMLScene.html#af22004ab04625f8746872e2d5ed37245">vtkMRMLScene::RemoveNode</a>.</p>

---
