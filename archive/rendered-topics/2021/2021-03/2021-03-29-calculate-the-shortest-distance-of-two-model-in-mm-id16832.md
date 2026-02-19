---
topic_id: 16832
title: "Calculate The Shortest Distance Of Two Model In Mm"
date: 2021-03-29
url: https://discourse.slicer.org/t/16832
---

# Calculate the shortest distance of two model in mm

**Topic ID**: 16832
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/calculate-the-shortest-distance-of-two-model-in-mm/16832

---

## Post #1 by @Raj_Kumar_Ranabhat (2021-03-29 20:29 UTC)

<p>Hi Experts,</p>
<p>I would like to calculate the shortest distance(in mm) of two models using VTK based on the point coordinates of the two models. How should I proceed, Is there a sample python script to find the shortest distance?</p>

---

## Post #2 by @lassoan (2021-04-03 03:01 UTC)

<p>Completely different algorithms are used depending on how close the models are and if they are overlapping or not.</p>
<p>If models mostly overlap and there are only small differences between them then you can use ModelToModelDistance extension to compute distance between the models and then get the point corresponding to the shortest distance.</p>
<p>For models that do not overlap and far away from each other you may find the closest point by a few iterations of finding closest point of mesh A to a randomly selected point of mesh B, then find the closest point in mesh B to that point of mesh A, etc. You can use <code>FindClosestPoint</code> method of any locator (vtkPointLocator, vtkCellLocator) to get closest point position on a mesh.</p>

---
