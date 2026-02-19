---
topic_id: 45397
title: "Creating A Heatmap From Corresponding Points"
date: 2025-12-08
url: https://discourse.slicer.org/t/45397
---

# Creating a heatmap from corresponding points

**Topic ID**: 45397
**Date**: 2025-12-08
**URL**: https://discourse.slicer.org/t/creating-a-heatmap-from-corresponding-points/45397

---

## Post #1 by @maas (2025-12-08 12:01 UTC)

<p>Hallo!</p>
<p>I’m trying to make a heatmap portraying the difference between a pre and post operation radius and ulna. I’ve managed to segment and overlay the bones. however I’m having issues creating the heatmap. When using the model to model distance extension I need to use the corresponding points option since the differences between the pre and post situations are too big.<br>
What would be the best way to do this?<br>
Should i use ALPACA to create a pointcloud and overlay this on the post operation situation? Or is it better to use slicerSALT with SPHARM-PDM? Is there a better direction I haven’t thought of? Could you point me in the right direction how to do this?</p>
<p>any help would be greatly appreciated!</p>

---

## Post #3 by @muratmaga (2025-12-09 02:20 UTC)

<aside class="quote no-group" data-username="maas" data-post="1" data-topic="45397">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b9e5f3/48.png" class="avatar"> maas:</div>
<blockquote>
<p>When using the model to model distance extension I need to use the corresponding points option since the differences between the pre and post situations are too big.</p>
</blockquote>
</aside>
<p>If the pre and post volumes/models are not accurately aligned, yes, you need to align them first. ALPACA does not help you there, but you can use the FastModelAlign to do a rigid alignment of the two segmented models. There are also other extensions you can use to do the alignment. Once the two models are closely aligned as best as possible, then run the model2model distance.</p>

---
