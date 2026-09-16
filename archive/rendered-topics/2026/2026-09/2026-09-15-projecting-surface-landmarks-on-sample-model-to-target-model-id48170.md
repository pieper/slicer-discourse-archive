---
topic_id: 48170
title: "Projecting surface landmarks on sample model to target model in ALPACA"
date: 2026-09-15
url: https://discourse.slicer.org/t/48170
last_bumped: 2026-09-15T16:37:49.520Z
---

# Projecting surface landmarks on sample model to target model in ALPACA

**Topic ID**: 48170
**Date**: 2026-09-15
**URL**: https://discourse.slicer.org/t/projecting-surface-landmarks-on-sample-model-to-target-model-in-alpaca/48170

---

## Post #1 by @JYTan (2026-09-15 14:06 UTC)

<p>Hi, I am new user of 3D slicer. I have generated a template mesh and surface landmarks of orbital volume segmentation and wish to project same numbers of surface landmarks from the template model to a set of target models using ALPACA in 3D slicer version 5.10.0. May I ask does same number of landmarks will be eventually projected at both the source and target models after running ALPACA? As the number of points are different between source and target pointclouds after running subsampling.. and May I ask is it possible to check the number of landmarks finally registered on both the model after running ALPACA? The tutorial I searched from community are from the previous version of 3D slicer and some functions have been removed or combined in current version. Highly appreciate if any explanation or suggestion could be provided. Thank you.</p>

---

## Post #2 by @muratmaga (2026-09-15 15:35 UTC)

<aside class="quote no-group" data-username="JYTan" data-post="1" data-topic="48170">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jytan/48/82814_2.png" class="avatar"> JYTan:</div>
<blockquote>
<p>ish to project same numbers of surface landmarks from the template model to a set of target models using ALPACA</p>
</blockquote>
</aside>
<p>Thats exactly what ALPACA does.</p>
<aside class="quote no-group" data-username="JYTan" data-post="1" data-topic="48170">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jytan/48/82814_2.png" class="avatar"> JYTan:</div>
<blockquote>
<p>May I ask is it possible to check the number of landmarks finally registered on both the model after running ALPACA?</p>
</blockquote>
</aside>
<p>No, need to check. Number of  transferred landmarks will identical to the ones you have for your source (template) model.</p>
<aside class="quote no-group" data-username="JYTan" data-post="1" data-topic="48170">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jytan/48/82814_2.png" class="avatar"> JYTan:</div>
<blockquote>
<p>e tutorial I searched from community</p>
</blockquote>
</aside>
<p>This is the official tutorial. Screenshot are small changes to the UI, but the functionality is identical to the documented workflow. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/ALPACA/README.md" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/ALPACA/README.md at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #3 by @JYTan (2026-09-15 16:13 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="2" data-topic="48170">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>No, need to check. Number of transferred landmarks will identical to the ones you have for your source (template).</p>
</blockquote>
</aside>
<p>Thank you for the clarification. May I ask does it mean that the number of transferred landmarks is same with the number of source landmarks used as template at the beginning, and the “run subsampling” step is functioned to generate point clouds of source and target for use to allign and capture the point of correspondence to project the landmark? What will be affected by the density of point clouds is the detail of morphology of the specimens and eventually the correspondence of the projected landmarks, instead of the number of landmarks. Is my understanding correct?</p>

---

## Post #4 by @muratmaga (2026-09-15 16:35 UTC)

<aside class="quote no-group" data-username="JYTan" data-post="3" data-topic="48170">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jytan/48/82814_2.png" class="avatar"> JYTan:</div>
<blockquote>
<p>and the “run subsampling” step is functioned to generate point clouds of source and target for use to allign and capture the point of correspondence to project the landmark?</p>
</blockquote>
</aside>
<p>You probably need to to read the orginal paper to understand the details of how ALPACA works: <a href="https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13689" rel="noopener nofollow ugc">https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13689</a></p>
<p>Subsampling steps involves extracting sufficiently dense point cloud to do the deformable registration which is then used to transfer the landmarks on the source model.</p>

---

## Post #5 by @JYTan (2026-09-15 16:37 UTC)

<p>Understood. Thank you for the clarification.</p>

---
