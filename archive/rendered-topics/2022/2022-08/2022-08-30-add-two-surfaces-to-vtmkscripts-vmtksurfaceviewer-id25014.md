---
topic_id: 25014
title: "Add Two Surfaces To Vtmkscripts Vmtksurfaceviewer"
date: 2022-08-30
url: https://discourse.slicer.org/t/25014
---

# Add two surfaces to vtmkscripts.vmtkSurfaceViewer

**Topic ID**: 25014
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/add-two-surfaces-to-vtmkscripts-vmtksurfaceviewer/25014

---

## Post #1 by @carlosar (2022-08-30 19:09 UTC)

<p>I’d like to compare the pre and post smoothed surface from the marching cubes script. Here is part of my code. I’m building my own pypes script, so I am trying to replicate what is found in this tutorial at the end: <a href="http://www.vmtk.org/tutorials/SurfaceForMeshing.html" class="inline-onebox" rel="noopener nofollow ugc">Prepare a surface for mesh generation | vmtk - the Vascular Modelling Toolkit</a></p>
<pre><code class="lang-auto">surface = vmtkscripts.vmtkMarchingCubes()
surface.Image = voi_selector.Image # image is loaded from CT data and the voi_selector crops the region of interest using vmtkscripts.vmtkImageVOISelector()
surface.Level = l
surface.Connectivity = 1
surface.Execute()

surface_viewer = vmtkscripts.vmtkSurfaceViewer()
surface_viewer.Surface=surface.Surface
surface_viewer.Execute()

smooth = vmtkscripts.vmtkSurfaceSmoothing()
smooth.NumberOfIterations = 10
smooth.PassBand = 0.1
smooth.Surface = surface.Surface
smooth.Execute()
surface_viewer.surface = smooth.Surface
surface_viewer.Execute()
</code></pre>
<p>What I am trying to do is just add both surfaces to the same viewer. Additionally, I am selecting various locations in my image (by looping through different bounds using the <code>vmtkscripts.vmtkImageVOISelector()</code> and I would also like to see them all at the same viewer. Currently, I save the intermediate steps, and open them in a Paraview, but wondering if I can do it all using the viewer.</p>
<p>Thanks in advance,<br>
Carlos</p>

---
