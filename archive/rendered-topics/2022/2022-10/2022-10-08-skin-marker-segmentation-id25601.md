---
topic_id: 25601
title: "Skin Marker Segmentation"
date: 2022-10-08
url: https://discourse.slicer.org/t/25601
---

# Skin marker segmentation

**Topic ID**: 25601
**Date**: 2022-10-08
**URL**: https://discourse.slicer.org/t/skin-marker-segmentation/25601

---

## Post #1 by @joanne40226 (2022-10-08 07:41 UTC)

<p>Hi community,<br>
I want to segment a skin marker from the user. So that the user can click on a point and simply get the skin marker segmented.<br>
However, for the segment editor module i dont think i can achieve my goal.<br>
I thought about do it programmically however not much pop up for now.</p>
<p>I hope after clicking the point M1, the whole skin marker can be segmented.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2018993662cb0302eed9cc83b05fb34ebdc1c0e4.jpeg" data-download-href="/uploads/short-url/4zVYPdVzkefBUWs5CajGdibAGfa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2018993662cb0302eed9cc83b05fb34ebdc1c0e4_2_690x378.jpeg" alt="image" data-base62-sha1="4zVYPdVzkefBUWs5CajGdibAGfa" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2018993662cb0302eed9cc83b05fb34ebdc1c0e4_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2018993662cb0302eed9cc83b05fb34ebdc1c0e4_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2018993662cb0302eed9cc83b05fb34ebdc1c0e4.jpeg 2x" data-dominant-color="373743"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1246×683 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you for your time!</p>

---

## Post #2 by @jay1987 (2022-10-08 09:34 UTC)

<p>if the skin maker is not too much,you can use [paint],[draw] tool to segment them manully,it’s simple to execute</p>

---

## Post #3 by @jay1987 (2022-10-08 09:37 UTC)

<p>If it is a task to be performed frequently,the method i mentioned above is not suitable ,maybe you can consider other solutions like deep learning task.</p>

---

## Post #4 by @joanne40226 (2022-10-08 10:10 UTC)

<p>Thank you for your reply!<br>
I do not think paint , draw will solve this case since I want it to be fast.<br>
However I think about doing it by image processing without deep learning<br>
Do you have any idea? Thank you!</p>

---

## Post #5 by @lassoan (2022-11-24 03:01 UTC)

<p>You can segment these markers fully automatically by using simple thresholding. Then, use Islands effect to put each marker in a separate segment. Finally, use Segment Statistics module to compute shape information (so that you can discard all pieces that are too small, too large, or not the right shape), and then use the computed position and orientation.</p>

---
