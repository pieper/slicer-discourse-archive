---
topic_id: 16633
title: "Segmentation Depth Peeling Carving"
date: 2021-03-19
url: https://discourse.slicer.org/t/16633
---

# Segmentation depth peeling/carving

**Topic ID**: 16633
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/segmentation-depth-peeling-carving/16633

---

## Post #1 by @mohammed_alshakhas (2021-03-19 11:43 UTC)

<p>im trying to achieve what i call it "segments depth peeling/carving  " not sure if that a proper term or not .</p>
<p>it is like what I do with volume through moving the ROI, making it disappear in the coronal plane .</p>
<p>for me in surgical planning, it would help greatly if I can do that with either segmentation or volumes. ( getting greedy here ) . it can allow me to visualize relationships slice by slice</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c569920fc64476ea21c13994ef408fb8c6c042.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c569920fc64476ea21c13994ef408fb8c6c042.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c569920fc64476ea21c13994ef408fb8c6c042.mp4</a>
    </source></video>
  </div> .<p></p>

---

## Post #2 by @lassoan (2021-03-26 02:50 UTC)

<p>You cannot clip segments but you can clip models, using Models module’s Clipping planes section.</p>
<p>You can export segmentation to models by right-clicking on the segmentation in Data module.</p>

---
