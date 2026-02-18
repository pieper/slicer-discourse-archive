# Slicer quit when using vtkStatisticalOutlierRemoval

**Topic ID**: 23381
**Date**: 2022-05-12
**URL**: https://discourse.slicer.org/t/slicer-quit-when-using-vtkstatisticaloutlierremoval/23381

---

## Post #1 by @efu98 (2022-05-12 02:09 UTC)

<p>Hello!<br>
I am trying to extract enclosed points of a point cloud inside a polydata using VTK.<br>
Extracting the points (with vtkExtractEnclosedPoints) seems to work. However, there are outlier points that aren’t inside the polydata that are still there.<br>
I’m trying to remove them using vtkStatisticalOutlierRemoval but Slicer crashes when I call the Update() function. I have tried using vtkRadiusOutlierRemoval but it does not seem to do anything (but it doesn’t make Slicer crash.)</p>
<p>I have created a C++ script independant from Slicer and used vtkStatisticalOutlierRemoval there and things are working well.</p>
<p>Here is my code:</p>
<pre><code class="lang-cpp">vtkNew&lt;vtkExtractEnclosedPoints&gt; extract;
extract-&gt;SetSurfaceData(customShape);
extract-&gt;SetInputData(mosaic);
extract-&gt;CheckSurfaceOn();
extract-&gt;Update();
		
vtkNew&lt;vtkStatisticalOutlierRemoval&gt; removal;
removal-&gt;SetInputConnection(extract-&gt;GetOutputPort());
removal-&gt;SetSampleSize(25);
removal-&gt;Update(); //Slicer crashes here
</code></pre>
<p>Am I doing something wrong?</p>
<p>Kind regards,</p>
<p>Elise</p>

---

## Post #2 by @lassoan (2022-05-12 02:13 UTC)

<p>This is a pure VTK issue, but if you provide sample data (<code>customShape</code> and <code>mosaic</code> polydata) that reproduce the issue then we can have a quick look.</p>

---

## Post #3 by @efu98 (2022-05-16 13:05 UTC)

<p>Hello! Sorry for the late reply.</p>
<p>I’ve solved the issue by using a markup closed curve to draw the region of interest. It’s quicker to compute and creates a cleaner shape.</p>
<p>I cannot share the mosaic but the issue is the same using randomly generated points (like on the <a href="https://kitware.github.io/vtk-examples/site/Cxx/Points/ExtractEnclosedPoints/" rel="noopener nofollow ugc">ExtractEnclosedPoints example</a>).</p>
<p>The <code>customShape</code> is actually the <code>closedSurfacePolyData</code> inside the <code>updateBrushModel</code> function in the scissor script (<code>qSlicersegmentBreastScissorWidget</code>) on the SegmentEditor. My guess is that it might have tiny polygons and points but i’m not sure.</p>
<p>Here is the <a href="https://filesender.renater.fr/?s=download&amp;token=c3cff411-b1ca-4b16-9e5a-e9fd751954f8" rel="noopener nofollow ugc">customShape</a> with a test script.</p>

---

## Post #4 by @lassoan (2022-05-16 15:43 UTC)

<aside class="quote no-group" data-username="efu98" data-post="3" data-topic="23381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/46a35a/48.png" class="avatar"> efu98:</div>
<blockquote>
<p>Here is the <a href="https://filesender.renater.fr/?s=download&amp;token=c3cff411-b1ca-4b16-9e5a-e9fd751954f8">customShape </a> with a test script.</p>
</blockquote>
</aside>
<p>This example works well for me with using customShape.vtk as input file, on Windows, with Slicer’s VTK version, both in debug and in release modes.</p>

---

## Post #5 by @efu98 (2022-05-25 22:20 UTC)

<p>Sorry for the late reply, it seems like I’ve managed to make it work by using<br>
<code>vtkVertexGlyphFilter</code> before displaying the polydata <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"><br>
Thank you for your help!</p>

---
