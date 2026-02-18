# Model to Model Distance Parameters

**Topic ID**: 6543
**Date**: 2019-04-19
**URL**: https://discourse.slicer.org/t/model-to-model-distance-parameters/6543

---

## Post #1 by @stevenagl12 (2019-04-19 16:20 UTC)

<p>What are the differences between the parameters in model to model distance? By that I mean, what’s the differences between absolute closest point, signed closest point, and closest point? How do these differences effect the shape model created?</p>

---

## Post #2 by @lassoan (2019-04-28 22:56 UTC)

<p>Since nobody seems to know this off hand, the best would be if you could have a look at the source code and get this information from there. We would appreciate if you shared what you’ve found so that we can add it to the module documentation.</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a></p>

---

## Post #3 by @ljod (2019-04-29 00:43 UTC)

<p>I had a student use this module in the past, so I know that signed distance is negative when one model is inside the other. I don’t know about the closest points computation. The module is based directly on a vtk filter according to this docs page:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance</a></p>
<p>VTK is well documented so you can read the docs for the filter to see what it does.<br>
<a href="https://vtk.org/doc/nightly/html/classvtkDistancePolyDataFilter.html" class="onebox" target="_blank" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkDistancePolyDataFilter.html</a></p>

---

## Post #4 by @styner (2020-07-06 15:49 UTC)

<p>A bit late reply:</p>
<ul>
<li>closest point correspondence does not assume that there is already an established correspondence between the meshes, but generates the correspondence on the fly (matching points as corresponding if the distance is closest across all points).</li>
<li>signed means that the sign of the distance (negative vs positive) depends on whether one surface is inside the other (like Lauren mentioned). This is computed relative to the target model, i.e. if the source surface at a given point is inside the target surface then that distance will be negative</li>
<li>corresponding_point_to_point: this means that there is already an established, index-wise correspondence (e.g. by using SlicerSALT to generate corresponding surfaces) and the distance is computed between points at the same index in each mesh.</li>
</ul>

---

## Post #5 by @sfglio (2021-01-21 21:21 UTC)

<p>I created two models from the sinus of two different CT scans which have been registered in the first step.</p>
<p>Does “model-to-model distance” allow me to create a distance-map (e.g. <a href="https://www.blendermarket.com/products/distance-map" class="inline-onebox" rel="noopener nofollow ugc">Distance Map - Blender Market</a>) in order to tell in which directions my models expanded/diminished??</p>
<p>Actually I am looking for a way to create a distance map of two models<br>
or in other words: I would like to get the distance numbers from the colors of the “shape population viewer”.</p>

---

## Post #7 by @seanchoi0519 (2021-06-26 06:51 UTC)

<p>hello <a class="mention" href="/u/sfglio">@sfglio</a> just wondering if you were successful in achieving this? I’d like to find a way to tell in which directions my models need expanded/diminished, and if possible, by how much (mm) through the color map. let me know</p>

---

## Post #8 by @lassoan (2021-06-27 03:00 UTC)

<p>The question was posted in <a href="https://discourse.slicer.org/t/model-to-model-distance-module-questions/3481/13">this topic</a> as well and it is currently being discussed there.</p>

---

## Post #9 by @sfglio (2021-07-02 13:30 UTC)

<p><a class="mention" href="/u/seanchoi0519">@seanchoi0519</a> The vtk output file allows nicely to visualize (i.e. color map) the difference between the  two models. however I have not found yet a practical approach to quantify the difference in directions between the two models. So I can just tell by judging visually that e.g. the difference between two models was mainly on the inferior side…</p>

---

## Post #10 by @lassoan (2021-07-02 18:31 UTC)

<p>You can use Dynamic Modeler module to cut out parts of a model (by drawing a curve on it or defining a ROI box, or cut it with planes), then get the scalar values of this clipped model as a numpy array and compute any statistics you need (average/min/max distance, histogram of thr distance distribution, etc).</p>

---

## Post #11 by @Daniel1 (2021-09-26 12:28 UTC)

<aside class="quote no-group" data-username="styner" data-post="4" data-topic="6543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/styner/48/1024_2.png" class="avatar"> styner:</div>
<blockquote>
<p>by using SlicerSALT to generate corresponding surfaces</p>
</blockquote>
</aside>
<p>Thank you for that - makes sense. How do we use SlicerSALT to generate corresponding surfaces in two models?</p>

---

## Post #12 by @lassoan (2021-09-28 13:40 UTC)

<p>See SlicerSALT tutorials <a href="https://salt.slicer.org/documentation/#tutorials">here</a>. If you have any question then create a new topic for it.</p>

---

## Post #13 by @KAMONCHAT_APIVANICHK (2022-08-19 12:47 UTC)

<p>Do the distance of ModetoModelDistance mean as same as Hausdorff distance? Can I use this module for comparing mask model and segmented model? Is its output reliable?</p>

---
