# measure 3D object

**Topic ID**: 7908
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/measure-3d-object/7908

---

## Post #1 by @ikram (2019-08-07 02:41 UTC)

<p>hi<br>
i want to measure a 3D object of aneurysm , and get the height , width and volume of the coil of the aneurysm and the aneurysm bubble !<br>
can anyone help me please <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=9" title=":confused:" class="emoji" alt=":confused:"></p>

---

## Post #2 by @lassoan (2019-08-07 03:20 UTC)

<p>You can use Segment Editor to segment the aneurysm sack and compute volume using Segment statistics module.</p>
<p>You can measure height and width by using annotation ruler (available in the toolbar). To find a good slice to measure in, you can show slice intersections (using dropdown menu of crosshair button in the toolbar) and rotate it using Reformat module or (if you use a recent Slicer Preview Release) then you may also rotate it using Ctrl+Alt+Left-click-and-drag.</p>

---
