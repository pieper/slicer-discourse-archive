# Axes of a markup plane

**Topic ID**: 28404
**Date**: 2023-03-16
**URL**: https://discourse.slicer.org/t/axes-of-a-markup-plane/28404

---

## Post #1 by @yshi (2023-03-16 01:20 UTC)

<p>Hi Slicer Community,</p>
<p>I created a plane with 3 markup points and would like to know how x, y, and z axes are defined. The document describes how x-axis is defined: “… the x-axis will be defined by the second (control point), and plane normal will be defined by the cross product of the vectors from the second and third points to the first point”. So I guess y-axis is defined by the third control point?</p>
<p>Thank you!</p>
<p>Slicer version 5.2.2<br>
Windows 11</p>

---

## Post #2 by @lassoan (2023-03-16 01:21 UTC)

<p>The y axis the cross product of the z and x axes.</p>

---

## Post #3 by @yshi (2023-03-16 01:39 UTC)

<p>Thank you for your reply! Right, but which is defined as y (or z)? Or, when I place the third control point, am I defining the y axis? Thanks.</p>

---

## Post #4 by @lassoan (2023-03-16 01:58 UTC)

<p>For the 3-point plane placement mode:</p>
<ul>
<li>x axis: p1 to p2</li>
<li>z axis: cross(p1 to p2, p1 to p3)</li>
<li>y axis: cross(z, x)</li>
</ul>

---

## Post #5 by @yshi (2023-03-16 04:45 UTC)

<p>I see, thank you so much!</p>

---
