# Make vtkMRMLMarkupsFiducialNode unselectable

**Topic ID**: 20081
**Date**: 2021-10-09
**URL**: https://discourse.slicer.org/t/make-vtkmrmlmarkupsfiducialnode-unselectable/20081

---

## Post #1 by @xianger-qi (2021-10-09 09:33 UTC)

<p>Default, the vtkMRMLMarkupsFiducailNode can be selected by left mouse press, But In my application, i want vtkMRMLMarkupsFiducailNode can’t be selected by mouse press, how can i implement it? Thanks for your help!</p>

---

## Post #2 by @lassoan (2021-10-10 12:57 UTC)

<p>You can call SetLocked(True) on the markup node to prevent any interactions.</p>

---

## Post #3 by @xianger-qi (2021-10-10 13:07 UTC)

<p>Yes, I have called vtkMRMLMarkupsFiducailNode → `SetNthMarkupLocked(true). But There are no effect. code below.</p>
<p>fiducial_node-&gt;AddFiducial(tuned_qua[0], tuned_qua[1], tuned_qua[2], “”);<br>
fiducial_node-&gt;SetNthFiducialLabel(i, “”);<br>
fiducial_node-&gt;SetNthFiducialVisibility(i, false);<br>
fiducial_node-&gt;SetNthMarkupLocked(i, true);<br>
fiducial_node-&gt;SetNthMarkupSelected(i, false);</p>

---

## Post #4 by @lassoan (2021-10-10 14:02 UTC)

<p>Don’t lock individual markup control point position, but the node.</p>

---
