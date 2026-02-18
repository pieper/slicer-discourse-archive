# Slow 2d slice update speed

**Topic ID**: 21206
**Date**: 2021-12-25
**URL**: https://discourse.slicer.org/t/slow-2d-slice-update-speed/21206

---

## Post #1 by @Hitesh_Ganjoo (2021-12-25 19:48 UTC)

<p>Hi,</p>
<p>I am trying to update the 2D slice views based on a normal(using the plane perpendicular to the normal as the slice plane).<br>
I am facing an issue with fast update of 2D views, and on initial analysis, it seems like vtkMRMLSliceNode::UpdateMatrices() takes the most time and the 2D slice update isnt real time and I need to reduce the rate of update to prevent the GUI from freezing… Is there a better way to update 2D slices realtime,if I want to update the 2D slice nodes several times per second?</p>
<p>Thanks,<br>
Hitesh</p>

---
