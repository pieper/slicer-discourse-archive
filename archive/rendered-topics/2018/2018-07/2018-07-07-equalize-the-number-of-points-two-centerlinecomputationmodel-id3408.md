---
topic_id: 3408
title: "Equalize The Number Of Points Two Centerlinecomputationmodel"
date: 2018-07-07
url: https://discourse.slicer.org/t/3408
---

# Equalize the number of points two CenterlineComputationModels

**Topic ID**: 3408
**Date**: 2018-07-07
**URL**: https://discourse.slicer.org/t/equalize-the-number-of-points-two-centerlinecomputationmodels/3408

---

## Post #1 by @shahrokh (2018-07-07 09:45 UTC)

<p>Hi Slicer Developers</p>
<p>I have two models with the names of CenterlineComputationModelMR and CenterlineComputationModelCT with the following information:<br>
<strong>CenterlineComputationModelMR</strong><br>
<em>Mesh Type: Surface Mesh (vtkPolyData)</em><br>
<em>Surface Area: 0.00 mm2</em><br>
<em>Volume: 0.00 mm3</em><br>
<em>Number of Points: 177</em></p>
<p><strong>CenterlineComputationModelCT</strong><br>
<em>Mesh Type: Surface Mesh (vtkPolyData)</em><br>
<em>Surface Area: 0.00 mm2</em><br>
<em>Volume: 0.00 mm3</em><br>
<em>Number of Points: 277</em></p>
<p>I want to make the same number of points such as 260 points. How can I do it?<br>
I need to do it(equalize the number of points) so I want use them as inputs to “Scattered Transform” modules.</p>
<p>Please guide me,<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-07-09 18:09 UTC)

<p>Determining point correspondences between two vessel trees is a difficult task. It is not just a matter of resampling a line.</p>
<p>Probably a more robust and simpler way would be to compute a distance map image from the trees and use intensity-based image registration to compute transform between them. These steps are performed by Segment registration extension. You just need to convert the input models to segments in a Segmentation node to be able to use it. Segmentations module import/export feature should be usable if the centerlines are tubular shapes. If centerlines are just lines then you can convert it to tubes by applying VTK tube filter.</p>

---
