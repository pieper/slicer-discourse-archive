---
topic_id: 30750
title: "How To Get The Shortest Path From A Fiducialmarkupnode To A"
date: 2023-07-24
url: https://discourse.slicer.org/t/30750
---

# How to get the shortest path from a fiducialmarkupnode to a curvenode

**Topic ID**: 30750
**Date**: 2023-07-24
**URL**: https://discourse.slicer.org/t/how-to-get-the-shortest-path-from-a-fiducialmarkupnode-to-a-curvenode/30750

---

## Post #1 by @jay1987 (2023-07-24 06:41 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56759c7f63ca35fd3c858ba8ae3a4d26e5cf1b18.jpeg" alt="image" data-base62-sha1="ckR2HotTv471yopxDb0QVrMdnSM" width="594" height="375"><br>
i create a curve use several control points (yellow arrow)<br>
and then i create a point (red arrow)<br>
i want to get the projection point from the point(right arrow) to the curve(yellow arrow) , whick means get the point in the curve which has the shortest path to the point</p>
<p>(PS. I try to change the curve into a model node and use FiducialsToModelDistance to get the shortest path , but it failed , the output is always (0,0,0) )</p>

---

## Post #2 by @Sunderlandkyl (2023-07-24 14:15 UTC)

<p>You could try <a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsCurveNode.html#af010bba5a55c6e1483ccbd80b5dcef05" rel="noopener nofollow ugc">vtkMRMLMarkupsCurveNode::GetClosestPointPositionAlongCurveWorld()</a>.</p>

---

## Post #3 by @jay1987 (2023-07-25 01:50 UTC)

<p>thank you <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> ,it’s really work!!</p>

---
