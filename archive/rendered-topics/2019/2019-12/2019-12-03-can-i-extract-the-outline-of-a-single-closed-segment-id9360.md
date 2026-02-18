# Can I extract the outline of a single closed segment?

**Topic ID**: 9360
**Date**: 2019-12-03
**URL**: https://discourse.slicer.org/t/can-i-extract-the-outline-of-a-single-closed-segment/9360

---

## Post #1 by @timeanddoctor (2019-12-03 10:24 UTC)

<p>Can I extract the outline/contour of each slice of closed segment and then draw a closed curve from it with code?</p>

---

## Post #2 by @lassoan (2019-12-03 14:38 UTC)

<p>Yes, sure. You can retrieve the closed surface representation of the segment, get intersection by using VTK cut filter, sort the points using vtkContourTriangulator, then add the polygon points as curve control points. This code may help: <a href="https://github.com/Slicer/Slicer/pull/1075/files">https://github.com/Slicer/Slicer/pull/1075/files</a></p>

---

## Post #3 by @timeanddoctor (2019-12-04 14:38 UTC)

<p>I  donnot know how to get intersection and create a closed curve from points after covert the segment to a polygon data with python(just learned python). Could you help me?<br>
segmentationNode=getNode(‘Segmentation’)<br>
segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)<br>
segmentPolyData=segmentationNode.GetClosedSurfaceRepresentation(segmentId)</p>

---

## Post #4 by @lassoan (2019-12-04 15:06 UTC)

<p>Once you have the closed surface representation, use standard VTK filters, as they are used in the segmentation displayable manager (see relevant code in the pull request above). You can get learn about VTK by studying the <a href="https://lorensen.github.io/VTKExamples/site/VTKBook/01Chapter1/">VTK textbook</a> and <a href="https://lorensen.github.io/VTKExamples/site/">VTK examples website</a>.</p>

---

## Post #5 by @Ge_Tang (2021-03-25 17:20 UTC)

<p>Hallo, Dr. Lassoan. I also want to get the outline from a reformat slice.<br>
I tried the vtk cutter. The problem is that the polydata I get from the segment do not have the attribute of GetOutputPort().</p>
<blockquote>
<p>n = getNode(nameSeg)<br>
s = n.GetSegmentation()<br>
ss = s.GetSegment(s.GetSegmentIdBySegmentName(nameRegion)).GetRepresentation(‘Closed surface’)<br>
circleCutter = vtk.vtkCutter()</p>
<h1>I cannot get the GetOutputPort from ss</h1>
<p>circleCutter.SetInputConnection(ss.GetOutputPort())</p>
</blockquote>

---

## Post #6 by @lassoan (2021-03-29 13:43 UTC)

<p>To set input data in a VTK filter, use <code>SetInputData</code> method.</p>

---

## Post #7 by @Ge_Tang (2021-04-08 08:46 UTC)

<p>Dear Dr. Lassoan<br>
Thank you so much!</p>

---
