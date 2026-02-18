# Measurenents and Point List are not connected.

**Topic ID**: 33041
**Date**: 2023-11-26
**URL**: https://discourse.slicer.org/t/measurenents-and-point-list-are-not-connected/33041

---

## Post #1 by @nikolay_dmitriyev (2023-11-26 17:38 UTC)

<p>Hi!<br>
Dear freinds and colegs,<br>
How can I create a Pointlist and connected measurements  -the line list? To be able to move points (from this list) and measurements changed automatically. Now, when you copy two points from the Point List to the Line - it is ok. But two new points with the line have been created, without names, and if you move the point from the list - the line is not changing.<br>
I will be sincerely grateful for an answer, or a link where to look.</p>

---

## Post #2 by @muratmaga (2023-11-26 18:36 UTC)

<p>Why aren’t you directly manipulating the control points of the lines? That will give you what you want.</p>

---

## Post #3 by @lassoan (2023-11-27 07:12 UTC)

<p>If using line markups does not work (e.g., you want to add many measurements between a set of points) then you can specify a keyboard shortcut that adds or updates all the measurements at once - see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#pre-populate-the-scene-with-measurements" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>Alternatively, you can add an observer that is called whenever you modify a point and automatically updates all the lines from the input points. See the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab bootcamp Slicer programming tutorial</a> for detailed example.</p>

---

## Post #4 by @nikolay_dmitriyev (2023-11-27 21:35 UTC)

<p>I need measurement of many equal structures. I created a list of 15 landmarks. But measurements should be 25 linear and 10 angular (for example). It will be very convenient to put one-time points and write lines and angles one time, which will be automatically calculated.<br>
For any new measurement, you only need to move or put this list of points.<br>
If you open old measurements - you can check the points’ position and if you change the position of one point all connected measurements will be recalculated.</p>

---

## Post #5 by @nikolay_dmitriyev (2023-11-27 21:39 UTC)

<p>Thank you. I will try! But I hoped (feel) that should be an easier solution.</p>

---

## Post #6 by @lassoan (2023-11-27 22:39 UTC)

<p>It should be all very easy, especially because bing chat or chatgpt should be able to generate all the Python code. You just need to describe in your own words what you want to measure and you get the code that you can copy-paste into the Python console. If there is some error then you can tell that to the chaybot and it will fix the code. It is not guaranteed that you don’t have to do any thinking, but the chances are quite good. If you get stuck then let us know and we can help (copy your prompts and the resulting code here, along with any error message).</p>

---
