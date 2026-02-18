# Using GetCursorPositionRAS and ignore a model

**Topic ID**: 15045
**Date**: 2020-12-14
**URL**: https://discourse.slicer.org/t/using-getcursorpositionras-and-ignore-a-model/15045

---

## Post #1 by @Niels (2020-12-14 11:33 UTC)

<p>I am using GetCursorPositionRAS on the vtkMRMLCrosshairNode singleton to get my mouse position when I am hitting a certain model. This works perfect.<br>
But now I would like to continuously display a stylus when hitting it. (with a certain colour, transparency, radius etc). For this I created a separate modelNode (sphere) and displayed it at the hit location.</p>
<p>But when the stylus is placed the next mouse hit will be the stylus itself. Can I ignore a certain model from the CrosshairNode? or should I display a stylus in another way?</p>

---

## Post #2 by @lassoan (2020-12-19 07:06 UTC)

<p>You can call <code>node.SetSelectable(False)</code> to exclude <code>node</code> from picking.</p>

---
