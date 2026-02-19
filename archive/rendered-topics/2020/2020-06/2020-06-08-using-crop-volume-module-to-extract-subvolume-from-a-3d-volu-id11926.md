---
topic_id: 11926
title: "Using Crop Volume Module To Extract Subvolume From A 3D Volu"
date: 2020-06-08
url: https://discourse.slicer.org/t/11926
---

# Using crop volume module to extract subvolume from a 3D volume

**Topic ID**: 11926
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/using-crop-volume-module-to-extract-subvolume-from-a-3d-volume/11926

---

## Post #1 by @Deepa (2020-06-08 13:57 UTC)

<p>Hello Everyone,</p>
<p>I have a 3D volume like the following that has been reconstructed from 2D images.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2474d5bf4d66d4459c50e8a31589bf2670791fb.jpeg" alt="image" data-base62-sha1="u0d22VxZBKdq3SyTgBOJEneIlqX" width="238" height="194"></p>
<p>I’d like to know if there is a way to remove the terminal branches from this volume . By terminal branches, I mean the free ends (i.e inlets/outlets of a 3D volume).</p>
<p>After removing the terminal branches, I’d like to extract a subvolume from the original volume.<br>
I had a chance to look at <a href="https://www.youtube.com/watch?v=1mYNwJbE7dQ" rel="noopener nofollow ugc">this</a> video tutorial that shows how to crop volumes by selecting regions in 2D images. I’d like to know if there exists a similar<br>
approach to crop volume.</p>
<p>Any suggestions on how to do this will be highly appreciated.</p>
<p>Deepa</p>

---

## Post #2 by @lassoan (2020-06-08 14:37 UTC)

<p>You can crop a segmentation using “Scissors” effect or for more complicated cuts, using “Surface cut” effect (provided by SegmentEditorExtraEffects extension).</p>

---

## Post #3 by @Deepa (2020-06-08 15:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you very much. I will check these options.</p>
<p>But prior to extracting the subvolume, I’d like to do the following</p>
<aside class="quote no-group" data-username="Deepa" data-post="1" data-topic="11926">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I’d like to know if there is a way to remove the terminal branches from this volume . By terminal branches, I mean the free ends (i.e inlets/outlets of a 3D volume).</p>
</blockquote>
</aside>
<p>Since the original volume is highly complex, I’d like to know if it is possible to programmatically remove the free ends. It will be difficult to manually locate these free ends.</p>

---

## Post #4 by @lassoan (2020-06-08 16:18 UTC)

<p>You don’t need to address this during segmentation. Centerline extraction module extracts all the endpoints that it can find and then extract those branches. But we can allow editing of these endpoints, so that you keep only selected branches.</p>

---

## Post #5 by @Deepa (2020-06-09 04:21 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>In the end, I would like to extract a 3D subvolume with one inlet free end and one outlet free end similar to <a href="/uploads/short-url/dhB0T1KRpkNoIfry97yVIAS58C7.png">this 2D</a>.</p>
<p>In the 3D volume image posted above, I could find many free ends and I wasn’t sure how to retain just one inlet and one outlet. For this reason, I had thought of removing all the free ends before extracting the subvolume. Once the subvolume is extracted, I could cut open two branches (located geometrically opposite) to create the inlet and outlet before feeding this subvolume to the centerline extraction module.</p>
<p>From what you have suggested, I think I shall do this vice-versa. First extract the subvolume, feed to the centerline extraction, delete terminal branches.</p>

---

## Post #7 by @lassoan (2020-06-20 21:52 UTC)

<p>Just for future reference, extraction of selected branches is now implemented:</p>
<aside class="quote quote-modified" data-post="1" data-topic="12117">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">New module: Extract Centerline (in SlicerVMTK extension)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We added a completely new module that makes vessel (or airway or any other tree structure) centerline extraction much faster, flexible, and robust. It can quickly extract a network, determine branch endpoints automatically, allows editing of endpoints, computing centerlines, branches, and quantitative metrics (radius, curvature, torsion, etc). The new “Extract Centerline” module is available in SlicerVMTK extension for latest Slicer-4.11 release (it replaces the old “Centerline Computation” modu…
  </blockquote>
</aside>


---
