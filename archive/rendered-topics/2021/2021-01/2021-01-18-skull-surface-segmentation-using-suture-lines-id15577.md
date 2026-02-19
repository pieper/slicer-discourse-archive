---
topic_id: 15577
title: "Skull Surface Segmentation Using Suture Lines"
date: 2021-01-18
url: https://discourse.slicer.org/t/15577
---

# Skull surface segmentation using suture lines

**Topic ID**: 15577
**Date**: 2021-01-18
**URL**: https://discourse.slicer.org/t/skull-surface-segmentation-using-suture-lines/15577

---

## Post #1 by @mucahit_calisan (2021-01-18 05:10 UTC)

<p>Hello there,<br>
I am at the beginning stage of 3D slicer. I’m trying to make a video of Andras Lasso named “Bone surface segmentation using suture lines”. Can you help me? I wonder if you can share the full version of the video or the steps more descriptively. Thank you so much.</p>

---

## Post #2 by @lassoan (2021-01-18 05:22 UTC)

<p>This has been discussed recently in these topics:</p>
<aside class="quote quote-modified" data-post="1" data-topic="12389">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/b4bc9f/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/working-with-sutures-1-voxel-wide-on-infant-skull-ct/12389">Working with sutures &lt;1 voxel wide on infant skull CT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: OS X Catalina (10.15.5) 
Slicer version: 4.10.2 r28257 
Expected behavior: Use thresholding or threshold masking + grow from seeds to create accurate segmentation of skull 
Actual behavior: Unable to use automated methods to appropriately distinguish the sutures on CT scan from surrounding bone due to how small they are - either I have to under-threshold the scan and I lose the sutures entirely but retain all of the bony structures or I over-threshold the scan and lose all of t…
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="12875">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohamed_attia/48/7576_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/skull-sutures-in-ct/12875">Skull sutures in CT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello everyone, 
I am new to 3D slicer. I am working on a research project that needs to extract the skull sutures. I was able to used manually to approximate them. I used “shift” to make the sutures more evident. I was wondering if there is a plugin that can help me to visualise and extract the sutures automatically?
  </blockquote>
</aside>

<p>I would suggest to try the techniques that were described there and let us know how it worked for you.</p>

---
