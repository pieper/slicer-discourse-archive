---
topic_id: 19415
title: "Any Way To Control Depth Of Scissor Cut"
date: 2021-08-30
url: https://discourse.slicer.org/t/19415
---

# Any way to control depth of scissor cut?

**Topic ID**: 19415
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/any-way-to-control-depth-of-scissor-cut/19415

---

## Post #1 by @akshay_pillai (2021-08-30 15:35 UTC)

<p>Is there any way to control the depth of the cut with scissors in segment editor in 3d programmatically or even using existing functions? Please let me know.</p>

---

## Post #2 by @muratmaga (2021-08-30 15:55 UTC)

<p>When cuttting in slice views, you can control if with the symmetric option.</p>

---

## Post #3 by @akshay_pillai (2021-08-30 16:11 UTC)

<p>Anyway I can control depth in 3d view?</p>

---

## Post #4 by @muratmaga (2021-08-30 16:55 UTC)

<p>I don’t think that’s available.</p>

---

## Post #5 by @lassoan (2021-08-30 23:52 UTC)

<p>There is not way to specify depth when cutting in 3D because there is no reference plane.</p>
<p>Instead, you can control the depth by rotating the view after the first cut by about 90 degrees, and remove the excess with a second cut. See step-by-step instructions in the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">craniotomy segmentation recipe</a>.</p>

---
