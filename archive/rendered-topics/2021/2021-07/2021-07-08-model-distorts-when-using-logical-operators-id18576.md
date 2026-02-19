---
topic_id: 18576
title: "Model Distorts When Using Logical Operators"
date: 2021-07-08
url: https://discourse.slicer.org/t/18576
---

# Model distorts when using logical operators

**Topic ID**: 18576
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/model-distorts-when-using-logical-operators/18576

---

## Post #1 by @t0ons80 (2021-07-08 12:09 UTC)

<p>Hello, I’m trying to create a mould using a dicom structure (as the hole) and an imported STL model as the mould itself.<br>
Currently I change the dicom structure into a binary label map, I then import an STL (the mould casing) as a model. I then move the dicom structure to inside the mould model and use the subtract logical operator to remove the structure from the mould.<br>
This does work however the resulting surface of the mould is very rounded/distorted like it has been smoothed and in some areas if the internal structure is too close to the mould wall a hole is created.<br>
Is there anyway I can do this without having these issues?</p>
<p>Thanks in advance</p>

---

## Post #2 by @pieper (2021-07-08 21:57 UTC)

<p>This thread should help:</p>
<aside class="quote quote-modified" data-post="1" data-topic="16048">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-experimental-feature-boolean-operations-union-intersection-difference-on-meshes/16048">New experimental feature: Boolean operations (union, intersection, difference) on meshes</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We have added a new module - Combine models - to Sandbox extension to compute union, intersection, or subtraction operations on models (surface meshes). 
This can be used to construct surgical guides and various other patient-specific devices by combining patient-specific meshes with CAD-designed parts. 
See short demo here: 

  <a href="https://www.youtube.com/watch?v=2MOAk2oNbKw" target="_blank" rel="noopener">
    [Combine patient and CAD models in 3D Slicer using union/intersection/difference operations]
  </a>


Although Segment Editor can also combine models using Logical oper…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2021-07-09 04:25 UTC)

<p>If you want to use the Segment Editor then you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">change the resolution of the segmentation</a>. If you created the segmentation by importing an STL file then Option B is applicable; and you need to specify a suitable spacing value (smaller the spacing the more accurate the segmentation is; but memory usage and computation time increases, too).</p>

---

## Post #4 by @t0ons80 (2021-07-09 08:15 UTC)

<p>Thank you Steve, sorry I can’t seem to find the Combine models extension though. I’m currently using V 4.11.20200930.</p>
<p>Simon</p>

---

## Post #5 by @lassoan (2021-07-09 14:50 UTC)

<p>You need to use a recent Slicer Preview Release and install the Sandbox extension.</p>

---
