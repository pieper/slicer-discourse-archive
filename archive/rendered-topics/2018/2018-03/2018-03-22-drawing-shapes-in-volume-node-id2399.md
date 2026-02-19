---
topic_id: 2399
title: "Drawing Shapes In Volume Node"
date: 2018-03-22
url: https://discourse.slicer.org/t/2399
---

# Drawing shapes in Volume Node

**Topic ID**: 2399
**Date**: 2018-03-22
**URL**: https://discourse.slicer.org/t/drawing-shapes-in-volume-node/2399

---

## Post #1 by @Vinny (2018-03-22 11:10 UTC)

<p>Hello 3D Slicer forum,</p>
<p>I’d like to draw shapes in the Volume node where the MRI image is located.  I’m relatively new to Slicer and have been learning to use the Python interactor, and specifically, interfacing with the VTK module.  For example, I’ve drawn a circle using vtkRegularPolygonSource and am able to display it as a model, but this is independent of any imaging volume node, just a strict geometric object.  I’d like to center that circle at a specific coordinate location within the imaging volume node.  I’m assuming a transformation node needs to be set up?  If so, how can I set up the transform between the VTK object and the imaging node?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @cpinter (2018-03-22 12:34 UTC)

<p>Hi Vinny,</p>
<p>I could answer in several different ways, but let’s narrow down the issue first:</p>
<ul>
<li>Is it important for you to use poly data for “drawing”?</li>
<li>Are you trying to automate something by python scripting? (i.e. What’s your overall goal?)</li>
</ul>
<p>Thanks!</p>

---

## Post #3 by @Vinny (2018-03-22 12:58 UTC)

<p>I’d like to delineate regions of interest (ROIs), either cubic or spherical, based on known anatomical landmarks, such as anterior/posterior commissures (AC/PC).  I’ve done some basic Python scripting (in Spyder) to determine the center coordinate that I’d like place in relation to these landmarks.  From this center coordinate, I’d like to construct a circle (2 mm radius) on that particular slice, and also a cubic ROI.  I guess if I want certain dimensions to construct these objects then I should construct them directly in the volume imaging node?  So, it’s not important that I use poly data for ‘drawing’ objects.</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2018-03-22 15:03 UTC)

<p>Have you looked at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">segmentation examples in the script repository</a>?</p>
<p>I think this example does exactly what you need - defines segments by “drawing” spheres as segments and use those as seeds for “Grow from seeds” effect:<br>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b</a></h4>
<h5>SegmentGrowCutSimple.py</h5>
<pre><code class="Python"># Generate input data
################################################

import SampleData

# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @Vinny (2018-03-22 15:10 UTC)

<p>Great, I did not come across this example.  I’ll go through it and give it a try.</p>
<p>Thanks for your help!</p>

---

## Post #6 by @Vinny (2018-03-23 00:30 UTC)

<p>Hi Andras,</p>
<p>I tried the code you gave and it worked wonderfully.  Also, instead of a sphere, I constructed a circle outline using vtkRegularPolygonSource() and was able to view it in the 3d viewer; however, I’m wondering why the circle outline does not appear in any of the slice views but the cross section of the sphere can be viewed in both the slice views and 3d viewer.</p>

---

## Post #7 by @lassoan (2018-03-23 02:29 UTC)

<p>Closed surface representation must contain closed 3D surface mesh (for example, because slice view is computed by cutting the mesh with the slice plane, but cutting a 2D polygon with a plane the result is nothing or a few points).</p>
<p>If you define your segment by a set of planar contours then you need to store it in planar contour representation:</p>
<pre><code>planarContour = vtkSegmentationCore.vtkSegmentationConverter.GetSegmentationPlanarContourRepresentationName()
segment.AddRepresentation(planarContour, polygonSource.GetOutput())
</code></pre>
<p>If you do this, then Slicer will show the segmentation correctly in both 2D and 3D views and it can also correctly compute closed surface and binary labelmap representations.</p>

---
