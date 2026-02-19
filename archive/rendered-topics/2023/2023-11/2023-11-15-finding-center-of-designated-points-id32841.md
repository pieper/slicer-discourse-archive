---
topic_id: 32841
title: "Finding Center Of Designated Points"
date: 2023-11-15
url: https://discourse.slicer.org/t/32841
---

# Finding center of designated points

**Topic ID**: 32841
**Date**: 2023-11-15
**URL**: https://discourse.slicer.org/t/finding-center-of-designated-points/32841

---

## Post #1 by @lccmyers (2023-11-15 17:28 UTC)

<p>I’m trying to figure out how to find the center of 4+ points that I place on a 3D model. I’m placing the points on two separate models (they’re vertebrae) and the center point would lie in the space in between the models.</p>

---

## Post #2 by @mikebind (2023-11-16 00:42 UTC)

<p>The centroid of the points would just be the average of the coordinates.  If the points are the control points of a markups node, the following would calculate it</p>
<pre><code class="lang-auto">myMarkupsNode = slicer.util.getNode('F') # replace 'F' with the name of the markups node containing your points

# Calculated center point position
import numpy as np
pointPositionArray = slicer.util.arrayFromMarkupsControlPoints(myMarkupsNode, world=True)
centerPosition = np.mean(pointPositionArray, axis=0)

# Create a new markups node and put a point at the calculated center
centerPointMarkupsNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'MyCenterPoint')
centerPointMarkupsNode.AddControlPoint(centerPosition)

</code></pre>

---
