---
topic_id: 19358
title: "How To Set Model Or Segmentation Occluded Visibility Like Ma"
date: 2021-08-25
url: https://discourse.slicer.org/t/19358
---

# How to set model or segmentation occluded visibility like Markups in 3D view？

**Topic ID**: 19358
**Date**: 2021-08-25
**URL**: https://discourse.slicer.org/t/how-to-set-model-or-segmentation-occluded-visibility-like-markups-in-3d-view/19358

---

## Post #1 by @slicer365 (2021-08-25 14:31 UTC)

<p>Slicer 4.11</p>
<p>As is shown in this video .</p>
<p>How to set model or segmentation occluded visibility like Markups in 3D view？</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f130b0af2248da2d4f29ce1bf77653388811b25b.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f130b0af2248da2d4f29ce1bf77653388811b25b.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f130b0af2248da2d4f29ce1bf77653388811b25b.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @lassoan (2021-08-26 03:26 UTC)

<p>What do you mean by how to do it? Doing the same that is done in the video does not work for you?</p>

---

## Post #3 by @slicer365 (2021-08-26 03:28 UTC)

<p>The video is only for Markups, not  for model and segmentation.In the model properties, there is no such option<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57b90df310f7ca0225c2f5b3c5d18a3d8b96be8e.jpeg" alt="捕获" data-base62-sha1="cw214FXv2uZ7o0WiUZ35YWMXOuq" width="282" height="203"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11f6fbc39e36e2d2b600e3166fceac4af1d5b052.jpeg" alt="捕获" data-base62-sha1="2yVh9h6bIc3w49eFD7Evu8UsAxA" width="291" height="189"></p>

---

## Post #4 by @lassoan (2021-08-26 03:54 UTC)

<p>This very special feature was developed for markups only. Its implementation was very complex (expensive to develop and maintain) and it makes the view content partially composited in 2D instead of 3D, so it should not be overused. Therefore I would not expect that this feature will be implemented for models.</p>

---
