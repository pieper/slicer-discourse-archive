# Combining Segmentations

**Topic ID**: 19381
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/combining-segmentations/19381

---

## Post #1 by @Alberto_Paredes (2021-08-26 23:36 UTC)

<p>Is there a way in 3D Slicer to combine two segmentations as one segmentation?</p>

---

## Post #2 by @lassoan (2021-08-27 01:42 UTC)

<p>Yes, sure. You can drag-and-drop segments between segmentations in the Data module; or use “Copy/move segments” section in Segmentations module.</p>

---

## Post #3 by @Alberto_Paredes (2021-09-01 14:51 UTC)

<p>When using the “Copy/move segments” section in the “Segmentations” module I see the top figure shown below.</p>
<p>I want to create a copy of the TL and FL segmentation, but instead of having two separate segmentations I want one segmentation called “Total”. I want this “Total” segmentation to be displayed as on color and I want to export the “Total” Segmentation as an STL File.</p>
<p>I tried to do this using the “Copy/move segments” section in the “Segmentations” module as shown in the top figure. I used the “Copy from current segmentation to other node” option to define the “Total” segmentation as a copy of both the FL and TL as shown in the top figure.</p>
<p>However, I don’t see the “Total” segmentation in the segmentation menu shown below the previous figure. Furthermore the “Total” segmentation is still shown as red for the “TL” and blue for the “FL” instead of just one color. Why is this?</p>
<p>Can you also explain to me what the difference is between a Model and Labelmap node is? Is there any documentation that you can provide me with so I can learn more about it. I’m still very new to 3D Slicer.</p>
<p>Thank you!</p>
<p><a href="/404" data-orig-href="upload://wNRZQDIkAp1tzLrAjpFO22baRmg.png">Capture|332x500</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/738d3755d58df8f716dcb799682b13dedacd0301.png" alt="Capture2" data-base62-sha1="gudsIYXyZErfIauovzOty71BaEx" width="633" height="190"></p>

---

## Post #4 by @lassoan (2021-09-06 13:01 UTC)

<p>Your can combine segments using the “logical operations” effect.</p>

---

## Post #5 by @Tobias (2024-01-25 22:04 UTC)

<p>Thank you! This is just what i needed!</p>

---
