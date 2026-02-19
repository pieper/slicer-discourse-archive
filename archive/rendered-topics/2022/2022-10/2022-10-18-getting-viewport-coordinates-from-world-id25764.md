---
topic_id: 25764
title: "Getting Viewport Coordinates From World"
date: 2022-10-18
url: https://discourse.slicer.org/t/25764
---

# Getting viewport coordinates from world

**Topic ID**: 25764
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/getting-viewport-coordinates-from-world/25764

---

## Post #1 by @dj_96 (2022-10-18 20:53 UTC)

<p>I have a 3d model loaded in vtk and I’m using vtkCellPicker to get the world coordinates for a point. But how can I keep track of the 2d position on the viewport that corresponds to that coordinate after I’ve rotated the model?</p>
<p>So the world coordinates are fixed but I want to coordinates of that 3d point on the 2d window(x,y).</p>

---

## Post #2 by @lassoan (2022-10-19 05:26 UTC)

<p>Usually we handle all interactions by markup points. So, it should not be necessary to use low-level tools, such as pickers. What is your end goal?</p>
<p>If you go lower level and use VTK then you can find answers to your questions on VTK forums. For example, <a href="https://stackoverflow.com/questions/69486555/how-to-convert-world-coordinate-to-view-coordinate-in-vtk">how to convert world to display coordinates</a>.</p>

---
