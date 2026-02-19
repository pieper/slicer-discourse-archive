---
topic_id: 19566
title: "Set The Color For Every Points In Vtkmrmlmarkupsfiducialnode"
date: 2021-09-08
url: https://discourse.slicer.org/t/19566
---

# Set the color for every points in vtkMRMLMarkupsFiducialNode

**Topic ID**: 19566
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/set-the-color-for-every-points-in-vtkmrmlmarkupsfiducialnode/19566

---

## Post #1 by @xianger-qi (2021-09-08 12:21 UTC)

<p>How can i set the color and radius value for every point in vtkMRMLMarkupsFiducialNode, with c++ language. Thanks for your help!</p>

---

## Post #2 by @lassoan (2021-09-08 15:12 UTC)

<p>Currently, markups module displays all fiducial points with the same radius and one of 2 colors. If you want to set radius and color for each point then you can use a model node for that. You can generate input for the model node using vtkGlyph3D filter.</p>

---
