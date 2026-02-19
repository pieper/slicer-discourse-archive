---
topic_id: 1814
title: "Using Segmentations From Changetracker"
date: 2018-01-11
url: https://discourse.slicer.org/t/1814
---

# Using segmentations from ChangeTracker

**Topic ID**: 1814
**Date**: 2018-01-11
**URL**: https://discourse.slicer.org/t/using-segmentations-from-changetracker/1814

---

## Post #1 by @JohnK (2018-01-11 19:36 UTC)

<p>I was successful in running the ChangeTracker module on longitudinal astrocytomas that had a homogeneous contrast signal. It worked great but I did not save the final results (assuming I could recall them when reloading my Scene).</p>
<p>However I can’t recall the results from the Scene. I see the baseline and follow-up ROI, and the BaselineROI_segmentation, but the segmentation editor does not seem to recognize the BaselineROI_segmentation as an input segmentation. Also the color coding (progression / regression) is not visible anymore.<br>
-Am I correct that the  ChangeTracker module does not store the results in the scene?<br>
-Does the segment editor not recognize segmentations performed by ChangeTracker?</p>
<p>Thanks! John</p>

---

## Post #2 by @ihnorton (2018-01-11 21:37 UTC)

<p>For this one:</p>
<aside class="quote no-group" data-username="JohnK" data-post="1" data-topic="1814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/59ef9b/48.png" class="avatar"> JohnK:</div>
<blockquote>
<p>-Does the segment editor not recognize segmentations performed by ChangeTracker?</p>
</blockquote>
</aside>
<p>I suspect the ChangeTracker writes a “labelmap”, which must be imported to Segmentations. See instructions and links in this comment and the follow-up:</p>
<aside class="quote quote-modified" data-post="3" data-topic="1081">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/73ab20/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-convert-volume-to-segmentation/1081/3">How to convert volume to segmentation?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thank you for your reply, Lassoan. But is there a more detail instruction on how to import the lablemap volume? I clicked the Import button, but nothing happened. [image]. In addition, it seems the Copy/move segments function will do the same job. [image] (Link: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Modules/Segmentations - Slicer Wiki</a>). However, it doesn’t say how to select the node in the right square. Operation system: Win7. Version: 4.7.0. Thank you very much.
  </blockquote>
</aside>


---
