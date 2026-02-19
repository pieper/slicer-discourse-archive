---
topic_id: 36195
title: "I Want To Know If It Is Possible To Do Image Registration On"
date: 2024-05-16
url: https://discourse.slicer.org/t/36195
---

# i want to know if it is possible to do image registration on images of different anatomical orientations 

**Topic ID**: 36195
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/i-want-to-know-if-it-is-possible-to-do-image-registration-on-images-of-different-anatomical-orientations/36195

---

## Post #1 by @zackster (2024-05-16 05:27 UTC)

<p>Hi everyone , I have volumes of different anatomical orientations , i want to know if a script exist to project them in the same anatomical orientation , or is the some ressources describing an approach to consider in the following case , it’ll be very helpful for me , and thank you all .</p>

---

## Post #2 by @muratmaga (2024-05-16 17:08 UTC)

<p>Please see this thread about manually aligning and resampling the images to a custom orientation:</p><aside class="quote quote-modified" data-post="12" data-topic="21861">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-properly-use-the-segment-editor-with-transformed-volumes/21861/12">How to properly use the segment editor with transformed volumes</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thank you, this sample image was helpful. 
A simple workflow can be: 

Select volume

The module switches to four-up view and enables interactive slice intersections


Rotate slice intersections using drag-and-drop to show axial slice in red and coronal slice in green
Click “Align” button

The module rotates volume to make the slice planes aligned with anatomical axes. The result is that the volume is oriented correctly in physical space, except there may be flips.


Click Flip LR, Flip AP, or F…
  </blockquote>
</aside>

<p>There many registration tools in Slicer (Brains, ANTs, Elastix) however, they all will require the starting orientations to be approximately similar.</p>

---
