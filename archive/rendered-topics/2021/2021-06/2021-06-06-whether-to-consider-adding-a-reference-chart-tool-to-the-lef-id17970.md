# Whether to consider adding a reference chart tool to the left of the 3D view

**Topic ID**: 17970
**Date**: 2021-06-06
**URL**: https://discourse.slicer.org/t/whether-to-consider-adding-a-reference-chart-tool-to-the-left-of-the-3d-view/17970

---

## Post #1 by @slicer365 (2021-06-06 06:34 UTC)

<p>For some projections or orthogonal views, I think it is very helpful to add a grid reference. Is there a  script to achieve this effect?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eb6659504afc29ad1bc1e1d6e084b37f951fc82.jpeg" data-download-href="/uploads/short-url/bek1C7SUwsCD3R6Y3Eg9SSnKOmC.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4eb6659504afc29ad1bc1e1d6e084b37f951fc82_2_517x214.jpeg" alt="捕获" data-base62-sha1="bek1C7SUwsCD3R6Y3Eg9SSnKOmC" width="517" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4eb6659504afc29ad1bc1e1d6e084b37f951fc82_2_517x214.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eb6659504afc29ad1bc1e1d6e084b37f951fc82.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eb6659504afc29ad1bc1e1d6e084b37f951fc82.jpeg 2x" data-dominant-color="6E6D7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">752×312 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-06 19:05 UTC)

<p>There are many ways to achieve this. Can you explain what your end goal is?</p>

---

## Post #3 by @slicer365 (2021-06-07 03:29 UTC)

<p>If I want to use scissor tool  to fill a cylinder, then I need to determine an axis, or a circle center, and then use this point as the starting point of the scissor.In addition, sometimes I need to register two models，Of course, there are many methods, but I can use the reference grid to translate.If I need to hollow a baffle, similar to this picture, then I can use scissor for circular cutting, but without a grid reference, the distribution of these holes will be irregular.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5c754c560f5446dd57665696e93fd8b77f3e111.jpeg" alt="捕获" data-base62-sha1="wMIp9Bkj0KkKDrlgA5P9YPbVZ8B" width="337" height="237"></p>

---

## Post #4 by @lassoan (2021-06-07 04:17 UTC)

<p>You can generate a set of cylinders (vtkCylinderSource), append them into a single polydata (vtkAppendPolyData), then add that to a model (<code>slicer.modules.models.logic().AddModel()</code>). You can then either combine it with a segmentation in Segment Editor (import the model and use logical operators effect) or subtract using Combine models module (in Sandbox extension).</p>

---
