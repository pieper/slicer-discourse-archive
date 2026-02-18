# Linux specific error placing plane markup

**Topic ID**: 32428
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/linux-specific-error-placing-plane-markup/32428

---

## Post #1 by @smrolfe (2023-10-26 17:50 UTC)

<p>I’m getting an error placing a plane markup when running on a Linux OS. I first noticed the bug using an older version (5.3.0) but it also exists on the latest nightly build. When I use either button to create a plane, the plane is immediately placed at the origin. Then, each time the cursor moves in and out of the scene, an additional plane is created. The following errors are generated:</p>
<pre><code class="lang-auto">[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] vtkMRMLMarkupsNode::GetNthControlPointPositionStatus failed: control point 1 does not exist
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] vtkMRMLMarkupsNode::GetNthControlPointPositionStatus failed: control point 1 does not exist
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] AddNControlPoints: number of points major than maximum number of control points allowed.
[VTK] vtkMRMLMarkupsNode::GetNthControlPointPositionStatus failed: control point 1 does not exist

</code></pre>
<p>I have confirmed that the plane markup works as expected on the Windows nightly version.</p>

---
