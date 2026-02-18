# Poly data intersection

**Topic ID**: 26304
**Date**: 2022-11-18
**URL**: https://discourse.slicer.org/t/poly-data-intersection/26304

---

## Post #1 by @anja_pantovic (2022-11-18 13:46 UTC)

<p>Hello,</p>
<p>I am trying to get the volume of an intersection between poly data objects. I am new to 3D slicer, so I would be very grateful if you could give me any guidelines on how to do this with python in 3D Slicer. Thanks!</p>

---

## Post #2 by @cpinter (2022-11-19 08:12 UTC)

<p>If the surfaces are closed then you can convert the models to segmentations (right-click in Data module), get their intersection in Segment Editor’s Logical operators tool, then get volume in Segment Statistics, or converting back to model and check the volume in Models module. I’m not completely sure if the Dynamic Modeler module has intersection tool, but if it has, then it might be simpler using that. If your surfaces are not closed then we need more info on them before being able to help.</p>

---

## Post #3 by @lassoan (2022-11-19 17:26 UTC)

<p>Dynamic modeler does not have Boolean operation for meshes, but you can use the Combine models module in Sandbox extension for that. However, Boolean operation on meshes is a very difficult and inherently error-prone operation, so I would recommend the segmentation based workflow that <a class="mention" href="/u/cpinter">@cpinter</a> described above.</p>

---

## Post #4 by @anja_pantovic (2022-11-28 12:47 UTC)

<p>Converting the models to segmentations was the way to go, thanks a lot!</p>

---

## Post #5 by @Max_LeVi (2023-06-19 09:41 UTC)

<p>use the segmentattion and iso extract is stable. but how to remove the step stair when change vtkpolydata to vtkimagedata?</p>

---
