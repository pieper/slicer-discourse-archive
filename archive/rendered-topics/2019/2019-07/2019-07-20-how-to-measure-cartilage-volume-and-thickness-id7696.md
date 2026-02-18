# How to measure cartilage volume and thickness

**Topic ID**: 7696
**Date**: 2019-07-20
**URL**: https://discourse.slicer.org/t/how-to-measure-cartilage-volume-and-thickness/7696

---

## Post #1 by @saf (2019-07-20 18:03 UTC)

<p>Can i use Slicer  for measure cartilage volume and thickness with ?<br>
if yes, how can I do please!</p>

---

## Post #2 by @cpinter (2019-07-20 23:58 UTC)

<p>You can segment the structures you want to measure (see segmentation tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" rel="nofollow noopener">here</a>, and you can find additional youtube videos if you do a search), and then you can get their volumes in the Segment Statistics module.</p>

---

## Post #3 by @lassoan (2019-07-21 03:11 UTC)

<p>You can get cartilage <em>thickness</em> as described here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2735">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735/2">How to analyze the thickness of the model</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    “Thickness” is not a very well defined term for models (surface meshes), but for shell-like meshes it is probably not too difficult to estimate it robustly and accurately. 
Potential approaches: 
A. Extract medial surface and estimate thickness as 2x of distance from medial surface. There are various ways of computing these in Slicer. One possible workflow: 

Compute medial surface using Simple Filters module - BinaryThinningImageFilter.
Compute distance map using Simple Filters module - Daniels…
  </blockquote>
</aside>


---

## Post #4 by @saf (2019-07-21 17:11 UTC)

<p>i already have a segmented image, i just need measure cartilage volume and thickness</p>

---

## Post #5 by @lassoan (2019-07-21 18:25 UTC)

<p>That’s perfect. Export the segmentation to model (right-click on the segmentation in Data module) and then follow the steps described in the linked post.</p>

---
