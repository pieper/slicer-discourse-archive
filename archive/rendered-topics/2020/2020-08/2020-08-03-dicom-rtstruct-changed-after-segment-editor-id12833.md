---
topic_id: 12833
title: "Dicom Rtstruct Changed After Segment Editor"
date: 2020-08-03
url: https://discourse.slicer.org/t/12833
---

# DICOM RTSTRUCT changed after segment editor

**Topic ID**: 12833
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/dicom-rtstruct-changed-after-segment-editor/12833

---

## Post #1 by @wuchuanjen (2020-08-03 15:29 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.10.2<br>
Expected behavior:export dicom RTSTRUCT correctly<br>
Actual behavior:<br>
First I loaded Dicom with RTSTRUCT, then I just wanted to modify one segment a little bit using segment editor. It is requested to convert contour into labelmap. After modification, I exported it to another Dicom subject with new study. However, when I opened the new one, the RTSTRUCT was changed. Some of contour having triangle and some of segments were combined as one. I was very frustrated. Does any one can help me?</p>

---

## Post #2 by @lassoan (2020-08-03 15:44 UTC)

<p>This is the expected behavior. RT structure set is very poor 3D representation, as it is highly anisotropic (contains high-resolution contours within a slice, and there is no information about contour shape between two slices).</p>
<p>Segment Editor module performs all editing in 3D labelmap at the chosen resolution. If you find that the default resolution is not sufficient to represent all relevant details then use higher resolution. A simple way of achieving that is by creating the binary labelmap representation using an “oversampling factor” larger than 1.0 (e.g., 1.5-2.0).</p>
<aside class="quote quote-modified" data-post="4" data-topic="11717">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/update-oversampling-factor/11717/4">Update oversampling factor</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    By the way on the UI you can set it by either long-clicking Create in the row oof binary labelmap if you don’t have that representation yet, or click Update if you have one already. Then select the path and you’ll see the parameters: 
[image]
  </blockquote>
</aside>

<p>Instead of just changing oversampling factor, you can specify custom resolution and extents using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html?highlight=geometry#panels-and-their-use">“Specify geometry” button in Segment Editor module</a>.</p>

---

## Post #3 by @cpinter (2020-08-03 15:44 UTC)

<p>You did two things that changed the segmentation.</p>
<ol>
<li>Change the master representation from planar contours (the original inefficient representation) to binary labelmap</li>
<li>Export it using a different CT image</li>
</ol>
<p>I would suggest increasing the resolution of the master volume. In Segmentations module if you long-click Create… in the row of Binary labelmap, choose the CT you will export it with (addresses <span class="hashtag">#2</span>), then click Set geometry and specify an oversampling of 2 (addresses <span class="hashtag">#1</span>).</p>

---

## Post #4 by @cpinter (2020-08-03 15:45 UTC)

<p>Oh, and please use a recent Preview version because 4.10.2 is almost two years old and one thing that improved significantly is the segmentation infrastructure.</p>

---

## Post #5 by @wuchuanjen (2020-08-04 13:17 UTC)

<p>Is there any way to edit contour directly instead of converting them to labelmap then converting back to dicom RT structure again?</p>

---

## Post #6 by @lassoan (2020-08-04 14:03 UTC)

<p>Slicer only supports true, direct 3D editing. Parallel contours are very poor representation of segmentations, so I would not recommend to use them at all and if you need DICOM export then switch to DICOM segmentation object instead.</p>

---
