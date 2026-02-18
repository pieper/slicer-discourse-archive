# Convert segmentation to closed curve markup

**Topic ID**: 27182
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/convert-segmentation-to-closed-curve-markup/27182

---

## Post #1 by @MayaSF (2023-01-10 23:22 UTC)

<p>Hi there,<br>
Is there a way I can convert a Segmentation to a Closed Curve Markup by sampling the outside boundary of the segmented area with a certain number of points? I find it significantly faster to use the Draw tool in Segment Editor to outline my specimens than to place hundreds of points with the Closed Curve Markup tool. However, I would like to export my outlines as json files rather than nrrd files, so they are easier to work with in R. Appreciate any suggestions you have.</p>
<p>Best,<br>
Maya</p>

---

## Post #2 by @lassoan (2023-01-11 04:52 UTC)

<p>Do you work with 3D data or just a single 2D image?</p>
<p>For 3D data, planar contour representation is highly problematic - based on our experience with RTSTRUCT DICOM information objects).</p>
<p>What is your end goal? What kind of processing or analysis would you like to do?</p>

---

## Post #3 by @MayaSF (2023-01-11 17:39 UTC)

<p>Hi Andras,<br>
Thanks for your reply! In this case, I am working with 2D images. My end goal is to make a number of measurements based on each outline, and I already have an R script that makes all these measurements and runs model comparison from coordinates in json files (I am not as comfortable in python). I do not think I can export a segmentation in a file format compatible with my R script, so converting the segmentations to closed curve markups would be the quickest solution to finish the pipeline.</p>

---

## Post #4 by @lassoan (2023-01-11 18:02 UTC)

<p>I see, it makes sense then. Some 2D measurements (such as perimeter) are indeed the easiest is to compute from a polyline representation.</p>
<p>To get a polyline representation from a labelmap image representation, you can use vtkDiscreteFlyingEdges2D followed by a vtkContourTriangulator. You can use VTK either in Python (in Slicer) or in R.</p>

---

## Post #5 by @MayaSF (2023-01-11 18:05 UTC)

<p>Perfect, thanks again!</p>

---
