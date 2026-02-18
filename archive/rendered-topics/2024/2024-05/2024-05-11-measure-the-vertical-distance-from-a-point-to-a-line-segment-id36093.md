# Measure the vertical distance from a point to a line segment

**Topic ID**: 36093
**Date**: 2024-05-11
**URL**: https://discourse.slicer.org/t/measure-the-vertical-distance-from-a-point-to-a-line-segment/36093

---

## Post #1 by @Olivia (2024-05-11 18:33 UTC)

<p>Hi, I am new to this software. I need to measure the minimum distance from a point to a line segment (aka perpendicular distance) in my measurements, but I haven’t found a suitable program that can do this, do you have any code that can help?<br>
Sincerely to the development team!<br>
Olivia</p>

---

## Post #2 by @ungi (2024-05-12 17:01 UTC)

<p>If you copy this code in the python interactor of Slicer, it will create a random point and a random line and calculate their distance. This assumes that the line is infinitely long, the two points are just there to define it.</p>
<pre><code class="lang-auto">import numpy as np

# Make sure point markup exists
fiducialNode = slicer.mrmlScene.GetFirstNodeByName("F")
if fiducialNode is None:
  fiducialNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "F")

# Make sure point markup has at least one point
if fiducialNode.GetNumberOfControlPoints() &lt; 1:
  pointCoordinates = np.random.rand(3) * 200 - 100
  fiducialNode.AddControlPoint(pointCoordinates[0], pointCoordinates[1], pointCoordinates[2])

# Make sure line markup exists
lineNode = slicer.mrmlScene.GetFirstNodeByName("L")
if lineNode is None:
  lineNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "L")

# Make sure line markup has at least two points
if lineNode.GetNumberOfControlPoints() &lt; 2:
  pointCoordinates = np.random.rand(3) * 200 - 100
  lineNode.AddControlPoint(pointCoordinates[0], pointCoordinates[1], pointCoordinates[2])
  pointCoordinates = np.random.rand(3) * 200 - 100
  lineNode.AddControlPoint(pointCoordinates[0], pointCoordinates[1], pointCoordinates[2])

# Get point coordinates from markups
point = np.array(fiducialNode.GetNthControlPointPositionWorld(0))
line_p1 = np.array(lineNode.GetNthControlPointPositionWorld(0))
line_p2 = np.array(lineNode.GetNthControlPointPositionWorld(1))

# Calculate distance
lineVector = line_p2 - line_p1
target = np.dot(point - line_p1, lineVector) / np.dot(lineVector, lineVector)
projectionPoint = target * lineVector + line_p1
distance = np.linalg.norm(point - projectionPoint)

print(f"Distance from point to line = {distance}")

</code></pre>

---

## Post #3 by @Olivia (2024-05-15 14:07 UTC)

<p>Thank you so much for your help, I tried this and it worked. But there is a little extra request, since the points and line segments I need to measure are defined by myself on the model, is it possible to change the code so that I can substitute the points and line segments I need to measure? (Sorry for needing your help as I am very bad with computers) Sincerely thank you again!</p>

---

## Post #4 by @ungi (2024-05-15 14:31 UTC)

<p>If you change the name of the point list “F” and the name of the line “L” in the code, then it should work with any point and line.</p>

---

## Post #5 by @Olivia (2024-05-15 15:18 UTC)

<p>This did work and I believe it solved my problem, thank you very much to you and the rest of the development team people.</p>

---
