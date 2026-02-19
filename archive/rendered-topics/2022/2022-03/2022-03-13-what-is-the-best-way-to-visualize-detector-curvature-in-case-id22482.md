---
topic_id: 22482
title: "What Is The Best Way To Visualize Detector Curvature In Case"
date: 2022-03-13
url: https://discourse.slicer.org/t/22482
---

# What is the best way to visualize detector curvature in case of forward projection calculation?

**Topic ID**: 22482
**Date**: 2022-03-13
**URL**: https://discourse.slicer.org/t/what-is-the-best-way-to-visualize-detector-curvature-in-case-of-forward-projection-calculation/22482

---

## Post #1 by @Mik (2022-03-13 10:29 UTC)

<p>I’m making a forward projection calculation using RTK.</p>
<p>In case of parallel geometry or a flat detector the detector surface can be visualize as a MarkupsPlaneNode.</p>
<p>What could you suggest in case of the detector with a radius? The scheme is <a href="http://www.openrtk.org/Doxygen/DocGeo3D.html#DR" rel="noopener nofollow ugc">here</a>. Can a grid transform be used in that case, and can it be applied to a MarkupsPlaneNode?</p>

---

## Post #2 by @mau_igna_06 (2022-03-13 11:58 UTC)

<p>You could create an uncapped cylinder of the corresponding size with vtkCylinderSource filter, assign its output to a modelNode and crop the model with two markupsPlanes created by code with the dynamicModeler’s tool planeCut</p>
<p>You can make same GUI and set up event observers to make this easy to edit if you want.</p>
<p>On your method the radial simmetry of the aproximated cylinder will be limited by volume spacing. In the method I described it will be limited by the resolution factor you set up on the cylinderSource.</p>
<p>If you want more points along the cylinder’s height you should use vtkTubeFilter instead of vtkCylinderSource</p>

---

## Post #3 by @Mik (2022-03-13 17:27 UTC)

<p>Thank you!</p>
<p>I’ve thought about using transformation for that purpose, if detector is flat, then linear transform, if it has a radius, then grid transform or something else.</p>
<p>I will think about using models for that.</p>

---
