---
topic_id: 32385
title: "Storing Multiple Arbitrary Point Orientation Pairs With A Ma"
date: 2023-10-23
url: https://discourse.slicer.org/t/32385
---

# Storing multiple arbitrary (point, orientation) pairs with a markups curve

**Topic ID**: 32385
**Date**: 2023-10-23
**URL**: https://discourse.slicer.org/t/storing-multiple-arbitrary-point-orientation-pairs-with-a-markups-curve/32385

---

## Post #1 by @Lee_Newberg (2023-10-23 15:59 UTC)

<p>A user gives me a <code>vtkMRMLMarkupsCurveNode</code> (or something similar such as a closed curve).  For each of several user-supplied points on the curve (though not necessarily control points), I want to store a camera orientation.</p>
<ol>
<li>I can specify a user-supplied <code>location</code> along the curve by its world coordinates (3 floating-point numbers) or I could boil it down to a distance along the user’s supplied curve (1 floating-point number).</li>
<li>I can specify the <code>orientation</code> for a location as (angle, axis_x, axis_y, axis_z) or a quaternion (also four floating point numbers), or a 3×3 matrix (which could be a numpy array or vtk.vtkMatrix3x3).</li>
</ol>
<p>How do I associate several <code>(location, orientation)</code> pairs with the user’s supplied <code>vtkMRMLMarkupsCurveNode</code>?  One way I see: create a second <code>vtkMRMLMarkupsCurveNode</code></p>
<ol>
<li>Somehow make the second <code>vtkMRMLMarkupsCurveNode</code> subservient to the first one – in a way that it would be saved or loaded each time the save or load operation is applied to the first <code>vtkMRMLMarkupsCurveNode</code>.  What’s the best way to associate these?</li>
<li>Set the control points of this subservient <code>vtkMRMLMarkupsCurveNode</code> to be the points where the user has supplied camera orientations.</li>
<li>Use the subservient <code>vtkMRMLMarkupsCurveNode</code>’s method <code>SetNthControlPointOrientation</code> to set the corresponding user-supplied orientation for each of these control points.</li>
</ol>
<p>Is this the best way to do this?  I looked at the <code>vtkMRMLMarkupsCurveNode.SetMeasurement</code> method, but I don’t see how to make the key of a supplied measurement be a 3-dimensional world coordinate position, nor do I see how to make a value of a supplied measurement be an orientation (4-dimensional or 3×3-dimensional).</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2023-10-23 17:22 UTC)

<p>Hi <a class="mention" href="/u/lee_newberg">@Lee_Newberg</a> -</p>
<p>A couple ideas.  Since these are rather specific to the endoscopy use case and closely linked to the source curve, I’d consider storing the extra orientation in a node attribute of the curve node, which can be as simple as a json string encoding the values, or you may want to have number keyword-value pairs for the point concepts.</p>
<p>Also, rather than storing the world space values of the points where the camera is defined, I think you’d want to convert them into something parameterized by the path length along the curve, so that if someone edits the curve you can calculate correct relative position so that the control point stays fixed to the curve.  You may want to do this in absolute length, or as a percentage of the length along the curve.</p>
<p>As we discussed, you may also want to support either a defined camera orientation at each of the specified points, or a lookat point, which would not need to be updated as the curve is edited.</p>

---
