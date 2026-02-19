---
topic_id: 31939
title: "Scalar Mapping Of Markup Curve Between Points"
date: 2023-09-27
url: https://discourse.slicer.org/t/31939
---

# Scalar mapping of markup curve between points

**Topic ID**: 31939
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/scalar-mapping-of-markup-curve-between-points/31939

---

## Post #1 by @Jeff_Zeyl (2023-09-27 19:36 UTC)

<p>I’m aiming to display a markup curve where the line between points is a unique solid color reflecting the distance between each control point, and which will update when points are modified.</p>
<p>My approach so far is to calculate the distance between each point and the previous, save this to an array (setting the first control point scalar value to 0), and add a static measurement to the markup curve. When a point is modified,I use RemoveAllMeasurements(), re-compute the distances, and re-add the updated measurements to the curve node.</p>
<blockquote>
<p>adjacent_dist = slicer.vtkMRMLStaticMeasurement()<br>
adjacent_dist.SetName(‘staticmeasure’)<br>
adjacent_dist.SetUnits(‘’)<br>
adjacent_dist.SetPrintFormat(“”)<br>
adjacent_dist.SetControlPointValues(adjacent_distArray)<br>
markupsNode.AddMeasurement(adjacent_dist)`</p>
</blockquote>
<p>Since each control point is associated with only a single distance value (reflecting the length between it and the previous point), the color effect is a gradient change along the line between each point value, which is not desired in this case.</p>
<p>Is there a way to access  how the scalars are mapped to the curve color (markupscurvedata array from slicer.util.arrayFromMarkupsCurveData())? Or is there a better approach?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c43cd17cd973ea6846e5c9380872b58b5eedd30.png" data-download-href="/uploads/short-url/8B7UvQ79QtdUg4Wl91Cr0eWrINq.png?dl=1" title="tube_color_markup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c43cd17cd973ea6846e5c9380872b58b5eedd30_2_606x500.png" alt="tube_color_markup" data-base62-sha1="8B7UvQ79QtdUg4Wl91Cr0eWrINq" width="606" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c43cd17cd973ea6846e5c9380872b58b5eedd30_2_606x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c43cd17cd973ea6846e5c9380872b58b5eedd30.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c43cd17cd973ea6846e5c9380872b58b5eedd30.png 2x" data-dominant-color="777A9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tube_color_markup</span><span class="informations">785×647 46.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-28 02:31 UTC)

<p>Measurement values are always lienarly interpolated between control points. It would not be hard to add more interpolation options, but we would only implement this if there were at least a couple of use cases.</p>
<p>For now, I would recommend to create a slightly larger diameter tube model with the colors you desire. By adding an observer to the curve node, you can always keep your tube model up-to-date (following changes in the curve node).</p>

---

## Post #3 by @Jeff_Zeyl (2023-10-12 14:50 UTC)

<p>For anyone interested in a similar effect I achieved the desired result with the code below and a polyline model. in this case I have the color of the connecting line change according to a threshold distance value of the connecting line<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1babfbf9903632e9c72000d846b746447d7d358b.png" data-download-href="/uploads/short-url/3WNmI7izsga723xvvjXHDOCnVx1.png?dl=1" title="linemodel_distance" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1babfbf9903632e9c72000d846b746447d7d358b.png" alt="linemodel_distance" data-base62-sha1="3WNmI7izsga723xvvjXHDOCnVx1" width="565" height="500" data-dominant-color="868761"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">linemodel_distance</span><span class="informations">651×576 29.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">import numpy as np
#markupsNode = getNode('original_markup')
markupsNode = getNode('resampled')
slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','newlinemodel')


def getdistancesbtwnpoints():
  numberfiducialpoints = markupsNode.GetNumberOfControlPoints()
  points = np.zeros([numberfiducialpoints,3])
  for k in range(0,numberfiducialpoints):
    markupsNode.GetNthControlPointPosition(k, points[k,:])
  # Calculate distances between adjacent points
  adjacent_distances = []
  for l in range(len(points) - 1):
    distance = np.linalg.norm(points[l + 1] - points[l])
    adjacent_distances.append(distance)
  # Convert the list of distances to a NumPy array
  adjacent_distances = np.array(adjacent_distances)
  # Print the distances
  #print(adjacent_distances)
  return adjacent_distances

adjdist = getdistancesbtwnpoints()

#####################create model########################

global polyline
polyline = vtk.vtkPolyData()

modelNode = getNode('newlinemodel')
modelNode.CreateDefaultDisplayNodes()
modelNode.SetAndObservePolyData(polyline)
modelNode.GetDisplayNode().SetSliceDisplayModeToProjection()
modelNode.GetDisplayNode().SetVisibility2D(1)
modelNode.GetDisplayNode().SetSliceIntersectionThickness(5)
# Set up coloring by selection array

def updatemodelcolor2(caller, event):
  print('Point locations')
  adjacent_dist = getdistancesbtwnpoints()
  points = vtk.vtkPoints()
  lines = vtk.vtkCellArray()
  for controlPointIndex in range(markupsNode.GetNumberOfControlPoints()):
        points.InsertNextPoint(markupsNode.GetNthControlPointPosition(controlPointIndex))#controlPointIndex])#
        print(markupsNode.GetNthControlPointPosition(controlPointIndex))
  polyline.SetPoints(points)
  # Create a VTK CellArray to define the connectivity (vtk.vtkPolyLine)
  #lines = vtk.vtkCellArray()
  num_points = markupsNode.GetNumberOfControlPoints()
  print(num_points)
  # Create line segments in a loop
  for i in range(num_points-1):
      line = vtk.vtkPolyLine()
      line.GetPointIds().InsertNextId(i)
      line.GetPointIds().InsertNextId(i + 1)
      lines.InsertNextCell(line)
  polyline.SetLines(lines)
  # Create an array of colors for each segment
  colors = vtk.vtkUnsignedCharArray()
  colors.SetNumberOfComponents(3)  # RGB colors
  colors.SetName("Colors_teeth")
  # Define a unique RGB color for each segment
  for j in range(num_points-1):
      print(f'line{j} is {adjacent_dist[j]}') 
      if adjacent_dist[j]&lt;1.5:
        #r, g, b = np.random.randint(0, 256, 3)  # Random RGB color for each segment
        colors.InsertNextTuple3(255, 0, 0)
      else:
         colors.InsertNextTuple3(0, 255, 0)
      #print(r,g,b)
  polyline.GetCellData().SetScalars(colors)
  polyline.Modified()

  modelNode.GetDisplayNode().SetActiveScalar("Colors_teeth", vtk.vtkAssignAttribute.CELL_DATA)
  modelNode.GetDisplayNode().SetAndObserveColorNodeID("")
  modelNode.GetDisplayNode().SetScalarVisibility(True)
  modelNode.GetDisplayNode().SetScalarRangeFlag(slicer.vtkMRMLDisplayNode.UseDirectMapping)
  modelNode.GetDisplayNode().SetLineWidth(5)

pt_observer = markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent,updatemodelcolor2)


</code></pre>

---
