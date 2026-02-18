# Creating two sets of "Slice intersection" in a "Three over three window"?

**Topic ID**: 24699
**Date**: 2022-08-09
**URL**: https://discourse.slicer.org/t/creating-two-sets-of-slice-intersection-in-a-three-over-three-window/24699

---

## Post #1 by @spencer.t.brinker (2022-08-09 22:36 UTC)

<p>This request is for attempting to produce two sets of independent “Slice Intersection” markers for independent use in top and bottom rows of a “Three over three” window. I use 3D slicer for a tracking one objects but I want to now track two separate objects using the “Slice intersections” as crosshairs.</p>
<p>I need help with an adjustment. A Three over three window is open with a human brain MRI being visualized as the volume (set as Refence). The top row are displaying Axial, Coronal, and Sagittal. I am currently in the Volume Reslice Driver module. The top rows Drivers are set to a Transform containing an object I am tracking with a navigation camera. The coordinates of a point on the object are set as the Transform’s translational LR PA and IS coordinates. This yields the “Slice intersections” in the top row windows to move with the spatial location of the object relative to the Brain MRI in the top row only. In essence, I am attempting to “turn on” or “create” a second set of “Slice intersections” markers to appear in the second row in order to create crosshairs for another object in a separate transform. Any advice?</p>

---

## Post #2 by @lassoan (2022-08-09 22:51 UTC)

<p>Slice intersections are already independent in each view group. The top row in “Three over three” view is view group 0, the bottom row is view group 1, so slice intersections can be set separately in each row. You can change the view group to 0 for all views in “View Controllers” module if you want all slice intersections appear in all views.</p>
<p>However, if you just want to highlight objects, I would recommend to use markups, models, or segmentations instead of relying on slice intersections.</p>

---

## Post #3 by @spencer.t.brinker (2022-08-10 22:40 UTC)

<p>Thanks for the tip!!</p>

---
