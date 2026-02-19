---
topic_id: 25639
title: "Planetoworld Set Position Of Plane To World Coordinate Syste"
date: 2022-10-11
url: https://discourse.slicer.org/t/25639
---

# PlaneToWorld: set position of plane to world coordinate system

**Topic ID**: 25639
**Date**: 2022-10-11
**URL**: https://discourse.slicer.org/t/planetoworld-set-position-of-plane-to-world-coordinate-system/25639

---

## Post #1 by @jegberink (2022-10-11 06:56 UTC)

<p>Hello Everyone,</p>
<p>I’m trying to create a coordinate system relative to the femur. I have selected three points to create a plane which will now represent the new coordinate system.</p>
<p>Because i work with slicermorphs automatic registration (ALPACA) in order to get a transform from one position to another, i would like my new coordinate system to allign with the world coordinate system so i can measure this position change automatically in the new coordinate system.</p>
<p>From what i gather i can use the example given here to get a transform from plane to the world coordinates: <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446/16" class="inline-onebox">Creating a new coordinate system - #16 by lassoan</a></p>
<p>So i create a plane “P” and insert the code snippet, however nothing happens. I’m sure i’m doing something wrong, some help would be great.</p>
<p>Thank you in advance</p>

---

## Post #2 by @lassoan (2022-10-19 06:28 UTC)

<p>Based on <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446/27" class="inline-onebox">Creating a new coordinate system - #27 by GL1984</a> it seems you have figured this out (i.e., that you can use the transformation matrix in a transform node and harden that transform - or its inverse - on your node), but if you still have questions then let us know.</p>

---
