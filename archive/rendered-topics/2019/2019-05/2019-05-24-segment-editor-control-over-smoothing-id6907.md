# Segment editor control over smoothing

**Topic ID**: 6907
**Date**: 2019-05-24
**URL**: https://discourse.slicer.org/t/segment-editor-control-over-smoothing/6907

---

## Post #1 by @the3dslicerdude (2019-05-24 03:24 UTC)

<p>I am unsure if this feature doesn’t already exist but I can’t seem to find it. When using the segment editor, the meshes it generates look heavily smoothed to the point where they loose a lot of detail (especially when compared to other software like invesaelius, mimics etc…) For me segment editor is the most powerful of all the different software I have tried, so it would be great to have control over how smoothed the mesh is so detail can be preserved</p>

---

## Post #2 by @lassoan (2019-05-24 03:36 UTC)

<p>You have full control over smoothing parameter (in drop-down menu of “Show 3D” button).</p>
<p>If you experience that you cannot represent the small details with enough accuracy then you may consider making the segmentation’s internal labelmap higher resolution than the input volume: click “Specify geometry” button next to the master volume selector, choose the input volume as “Source geometry”, set “Oversampling factor” to something between 1.5-3.0, and click OK.</p>

---

## Post #3 by @the3dslicerdude (2019-05-24 03:46 UTC)

<p>Thank you so much for the reply, I’ll try it out tonight and see how it goes</p>

---

## Post #4 by @the3dslicerdude (2019-05-24 04:36 UTC)

<p>Just tried it out and those two things were exactly what I was after, thank you so much. Although they don’t up-res the segments already made but I kind of expected that</p>

---

## Post #5 by @lassoan (2023-03-21 03:12 UTC)



---
