---
topic_id: 6539
title: "Calculating The Average Deformations From Model To Model Dis"
date: 2019-04-19
url: https://discourse.slicer.org/t/6539
---

# Calculating the average deformations from Model to Model Distance

**Topic ID**: 6539
**Date**: 2019-04-19
**URL**: https://discourse.slicer.org/t/calculating-the-average-deformations-from-model-to-model-distance/6539

---

## Post #1 by @stevenagl12 (2019-04-19 01:29 UTC)

<p>Is there a way to compute the average Hausdorf distances between models so that you can show the average displacement? Also, can you create an average model, or a minimum/maximum model given specified points such as a statistical shape model?</p>

---

## Post #2 by @cpinter (2019-04-19 16:49 UTC)

<p>You can use the Segment Comparison module in the SlicerRT extension. To compare the models, you first need to convert them to segmentations. You can do it in the Data module by right-clicking the models and choosing “Convert model to segmentation node”.</p>
<p>I think an average model can best be created from the labelmap representations (then converted back to surface). You can export the segments to labelmaps and sum them together (Add Scalar Volumes or Simple Filters module) to get a probabilistic-like image. Or you can create then manipulate distance maps to get the average model. The best way depends on what you want exactly.</p>

---

## Post #3 by @lassoan (2019-04-19 18:00 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="1" data-topic="6539">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Also, can you create an average model, or a minimum/maximum model given specified points such as a statistical shape model?</p>
</blockquote>
</aside>
<p><a href="http://salt.slicer.org/">SlicerSALT extension</a> should be able to provide these. <a class="mention" href="/u/muratmaga">@muratmaga</a>’s morphometry extension may be usable for this, too.</p>

---

## Post #4 by @muratmaga (2019-04-19 18:14 UTC)

<p>I think SPharm is probably your best bet. We currently do not have tools to generate average models directly from meshes. If you have landmarks that go with the models, SlicerMorph can do it.</p>
<p>Outside of Slicer, you can also try Shape Works Studio from Utah (<a href="https://www.sci.utah.edu/software/shapeworks.html" rel="nofollow noopener">https://www.sci.utah.edu/software/shapeworks.html</a>), but you will need to provide labelmaps already aligned in a common coordinate system as your input.</p>

---

## Post #5 by @stevenagl12 (2019-04-26 15:40 UTC)

<p>With my models, I am trying to avoid doing landmark based Procrustes to align them. How do you build an average model in SPharm?</p>

---

## Post #6 by @lassoan (2019-04-26 17:40 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="5" data-topic="6539">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>With my models, I am trying to avoid doing landmark based Procrustes to align them.</p>
</blockquote>
</aside>
<p>No matter what you do, probably landmarks are still the best option for initial alignment (moments-based alignment is not accurate enough, ICP is not robust enough, etc.). Parametric models then help you getting correspondence between all the points (not just the landmarks).</p>
<aside class="quote no-group" data-username="stevenagl12" data-post="5" data-topic="6539">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>How do you build an average model in SPharm?</p>
</blockquote>
</aside>
<p>See <a href="http://salt.slicer.org/documentation/" class="inline-onebox">Documentation • SlicerSALT</a>. Tutorials are in a very well hidden section near the bottom right of the page.</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> If you want to people to find these tutorials, make them much more visible (for example, add green buttons to that section as well, or move tutorials section into a new row).</p>

---

## Post #7 by @lassoan (2021-02-28 13:37 UTC)

<p>A post was split to a new topic: <a href="/t/get-average-deformation-from-model-to-model/16271">Get average deformation from model to model</a></p>

---
