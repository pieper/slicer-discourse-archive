# Moving a subset of points in a list

**Topic ID**: 29198
**Date**: 2023-04-28
**URL**: https://discourse.slicer.org/t/moving-a-subset-of-points-in-a-list/29198

---

## Post #1 by @smrolfe (2023-04-28 21:39 UTC)

<p>I would like to select a subset of control points in a point list and translate/rotate these together, while the unselected points are stationary. I can make this work by copying the moving points into a new point list, translating/rotating and copying new positions back into the original node (to preserve the order). Is there a better way to do this?</p>
<p>Ideally, I would like to be able to lock some points and use the interaction handles to move the unlocked points only. However, <a href="https://github.com/Slicer/Slicer/blob/661e00945f7a1f695e939366bcaf10e9481f2ada/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L160" rel="noopener nofollow ugc">when any point is locked, these functions are disabled</a>.</p>

---

## Post #2 by @muratmaga (2023-05-03 01:51 UTC)

<p>any comments for this? This is sort of a blocking issue for us…</p>

---

## Post #3 by @pieper (2023-05-03 12:44 UTC)

<p>The method you describe makes sense <a class="mention" href="/u/smrolfe">@smrolfe</a>.  Maybe we could make an option in the Markups Editor to make this easier to do by managing all the temporary infrastructure during trans.ation/rotation.</p>

---

## Post #4 by @smrolfe (2023-05-03 17:38 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I think it could be doable in the Markups Editor, but was wondering if it might make sense to change this in the Markups module since it could be broadly useful, and probably simpler from a user perspective.</p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #5 by @pieper (2023-05-03 21:53 UTC)

<p>Yes, making this a core feature makes more sense.</p>

---

## Post #6 by @lassoan (2023-05-03 22:20 UTC)

<p>The markups module is ready extremely complex (both the GUI and underlying logic). To keep things easier to develop and maintain, it would be probably better to implement this in a separate module.</p>

---
