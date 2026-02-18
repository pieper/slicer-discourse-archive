# Inverting points on Spline

**Topic ID**: 35296
**Date**: 2024-04-04
**URL**: https://discourse.slicer.org/t/inverting-points-on-spline/35296

---

## Post #1 by @bw3232 (2024-04-04 20:15 UTC)

<p>I created many splines for measurements. I wanted to use the endoscopy feature, but in the other direction that I placed the points. Is there an easy way to invert the order of the points?</p>

---

## Post #2 by @rfenioux (2024-04-05 09:42 UTC)

<p>In the Markups module, under control points &gt; advanced you will find buttons to move control points up or down in the list.</p>
<p>Otherwise you can do this in python :</p>
<pre><code class="lang-auto">import numpy as np
curveNode = slicer.util.getNode('OC')
points_array = slicer.util.arrayFromMarkupsControlPoints(curveNode)
slicer.util.updateMarkupsControlPointsFromArray(curveNode, np.flip(points_array, axis=0))
</code></pre>

---
