# Physical distances in the slice view via python

**Topic ID**: 31593
**Date**: 2023-09-06
**URL**: https://discourse.slicer.org/t/physical-distances-in-the-slice-view-via-python/31593

---

## Post #1 by @laurabc (2023-09-06 15:15 UTC)

<p>Hello all,</p>
<p>I want to measure physical distances in a slice view  (I previously reformatted the volume and zoomed in). I know I can set markers and get the physical distance with the line tool, but I would like to do it programmatically via a python script. Is there a way to transform the coordinates to physical distances? Or to know the size of a pixel in the slice view? Or to know the physical size of the slice view? Any option that would allow me to obtain physical units.</p>
<p>Thanks<br>
Laura</p>

---

## Post #2 by @mikebind (2023-09-06 18:28 UTC)

<p>The simplest way would be to put some kind of Markups points at the locations you want to measure between. This could be control points for a MarkupsCurve or a MarkupsPointList, for example.  Then the coordinates of these points in physical units are easily accessible and you can just calculate the euclidean distance between them.</p>
<pre><code class="lang-auto">import numpy as np
markupsNode = getNode('MyPoints')
pos0 = np.zeros(3) #  initialize variable to hold the coordinates of the first point
markupsNode.GetNthControlPointPositionWorld(0, pos0) # get coord of first point
pos1 = np.zeros(3) # initialize variable to hold coord of second point
markupsNode.GetNthControlPointPositionWorld(1, pos1) # get coord of second point
# Calculate the physical distance between these points (in millimeters because Slicer world coordinates are in mm)
distanceBetweenPointsMm = np.linalg.norm(pos1-pos2) 
</code></pre>
<p>The placed points can be in a single slice view or placed in 3D or placed on different slices, etc., it doesn’t matter.  Slicer keeps track of everything in a physical 3D spatial representation.</p>

---
