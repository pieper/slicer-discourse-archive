---
topic_id: 29867
title: "Draw Plane Based On Angle To Another Plane And 2 Markup Poin"
date: 2023-06-06
url: https://discourse.slicer.org/t/29867
---

# Draw plane based on angle to another plane and 2 markup points

**Topic ID**: 29867
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/draw-plane-based-on-angle-to-another-plane-and-2-markup-points/29867

---

## Post #1 by @Holmes_Tran (2023-06-06 15:39 UTC)

<p>Hi, I have a predefined plane P1, a line L1 through that plane at an angle A. I’d like to draw a plane P2 that contains L1 and at an angle A with P1.</p>
<p>How can I do that in Python? also, is there any easy way to this using GUI?</p>
<p>Thanks for your time</p>

---

## Post #2 by @lassoan (2023-06-16 16:49 UTC)

<p>There is no GUI for this in Slicer, but you can compute the plane position and normal vector fairly easily:</p>
<ul>
<li>P2 plane position is the intersection of P1 and L1</li>
<li>P2 plane normal is the cross product of L1 and L1’, where L1’ is the projection of L1 line on P1 plane</li>
</ul>

---
