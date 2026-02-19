---
topic_id: 20174
title: "Computing And Accessing Normals From Cells Instead Of Points"
date: 2021-10-15
url: https://discourse.slicer.org/t/20174
---

# Computing and accessing normals from cells instead of points

**Topic ID**: 20174
**Date**: 2021-10-15
**URL**: https://discourse.slicer.org/t/computing-and-accessing-normals-from-cells-instead-of-points/20174

---

## Post #1 by @adamy (2021-10-15 15:25 UTC)

<p>Hi all, I am very new to using Slicer. I would like to generate normals for each cell instead of the default point normals.</p>
<p>I have been able to set the cell normals flag on (and the point cell normals flag off) in the python interactor using <code>vtk.vtkPolyDataNormals().ComputeCellNormalsOn()</code> however I am not sure how to actually generate an array of normals after the flags have been set. Using <code>getNode("Output Volume").GetPolyData().GetCellData().GetArray("Normals")</code> yields nothing.</p>
<p>Any suggestions on how to generate and access cell normals?</p>

---
