# Smoothing vtkPolyData

**Topic ID**: 18969
**Date**: 2021-07-29
**URL**: https://discourse.slicer.org/t/smoothing-vtkpolydata/18969

---

## Post #1 by @manuela_lizarazu (2021-07-29 12:38 UTC)

<p>Hi I am trying to smooth a vtkPolyData surface mesh. I do not have the smoothing brush because is not a segmentation. I can see the data under the models module. Do you how this can be achieved?</p>
<p>Thanks!!!</p>

---

## Post #2 by @smrolfe (2021-07-29 16:34 UTC)

<p>For models you can use the smoothing filter in the Surface Toolbox module.</p>

---

## Post #3 by @lalamax3d (2024-01-29 13:58 UTC)

<p>thanks,<br>
is there a way to use brush to apply selective smoothing and not on whole mesh.<br>
just like, volume segmentation has smooth brush…Q. can we use it on mesh object.</p>

---

## Post #4 by @cpinter (2024-01-30 18:23 UTC)

<p>I’m not aware of such feature aready implemented. I could imagine allowing editing closed surface representation in Segment Editor (and only enabling very select set of tools, which are prepared for this case), then make the smoothing brush do this in the area of the brush. As a starter idea I’d try smoothing the polydata, and merge the original and the output considering the area of the brush. But all this would take considerable development time, especially that currently we simply don’t allow any editing on closed surface representation from Segment Editor. Not sure if anyone else has a better idea.</p>

---
