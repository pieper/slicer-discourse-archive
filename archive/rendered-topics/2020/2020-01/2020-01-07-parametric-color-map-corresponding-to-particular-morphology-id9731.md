# Parametric color map corresponding to particular morphology

**Topic ID**: 9731
**Date**: 2020-01-07
**URL**: https://discourse.slicer.org/t/parametric-color-map-corresponding-to-particular-morphology/9731

---

## Post #1 by @hherhold (2020-01-07 23:43 UTC)

<p>Greetings Slicers,</p>
<p>Is it possible to define a parametric color map where the color is defined by the morphology of a particular slice? For example, say you wanted to display lung tracheae or blood vessels, and display those with a larger cross-sectional area as blue, and those with smaller area as red? I realize you’d have to pick a slice direction to calculate cross-sectional area, but is it possible to use that quantity in a color lookup for a segment?</p>
<p>If it’s not possible to use a color map in a segment, is it possible to assign colors to model vertices?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-01-08 03:11 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="9731">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Is it possible to define a parametric color map where the color is defined by the morphology of a particular slice?</p>
</blockquote>
</aside>
<p>You can define and display any parametric color maps.</p>
<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="9731">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>For example, say you wanted to display lung tracheae or blood vessels, and display those with a larger cross-sectional area as blue, and those with smaller area as red?</p>
</blockquote>
</aside>
<p>This one should be easy. See steps described <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735/2">here</a>. You can also use SlicerVMTK extension to extract centerline curve and get radius at each centerline point.</p>
<p>If you want to extract part of a model corresponding to a certain radius range, then you can apply vtkThreshold filter to the model (see example <a href="https://discourse.slicer.org/t/use-segmentations-in-cad-or-fem-software/1626/34">here</a>).</p>

---

## Post #3 by @hherhold (2020-01-10 17:38 UTC)

<p>OK, I have my medial surface from the Binary Image Thinning Filter, but I’m confused by the Danielsson Distance Image Map Filter. Is the input to the filter the original label map, or the medial surface? It looks like there is one input - shouldn’t it need two to compute a distance? (Or am I just misunderstanding things here…)</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #4 by @hherhold (2020-01-10 17:42 UTC)

<p>Oh wait - I had the output set up as a label map volume. I think that’s the issue…</p>

---
