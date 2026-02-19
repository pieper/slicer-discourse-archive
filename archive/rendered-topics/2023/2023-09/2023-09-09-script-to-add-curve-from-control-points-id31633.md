---
topic_id: 31633
title: "Script To Add Curve From Control Points"
date: 2023-09-09
url: https://discourse.slicer.org/t/31633
---

# Script to add curve from control points

**Topic ID**: 31633
**Date**: 2023-09-09
**URL**: https://discourse.slicer.org/t/script-to-add-curve-from-control-points/31633

---

## Post #1 by @ghthomas (2023-09-09 11:37 UTC)

<p>I have a dataset of thousands of scans that have already been landmarked. I now want to use a subset of existing landmarks to define new curves. This is quite straightforward to do manually by adding curves with the markups toolbox but I am stuck trying to script the same process (necessary because of the size of the dataset). It is possibly straightforward but I am a Slicer and Python novice. Below is a brief script of where I have got to so far. I can read the scan in and read in a csv containing coordinates for two control points defining the ends points of the curve. I can define the curve type (here, arbitrarily using a Kochanek spline). Next, I want to:</p>
<ol>
<li>include code to implement “Constrain to Model” from Curve Settings menu and constrain to the input model (shoebillNode)</li>
<li>Resample the curve to e.g. 10 resampled points and set the output node to markupsNode1 from the script below.</li>
<li>Output to file the resampled curve</li>
</ol>
<p>I hope that makes sense. I would greatly appreciate suggestions on how to script this. At this point I am not even sure which functions I need.<br>
Many thanks<br>
Gavin</p>
<pre><code class="lang-auto"># Read obj model
shoebillNode = slicer.util.loadModel('Balaeniceps_rex_2.obj')

# Read markups with two points
markupsNode1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
slicer.modules.markups.logic().ImportControlPointsFromCSV(markupsNode1, 'Table1.csv')

# Input control points (not sure if this is necessary - does it do anything different to the previous two lines?)
slicer.vtkProjectMarkupsCurvePointsFilter().SetInputCurveNode(markupsNode1)

# Kochanek spline
slicer.vtkMRMLMarkupsCurveNode.SetCurveTypeToKochanekSpline(markupsNode1)
</code></pre>

---

## Post #2 by @lassoan (2023-09-10 01:46 UTC)

<aside class="quote no-group" data-username="ghthomas" data-post="1" data-topic="31633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/49beb7/48.png" class="avatar"> ghthomas:</div>
<blockquote>
<p>code to implement “Constrain to Model”</p>
</blockquote>
</aside>
<p>You can do this:</p>
<pre data-code-wrap="python"><code class="lang-python">markupsNode1.SetAndObserveSurfaceConstraintNode(shoebillNode)
</code></pre>
<hr>
<aside class="quote no-group" data-username="ghthomas" data-post="1" data-topic="31633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/49beb7/48.png" class="avatar"> ghthomas:</div>
<blockquote>
<p>Resample the curve to e.g. 10 resampled points and set the output node to markupsNode1 from the script below.</p>
</blockquote>
</aside>
<p>You specify not the number of control points but instead the distance between them:</p>
<pre data-code-wrap="python"><code class="lang-python">markupsNode1.ResampleCurveWorld(15.0)
</code></pre>
<hr>
<aside class="quote no-group" data-username="ghthomas" data-post="1" data-topic="31633">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/49beb7/48.png" class="avatar"> ghthomas:</div>
<blockquote>
<p>Output to file the resampled curve</p>
</blockquote>
</aside>
<p>The simplest and most rich export is to json:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.exportNode(markupsNode1, "c:/tmp/mycurve.mrk.json")
</code></pre>
<p>I would not recommend to export point coordinates into CSV, because you would lose all metadata, but if you want to do it anyway then you can export the points to a numpy array:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy
a = slicer.util.arrayFromMarkupsControlPoints(markupsNode1)
numpy.savetxt("c:/tmp/mycurve.csv", a, delimiter=",")
</code></pre>

---

## Post #3 by @ghthomas (2023-09-11 09:16 UTC)

<p>Thank you - that is exactly what I was looking for.</p>

---
