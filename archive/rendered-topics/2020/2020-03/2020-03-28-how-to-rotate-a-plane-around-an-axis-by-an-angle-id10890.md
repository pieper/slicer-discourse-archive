# How to rotate a plane around an axis by an angle

**Topic ID**: 10890
**Date**: 2020-03-28
**URL**: https://discourse.slicer.org/t/how-to-rotate-a-plane-around-an-axis-by-an-angle/10890

---

## Post #1 by @siaeleni (2020-03-28 18:19 UTC)

<p>Hello,<br>
I have a plane and I want to rotate that plane around an arbitrary axis by a specific angle.For my axis, I do have two points where I can define my axis A and B, and doesn’t start from the (0,0,0).<br>
I try to generate my Rotation matrix I user <a href="https://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle" rel="nofollow noopener">https://en.wikipedia.org/wiki/Rotation_matrix#Axis_and_angle</a> formula and a translation, but unfortunately, it is not working. Do you have any reccomendation?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-03-28 19:45 UTC)

<p>Hi <a class="mention" href="/u/siaeleni">@siaeleni</a> -</p>
<p>You’ll find the formulas for this in computer graphics textbooks and presentations (<a href="https://www.engr.uvic.ca/~mech410/lectures/4_2_RotateArbi.pdf">this one</a> for example looks right).  The basic idea is to make a vtkMatrix4x4 for a linear transform node that is the concatenation of several operations.  First translates one point of the line to the origin, then rotate the line to so it is on one of the main axes, then rotate around that axis and then apply the inverse rotations and translation.  This should just be a series of matrix multiplies.</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2020-03-28 21:49 UTC)

<p>In the Slicer script repository there is a complete example of how to rotate a node around a line: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_line">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_line</a></p>

---

## Post #4 by @siaeleni (2020-03-31 00:05 UTC)

<p>Thanks a lot for your help!</p>

---
