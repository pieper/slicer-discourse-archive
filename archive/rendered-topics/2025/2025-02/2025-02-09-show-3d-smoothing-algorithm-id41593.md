---
topic_id: 41593
title: "Show 3D Smoothing Algorithm"
date: 2025-02-09
url: https://discourse.slicer.org/t/41593
---

# Show 3D Smoothing Algorithm

**Topic ID**: 41593
**Date**: 2025-02-09
**URL**: https://discourse.slicer.org/t/show-3d-smoothing-algorithm/41593

---

## Post #1 by @aiacocca (2025-02-09 22:46 UTC)

<p>Hello! I was wondering what smoothing algorithm the “Show 3D” smoothing option uses in the segment editor.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2025-02-10 15:00 UTC)

<p>The default smoothing algorithm is the flying edges, see</p>
<p>Pinter, C., Lasso, A., &amp; Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. <a href="https://doi.org/10.1016/j.cmpb.2019.02.011" class="inline-onebox">Redirecting</a></p>
<p>The experimental algorithm is SurfaceNets, see</p>
<aside class="quote quote-modified" data-post="1" data-topic="32430">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-surface-model-generation-method-surfacenets/32430">New surface model generation method: SurfaceNets</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We have now integrated the <a href="https://www.kitware.com/really-fast-isocontouring/">SurfaceNets isocontouring method</a> into “Show 3D” functionality of the Segment Editor! 
The new experimental algorithm provides a ~7x speedup to the generation of surface models from segmentations compared to the default method (Flying Edges).  The option can be enabled from the Show 3D menu in the Segment Editor. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa0f30b0f9126fe9fbe67ffe83bad76b39329926.png" data-download-href="/uploads/short-url/ogpIjO8UmEKSgJymSQj2LvWkMey.png?dl=1" title="Screenshot 2023-10-26 13.52.11">[Screenshot 2023-10-26 13.52.11]</a> 




Default FlyingEdges Method
SurfaceNets with default smoothing (fast)
SurfaceNets with built in Smoothing (faster)




<a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1d5243a8991793aab9222c2b7167cefe94a9fc4.jpeg" data-download-href="/uploads/short-url/tWgrAh1zmZb6wpgS9fTWnPQKvti.jpeg?dl=1" title="Screenshot 2023-10-26 14.17.35">[…</a>
  </blockquote>
</aside>

<p>I’m sure this topic has been answered several times on the forum but the search function on discourse is horrible, so here it is again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
