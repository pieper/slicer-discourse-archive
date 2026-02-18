# Mean distance calculation of two 3D objects

**Topic ID**: 25595
**Date**: 2022-10-07
**URL**: https://discourse.slicer.org/t/mean-distance-calculation-of-two-3d-objects/25595

---

## Post #1 by @Chm (2022-10-07 19:14 UTC)

<p>I load in 3D Slicer two identical 3D objects after segmentation and my target is to compare all the edges between the surfaces of these 3D objects and calculate the mean distance. I use the module “Fiducial Registration Wizard” to markup the spots(edges) in the surfaces and the module " Fiducials - Model Registration" for calculation the mean distance.</p>
<p>In detail, from the module “Fiducial Registration Wizard” i markup manually a lot of spots(edges) in the surface of my 3D objects but i would like to take automatically all the spots(edges) of each object. So the first question is, how can i achieve that?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @ungi (2022-10-08 13:36 UTC)

<p>It’s hard to manage many points in Fiducial Registration Wizard, because points need to be in the same order in both lists. By increasing the number of points, you increase the chance that there will be a mistake in the order. The conventional way of registration would be to start with three carefully selected point pairs on both models to calculate an initial registration using Fiducial Registration Wizard. Then, use Model Registration to refine the registration in a second step. Model Registration automatically extracts all points of one of the models, and iteratively brings them closer to the other model, disregarding the order of points.</p>

---

## Post #3 by @Chm (2022-10-09 15:45 UTC)

<p>Thanks a lot Tamas. Checking it and let you know</p>

---

## Post #4 by @Chm (2022-10-13 18:19 UTC)

<p>Dear Team,</p>
<p>I selected three points of pairs on both models and after the initial registration i get the result : RMS Error : 1.71. What is the meaning of this value ? We need this value to be closer to zero ?</p>
<p>Additionally from the Model Registration i have the below scenarios, how the Input fixed dense and Input moving sparse models work ?</p>
<p>Input fixed dense model : Model 1</p>
<p>Input moving sparse model : Model 2</p>
<p>Mean distance after registration : 1.29</p>
<p>Input fixed dense model : Model 2</p>
<p>Input moving sparse model : Model 1</p>
<p>Mean distance after registration : 2.17</p>
<p>And a last question, i hope, is there any tool/module in 3D Slicer that extracts all points(edges) from a 3D surface model?</p>
<p>Thanks again</p>

---

## Post #5 by @lassoan (2022-10-21 03:27 UTC)

<aside class="quote no-group" data-username="ungi" data-post="2" data-topic="25595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>It’s hard to manage many points in Fiducial Registration Wizard, because points need to be in the same order in both lists.</p>
</blockquote>
</aside>
<p>Automatic reordering feature was added to Fiducial Registration Wizard. You can mark points in arbitrary order, up to 7 points, if the points are not placed in a symmetric pattern.</p>
<aside class="quote no-group" data-username="Chm" data-post="4" data-topic="25595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chm/48/16855_2.png" class="avatar"> Chm:</div>
<blockquote>
<p>RMS Error : 1.71. What is the meaning of this value ? We need this value to be closer to zero ?</p>
</blockquote>
</aside>
<p>The value characterizes the residual error after aligning the landmark points. The lower the value the better.</p>
<p>Since usually you aim for having less than 1mm overall error in most image-guided therapy applications, this value is a bit high (especially considering that landmark registration may be just on error component). Try to mark your points more accurately.</p>
<p>If you expect that the segmentations cannot be accurately aligned with rigid registration because you align objects that may deform then you may choose to use a warping transform.</p>

---
