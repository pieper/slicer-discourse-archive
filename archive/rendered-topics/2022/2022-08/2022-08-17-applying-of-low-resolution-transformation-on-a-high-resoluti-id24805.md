---
topic_id: 24805
title: "Applying Of Low Resolution Transformation On A High Resoluti"
date: 2022-08-17
url: https://discourse.slicer.org/t/24805
---

# Applying of low resolution transformation on a high resolution dataset

**Topic ID**: 24805
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/applying-of-low-resolution-transformation-on-a-high-resolution-dataset/24805

---

## Post #1 by @Stephanie (2022-08-17 11:10 UTC)

<p>Good afternoon to everyone,</p>
<p>We use a skeleton vasculature dataset. This is a graph composed of nodes which have properties of position and radius, and edges that specify the connectivity of the former.</p>
<p>We apply 2 transformations on this dataset: an affine transformation (25 µm in resolution dataset) and a non-linear transformation (25 µm in resolution dataset) in order to be aligned to a reference dataset (Allen Institute for Brain Science , annotation atlas CCFV3). The resolution of our dataset (source) is 1µm and the atlas’ resolution (target) is 25 µm. The resolution of the source dataset and the transformations’ dataset is therefore different.</p>
<p>We use the TransformPoint method to apply the transformations on each 3D point coordinate of the source dataset.</p>
<p>I was wondering if the TransformPoint function performs any kind of interpolation on the transformation to obtain a 1um resolution transformation field to apply to the source dataset?<br>
If not, is there a function that I could use to do this?</p>
<p>Thanks for your help!</p>
<p>Stephanie</p>

---

## Post #2 by @lassoan (2022-08-17 11:32 UTC)

<p>Yes, transforms are smoothly interpolated (using linear, or cubic, bspline, thin-plate spline, etc. methods - depending on the transform type) in the entire 3D space.</p>
<p>If you use <code>vtkMRMLTransformNode::GetTransformBetweenNodes()</code> method then you’ll get a VTK transform that contains all the transform components (affine and non-linear) properly concatenated. You can then use <code>TransformPoint</code> to iterate through each point, but it is about 100x faster if you put your vessel model into a vtkPolyData and apply the transform using a vtkTransformPolyDataFilter.</p>
<p>It will make everything even simpler if you put your vessel model into a vtkPolyData and set that into a model node because then you can visualize your vasculature and apply the transform with two clicks (or 2-3 lines of Python code).</p>

---

## Post #3 by @Stephanie (2022-08-17 13:50 UTC)

<p>Thank you very much for your quick response. I have all I need!</p>

---
