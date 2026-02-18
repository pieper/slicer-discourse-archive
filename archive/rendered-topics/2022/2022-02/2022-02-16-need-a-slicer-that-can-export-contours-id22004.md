# Need a slicer that can export contours

**Topic ID**: 22004
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/need-a-slicer-that-can-export-contours/22004

---

## Post #1 by @BOB_GER (2022-02-16 20:52 UTC)

<p>Hi,</p>
<p>i am looking for a software that can silce my 3D solid and export the contourelements for printing. I file like dxf or any readable format would be fine. Ok, of course i can take the Gcode and look for the different elements (Line, Arc, Spline). But i would to go the other way. I am a developer of an Offline Programming system for robots and do not have time to program my own slicer.<br>
If the is no software that can export contours, do you know of a good slicer that can generate gcode with spline. I do not want to approximate a spline by may small arcs.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2022-02-17 11:04 UTC)

<p>I am not familiar with <code>dxf</code> or <code>gcode</code> but Slicer can generate parallel contours from a surface. The contour points will be individual points, not splines. Would that be helpful?</p>
<p>See “planar contours” on this page <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>

---
