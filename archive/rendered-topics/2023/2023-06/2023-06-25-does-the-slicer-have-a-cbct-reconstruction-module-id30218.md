---
topic_id: 30218
title: "Does The Slicer Have A Cbct Reconstruction Module"
date: 2023-06-25
url: https://discourse.slicer.org/t/30218
---

# Does the slicer have a CBCT reconstruction module？

**Topic ID**: 30218
**Date**: 2023-06-25
**URL**: https://discourse.slicer.org/t/does-the-slicer-have-a-cbct-reconstruction-module/30218

---

## Post #1 by @ma1282029525 (2023-06-25 07:40 UTC)

<p>Does the slicer have a CBCT reconstruction module？</p>

---

## Post #2 by @Mik (2023-06-25 11:00 UTC)

<p>Quite possible there is no such. Try to use RTK, which is part of ITK nowadays. What kind of functionality do you expect of such module?</p>
<aside class="quote" data-post="2" data-topic="27200">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/trying-to-writing-a-module-for-cross-sectional-image-reconstruction/27200/2">Trying to writing a module for cross-sectional image reconstruction</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Maybe this will help:
  </blockquote>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="http://www.openrtk.org/">
  <header class="source">
      <img src="http://www.openrtk.org/RTK/img/rtk_favicon.ico" class="site-icon" width="16" height="11">

      <a href="http://www.openrtk.org/" target="_blank" rel="noopener nofollow ugc">openrtk.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="http://www.openrtk.org/" target="_blank" rel="noopener nofollow ugc">RTK - Reconstruction Toolkit</a></h3>

  <p>RTK is an open-source, cross-platform system that provides developers with an extensive suite of software tools for image analysis.   </p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2023-06-25 17:27 UTC)

<p>Note that if you want to reconstruct an image from a clinical X-ray system, you need to have accurate information about the C-arm orientation for each frame and accurate kinematic model of the C-arm. For each orientation, the kinematic model can provide the focal point position of the X-ray source, and position and orientation of the detector - taking into account mechanical deformation of the arm due to its own weight and dynamic loads due to fast rotation. Without accurate sensor reading and kinematic model, RTK’s reconstruction will be much lower quality than what the manufacturer’s software provides.</p>

---
