---
topic_id: 30978
title: "Level Tracing And Reformatting The View"
date: 2023-08-04
url: https://discourse.slicer.org/t/30978
---

# Level Tracing and Reformatting the View

**Topic ID**: 30978
**Date**: 2023-08-04
**URL**: https://discourse.slicer.org/t/level-tracing-and-reformatting-the-view/30978

---

## Post #1 by @Dominick_Dickerson (2023-08-04 15:11 UTC)

<p>It appears that the level tracing tool only works in the initial axial/saggital/coronal planes and not when the view of the slice is reformatted using the reformat widget.  Is this because the “level tracing” tool has the orientation of the slices hard coded into it?</p>
<p>Is it possible to have that be dynamic so that the tool would work in any plane not just the preset axial/saggital/coronal?</p>

---

## Post #2 by @pieper (2023-08-04 15:18 UTC)

<p>The LevelTracing tool only works in a voxel space plane.  If you want to work in a different plane you would need to apply a transform and resample the volume.  The CropVolume module with a rotated ROI can be a convenient way to do this.</p>

---
