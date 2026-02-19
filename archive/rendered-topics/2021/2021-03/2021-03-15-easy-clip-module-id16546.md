---
topic_id: 16546
title: "Easy Clip Module"
date: 2021-03-15
url: https://discourse.slicer.org/t/16546
---

# Easy clip module

**Topic ID**: 16546
**Date**: 2021-03-15
**URL**: https://discourse.slicer.org/t/easy-clip-module/16546

---

## Post #1 by @MFS-YES (2021-03-15 10:43 UTC)

<p>Hi, by the way, I did a bone segmentation, so after isolating the region of interest I used the Easy clip module to clip and measure different bone cross-sections, the problem is that the axial, sagittal, and coronal images that I need disappear automatically. Is it normal? so is it possible to use the Easy clip module while keeping the sagittal, axial, and coronal view? or is there another procedure that can solve this problem?</p>

---

## Post #2 by @manjula (2021-03-15 10:48 UTC)

<p>try dynamic modeler which can save both parts of the model and do multiple clipping at once and much more.</p>
<p>It is installed by default in recent slicer versions.</p>
<aside class="quote quote-modified" data-post="1" data-topic="11759">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-dynamic-modeler-parametric-surface-editing-for-biomedical-applications/11759">New module: Dynamic Modeler - parametric surface editing for biomedical applications</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We have added a new module called “Dynamic Modeler” to the latest Slicer preview releases (4.11). This module provides an extensible framework for automatic processing of mesh nodes by executing “Tools” on the input to generate output mesh. 

  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    [3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications]
  </a>


Output of a tool can be used as input in another tool, which allows specification of complex editing operations. This is similar to “parametric editing” in eng…
  </blockquote>
</aside>


---
