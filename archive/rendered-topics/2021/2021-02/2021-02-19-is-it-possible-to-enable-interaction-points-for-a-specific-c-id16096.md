---
topic_id: 16096
title: "Is It Possible To Enable Interaction Points For A Specific C"
date: 2021-02-19
url: https://discourse.slicer.org/t/16096
---

# Is it possible to enable interaction points for a specific control point with a Marksup node?

**Topic ID**: 16096
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/is-it-possible-to-enable-interaction-points-for-a-specific-control-point-with-a-marksup-node/16096

---

## Post #1 by @muratmaga (2021-02-19 19:10 UTC)

<p>As it is, interaction handles applies to all the control points within a node. Would be possible to enable for single points for better control over axis of movement in 3D viewer? (i.e., without exporting that point temporarily as a singleton and move it back when it is done?)</p>

---

## Post #2 by @lassoan (2021-02-19 19:34 UTC)

<p>Rotation is not applicable to a single point and translation is already supported. With the recently exposed “snapping” behavior the translation can be already constrained to be in the camera’s normal plane in 3D view or on a visible surface. Can you describe tasks that are hard to perform using the current implementation?</p>

---

## Post #3 by @muratmaga (2021-02-19 22:07 UTC)

<p>I am deforming a surface using IGT Fiducial Registration wizard. There are about 50 or so control points. I just want to have more control over translating a point interactively in 3D viewer. Widgets help that, but it applies to all points. Something like this e.g.,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1428af4ad11da4f38e1a09b965fe34a032ca990.jpeg" data-download-href="/uploads/short-url/n0zrhsj9KsJzh3fCG2nSTnDdsSA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1428af4ad11da4f38e1a09b965fe34a032ca990.jpeg" alt="image" data-base62-sha1="n0zrhsj9KsJzh3fCG2nSTnDdsSA" width="420" height="500" data-dominant-color="9A9ABD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">452×538 52.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-02-19 22:44 UTC)

<p>You can do this already if you set point placement to unconstrained. Then, in an axial view you can only move the points along AP and LR axes. I don’t think constraining to one line would be often useful, and it could be quite complicated to specify a direction. We could lock point translation to a single axis in screen space when a modifier key is pressed, it would be easy to implement, but hard to discover, and would not be possible to use that mouse gesture for other things. You could also change point position along a single axis using spinboxes in the markups control point table. Alternatively, you can click on a markup to show it in all slice views and you can move the markup in a selected slice plane.</p>

---
