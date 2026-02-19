---
topic_id: 3115
title: "How To Know The Dimensions Of A 3D Model Using Slicer"
date: 2018-06-07
url: https://discourse.slicer.org/t/3115
---

# How to know the dimensions of a 3D model using Slicer?

**Topic ID**: 3115
**Date**: 2018-06-07
**URL**: https://discourse.slicer.org/t/how-to-know-the-dimensions-of-a-3d-model-using-slicer/3115

---

## Post #1 by @m.hilani (2018-06-07 16:47 UTC)

<p>Hello,</p>
<p>I am performing tissue segmentation for 3D printing. I would like to know the volume of the end result 3D model and some of its dimensions to compare it with some reference measures from the literature.</p>
<p>Is there a way to know these measures using 3D slicer?</p>
<p>Thank you,<br>
Michel</p>

---

## Post #2 by @pieper (2018-06-07 18:17 UTC)

<p>Try the SegmentStatistics module in the nightly:</p>
<div class="lazyYT" data-youtube-id="fM_rxfDTRi0" data-youtube-title="Segment statistics - new module in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @m.hilani (2018-07-02 19:05 UTC)

<p>This module gives details concerning the volume and surface are of the segmented tissues in cm and mm cube.<br>
Is there any way to extract the weight of the tissues through 3Dslicer and these numbers?</p>
<p>Thank you!</p>

---

## Post #4 by @pieper (2018-07-02 19:23 UTC)

<p>Should be easy to estimate weight if you know the volume and density of the tissue, right? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @m.hilani (2018-07-02 20:41 UTC)

<p>Yes, I was thinking about that too, but I wasn’t sure if we could apply this formula on the anatomical organs and tissues as well.<br>
I will do that then!</p>
<p>Thanks!</p>

---
