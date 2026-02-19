---
topic_id: 39657
title: "Ct Vessel Contouring"
date: 2024-10-11
url: https://discourse.slicer.org/t/39657
---

# CT vessel contouring

**Topic ID**: 39657
**Date**: 2024-10-11
**URL**: https://discourse.slicer.org/t/ct-vessel-contouring/39657

---

## Post #1 by @LuKo (2024-10-11 13:09 UTC)

<p>Dear 3D slicer experts<br>
Dear All,</p>
<p>I am looking for way to contour arteries on CT images, to mark the lumen and vessel.</p>
<p>Any hints on how to do it, or what extension to use?</p>
<p>Thank you!</p>

---

## Post #2 by @chir.set (2024-10-11 18:33 UTC)

<aside class="quote no-group" data-username="LuKo" data-post="1" data-topic="39657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luko/48/78206_2.png" class="avatar"> LuKo:</div>
<blockquote>
<p>the lumen and vessel</p>
</blockquote>
</aside>
<p>For the lumen, the ‘Segment editor’ is your friend. You may also consider the SlicerVMTK extension.</p>
<p>If you are working on healthy arteries, the lumen is the vessel. If you are working on diseased non-aneurysmal arteries, you may draw the wall at best <em>estimate</em> using the Shape::Tube node in the ExtraMarkups extension. If you are working on aneurysmal arteries, the ‘Fill between slices’ effect of the ‘Segment editor’ is helpful for wall-to-wall segmentation.</p>
<p>Please refer to the documentation pages of these extensions.</p>

---
