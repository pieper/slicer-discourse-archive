---
topic_id: 31770
title: "3D Coordinates From Points Equidistance Along A Curved Path"
date: 2023-09-18
url: https://discourse.slicer.org/t/31770
---

# 3D coordinates from points equidistance along a curved path 

**Topic ID**: 31770
**Date**: 2023-09-18
**URL**: https://discourse.slicer.org/t/3d-coordinates-from-points-equidistance-along-a-curved-path/31770

---

## Post #1 by @sjang (2023-09-18 12:54 UTC)

<p>Along a curved path, I need the 3D coordinates (x, y, z) every 0.2mm.</p>
<p>In this post (<a href="https://discourse.slicer.org/t/create-equidistant-points-along-curve-for-automated-measurements/19870" class="inline-onebox">Create equidistant points along curve for automated measurements</a>), the solution to getting equidistant points is to resample by selecting the number of points to make along the already made curved path (i.e. 10 points along the curved path).</p>
<p>However, I want to make a point at a set distance (i.e. one point every 0.2mm along the curved path). Does anyone have any recommendations?</p>

---

## Post #2 by @Jeff_Zeyl (2023-09-18 12:59 UTC)

<p>With Python I believe you could use this function <a href="https://discourse.slicer.org/t/how-to-resample-curve-nodes-programmatically/16395/4" class="inline-onebox">How to resample curve nodes programmatically? - #4 by lassoan</a></p>

---

## Post #3 by @lassoan (2023-09-18 13:08 UTC)

<p>What is described in that post is applicable here, too. You can compute the number of points as: <code>CurveLength / 0.2 + 1</code>. If having less control points does not allow reproducing the curve shape with sufficient accuracy then you can use a smaller distance, such as <code>DesiredDistance</code>/<code>N</code>, and then use every <code>N</code>-th point.</p>
<p>You can of also get points at any distance along the curve using Python scripting. For example to get the 5th point with 0.2mm sampling distance:</p>
<pre><code class="lang-python">distance = 0.2 * 5
pointPosition = [0, 0, 0]  # this will store the result
startingPointIndex = 0
getNode('OC').GetPositionAlongCurveWorld(pointPosition, startingPointIndex, distance)
print(p)
</code></pre>

---

## Post #4 by @Chuan (2023-09-21 07:43 UTC)

<p>Hi Jeff,</p>
<p>Have you used this function in python before? What I see here is coded by C++/C, does that mean I should call C function in python?</p>
<p>Best,<br>
Chuan</p>

---

## Post #5 by @Jeff_Zeyl (2023-09-22 16:18 UTC)

<p>It’s a python function. Another example: getNode(‘mycurve’).ResampleCurveWorld(1) will take your curve named ‘mycurve’ and resample it so points are 1 mm apart</p>

---
