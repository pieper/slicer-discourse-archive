---
topic_id: 20117
title: "Slice Thickness"
date: 2021-10-12
url: https://discourse.slicer.org/t/20117
---

# Slice thickness

**Topic ID**: 20117
**Date**: 2021-10-12
**URL**: https://discourse.slicer.org/t/slice-thickness/20117

---

## Post #1 by @henrysmith123 (2021-10-12 13:53 UTC)

<p>How can I change the thickness of the CBCT slice for viewing? I’m talking about a function that is in all programs for viewing CT, where I can adjust the slice thickness, for example, 2mm, and still in the 2mm area they will be summed up into one slice</p>

---

## Post #2 by @lassoan (2021-10-13 03:17 UTC)

<p>There is no graphical user interface for this (interestingly, over the many years none of the funding projects required this), but you can easily enable this by copy-pasting <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections">these few lines of code</a> into the Python console.</p>
<p>If you need this feature frequently then you can create a small Python scripted module for this that would provide a convenient user interface.</p>

---

## Post #4 by @Luis_quiterio (2023-11-10 05:05 UTC)

<p>Has this feature been added in recent upgrades? I want to adjust Adjust Slice Thickness on CBCT dicom images.</p>
<p>Thanks</p>

---

## Post #5 by @pieper (2023-11-10 13:54 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="32432">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-feature-thick-slab-reconstruction-from-slice-controllers-and-views/32432">New feature: Thick slab reconstruction from slice controllers and views</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thick slab reconstruction (TSR) can now be enabled and modified from the slice controllers and slice views! 
Enabling thick slab reconstruction as well as selection of the composite method (min, max, mean or sum) has been available through the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections">python console</a>. 
Now these options are available through both the slice controller and the right-click context menu on the slice views.  If the interactive option is selected, the thickness, angle and position of the TSR can be adjusted by moving the slice…
  </blockquote>
</aside>


---

## Post #6 by @Melodicpinpon (2023-12-28 15:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Do you think that you could add a slice-thickness control to Slicer?</p>

---

## Post #7 by @lassoan (2023-12-28 17:00 UTC)

<p>The feature is already available in recent Slicer versions. See the topic that <a class="mention" href="/u/pieper">@pieper</a> linked above for details.</p>

---
