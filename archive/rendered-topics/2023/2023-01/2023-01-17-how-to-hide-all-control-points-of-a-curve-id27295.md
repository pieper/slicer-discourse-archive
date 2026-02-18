# How to hide all control points of a curve

**Topic ID**: 27295
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/how-to-hide-all-control-points-of-a-curve/27295

---

## Post #1 by @wrc (2023-01-17 12:30 UTC)

<p>Hello, I want to hide all control points and only show the curve. How to achieve that by the API from vtkMRMLMarkupsDisplayNode?</p>

---

## Post #2 by @cpinter (2023-01-17 12:52 UTC)

<p>You can increase LineThickness to maximum and decrease GlyphSize/Scale. Then you won’t see the control points because they will have the same size as the line. If you want to prevent interaction, you can also lock the curve. There are other ways but I think this is the simplest.</p>

---

## Post #3 by @Sunderlandkyl (2023-01-17 15:29 UTC)

<p>Not from vtkMRMLMarkupsDisplayNode, but vtkMRMLMarkupsNode has the <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#a51b6b37d38a92df2ddd5027d60bc59b6" rel="noopener nofollow ugc">SetNthControlPointVisibility</a> function.</p>

---
