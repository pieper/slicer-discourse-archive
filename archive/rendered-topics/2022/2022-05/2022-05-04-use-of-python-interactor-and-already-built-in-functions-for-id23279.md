---
topic_id: 23279
title: "Use Of Python Interactor And Already Built In Functions For"
date: 2022-05-04
url: https://discourse.slicer.org/t/23279
---

# Use of python interactor and already built-in functions for workflow efficiency

**Topic ID**: 23279
**Date**: 2022-05-04
**URL**: https://discourse.slicer.org/t/use-of-python-interactor-and-already-built-in-functions-for-workflow-efficiency/23279

---

## Post #1 by @Jacktat (2022-05-04 14:31 UTC)

<p>Hi everyone,<br>
I have achieved what I want to do with slicer, which was segment a vessel, compute centerline, extract CE diameter, and compute the maximum Feret diameter of that cross-section (I want to do this for the whole vessel with a set spacing between each cross-section).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77629059c9d4d02c09cd15f1c65e8b985cf26d45.png" alt="image" data-base62-sha1="h27ZrN9jqcwxgzESdaaFTNzocqV" width="284" height="235"><br>
Segmentation, centerline computation and CE diameter computation were staightforward with Slicer. However, for the maximum feret diameter, I saw the cross section for a single slice in my Subject hierarchy tree, and exported the .vtk file, loaded it into MATLAB, calculated the furthest distance between all coordianates and I had it.</p>
<p>However, I want to do this for the whole vessel instead of only 1 cross-section, as well as for a couple more DICOM data sets. I am sure this is all programmed into the software, I’m just not sure how to do it / access these functions.</p>
<p>To do this I have two questions:</p>
<ol>
<li>As mentioned, I currently manually calculated the feret diameter of the plane outside of Slicer, but I am pretty sure I can do this within the software. When looking through the code of e.g. CrossSectionAnalysis.py I see lines like (lines 1107-1131):</li>
</ol>
<pre><code class="lang-auto"># Place a plane perpendicular to the centerline
    plane = vtk.vtkPlane()
    plane.SetOrigin(center)
    plane.SetNormal(normal)
</code></pre>
<p>…</p>
<pre><code class="lang-auto"># Cut through the closed surface and get the points of the contour.
    planeCut = vtk.vtkCutter()
    planeCut.SetInputData(closedSurfacePolyData)
    planeCut.SetCutFunction(plane)
    planeCut.Update()
    planePoints = vtk.vtkPoints()
    planePoints = planeCut.GetOutput().GetPoints()
    # 
</code></pre>
<p>So it looks like there are also built-in functions sort of doing what I want, the problem is that I dont really know how to access those functions or use the python interactor.</p>
<ol start="2">
<li>If this is not possible, can I then at least quickly export all the .vtk cross sections with a particular spacing. So that I can then do the computation myself with MATLAB?</li>
</ol>
<p>Thanks a lot guys.<br>
Cheers,<br>
Jack</p>

---

## Post #2 by @lassoan (2022-05-06 14:08 UTC)

<p>If you are somewhat familiar with Python (and preferably with VTK library, and if you want to create GUI then also Qt) then the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab bootcamp Slicer programming tutorial</a> is a good way to learn about how to use Python scripting in Slicer.</p>
<p>After that you should be ready to modify the CrossSectionAnalysis.py script to allow plotting not just <code>MIS diameter</code>, <code>CE diameter</code>, and <code>Cross-section area</code> but also Feret’s diameter.</p>

---
