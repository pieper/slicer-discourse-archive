---
topic_id: 24148
title: "Visualization Of Stl Surface Orientation Flipped Between Mac"
date: 2022-07-01
url: https://discourse.slicer.org/t/24148
---

# visualization of STL surface orientation flipped between machines

**Topic ID**: 24148
**Date**: 2022-07-01
**URL**: https://discourse.slicer.org/t/visualization-of-stl-surface-orientation-flipped-between-machines/24148

---

## Post #1 by @ChantelC (2022-07-01 19:25 UTC)

<p>I am visualizing the output of the mri2mesh simnibs pipeline gray matter and white matter segmentation surfaces against the original mri in slicer on a mac server (mojave 10.14.6) and the .stl surfaces are flipped in orientation. I tried the latest version of slicer as well as 4.13.0 and they were flipped on both. However, when I visualize the same surfaces on my laptop (Monterey 12.2.1) in slicer the orientation is correct. Any ideas on how to fix this?</p>

---

## Post #2 by @pieper (2022-07-01 19:40 UTC)

<p>Probably you have different slicer versions.  Check this information for guidance:</p>
<aside class="quote" data-post="2" data-topic="16441">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/exported-stl-files-dont-match-view-in-slicer/16441/2">Exported STL files dont match view in Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Slicer now reads all files in LPS coordinate system. Before Slicer-4.11, it expected STL files to be in RAS coordinate system by default. See more information about how to avoid RAS/LPS mismatch in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">migration guide</a>. 
If there is no LPS/RAS issue but slight position and/or orientation differences then most likely that other software does not properly take into account image origin, spacing, or axis directions of the input volume.
  </blockquote>
</aside>


---

## Post #3 by @ChantelC (2022-07-01 20:17 UTC)

<p>Great, this has solved the issue. Thank you very much.</p>

---
