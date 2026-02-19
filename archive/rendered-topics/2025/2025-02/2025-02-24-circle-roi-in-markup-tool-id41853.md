---
topic_id: 41853
title: "Circle Roi In Markup Tool"
date: 2025-02-24
url: https://discourse.slicer.org/t/41853
---

# Circle ROI in markup tool

**Topic ID**: 41853
**Date**: 2025-02-24
**URL**: https://discourse.slicer.org/t/circle-roi-in-markup-tool/41853

---

## Post #1 by @Ash_Alarfaj (2025-02-24 08:47 UTC)

<p>Hi<br>
In mark up there is only rectangular box ROI, I need circle ROI? to measure the signal in MRI</p>

---

## Post #2 by @jamesobutler (2025-02-24 12:53 UTC)

<p>You can use the Paint or Scissors segment editor effect which have circle based drawing methods to create your segmentation using the Segment Editor module. You can then use the segmentation in the Segment Statistics module to get stats based on the intensity values it covers.</p>
<p>This process of segmenting to get stats is how you previously did things as in:</p>
<aside class="quote quote-modified" data-post="1" data-topic="3109">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/problem-with-segment-editor-paint/3109">Problem with segment editor paint</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system:Windows <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a506de6ab74bfd650d5104a7e54f2a6e8d67c03.jpeg" data-download-href="/uploads/short-url/fauVIbG0l9lb5l7LgSEG4PZ7URl.jpg?dl=1" title="paint%20problem%20disable" rel="noopener nofollow ugc">[paint%20problem%20disable]</a> 
Slicer version:4.9 
Expected behavior: apply paint 
Actual behavior: doesn’t work! 
Hi could please help me, I start segmentation by applying the threshold, then correct it by paint and eras, but now, paint doesn’t work with me, in the middle of my segmentation I went to volume rendering and I can’t undo the volume rendering so does it affect the paint?
  </blockquote>
</aside>


---
