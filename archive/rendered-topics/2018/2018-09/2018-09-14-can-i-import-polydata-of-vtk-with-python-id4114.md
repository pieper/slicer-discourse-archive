---
topic_id: 4114
title: "Can I Import Polydata Of Vtk With Python"
date: 2018-09-14
url: https://discourse.slicer.org/t/4114
---

# Can I import PolyData of vtk with python

**Topic ID**: 4114
**Date**: 2018-09-14
**URL**: https://discourse.slicer.org/t/can-i-import-polydata-of-vtk-with-python/4114

---

## Post #1 by @timeanddoctor (2018-09-14 00:11 UTC)

<p>Can I import this <a href="https://www.vtk.org/Wiki/VTK/Examples/Cxx/PolyData/BooleanOperationPolyDataFilter" rel="nofollow noopener">PolyDataFilter</a> of vtk with python.</p>

---

## Post #2 by @pieper (2018-09-14 00:24 UTC)

<p>Yes, that is available via python:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; vtk.vtkBooleanOperationPolyDataFilter()
(vtkFiltersGeneralPython.vtkBooleanOperationPolyDataFilter)0x7fae97fa98d8
</code></pre>

---

## Post #3 by @lassoan (2018-09-14 00:52 UTC)

<p>Boolean operation on meshes are extremely difficult to implement correctly. Most implementation are flawed, including expensive commercial software and various open-source libraries. Unfortunately, VTK’s <code>vtkBooleanOperationPolyDataFilter()</code> is very unreliable, too. It randomly gives incorrect results (typically large artifacts appearing at various places) even for well-behaved, completely valid inputs.</p>
<p>If you need reliable Boolean mesh operations then you can convert meshes to labelmap images, perform Boolean operation in the image domain, then convert the result to mesh. This is of course a somewhat lossy operation, but that’s the only reliable solution that is readily available. You can achieve arbitrarily high fidelity, at the cost of increased memory usage and computation time. This approach is used in Segment Editor / Logical operations effect.</p>

---

## Post #4 by @timeanddoctor (2018-09-14 17:06 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="4114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>vtk.vtkBooleanOperationPolyDataFilter()</p>
</blockquote>
</aside>
<p>Thanks.<br>
Dear Pieper,<br>
I donnot know how to set the parameters? The follow code I tried seems wrong… and could you help me correct it, thanks.</p>
<pre><code>    input1 = model1.GetOutput()
    sphere1Tri = vtk.vtkTriangleFilter()
    sphere1Tri.SetInputData(input1)

    #model2
    input2 = model2.GetOutput()
    sphere2Tri = vtk.vtkTriangleFilter()
    sphere2Tri.SetInputData(input2)
    #booleanOperation

    booleanOperation = vtk.vtkBooleanOperationPolyDataFilter()
    # booleanOperation.SetOperationToUnion()
    booleanOperation.SetOperationToIntersection()
    # booleanOperation.SetOperationToDifference()

    booleanOperation.SetInputConnection(0, model2)
    booleanOperation.SetInputConnection(1, model1)
    booleanOperation.Update()
</code></pre>

---

## Post #5 by @timeanddoctor (2018-09-14 17:08 UTC)

<p>Dear Lassoan<br>
Thank you very much.<br>
I just try to run it between two cylinder.</p>

---

## Post #6 by @lassoan (2018-09-14 17:30 UTC)

<aside class="quote no-group" data-username="timeanddoctor" data-post="5" data-topic="4114">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>I just try to run it between two cylinder.</p>
</blockquote>
</aside>
<p>It can randomly fail, even for two simply cylinders, depending on their size and position.</p>

---

## Post #7 by @pieper (2018-09-14 18:09 UTC)

<p>I agree with Andras - booleans on polydata are fragile due to numerical rounding issues.</p>
<p>In any case if you want to try it you need something like:</p>
<pre><code class="lang-auto">booleanOperation.SetInputConnection(0, sphere2Tri.GetOutputPort())
</code></pre>
<p>because it needs the pipeline, not just the data as input.</p>

---

## Post #8 by @Saima (2019-08-15 10:08 UTC)

<p>Hi Andras,<br>
Why the vtkpolydata has no faces and no face_normals.</p>

---

## Post #9 by @lassoan (2019-08-15 15:16 UTC)

<p>I’m not sure what you mean or how it is related to the discussion above. If your question is still relevant then please post it in a new topic, describing in detail what you do, what you expect to happen, and what happens instead.</p>

---
